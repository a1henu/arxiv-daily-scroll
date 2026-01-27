---
layout: default
title: Optimal Use of Preferences in Artificial Intelligence Algorithms
---

# Optimal Use of Preferences in Artificial Intelligence Algorithms
**arXiv**：[2601.18732v1](https://arxiv.org/abs/2601.18732) · [PDF](https://arxiv.org/pdf/2601.18732.pdf)  
**作者**：Joshua S. Gans  

**一句话要点**：提出基于信息设计的最优偏好嵌入方法，为模块化AI管道提供理论基础。

**关键词**：偏好嵌入, 信息设计, 决策理论, 模块化AI, 后处理优化

## 3 点简述
- 核心问题：AI算法中偏好嵌入与决策分离的最优条件。
- 方法要点：利用信息递减价值条件，证明无偏好训练在期望效用决策中占优。
- 实验或效果：提供设计指导，支持后处理保留可选性或嵌入偏好自动化阈值。

## 摘要（原文）

> Machine learning systems embed preferences either in training losses or through post-processing of calibrated predictions. Applying information design methods from Strack and Yang (2024), this paper provides decision problem agnostic conditions under which separation training preference free and applying preferences ex post is optimal. Unlike prior work that requires specifying downstream objectives, the welfare results here apply uniformly across decision problems. The key primitive is a diminishing-value-of-information condition: relative to a fixed (normalised) preference-free loss, preference embedding makes informativeness less valuable at the margin, inducing a mean-preserving contraction of learned posteriors. Because the value of information is convex in beliefs, preference-free training weakly dominates for any expected utility decision problem. This provides theoretical foundations for modular AI pipelines that learn calibrated probabilities and implement asymmetric costs through downstream decision rules. However, separation requires users to implement optimal decision rules. When cognitive constraints bind, as documented in human AI decision-making, preference embedding can dominate by automating threshold computation. These results provide design guidance: preserve optionality through post-processing when objectives may shift; embed preferences when decision-stage frictions dominate.

