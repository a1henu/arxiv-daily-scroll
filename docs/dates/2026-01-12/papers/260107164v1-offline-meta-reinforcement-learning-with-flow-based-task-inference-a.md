---
layout: default
title: Offline Meta-Reinforcement Learning with Flow-Based Task Inference and Adaptive Correction of Feature Overgeneralization
---

# Offline Meta-Reinforcement Learning with Flow-Based Task Inference and Adaptive Correction of Feature Overgeneralization
**arXiv**：[2601.07164v1](https://arxiv.org/abs/2601.07164) · [PDF](https://arxiv.org/pdf/2601.07164.pdf)  
**作者**：Min Wang, Xin Li, Mingzhong Wang, Hasnaa Bennis  

**一句话要点**：提出FLORA方法，通过流式任务推断和自适应特征校正解决离线元强化学习中的特征过泛化问题。

**关键词**：离线元强化学习, 特征过泛化, 流式任务推断, 自适应校正, Q值分解, OOD样本识别

## 3 点简述
- 核心问题：离线元强化学习中，Q值分解导致特征过泛化，引入估计偏差，影响策略性能。
- 方法要点：FLORA建模特征分布以识别OOD样本，集成返回反馈机制自适应调整特征，并使用可逆变换链学习精确任务表示。
- 实验或效果：理论和实验表明，FLORA相比基线方法，在多种环境中实现快速适应和元策略改进。

## 摘要（原文）

> Offline meta-reinforcement learning (OMRL) combines the strengths of learning from diverse datasets in offline RL with the adaptability to new tasks of meta-RL, promising safe and efficient knowledge acquisition by RL agents. However, OMRL still suffers extrapolation errors due to out-of-distribution (OOD) actions, compromised by broad task distributions and Markov Decision Process (MDP) ambiguity in meta-RL setups. Existing research indicates that the generalization of the $Q$ network affects the extrapolation error in offline RL. This paper investigates this relationship by decomposing the $Q$ value into feature and weight components, observing that while decomposition enhances adaptability and convergence in the case of high-quality data, it often leads to policy degeneration or collapse in complex tasks. We observe that decomposed $Q$ values introduce a large estimation bias when the feature encounters OOD samples, a phenomenon we term ''feature overgeneralization''. To address this issue, we propose FLORA, which identifies OOD samples by modeling feature distributions and estimating their uncertainties. FLORA integrates a return feedback mechanism to adaptively adjust feature components. Furthermore, to learn precise task representations, FLORA explicitly models the complex task distribution using a chain of invertible transformations. We theoretically and empirically demonstrate that FLORA achieves rapid adaptation and meta-policy improvement compared to baselines across various environments.

