---
layout: default
title: Hinge Regression Tree: A Newton Method for Oblique Regression Tree Splitting
---

# Hinge Regression Tree: A Newton Method for Oblique Regression Tree Splitting
**arXiv**：[2602.05371v1](https://arxiv.org/abs/2602.05371) · [PDF](https://arxiv.org/pdf/2602.05371.pdf)  
**作者**：Hongyi Li, Han Lin, Jun Xu  

**一句话要点**：提出Hinge回归树，通过牛顿方法解决倾斜回归树分裂的NP难问题。

**关键词**：倾斜决策树, 牛顿方法, 回归树分裂, 非线性优化, 通用逼近器

## 3 点简述
- 倾斜决策树结合树透明性与多元决策边界，但高质量分裂学习为NP难问题。
- HRT将分裂重构为非线性最小二乘问题，采用阻尼牛顿法进行交替拟合。
- 实验表明HRT在合成和真实基准上匹配或优于基线，结构更紧凑。

## 摘要（原文）

> Oblique decision trees combine the transparency of trees with the power of multivariate decision boundaries, but learning high-quality oblique splits is NP-hard, and practical methods still rely on slow search or theory-free heuristics. We present the Hinge Regression Tree (HRT), which reframes each split as a non-linear least-squares problem over two linear predictors whose max/min envelope induces ReLU-like expressive power. The resulting alternating fitting procedure is exactly equivalent to a damped Newton (Gauss-Newton) method within fixed partitions. We analyze this node-level optimization and, for a backtracking line-search variant, prove that the local objective decreases monotonically and converges; in practice, both fixed and adaptive damping yield fast, stable convergence and can be combined with optional ridge regularization. We further prove that HRT's model class is a universal approximator with an explicit $O(δ^2)$ approximation rate, and show on synthetic and real-world benchmarks that it matches or outperforms single-tree baselines with more compact structures.

