# mpc_controller.py
"""Model predictive control using CasADi."""

import casadi as ca


class MPCController:
    def __init__(self, horizon: int = 10, dt: float = 1.0):
        self.horizon = horizon
        self.dt = dt
        self.opti = ca.Opti()
        # state and control trajectories
        self.X = self.opti.variable(self.horizon + 1)
        self.U = self.opti.variable(self.horizon)
        self.x0 = self.opti.parameter()
        self.x_ref = self.opti.parameter(self.horizon+1)
        self._build_problem()

    def _build_problem(self):
        Q = 1.0  # comfort error weight
        R = 0.1  # energy cost weight
        # dynamics constraint: x_{k+1} = x_k + dt*(u + (outside-x_k)*0.1)
        self.outside = self.opti.parameter()
        for k in range(self.horizon):
            self.opti.subject_to(
                self.X[k+1] == self.X[k] + self.dt*(self.U[k] + (self.outside - self.X[k])*0.1)
            )
        # cost
        cost = 0
        for k in range(self.horizon):
            cost += Q*(self.X[k]-self.x_ref[k])**2 + R*(self.U[k]**2)
        self.opti.minimize(cost)
        # constraints
        self.opti.subject_to(self.opti.bounded(18, self.X, 26))
        self.opti.subject_to(self.opti.bounded(-2, self.U, 2))
        self.opti.set_value(self.outside, 20)
        self.opti.solver('ipopt')

    def solve(self, current_temp, target_temp, outside_temp=20):
        self.opti.set_value(self.x0, current_temp)
        self.opti.set_value(self.x_ref, [target_temp]*(self.horizon+1))
        self.opti.set_value(self.outside, outside_temp)
        sol = self.opti.solve()
        u_opt = sol.value(self.U[0])
        return float(u_opt)
