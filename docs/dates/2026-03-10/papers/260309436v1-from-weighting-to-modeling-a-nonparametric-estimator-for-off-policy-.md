---
layout: default
title: From Weighting to Modeling: A Nonparametric Estimator for Off-Policy Evaluation
---

# From Weighting to Modeling: A Nonparametric Estimator for Off-Policy Evaluation
**arXiv**：[2603.09436v1](https://arxiv.org/abs/2603.09436) · [PDF](https://arxiv.org/pdf/2603.09436.pdf)  
**作者**：Rong J. B. Zhu  

**一句话要点**：提出非参数加权方法以解决上下文赌博机中离策略评估的高方差问题

**关键词**：离策略评估, 上下文赌博机, 非参数加权, 方差减少, 奖励建模, 值估计

## 3 点简述
- 核心问题：离策略评估中逆概率加权方法因分母概率导致高方差，现有方法未直接解决此问题。
- 方法要点：引入非参数加权方法构建权重，结合奖励预测形成模型辅助非参数加权，降低方差并保持低偏差。
- 实验或效果：实证比较显示，该方法在值估计中实现更低方差，同时维持低偏差，优于现有技术。

## 摘要（原文）

> We study off-policy evaluation in the setting of contextual bandits, where we aim to evaluate a new policy using historical data that consists of contexts, actions and received rewards. This historical data typically does not faithfully represent action distribution of the new policy accurately. A common approach, inverse probability weighting (IPW), adjusts for these discrepancies in action distributions. However, this method often suffers from high variance due to the probability being in the denominator. The doubly robust (DR) estimator reduces variance through modeling reward but does not directly address variance from IPW. In this work, we address the limitation of IPW by proposing a Nonparametric Weighting (NW) approach that constructs weights using a nonparametric model. Our NW approach achieves low bias like IPW but typically exhibits significantly lower variance. To further reduce variance, we incorporate reward predictions -- similar to the DR technique -- resulting in the Model-assisted Nonparametric Weighting (MNW) approach. The MNW approach yields accurate value estimates by explicitly modeling and mitigating bias from reward modeling, without aiming to guarantee the standard doubly robust property. Extensive empirical comparisons show that our approaches consistently outperform existing techniques, achieving lower variance in value estimation while maintaining low bias.

