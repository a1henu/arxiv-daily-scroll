---
layout: default
title: Staggered Environment Resets Improve Massively Parallel On-Policy Reinforcement Learning
---

# Staggered Environment Resets Improve Massively Parallel On-Policy Reinforcement Learning
**arXiv**：[2511.21011v1](https://arxiv.org/abs/2511.21011) · [PDF](https://arxiv.org/pdf/2511.21011.pdf)  
**作者**：Sid Bharthulwar, Stone Tao, Hao Su  

**一句话要点**：提出交错重置以解决大规模并行强化学习中的非平稳性问题

**关键词**：强化学习, 大规模并行仿真, 非平稳性, 交错重置, 样本效率, 机器人环境

## 3 点简述
- 核心问题：同步重置在高UTD比设置下引入有害非平稳性，扭曲学习信号
- 方法要点：采用交错重置，环境在任务周期内不同时间点初始化，增加时间多样性
- 实验或效果：在机器人环境中提升样本效率、收敛速度和最终性能

## 摘要（原文）

> Massively parallel GPU simulation environments have accelerated reinforcement learning (RL) research by enabling fast data collection for on-policy RL algorithms like Proximal Policy Optimization (PPO). To maximize throughput, it is common to use short rollouts per policy update, increasing the update-to-data (UTD) ra- tio. However, we find that, in this setting, standard synchronous resets introduce harmful nonstationarity, skewing the learning signal and destabilizing training. We introduce staggered resets, a simple yet effective technique where environments are initialized and reset at varied points within the task horizon. This yields training batches with greater temporal diversity, reducing the nonstationarity induced by synchronized rollouts. We characterize dimensions along which RL environments can benefit significantly from staggered resets through illustrative toy environ- ments. We then apply this technique to challenging high-dimensional robotics environments, achieving significantly higher sample efficiency, faster wall-clock convergence, and stronger final performance. Finally, this technique scales better with more parallel environments compared to naive synchronized rollouts.

