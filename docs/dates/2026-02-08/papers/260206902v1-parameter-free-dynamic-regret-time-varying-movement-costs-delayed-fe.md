---
layout: default
title: Parameter-free Dynamic Regret: Time-varying Movement Costs, Delayed Feedback, and Memory
---

# Parameter-free Dynamic Regret: Time-varying Movement Costs, Delayed Feedback, and Memory
**arXiv**：[2602.06902v1](https://arxiv.org/abs/2602.06902) · [PDF](https://arxiv.org/pdf/2602.06902.pdf)  
**作者**：Emmanuel Esposito, Andrew Jacobsen, Hao Qiu, Mengxiao Zhang  

**一句话要点**：提出参数自由动态遗憾算法，处理时变移动成本、延迟反馈和记忆的在线凸优化问题。

**关键词**：在线凸优化, 动态遗憾, 时变移动成本, 延迟反馈, 比较器自适应, 参数自由算法

## 3 点简述
- 研究在线凸优化中时变移动成本的动态遗憾问题，允许移动成本系数任意变化。
- 设计新算法实现比较器自适应的动态遗憾界，恢复静态和动态遗憾的最优保证。
- 将延迟反馈和时变记忆问题转化为时变移动成本，展示结果的多功能性和独立兴趣。

## 摘要（原文）

> In this paper, we study dynamic regret in unconstrained online convex optimization (OCO) with movement costs. Specifically, we generalize the standard setting by allowing the movement cost coefficients $λ_t$ to vary arbitrarily over time. Our main contribution is a novel algorithm that establishes the first comparator-adaptive dynamic regret bound for this setting, guaranteeing $\widetilde{\mathcal{O}}(\sqrt{(1+P_T)(T+\sum_t λ_t)})$ regret, where $P_T$ is the path length of the comparator sequence over $T$ rounds. This recovers the optimal guarantees for both static and dynamic regret in standard OCO as a special case where $λ_t=0$ for all rounds. To demonstrate the versatility of our results, we consider two applications: OCO with delayed feedback and OCO with time-varying memory. We show that both problems can be translated into time-varying movement costs, establishing a novel reduction specifically for the delayed feedback setting that is of independent interest. A crucial observation is that the first-order dependence on movement costs in our regret bound plays a key role in enabling optimal comparator-adaptive dynamic regret guarantees in both settings.

