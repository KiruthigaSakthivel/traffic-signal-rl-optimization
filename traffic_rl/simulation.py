import random
import pandas as pd


def run_simulation(steps=200, arrival_rate=0.5, seed=42):
    rng = random.Random(seed)
    fixed_ns = fixed_ew = adaptive_ns = adaptive_ew = 0
    fixed_wait_total = adaptive_wait_total = 0
    adaptive_decisions = 0
    history = []
    q_table = {}
    alpha, gamma, epsilon = 0.15, 0.85, 0.10
    previous_state = previous_action = None
    previous_reward = 0.0

    for step in range(steps):
        fixed_ns += int(rng.random() < arrival_rate)
        fixed_ew += int(rng.random() < arrival_rate)
        adaptive_ns += int(rng.random() < arrival_rate)
        adaptive_ew += int(rng.random() < arrival_rate)

        # Fixed-time controller alternates green directions every 10 steps.
        fixed_green = 'NS' if (step // 10) % 2 == 0 else 'EW'
        if fixed_green == 'NS':
            fixed_ns = max(0, fixed_ns - 2)
        else:
            fixed_ew = max(0, fixed_ew - 2)

        state = (min(adaptive_ns, 10), min(adaptive_ew, 10))
        actions = ['NS', 'EW']
        if rng.random() < epsilon:
            action = rng.choice(actions)
        else:
            values = [q_table.get((state, a), 0.0) for a in actions]
            action = actions[values.index(max(values))]

        if action == 'NS':
            adaptive_ns = max(0, adaptive_ns - 2)
        else:
            adaptive_ew = max(0, adaptive_ew - 2)

        reward = -(adaptive_ns + adaptive_ew)
        next_state = (min(adaptive_ns, 10), min(adaptive_ew, 10))
        if previous_state is not None:
            old = q_table.get((previous_state, previous_action), 0.0)
            best_next = max(q_table.get((next_state, a), 0.0) for a in actions)
            q_table[(previous_state, previous_action)] = old + alpha * (previous_reward + gamma * best_next - old)
        previous_state, previous_action, previous_reward = state, action, reward
        adaptive_decisions += 1

        fixed_wait_total += fixed_ns + fixed_ew
        adaptive_wait_total += adaptive_ns + adaptive_ew
        history.append({
            'step': step + 1,
            'fixed_queue': fixed_ns + fixed_ew,
            'adaptive_queue': adaptive_ns + adaptive_ew,
            'fixed_ns_queue': fixed_ns,
            'fixed_ew_queue': fixed_ew,
            'adaptive_ns_queue': adaptive_ns,
            'adaptive_ew_queue': adaptive_ew,
            'adaptive_action': action,
        })

    df = pd.DataFrame(history)
    return {
        'history': df,
        'summary': {
            'fixed_avg_wait': fixed_wait_total / steps,
            'adaptive_avg_wait': adaptive_wait_total / steps,
            'adaptive_decisions': adaptive_decisions,
        }
    }
