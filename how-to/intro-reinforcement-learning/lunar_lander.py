#!/usr/bin/env python3

from tensorforce.execution import Runner

RUNNER = Runner(
    agent='agent.json',
    environment=dict(environment='gym', level='LunarLander-v2', visualize=True),
    max_episode_timesteps=500
)


if __name__ == '__main__':

    RUNNER.run(num_episodes=200)