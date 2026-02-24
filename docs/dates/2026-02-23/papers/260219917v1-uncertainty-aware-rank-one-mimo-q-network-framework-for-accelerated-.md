---
layout: default
title: Uncertainty-Aware Rank-One MIMO Q Network Framework for Accelerated Offline Reinforcement Learning
---

# Uncertainty-Aware Rank-One MIMO Q Network Framework for Accelerated Offline Reinforcement Learning
**arXiv**：[2602.19917v1](https://arxiv.org/abs/2602.19917) · [PDF](https://arxiv.org/pdf/2602.19917.pdf)  
**作者**：Thanh Nguyen, Tung Luu, Tri Ton, Sungwoong Kim, Chang D. Yoo  

**一句话要点**：提出不确定性感知的秩一MIMO Q网络框架，以加速离线强化学习并缓解分布外数据误差。

**关键词**：离线强化学习, 不确定性量化, 秩一MIMO网络, 分布外数据, Q函数建模, 计算效率

## 3 点简述
- 核心问题：离线强化学习中分布外数据导致的推断误差，现有方法存在保守性、不精确性和高计算开销。
- 方法要点：通过量化数据不确定性并融入训练损失，结合秩一MIMO架构高效建模不确定性感知Q函数，平衡精度与效率。
- 实验或效果：在D4RL基准测试中实现先进性能，同时保持计算高效性，验证了框架的有效性。

## 摘要（原文）

> Offline reinforcement learning (RL) has garnered significant interest due to its safe and easily scalable paradigm. However, training under this paradigm presents its own challenge: the extrapolation error stemming from out-of-distribution (OOD) data. Existing methodologies have endeavored to address this issue through means like penalizing OOD Q-values or imposing similarity constraints on the learned policy and the behavior policy. Nonetheless, these approaches are often beset by limitations such as being overly conservative in utilizing OOD data, imprecise OOD data characterization, and significant computational overhead. To address these challenges, this paper introduces an Uncertainty-Aware Rank-One Multi-Input Multi-Output (MIMO) Q Network framework. The framework aims to enhance Offline Reinforcement Learning by fully leveraging the potential of OOD data while still ensuring efficiency in the learning process. Specifically, the framework quantifies data uncertainty and harnesses it in the training losses, aiming to train a policy that maximizes the lower confidence bound of the corresponding Q-function. Furthermore, a Rank-One MIMO architecture is introduced to model the uncertainty-aware Q-function, \TP{offering the same ability for uncertainty quantification as an ensemble of networks but with a cost nearly equivalent to that of a single network}. Consequently, this framework strikes a harmonious balance between precision, speed, and memory efficiency, culminating in improved overall performance. Extensive experimentation on the D4RL benchmark demonstrates that the framework attains state-of-the-art performance while remaining computationally efficient. By incorporating the concept of uncertainty quantification, our framework offers a promising avenue to alleviate extrapolation errors and enhance the efficiency of offline RL.

