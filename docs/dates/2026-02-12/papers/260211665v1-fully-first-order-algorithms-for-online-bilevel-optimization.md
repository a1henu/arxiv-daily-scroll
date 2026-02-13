---
layout: default
title: Fully First-Order Algorithms for Online Bilevel Optimization
---

# Fully First-Order Algorithms for Online Bilevel Optimization
**arXiv**：[2602.11665v1](https://arxiv.org/abs/2602.11665) · [PDF](https://arxiv.org/pdf/2602.11665.pdf)  
**作者**：Tingkai Jia, Cheng Chen  

**一句话要点**：提出全一阶算法以解决在线双层优化中的高计算成本问题

**关键词**：在线双层优化, 全一阶算法, 非凸优化, 遗憾分析, 自适应迭代

## 3 点简述
- 研究非凸-强凸在线双层优化，现有方法依赖Hessian-向量积导致高计算开销
- 通过重构为带不等式约束的单层在线问题，消除隐式微分需求，实现全一阶算法
- 理论保证达到O(1 + V_T + H_{2,T})遗憾，改进变体自适应内迭代，遗憾为O(√T + V_T)

## 摘要（原文）

> In this work, we study non-convex-strongly-convex online bilevel optimization (OBO). Existing OBO algorithms are mainly based on hypergradient descent, which requires access to a Hessian-vector product (HVP) oracle and potentially incurs high computational costs. By reformulating the original OBO problem as a single-level online problem with inequality constraints and constructing a sequence of Lagrangian function, we eliminate the need for HVPs arising from implicit differentiation. Specifically, we propose a fully first-order algorithm for OBO, and provide theoretical guarantees showing that it achieves regret of $O(1 + V_T + H_{2,T})$. Furthermore, we develop an improved variant with an adaptive inner-iteration scheme, which removes the dependence on the drift variation of the inner-level optimal solution and achieves regret of $O(\sqrt{T} + V_T)$. This regret have the advatange when $V_{T}\ge O(\sqrt{T})$.

