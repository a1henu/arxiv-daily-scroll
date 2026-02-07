---
layout: default
title: UAV Trajectory Optimization via Improved Noisy Deep Q-Network
---

# UAV Trajectory Optimization via Improved Noisy Deep Q-Network
**arXiv**：[2602.05644v1](https://arxiv.org/abs/2602.05644) · [PDF](https://arxiv.org/pdf/2602.05644.pdf)  
**作者**：Zhang Hengyu, Maryam Cheraghy, Liu Wei, Armin Farhadi, Meysam Soltanpour, Zhong Zhuoqing  

**一句话要点**：提出改进噪声深度Q网络以增强无人机在模拟环境中的轨迹优化探索与稳定性。

**关键词**：无人机轨迹优化, 深度强化学习, 噪声深度Q网络, 探索增强, 训练稳定性, 模拟环境

## 3 点简述
- 核心问题：无人机在深度强化学习中探索不足和训练不稳定，影响轨迹优化效率。
- 方法要点：结合残差噪声线性层与自适应噪声调度增强探索，通过平滑损失和软目标网络更新提升稳定性。
- 实验或效果：在15*15网格导航环境中，相比标准DQN，模型收敛更快，奖励提升高达+40，快速达到任务最小步数要求。

## 摘要（原文）

> This paper proposes an Improved Noisy Deep Q-Network (Noisy DQN) to enhance the exploration and stability of Unmanned Aerial Vehicle (UAV) when applying deep reinforcement learning in simulated environments. This method enhances the exploration ability by combining the residual NoisyLinear layer with an adaptive noise scheduling mechanism, while improving training stability through smooth loss and soft target network updates. Experiments show that the proposed model achieves faster convergence and up to $+40$ higher rewards compared to standard DQN and quickly reach to the minimum number of steps required for the task 28 in the 15 * 15 grid navigation environment set up. The results show that our comprehensive improvements to the network structure of NoisyNet, exploration control, and training stability contribute to enhancing the efficiency and reliability of deep Q-learning.

