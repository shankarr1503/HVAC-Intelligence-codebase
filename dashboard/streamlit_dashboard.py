"""Streamlit dashboard displaying basic HVAC metrics."""
import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.title("HVAC Intelligence Dashboard")

    st.header("Temperature Trends")
    times = pd.date_range(start="2026-01-01", periods=24, freq="H")
    temps = np.random.normal(loc=22, scale=2, size=24)
    st.line_chart(pd.DataFrame({'temperature': temps}, index=times))

    st.header("Energy Usage")
    energy = np.abs(np.random.normal(loc=0.5, scale=0.1, size=24))
    st.bar_chart(pd.DataFrame({'energy': energy}, index=times))

    st.header("Comfort Scores")
    comfort = np.clip(1 - np.abs(temps - 22) / 10, 0, 1)
    st.area_chart(pd.DataFrame({'comfort': comfort}, index=times))


if __name__ == '__main__':
    main()
