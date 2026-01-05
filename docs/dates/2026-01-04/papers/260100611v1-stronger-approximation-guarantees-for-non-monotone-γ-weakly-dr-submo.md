---
layout: default
title: Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization
---

# Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization
**arXiv**：[2601.00611v1](https://arxiv.org/abs/2601.00611) · [PDF](https://arxiv.org/pdf/2601.00611.pdf)  
**作者**：Hareshkumar Jadav, Ranveer Singh, Vaneet Aggarwal  

**一句话要点**：提出基于Frank-Wolfe和双贪婪的算法，用于非单调γ-弱DR-次模函数在向下封闭凸体上的最大化问题。

**关键词**：次模优化, 非单调函数, 近似算法, 向下封闭凸体, γ-弱DR-次模性

## 3 点简述
- 研究非单调γ-弱DR-次模函数在向下封闭凸体上的最大化问题，这是机器学习和优化中的基础问题。
- 结合Frank-Wolfe引导的连续贪婪框架和γ感知的双贪婪步骤，处理非单调性，提供简单有效的算法。
- 算法保证随γ平滑变化，当γ=1时恢复0.401近似比，对γ<1提供优于先前报告的近似保证。

## 摘要（原文）

> Maximizing submodular objectives under constraints is a fundamental problem in machine learning and optimization. We study the maximization of a nonnegative, non-monotone $γ$-weakly DR-submodular function over a down-closed convex body. Our main result is an approximation algorithm whose guarantee depends smoothly on $γ$; in particular, when $γ=1$ (the DR-submodular case) our bound recovers the $0.401$ approximation factor, while for $γ<1$ the guarantee degrades gracefully and, it improves upon previously reported bounds for $γ$-weakly DR-submodular maximization under the same constraints. Our approach combines a Frank-Wolfe-guided continuous-greedy framework with a $γ$-aware double-greedy step, yielding a simple yet effective procedure for handling non-monotonicity. This results in state-of-the-art guarantees for non-monotone $γ$-weakly DR-submodular maximization over down-closed convex bodies.

