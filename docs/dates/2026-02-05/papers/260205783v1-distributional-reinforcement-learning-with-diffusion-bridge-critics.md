---
layout: default
title: Distributional Reinforcement Learning with Diffusion Bridge Critics
---

# Distributional Reinforcement Learning with Diffusion Bridge Critics
**arXiv**：[2602.05783v1](https://arxiv.org/abs/2602.05783) · [PDF](https://arxiv.org/pdf/2602.05783.pdf)  
**作者**：Shutong Ding, Yimiao Zhou, Ke Hu, Mokai Pan, Shan Zhong, Yanwei Fu, Jingya Wang, Ye Shi  

**一句话要点**：提出扩散桥评论家以提升强化学习中的价值分布估计精度

**关键词**：分布强化学习, 扩散桥模型, 价值分布估计, 逆累积分布函数, 机器人控制, 即插即用组件

## 3 点简述
- 现有扩散强化学习方法忽视评论家，而价值估计对策略优化至关重要
- DBC直接建模Q值的逆累积分布函数，利用扩散桥匹配能力防止分布坍缩
- 在MuJoCo基准测试中，DBC优于先前分布评论家模型，且可即插即用

## 摘要（原文）

> Recent advances in diffusion-based reinforcement learning (RL) methods have demonstrated promising results in a wide range of continuous control tasks. However, existing works in this field focus on the application of diffusion policies while leaving the diffusion critics unexplored. In fact, since policy optimization fundamentally relies on the critic, accurate value estimation is far more important than policy expressiveness. Furthermore, given the stochasticity of most reinforcement learning tasks, it has been confirmed that the critic is more appropriately depicted with a distributional model. Motivated by these points, we propose a novel distributional RL method with Diffusion Bridge Critics (DBC). DBC directly models the inverse cumulative distribution function (CDF) of the Q value. This allows us to accurately capture the value distribution and prevents it from collapsing into a trivial Gaussian distribution owing to the strong distribution-matching capability of the diffusion bridge. Moreover, we further derive an analytic integral formula to address discretization errors in DBC, which is essential in value estimation. To our knowledge, DBC is the first work to employ the diffusion bridge model as the critic. Notably, DBC is also a plug-and-play component and can be integrated into most existing RL frameworks. Experimental results on MuJoCo robot control benchmarks demonstrate the superiority of DBC compared with previous distributional critic models.

