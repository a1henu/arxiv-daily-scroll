---
layout: default
title: Achieving Better Local Regret Bound for Online Non-Convex Bilevel Optimization
---

# Achieving Better Local Regret Bound for Online Non-Convex Bilevel Optimization
**arXiv**：[2602.06457v1](https://arxiv.org/abs/2602.06457) · [PDF](https://arxiv.org/pdf/2602.06457.pdf)  
**作者**：Tingkai Jia, Haiguang Wang, Cheng Chen  

**一句话要点**：提出在线双层优化算法，实现标准与窗口平均局部遗憾的最优界

**关键词**：在线双层优化, 局部遗憾界, 梯度评估, 窗口分析, 机器学习优化

## 3 点简述
- 针对在线双层优化中局部遗憾界最优性未知的问题
- 设计算法分别达到标准遗憾Ω(1+V_T)和窗口平均遗憾Ω(T/W^2)的最优界
- 实验验证理论结果并展示方法的实际有效性

## 摘要（原文）

> Online bilevel optimization (OBO) has emerged as a powerful framework for many machine learning problems. Prior works have developed several algorithms that minimize the standard bilevel local regret or the window-averaged bilevel local regret of the OBO problem, but the optimality of existing regret bounds remains unclear. In this work, we establish optimal regret bounds for both settings. For standard bilevel local regret, we propose an algorithm that achieves the optimal regret $Ω(1+V_T)$ with at most $O(T\log T)$ total inner-level gradient evaluations. We further develop a fully single-loop algorithm whose regret bound includes an additional gradient-variation terms. For the window-averaged bilevel local regret, we design an algorithm that captures sublinear environmental variation through a window-based analysis and achieves the optimal regret $Ω(T/W^2)$. Experiments validate our theoretical findings and demonstrate the practical effectiveness of the proposed methods.

