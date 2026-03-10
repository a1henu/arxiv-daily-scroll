---
layout: default
title: Impact of Connectivity on Laplacian Representations in Reinforcement Learning
---

# Impact of Connectivity on Laplacian Representations in Reinforcement Learning
**arXiv**：[2603.08558v1](https://arxiv.org/abs/2603.08558) · [PDF](https://arxiv.org/pdf/2603.08558.pdf)  
**作者**：Tommaso Giorgi, Pierriccardo Olivieri, Keyue Jiang, Laura Toni, Matteo Papini  

**一句话要点**：分析连通性对强化学习中拉普拉斯表示的影响，提供近似误差上界与端到端误差分解

**关键词**：强化学习, 状态表示学习, 拉普拉斯特征向量, 代数连通性, 误差分析, 图拓扑结构

## 3 点简述
- 核心问题：大规模强化学习中状态表示学习受状态图连通性影响，现有方法基于拉普拉斯特征向量构建表示，但近似误差与图拓扑结构的关系未知
- 方法要点：证明线性值函数近似在学得谱特征下的误差上界，误差随状态图代数连通性缩放，并分解特征向量估计引入的误差
- 实验或效果：在网格世界环境中进行数值模拟，验证理论结果，适用于一般策略且无转移核对称性假设

## 摘要（原文）

> Learning compact state representations in Markov Decision Processes (MDPs) has proven crucial for addressing the curse of dimensionality in large-scale reinforcement learning (RL) problems. Existing principled approaches leverage structural priors on the MDP by constructing state representations as linear combinations of the state-graph Laplacian eigenvectors. When the transition graph is unknown or the state space is prohibitively large, the graph spectral features can be estimated directly via sample trajectories. In this work, we prove an upper bound on the approximation error of linear value function approximation under the learned spectral features. We show how this error scales with the algebraic connectivity of the state-graph, grounding the approximation quality in the topological structure of the MDP. We further bound the error introduced by the eigenvector estimation itself, leading to an end-to-end error decomposition across the representation learning pipeline. Additionally, our expression of the Laplacian operator for the RL setting, although equivalent to existing ones, prevents some common misunderstandings, of which we show some examples from the literature. Our results hold for general (non-uniform) policies without any assumptions on the symmetry of the induced transition kernel. We validate our theoretical findings with numerical simulations on gridworld environments.

