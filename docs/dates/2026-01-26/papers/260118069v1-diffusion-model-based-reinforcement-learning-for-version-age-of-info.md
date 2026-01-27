---
layout: default
title: Diffusion Model-based Reinforcement Learning for Version Age of Information Scheduling: Average and Tail-Risk-Sensitive Control
---

# Diffusion Model-based Reinforcement Learning for Version Age of Information Scheduling: Average and Tail-Risk-Sensitive Control
**arXiv**：[2601.18069v1](https://arxiv.org/abs/2601.18069) · [PDF](https://arxiv.org/pdf/2601.18069.pdf)  
**作者**：Haoyuan Pan, Sizhao Chen, Zhaorui Wang, Tse-Tin Chan  

**一句话要点**：提出基于扩散模型的强化学习算法，用于多用户无线系统中版本信息年龄的平均和尾部风险敏感调度。

**关键词**：版本信息年龄调度, 扩散模型强化学习, 尾部风险敏感控制, 多用户无线系统, 条件风险价值优化

## 3 点简述
- 核心问题：现有版本信息年龄调度方法主要关注最小化平均值，忽略了随机包到达和不可靠信道下罕见但严重的陈旧事件，可能影响可靠性。
- 方法要点：首先提出D2SAC算法，通过扩散去噪过程生成动作，优化平均性能；然后提出RS-D3SAC算法，结合扩散行动器和基于分位数的分布评论家，显式建模返回分布，实现基于CVaR的尾部风险优化。
- 实验或效果：模拟显示D2SAC降低平均版本信息年龄，RS-D3SAC在保持平均性能的同时显著减少CVaR，分布评论家主导尾部风险降低，扩散行动器提供补充细化。

## 摘要（原文）

> Ensuring timely and semantically accurate information delivery is critical in real-time wireless systems. While Age of Information (AoI) quantifies temporal freshness, Version Age of Information (VAoI) captures semantic staleness by accounting for version evolution between transmitters and receivers. Existing VAoI scheduling approaches primarily focus on minimizing average VAoI, overlooking rare but severe staleness events that can compromise reliability under stochastic packet arrivals and unreliable channels. This paper investigates both average-oriented and tail-risk-sensitive VAoI scheduling in a multi-user status update system with long-term transmission cost constraints. We first formulate the average VAoI minimization problem as a constrained Markov decision process and introduce a deep diffusion-based Soft Actor-Critic (D2SAC) algorithm. By generating actions through a diffusion-based denoising process, D2SAC enhances policy expressiveness and establishes a strong baseline for mean performance. Building on this foundation, we put forth RS-D3SAC, a risk-sensitive deep distributional diffusion-based Soft Actor-Critic algorithm. RS-D3SAC integrates a diffusion-based actor with a quantile-based distributional critic, explicitly modeling the full VAoI return distribution. This enables principled tail-risk optimization via Conditional Value-at-Risk (CVaR) while satisfying long-term transmission cost constraints. Extensive simulations show that, while D2SAC reduces average VAoI, RS-D3SAC consistently achieves substantial reductions in CVaR without sacrificing mean performance. The dominant gain in tail-risk reduction stems from the distributional critic, with the diffusion-based actor providing complementary refinement to stabilize and enrich policy decisions, highlighting their effectiveness for robust and risk-aware VAoI scheduling in multi-user wireless systems.

