---
layout: default
title: A Fully First-Order Layer for Differentiable Optimization
---

# A Fully First-Order Layer for Differentiable Optimization
**arXiv**：[2512.02494v1](https://arxiv.org/abs/2512.02494) · [PDF](https://arxiv.org/pdf/2512.02494.pdf)  
**作者**：Zihao Zhao, Kai-Chia Mo, Shing-Hei Ho, Brandon Amos, Kai Wang  

## 摘要（原文）

> Differentiable optimization layers enable learning systems to make decisions by solving embedded optimization problems. However, computing gradients via implicit differentiation requires solving a linear system with Hessian terms, which is both compute- and memory-intensive. To address this challenge, we propose a novel algorithm that computes the gradient using only first-order information. The key insight is to rewrite the differentiable optimization as a bilevel optimization problem and leverage recent advances in bilevel methods. Specifically, we introduce an active-set Lagrangian hypergradient oracle that avoids Hessian evaluations and provides finite-time, non-asymptotic approximation guarantees. We show that an approximate hypergradient can be computed using only first-order information in $\tilde{\oo}(1)$ time, leading to an overall complexity of $\tilde{\oo}(δ^{-1}ε^{-3})$ for constrained bilevel optimization, which matches the best known rate for non-smooth non-convex optimization. Furthermore, we release an open-source Python library that can be easily adapted from existing solvers. Our code is available here: https://github.com/guaguakai/FFOLayer.

