# traffic-signal-rl-optimization
# Reinforcement Learning-Based Dynamic Traffic Signal Optimization for Smart Cities

## Overview
This project simulates an intelligent traffic signal controller that uses a reinforcement-learning-inspired approach to adapt green-light decisions based on traffic queues.

## Objectives
- Simulate traffic at a two-direction intersection.
- Compare fixed-time and adaptive signal control.
- Visualize queue lengths and waiting times.
- Export simulation results as CSV.

## Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- Tabular Q-learning-inspired controller

## Installation
1. Install Python 3.10 or later.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:
   `python -m pip install -r requirements.txt`
5. Start the dashboard:
   `python -m streamlit run app.py`
6. Open the local URL displayed in the terminal.

## Project Structure
- `app.py` — Streamlit dashboard
- `traffic_rl/simulation.py` — traffic simulation and controller
- `tests/test_simulation.py` — basic tests
- `requirements.txt` — dependencies

## Limitations
This is an educational simulation using generated traffic data. It does not control real traffic lights or use live sensor data. Results depend on the simulation settings and do not guarantee that adaptive control will outperform fixed-time control.

## Future Improvements
- Add real traffic datasets.
- Test more intersections.
- Explore deep reinforcement learning.
- Integrate a traffic simulator such as SUMO.
