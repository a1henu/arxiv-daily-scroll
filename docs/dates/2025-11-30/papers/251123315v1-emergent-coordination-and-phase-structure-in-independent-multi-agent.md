---
layout: default
title: Emergent Coordination and Phase Structure in Independent Multi-Agent Reinforcement Learning
---

# Emergent Coordination and Phase Structure in Independent Multi-Agent Reinforcement Learning
**arXiv**：[2511.23315v1](https://arxiv.org/abs/2511.23315) · [PDF](https://arxiv.org/pdf/2511.23315.pdf)  
**作者**：Azusa Yamaguchi  

**一句话要点**：揭示独立多智能体强化学习中基于核漂移的协调相结构

**关键词**：多智能体强化学习, 独立Q学习, 相结构分析, 核漂移, 协调动力学, 去中心化系统

## 3 点简述
- 研究去中心化MARL中协调涌现、波动或崩溃的动力学机制
- 通过大规模实验构建相图，识别稳定协调、脆弱过渡和混乱相
- 发现核漂移与同步的竞争驱动相变，小不对称性是关键因素

## 摘要（原文）

> A clearer understanding of when coordination emerges, fluctuates, or collapses in decentralized multi-agent reinforcement learning (MARL) is increasingly sought in order to characterize the dynamics of multi-agent learning systems. We revisit fully independent Q-learning (IQL) as a minimal decentralized testbed and run large-scale experiments across environment size L and agent density rho. We construct a phase map using two axes - the cooperative success rate (CSR) and a stability index derived from TD-error variance - revealing three distinct regimes: a coordinated and stable phase, a fragile transition region, and a jammed or disordered phase. A sharp double Instability Ridge separates these regimes and corresponds to persistent kernel drift, the time-varying shift of each agent's effective transition kernel induced by others' policy updates. Synchronization analysis further shows that temporal alignment is required for sustained cooperation, and that competition between drift and synchronization generates the fragile regime. Removing agent identifiers eliminates drift entirely and collapses the three-phase structure, demonstrating that small inter-agent asymmetries are a necessary driver of drift. Overall, the results show that decentralized MARL exhibits a coherent phase structure governed by the interaction between scale, density, and kernel drift, suggesting that emergent coordination behaves as a distribution-interaction-driven phase phenomenon.

