# mpc_controller.py
"""Model predictive control using CasADi."""

import threading

import casadi as ca


class MPCController:
    def __init__(self, horizon: int = 10, dt: float = 1.0,
                 comfort_min: float = 18.0, comfort_max: float = 26.0):
        self.horizon = horizon
        self.dt = dt
        self.comfort_min = comfort_min
        self.comfort_max = comfort_max
        # the Opti instance is mutated on every solve, so serialize access
        self._lock = threading.Lock()
        self.opti = ca.Opti()
        # state and control trajectories
        self.X = self.opti.variable(self.horizon + 1)
        self.U = self.opti.variable(self.horizon)
        # slack on the comfort band so the problem stays feasible when the
        # initial temperature is outside it
        self.S = self.opti.variable(self.horizon + 1)
        self.x0 = self.opti.parameter()
        self.x_ref = self.opti.parameter(self.horizon + 1)
        self.outside = self.opti.parameter()
        self._build_problem()

    def _build_problem(self):
        Q = 1.0  # comfort error weight
        R = 0.1  # energy cost weight
        W = 100.0  # comfort band violation weight
        self.opti.subject_to(self.X[0] == self.x0)
        # dynamics constraint: x_{k+1} = x_k + dt*(u + (outside-x_k)*0.1)
        for k in range(self.horizon):
            self.opti.subject_to(
                self.X[k+1] == self.X[k] + self.dt*(self.U[k] + (self.outside - self.X[k])*0.1)
            )
        # cost
        cost = 0
        for k in range(self.horizon):
            cost += Q*(self.X[k+1]-self.x_ref[k+1])**2 + R*(self.U[k]**2)
        cost += W*ca.sumsqr(self.S)
        self.opti.minimize(cost)
        # constraints
        self.opti.subject_to(self.S >= 0)
        self.opti.subject_to(self.X >= self.comfort_min - self.S)
        self.opti.subject_to(self.X <= self.comfort_max + self.S)
        self.opti.subject_to(self.opti.bounded(-2, self.U, 2))
        self.opti.set_value(self.outside, 20)
        self.opti.solver('ipopt', {"print_time": False}, {"print_level": 0, "sb": "yes"})

    def solve(self, current_temp, target_temp, outside_temp=20):
        with self._lock:
            self.opti.set_value(self.x0, current_temp)
            self.opti.set_value(self.x_ref, [target_temp]*(self.horizon+1))
            self.opti.set_value(self.outside, outside_temp)
            sol = self.opti.solve()
            return float(sol.value(self.U[0]))
