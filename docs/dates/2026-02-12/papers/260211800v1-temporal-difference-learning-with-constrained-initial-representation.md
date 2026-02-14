---
layout: default
title: Temporal Difference Learning with Constrained Initial Representations
---

# Temporal Difference Learning with Constrained Initial Representations
**arXiv**：[2602.11800v1](https://arxiv.org/abs/2602.11800) · [PDF](https://arxiv.org/pdf/2602.11800.pdf)  
**作者**：Jiafei Lyu, Jingwen Yang, Zhongjian Qiao, Runze Liu, Zeyuan Liu, Deheng Ye, Zongqing Lu, Xiu Li  

**一句话要点**：提出CIR框架，通过约束初始表示提升离策略强化学习的样本效率与稳定性。

**关键词**：强化学习, 离策略学习, 样本效率, 表示学习, 连续控制, Tanh激活

## 3 点简述
- 核心问题：离策略强化学习存在分布偏移和训练不稳定问题，影响样本效率。
- 方法要点：引入Tanh激活和归一化约束初始表示，结合跳跃连接和凸Q学习优化训练。
- 实验或效果：在连续控制任务中表现优异，竞争力强或超越现有基线方法。

## 摘要（原文）

> Recently, there have been numerous attempts to enhance the sample efficiency of off-policy reinforcement learning (RL) agents when interacting with the environment, including architecture improvements and new algorithms. Despite these advances, they overlook the potential of directly constraining the initial representations of the input data, which can intuitively alleviate the distribution shift issue and stabilize training. In this paper, we introduce the Tanh function into the initial layer to fulfill such a constraint. We theoretically unpack the convergence property of the temporal difference learning with the Tanh function under linear function approximation. Motivated by theoretical insights, we present our Constrained Initial Representations framework, tagged CIR, which is made up of three components: (i) the Tanh activation along with normalization methods to stabilize representations; (ii) the skip connection module to provide a linear pathway from the shallow layer to the deep layer; (iii) the convex Q-learning that allows a more flexible value estimate and mitigates potential conservatism. Empirical results show that CIR exhibits strong performance on numerous continuous control tasks, even being competitive or surpassing existing strong baseline methods.

