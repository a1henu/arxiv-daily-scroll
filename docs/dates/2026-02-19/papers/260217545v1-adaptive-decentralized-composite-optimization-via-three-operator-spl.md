---
layout: default
title: Adaptive Decentralized Composite Optimization via Three-Operator Splitting
---

# Adaptive Decentralized Composite Optimization via Three-Operator Splitting
**arXiv**：[2602.17545v1](https://arxiv.org/abs/2602.17545) · [PDF](https://arxiv.org/pdf/2602.17545.pdf)  
**作者**：Xiaokai Chen, Ilya Kuruzov, Gesualdo Scutari  

**一句话要点**：提出自适应去中心化复合优化方法，通过三算子分裂解决网络优化问题。

**关键词**：去中心化优化, 复合优化, 三算子分裂, 自适应步长, 网络优化, 收敛分析

## 3 点简述
- 研究去中心化网络优化，最小化局部平滑凸损失与非平滑凸扩展值项之和。
- 基于三算子分裂因子化，引入BCV预条件度量，实现自适应步长调整与轻量共识协议。
- 理论证明收敛性，数值实验验证自适应步长策略的有效性。

## 摘要（原文）

> The paper studies decentralized optimization over networks, where agents minimize a sum of {\it locally} smooth (strongly) convex losses and plus a nonsmooth convex extended value term. We propose decentralized methods wherein agents {\it adaptively} adjust their stepsize via local backtracking procedures coupled with lightweight min-consensus protocols. Our design stems from a three-operator splitting factorization applied to an equivalent reformulation of the problem. The reformulation is endowed with a new BCV preconditioning metric (Bertsekas-O'Connor-Vandenberghe), which enables efficient decentralized implementation and local stepsize adjustments. We establish robust convergence guarantees. Under mere convexity, the proposed methods converge with a sublinear rate. Under strong convexity of the sum-function, and assuming the nonsmooth component is partly smooth, we further prove linear convergence. Numerical experiments corroborate the theory and highlight the effectiveness of the proposed adaptive stepsize strategy.

