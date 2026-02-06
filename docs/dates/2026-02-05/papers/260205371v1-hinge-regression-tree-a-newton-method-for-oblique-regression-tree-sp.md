---
layout: default
title: Hinge Regression Tree: A Newton Method for Oblique Regression Tree Splitting
---

# Hinge Regression Tree: A Newton Method for Oblique Regression Tree Splitting
**arXiv**：[2602.05371v1](https://arxiv.org/abs/2602.05371) · [PDF](https://arxiv.org/pdf/2602.05371.pdf)  
**作者**：Hongyi Li, Han Lin, Jun Xu  

**一句话要点**：提出Hinge回归树以高效学习斜决策树分裂，通过牛顿方法优化非线性最小二乘问题。

**关键词**：斜决策树, 牛顿方法, 非线性最小二乘, 回归树, 通用逼近器, 机器学习基准

## 3 点简述
- 斜决策树学习高质量分裂是NP难问题，现有方法依赖慢速搜索或启发式。
- HRT将分裂重构为非线性最小二乘问题，采用阻尼牛顿法进行交替拟合，保证单调收敛。
- 在合成和真实基准测试中，HRT以更紧凑结构匹配或超越单树基线，具有通用逼近能力。

## 摘要（原文）

> Oblique decision trees combine the transparency of trees with the power of multivariate decision boundaries, but learning high-quality oblique splits is NP-hard, and practical methods still rely on slow search or theory-free heuristics. We present the Hinge Regression Tree (HRT), which reframes each split as a non-linear least-squares problem over two linear predictors whose max/min envelope induces ReLU-like expressive power. The resulting alternating fitting procedure is exactly equivalent to a damped Newton (Gauss-Newton) method within fixed partitions. We analyze this node-level optimization and, for a backtracking line-search variant, prove that the local objective decreases monotonically and converges; in practice, both fixed and adaptive damping yield fast, stable convergence and can be combined with optional ridge regularization. We further prove that HRT's model class is a universal approximator with an explicit $O(δ^2)$ approximation rate, and show on synthetic and real-world benchmarks that it matches or outperforms single-tree baselines with more compact structures.

