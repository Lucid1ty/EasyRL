# 以下是最基本的环境,和简单的代码
# import gym  # 导入 Gym 的 Python 接口环境包
# env = gym.make('CartPole-v1')  # 构建实验环境
# env.reset()  # 重置一个 episode
# for _ in range(1000):
#     env.render()  # 显示图形界面
#     action = env.action_space.sample()  # 从动作空间中随机选取一个动作
#     observation, reward, done, info = env.step(action)
#     env.step(action)    # 用于提交动作，括号内是具体的动作
#     print(observation)
#
# env.close()  # 关闭环境


# 想要查看当前 Gym 库已经注册了哪些环境，可以使用以下代码：
from gym import envs
env_specs = envs.registry.all()
envs_ids = [env_spec.id for env_spec in env_specs]
print(envs_ids)




