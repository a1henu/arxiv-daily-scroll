---
layout: default
title: Adaptive Surrogate Gradients for Sequential Reinforcement Learning in Spiking Neural Networks
---

# Adaptive Surrogate Gradients for Sequential Reinforcement Learning in Spiking Neural Networks
**arXiv**：[2510.24461v1](https://arxiv.org/abs/2510.24461) · [PDF](https://arxiv.org/pdf/2510.24461.pdf)  
**作者**：Korneel Van den Berghe, Stein Stroobants, Vijay Janapa Reddi, G. C. H. E. de Croon  

**一句话要点**：提出自适应代理梯度和引导策略以优化脉冲神经网络在强化学习中的训练性能

**关键词**：脉冲神经网络, 代理梯度, 强化学习, 自适应训练, 机器人控制

## 3 点简述
- 核心问题：脉冲神经元的不可微性和状态动态在强化学习中导致梯度优化困难和序列训练受限
- 方法要点：分析代理梯度斜率影响，结合自适应斜率调度和特权引导策略提升训练效率
- 实验或效果：在无人机位置控制任务中，平均回报达400点，显著优于基线方法

## 摘要（原文）

> Neuromorphic computing systems are set to revolutionize energy-constrained
> robotics by achieving orders-of-magnitude efficiency gains, while enabling
> native temporal processing. Spiking Neural Networks (SNNs) represent a
> promising algorithmic approach for these systems, yet their application to
> complex control tasks faces two critical challenges: (1) the non-differentiable
> nature of spiking neurons necessitates surrogate gradients with unclear
> optimization properties, and (2) the stateful dynamics of SNNs require training
> on sequences, which in reinforcement learning (RL) is hindered by limited
> sequence lengths during early training, preventing the network from bridging
> its warm-up period.
>   We address these challenges by systematically analyzing surrogate gradient
> slope settings, showing that shallower slopes increase gradient magnitude in
> deeper layers but reduce alignment with true gradients. In supervised learning,
> we find no clear preference for fixed or scheduled slopes. The effect is much
> more pronounced in RL settings, where shallower slopes or scheduled slopes lead
> to a 2.1x improvement in both training and final deployed performance. Next, we
> propose a novel training approach that leverages a privileged guiding policy to
> bootstrap the learning process, while still exploiting online environment
> interactions with the spiking policy. Combining our method with an adaptive
> slope schedule for a real-world drone position control task, we achieve an
> average return of 400 points, substantially outperforming prior techniques,
> including Behavioral Cloning and TD3BC, which achieve at most --200 points
> under the same conditions. This work advances both the theoretical
> understanding of surrogate gradient learning in SNNs and practical training
> methodologies for neuromorphic controllers demonstrated in real-world robotic
> systems.

