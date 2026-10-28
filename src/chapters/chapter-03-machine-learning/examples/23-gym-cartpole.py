# Example 3.23 — random agent on CartPole (Gymnasium, not gym) (README Step 13)
# TODO:
# - import gymnasium as gym; env = gym.make('CartPole-v1', render_mode='human')
# - 20 episodes: observation, info = env.reset()
# - inner loop: action = env.action_space.sample(); observation, reward, terminated, truncated, info = env.step(action)
# - stop the episode when terminated or truncated; env.close() at the end
# Expected: a CartPole window and 'episode finished after N timesteps' lines.
