---
layout: default
title: Operationalizing Stein's Method for Online Linear Optimization: CLT-Based Optimal Tradeoffs
---

# Operationalizing Stein's Method for Online Linear Optimization: CLT-Based Optimal Tradeoffs
**arXiv**：[2602.06545v1](https://arxiv.org/abs/2602.06545) · [PDF](https://arxiv.org/pdf/2602.06545.pdf)  
**作者**：Zhiyu Zhang, Aaditya Ramdas  

**一句话要点**：提出基于Stein方法的在线线性优化算法，实现计算高效且性能尖锐的对抗性优化

**关键词**：在线线性优化, Stein方法, 对抗性优化, 计算效率, 性能权衡, 中心极限定理

## 3 点简述
- 核心问题：对抗性在线线性优化中性能权衡与计算效率的平衡难题
- 方法要点：利用Stein方法构建算法，实现加性尖锐的遗憾与总损失上界
- 实验或效果：算法在计算复杂度相同下优于OGD和MWU，支持连续最优权衡

## 摘要（原文）

> Adversarial online linear optimization (OLO) is essentially about making performance tradeoffs with respect to the unknown difficulty of the adversary. In the setting of one-dimensional fixed-time OLO on a bounded domain, it has been observed since Cover (1966) that achievable tradeoffs are governed by probabilistic inequalities, and these descriptive results can be converted into algorithms via dynamic programming, which, however, is not computationally efficient. We address this limitation by showing that Stein's method, a classical framework underlying the proofs of probabilistic limit theorems, can be operationalized as computationally efficient OLO algorithms. The associated regret and total loss upper bounds are "additively sharp", meaning that they surpass the conventional big-O optimality and match normal-approximation-based lower bounds by additive lower order terms. Our construction is inspired by the remarkably clean proof of a Wasserstein martingale central limit theorem (CLT) due to Röllin (2018).
>   Several concrete benefits can be obtained from this general technique. First, with the same computational complexity, the proposed algorithm improves upon the total loss upper bounds of online gradient descent (OGD) and multiplicative weight update (MWU). Second, our algorithm can realize a continuum of optimal two-point tradeoffs between the total loss and the maximum regret over comparators, improving upon prior works in parameter-free online learning. Third, by allowing the adversary to randomize on an unbounded support, we achieve sharp in-expectation performance guarantees for OLO with noisy feedback.

