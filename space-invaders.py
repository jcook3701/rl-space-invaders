import gym

env = gym.make("SpaceInvaders-v0")

for i_episode in range(20):
    observation = env.reset()
    for t in range(10000):
        env.render()
        print(env.action_space)
        print(env.observation_space)
        action = env.action_space.sample()
        print(action)
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode {} finished after {} timesteps".format(i_episode, t+1))
            break
env.close()
