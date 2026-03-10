---
layout: default
title: PolyFormer: learning efficient reformulations for scalable optimization under complex physical constraints
---

# PolyFormer: learning efficient reformulations for scalable optimization under complex physical constraints
**arXiv**：[2603.08283v1](https://arxiv.org/abs/2603.08283) · [PDF](https://arxiv.org/pdf/2603.08283.pdf)  
**作者**：Yilin Wen, Yi Guo, Bo Zhao, Wei Qi, Zechun Hu, Colin Jones, Jian Sun  

**一句话要点**：提出PolyFormer以简化复杂物理约束下的可扩展优化问题

**关键词**：物理信息机器学习, 约束优化, 多面体重构, 可扩展计算, 优化求解器

## 3 点简述
- 核心问题：现实优化受复杂物理定律约束，计算可扩展性受限。
- 方法要点：学习几何结构，转化为高效多面体重构，解耦问题复杂度。
- 实验或效果：在三个问题中实现最高6,400倍加速和99.87%内存减少，保持解质量。

## 摘要（原文）

> Real-world optimization problems are often constrained by complex physical laws that limit computational scalability. These constraints are inherently tied to complex regions, and thus learning models that incorporate physical and geometric knowledge, i.e., physics-informed machine learning (PIML), offer a promising pathway for efficient solution. Here, we introduce PolyFormer, which opens a new direction for PIML in prescriptive optimization tasks, where physical and geometric knowledge is not merely used to regularize learning models, but to simplify the problems themselves. PolyFormer captures geometric structures behind constraints and transforms them into efficient polytopic reformulations, thereby decoupling problem complexity from solution difficulty and enabling off-the-shelf optimization solvers to efficiently produce feasible solutions with acceptable optimality loss. Through evaluations across three important problems (large-scale resource aggregation, network-constrained optimization, and optimization under uncertainty), PolyFormer achieves computational speedups up to 6,400-fold and memory reductions up to 99.87%, while maintaining solution quality competitive with or superior to state-of-the-art methods. These results demonstrate that PolyFormer provides an efficient and reliable solution for scalable constrained optimization, expanding the scope of PIML to prescriptive tasks in scientific discovery and engineering applications.

