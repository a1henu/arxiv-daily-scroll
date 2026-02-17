---
layout: default
title: Parameter-Minimal Neural DE Solvers via Horner Polynomials
---

# Parameter-Minimal Neural DE Solvers via Horner Polynomials
**arXiv**：[2602.14737v1](https://arxiv.org/abs/2602.14737) · [PDF](https://arxiv.org/pdf/2602.14737.pdf)  
**作者**：T. Matulić, D. Seršić  

**一句话要点**：提出基于霍纳多项式的参数最小化神经网络架构以高效求解微分方程

**关键词**：微分方程求解, 霍纳多项式, 参数最小化, 神经网络架构, 科学建模, 分段连续

## 3 点简述
- 核心问题：传统神经网络求解微分方程参数多，计算资源需求高，影响科学建模效率
- 方法要点：限制假设类为霍纳分解多项式，构建隐式可微试解，通过固定低阶自由度精确满足初始条件
- 实验或效果：在ODE基准和热方程示例中，数十参数模型准确匹配解及其导数，优于小MLP和正弦表示基线

## 摘要（原文）

> We propose a parameter-minimal neural architecture for solving differential equations by restricting the hypothesis class to Horner-factorized polynomials, yielding an implicit, differentiable trial solution with only a small set of learnable coefficients. Initial conditions are enforced exactly by construction by fixing the low-order polynomial degrees of freedom, so training focuses solely on matching the differential-equation residual at collocation points. To reduce approximation error without abandoning the low-parameter regime, we introduce a piecewise ("spline-like") extension that trains multiple small Horner models on subintervals while enforcing continuity (and first-derivative continuity) at segment boundaries. On illustrative ODE benchmarks and a heat-equation example, Horner networks with tens (or fewer) parameters accurately match the solution and its derivatives and outperform small MLP and sinusoidal-representation baselines under the same training settings, demonstrating a practical accuracy-parameter trade-off for resource-efficient scientific modeling.

