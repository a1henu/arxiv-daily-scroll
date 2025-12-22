---
layout: default
title: Distributed Learning in Markovian Restless Bandits over Interference Graphs for Stable Spectrum Sharing
---

# Distributed Learning in Markovian Restless Bandits over Interference Graphs for Stable Spectrum Sharing
**arXiv**：[2512.17161v1](https://arxiv.org/abs/2512.17161) · [PDF](https://arxiv.org/pdf/2512.17161.pdf)  
**作者**：Liad Lea Didi, Kobi Cohen  

**一句话要点**：提出SMILE算法以解决干扰图下多认知实体频谱共享的稳定分配问题

**关键词**：分布式学习, 马尔可夫多臂赌博机, 干扰图, 频谱共享, 稳定匹配, 通信约束网络

## 3 点简述
- 研究干扰图建模的无线网络中多认知实体的分布式频谱共享，目标为全局稳定且干扰感知的信道分配
- 开发SMILE算法，结合未知马尔可夫奖励的分布式学习与图约束协调，实现探索与利用的平衡
- 证明算法收敛至最优稳定分配，仿真验证其鲁棒性、可扩展性和效率

## 摘要（原文）

> We study distributed learning for spectrum access and sharing among multiple cognitive communication entities, such as cells, subnetworks, or cognitive radio users (collectively referred to as cells), in communication-constrained wireless networks modeled by interference graphs. Our goal is to achieve a globally stable and interference-aware channel allocation. Stability is defined through a generalized Gale-Shapley multi-to-one matching, a well-established solution concept in wireless resource allocation. We consider wireless networks where L cells share S orthogonal channels and cannot simultaneously use the same channel as their neighbors. Each channel evolves as an unknown restless Markov process with cell-dependent rewards, making this the first work to establish global Gale-Shapley stability for channel allocation in a stochastic, temporally varying restless environment. To address this challenge, we develop SMILE (Stable Multi-matching with Interference-aware LEarning), a communication-efficient distributed learning algorithm that integrates restless bandit learning with graph-constrained coordination. SMILE enables cells to distributedly balance exploration of unknown channels with exploitation of learned information. We prove that SMILE converges to the optimal stable allocation and achieves logarithmic regret relative to a genie with full knowledge of expected utilities. Simulations validate the theoretical guarantees and demonstrate SMILE's robustness, scalability, and efficiency across diverse spectrum-sharing scenarios.

