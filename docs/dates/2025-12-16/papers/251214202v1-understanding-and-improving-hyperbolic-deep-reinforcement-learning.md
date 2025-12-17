---
layout: default
title: Understanding and Improving Hyperbolic Deep Reinforcement Learning
---

# Understanding and Improving Hyperbolic Deep Reinforcement Learning
**arXiv**：[2512.14202v1](https://arxiv.org/abs/2512.14202) · [PDF](https://arxiv.org/pdf/2512.14202.pdf)  
**作者**：Timo Klein, Thomas Lang, Andrii Shkabrii, Alexander Sturm, Kevin Sidak, Lukas Miklautz, Claudia Plant, Yllka Velaj, Sebastian Tschiatschek  

**一句话要点**：提出Hyper++以解决强化学习中双曲特征空间优化不稳定的问题

**关键词**：双曲强化学习, 特征表示, 优化稳定性, PPO算法, 梯度分析

## 3 点简述
- 核心问题：双曲特征空间在强化学习中因大范数嵌入导致梯度训练不稳定
- 方法要点：通过分类价值损失、特征正则化和优化友好层设计提升稳定性
- 实验或效果：在ProcGen和Atari-5上优于基线，减少约30%训练时间

## 摘要（原文）

> The performance of reinforcement learning (RL) agents depends critically on the quality of the underlying feature representations. Hyperbolic feature spaces are well-suited for this purpose, as they naturally capture hierarchical and relational structure often present in complex RL environments. However, leveraging these spaces commonly faces optimization challenges due to the nonstationarity of RL. In this work, we identify key factors that determine the success and failure of training hyperbolic deep RL agents. By analyzing the gradients of core operations in the Poincaré Ball and Hyperboloid models of hyperbolic geometry, we show that large-norm embeddings destabilize gradient-based training, leading to trust-region violations in proximal policy optimization (PPO). Based on these insights, we introduce Hyper++, a new hyperbolic PPO agent that consists of three components: (i) stable critic training through a categorical value loss instead of regression; (ii) feature regularization guaranteeing bounded norms while avoiding the curse of dimensionality from clipping; and (iii) using a more optimization-friendly formulation of hyperbolic network layers. In experiments on ProcGen, we show that Hyper++ guarantees stable learning, outperforms prior hyperbolic agents, and reduces wall-clock time by approximately 30%. On Atari-5 with Double DQN, Hyper++ strongly outperforms Euclidean and hyperbolic baselines. We release our code at https://github.com/Probabilistic-and-Interactive-ML/hyper-rl .

