---
layout: default
title: Invariance-Based Dynamic Regret Minimization
---

# Invariance-Based Dynamic Regret Minimization
**arXiv**：[2603.03843v1](https://arxiv.org/abs/2603.03843) · [PDF](https://arxiv.org/pdf/2603.03843.pdf)  
**作者**：Margherita Lazzaretto, Jonas Peters, Niklas Pfister  

**一句话要点**：提出ISD-linUCB算法，利用历史数据学习奖励模型不变性以优化非平稳线性赌博机动态遗憾。

**关键词**：非平稳线性赌博机, 动态遗憾最小化, 不变性学习, 在线学习, 奖励模型分解, ISD-linUCB算法

## 3 点简述
- 研究非平稳线性赌博机问题，奖励模型参数随时间变化，历史数据可能包含部分有用信息。
- 假设奖励模型分解为平稳与非平稳成分，利用历史数据学习不变性以降低问题维度。
- 理论与实验表明，在快速变化环境中，利用不变性可显著减少动态遗憾，提升在线性能。

## 摘要（原文）

> We consider stochastic non-stationary linear bandits where the linear parameter connecting contexts to the reward changes over time. Existing algorithms in this setting localize the policy by gradually discarding or down-weighting past data, effectively shrinking the time horizon over which learning can occur. However, in many settings historical data may still carry partial information about the reward model. We propose to leverage such data while adapting to changes, by assuming the reward model decomposes into stationary and non-stationary components. Based on this assumption, we introduce ISD-linUCB, an algorithm that uses past data to learn invariances in the reward model and subsequently exploits them to improve online performance. We show both theoretically and empirically that leveraging invariance reduces the problem dimensionality, yielding significant regret improvements in fast-changing environments when sufficient historical data is available.

