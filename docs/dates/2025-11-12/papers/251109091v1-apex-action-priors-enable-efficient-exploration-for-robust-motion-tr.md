---
layout: default
title: APEX: Action Priors Enable Efficient Exploration for Robust Motion Tracking on Legged Robots
---

# APEX: Action Priors Enable Efficient Exploration for Robust Motion Tracking on Legged Robots
**arXiv**：[2511.09091v1](https://arxiv.org/abs/2511.09091) · [PDF](https://arxiv.org/pdf/2511.09091.pdf)  
**作者**：Shivam Sood, Laukik Nakhwa, Sun Ge, Yuhong Cao, Jin Cheng, Fatemah Zargarbashi, Taerim Yoon, Sungjoon Choi, Stelian Coros, Guillaume Sartoretti  

**一句话要点**：提出APEX方法以提升腿式机器人运动跟踪的鲁棒性和效率

**关键词**：腿式机器人, 强化学习, 动作先验, 运动跟踪, 样本效率, 鲁棒控制

## 3 点简述
- 核心问题：现有运动跟踪方法依赖参考数据，适应性差且需大量调参
- 方法要点：集成衰减动作先验和多评价器框架，引导强化学习探索
- 实验或效果：在仿真和真实机器人上验证，提高稳定性、效率和泛化能力

## 摘要（原文）

> Learning natural, animal-like locomotion from demonstrations has become a core paradigm in legged robotics. Despite the recent advancements in motion tracking, most existing methods demand extensive tuning and rely on reference data during deployment, limiting adaptability. We present APEX (Action Priors enable Efficient Exploration), a plug-and-play extension to state-of-the-art motion tracking algorithms that eliminates any dependence on reference data during deployment, improves sample efficiency, and reduces parameter tuning effort. APEX integrates expert demonstrations directly into reinforcement learning (RL) by incorporating decaying action priors, which initially bias exploration toward expert demonstrations but gradually allow the policy to explore independently. This is combined with a multi-critic framework that balances task performance with motion style. Moreover, APEX enables a single policy to learn diverse motions and transfer reference-like styles across different terrains and velocities, while remaining robust to variations in reward design. We validate the effectiveness of our method through extensive experiments in both simulation and on a Unitree Go2 robot. By leveraging demonstrations to guide exploration during RL training, without imposing explicit bias toward them, APEX enables legged robots to learn with greater stability, efficiency, and generalization. We believe this approach paves the way for guidance-driven RL to boost natural skill acquisition in a wide array of robotic tasks, from locomotion to manipulation. Website and code: https://marmotlab.github.io/APEX/.

