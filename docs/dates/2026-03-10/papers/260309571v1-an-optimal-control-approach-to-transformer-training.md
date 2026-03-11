---
layout: default
title: An Optimal Control Approach To Transformer Training
---

# An Optimal Control Approach To Transformer Training
**arXiv**：[2603.09571v1](https://arxiv.org/abs/2603.09571) · [PDF](https://arxiv.org/pdf/2603.09571.pdf)  
**作者**：Kağan Akman, Naci Saldı, Serdar Yüksel  

**一句话要点**：提出基于最优控制的Transformer训练方法，以解决结构约束下的全局优化问题。

**关键词**：Transformer训练, 最优控制, McKean-Vlasov动力学, 概率测度提升, 全局优化, 量化训练

## 3 点简述
- 核心问题：Transformer训练需满足输入独立性、集合控制和位置依赖等结构约束。
- 方法要点：将Transformer建模为无噪声McKean-Vlasov动力学的粒子系统，通过提升到概率测度构建MDP。
- 实验或效果：证明存在全局最优策略，提出三重量化训练，确保稳定性和经验一致性。

## 摘要（原文）

> In this paper, we develop a rigorous optimal control-theoretic approach to Transformer training that respects key structural constraints such as (i) realized-input-independence during execution, (ii) the ensemble control nature of the problem, and (iii) positional dependence. We model the Transformer architecture as a discrete-time controlled particle system with shared actions, exhibiting noise-free McKean-Vlasov dynamics. While the resulting dynamics is not Markovian, we show that lifting it to probability measures produces a fully-observed Markov decision process (MDP). Positional encodings are incorporated into the state space to preserve the sequence order under lifting.
>   Using the dynamic programming principle, we establish the existence of globally optimal policies under mild assumptions of compactness. We further prove that closed-loop policies in the lifted is equivalent to an initial-distribution dependent open-loop policy, which are realized-input-independent and compatible with standard Transformer training.
>   To train a Transformer, we propose a triply quantized training procedure for the lifted MDP by quantizing the state space, the space of probability measures, and the action space, and show that any optimal policy for the triply quantized model is near-optimal for the original training problem.
>   Finally, we establish stability and empirical consistency properties of the lifted model by showing that the value function is continuous with respect to the perturbations of the initial empirical measures and convergence of policies as the data size increases. This approach provides a globally optimal and robust alternative to gradient-based training without requiring smoothness or convexity.

