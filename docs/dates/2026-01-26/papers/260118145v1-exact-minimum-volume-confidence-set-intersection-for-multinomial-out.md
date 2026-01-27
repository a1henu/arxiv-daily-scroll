---
layout: default
title: Exact Minimum-Volume Confidence Set Intersection for Multinomial Outcomes
---

# Exact Minimum-Volume Confidence Set Intersection for Multinomial Outcomes
**arXiv**：[2601.18145v1](https://arxiv.org/abs/2601.18145) · [PDF](https://arxiv.org/pdf/2601.18145.pdf)  
**作者**：Heguang Lin, Binhao Chen, Mengze Li, Daniel Pimentel-Alarcón, Matthew L. Malloy  

**一句话要点**：提出认证算法以解决多项分布最小体积置信集交集判定问题

**关键词**：置信集计算, 多项分布, A/B测试, 几何划分, 认证算法, 参数空间优化

## 3 点简述
- 核心问题：多项分布参数的最小体积置信集因p值不连续而难以直接计算交集
- 方法要点：利用似然排序在log-odds坐标中诱导半空间约束，实现参数空间自适应几何划分
- 实验或效果：针对三类别设计高效认证算法，可判定交集、不相交或不确定结果

## 摘要（原文）

> Computation of confidence sets is central to data science and machine learning, serving as the workhorse of A/B testing and underpinning the operation and analysis of reinforcement learning algorithms. Among all valid confidence sets for the multinomial parameter, minimum-volume confidence sets (MVCs) are optimal in that they minimize average volume, but they are defined as level sets of an exact p-value that is discontinuous and difficult to compute. Rather than attempting to characterize the geometry of MVCs directly, this paper studies a practically motivated decision problem: given two observed multinomial outcomes, can one certify whether their MVCs intersect? We present a certified, tolerance-aware algorithm for this intersection problem. The method exploits the fact that likelihood ordering induces halfspace constraints in log-odds coordinates, enabling adaptive geometric partitioning of parameter space and computable lower and upper bounds on p-values over each cell. For three categories, this yields an efficient and provably sound algorithm that either certifies intersection, certifies disjointness, or returns an indeterminate result when the decision lies within a prescribed margin. We further show how the approach extends to higher dimensions. The results demonstrate that, despite their irregular geometry, MVCs admit reliable certified decision procedures for core tasks in A/B testing.

