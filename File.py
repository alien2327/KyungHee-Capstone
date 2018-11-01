import gym                                         #gym 모듈을 실행
env = gym.make('CartPole-v0')                      #CartPole-v0 환경 설정
for i_episode in range(20):                        #20 범위에서 episode를 실행
    observation = env.reset()                      #env.reset()으로 과정 시작
    for t in range(500):                           #프로그램 실행 시간
        env.render()
        print(observation)                         #env.reset()을 송출
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)      #action, reward 설정
        if done:
            print("Episode finished after {} timesteps".format(t+1))        #프로그램 실행 결과를 송출
            break
    env.close()
