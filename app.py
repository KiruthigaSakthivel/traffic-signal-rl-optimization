import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from traffic_rl.simulation import run_simulation

st.set_page_config(page_title='Smart Traffic Signal Optimization', layout='wide')
st.title('Reinforcement Learning-Based Dynamic Traffic Signal Optimization')
st.write('Compare fixed-time traffic signals with an adaptive, Q-learning-inspired controller in a simulated intersection.')

steps = st.slider('Simulation duration (steps)', 50, 500, 200, 50)
arrival_rate = st.slider('Traffic arrival rate', 0.1, 1.0, 0.5, 0.1)
seed = st.number_input('Random seed', min_value=0, max_value=10000, value=42)

if st.button('Run simulation', type='primary'):
    with st.spinner('Running traffic simulation...'):
        results = run_simulation(steps=int(steps), arrival_rate=arrival_rate, seed=int(seed))
    st.session_state['traffic_results'] = results

if 'traffic_results' in st.session_state:
    results = st.session_state['traffic_results']
    summary = results['summary']
    c1, c2, c3 = st.columns(3)
    c1.metric('Fixed-time average waiting', f"{summary['fixed_avg_wait']:.2f}")
    c2.metric('Adaptive average waiting', f"{summary['adaptive_avg_wait']:.2f}")
    c3.metric('Adaptive decisions', str(summary['adaptive_decisions']))

    df = results['history']
    st.subheader('Traffic queue comparison')
    fig, ax = plt.subplots()
    ax.plot(df['step'], df['fixed_queue'], label='Fixed-time queue')
    ax.plot(df['step'], df['adaptive_queue'], label='Adaptive queue')
    ax.set_xlabel('Simulation step')
    ax.set_ylabel('Vehicles waiting')
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)

    st.subheader('Simulation results')
    st.dataframe(df.tail(20), use_container_width=True)
    st.download_button('Download results as CSV', df.to_csv(index=False), 'traffic_simulation_results.csv', 'text/csv')
else:
    st.info('Choose the simulation settings and click Run simulation to view results.')

st.caption('Educational simulation only. It does not control real-world traffic signals.')
