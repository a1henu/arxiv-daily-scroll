---
layout: default
title: Towards Bound Consistency for the No-Overlap Constraint Using MDDs
---

# Towards Bound Consistency for the No-Overlap Constraint Using MDDs
**arXiv**：[2601.14784v1](https://arxiv.org/abs/2601.14784) · [PDF](https://arxiv.org/pdf/2601.14784.pdf)  
**作者**：Amaury Guichard, Laurent Michel, Hélène Verhaeghe, Pierre Schaus  

**一句话要点**：提出基于MDD的边界一致性算法以强化无重叠约束的过滤

**关键词**：无重叠约束, 边界一致性, 多值决策图, 约束规划, 过滤算法, 排序问题

## 3 点简述
- 核心问题：无重叠约束的边界一致性计算是NP完全问题，需高效近似方法。
- 方法要点：利用MDD提取作业时间窗口边界，多项式时间内收紧起止时间，并限制MDD宽度以控制复杂度。
- 实验效果：在带时间窗口的排序问题中，相比现有算法，显著减少搜索树节点数和求解时间。

## 摘要（原文）

> Achieving bound consistency for the no-overlap constraint is known to be NP-complete. Therefore, several polynomial-time tightening techniques, such as edge finding, not-first-not-last reasoning, and energetic reasoning, have been introduced for this constraint. In this work, we derive the first bound-consistent algorithm for the no-overlap constraint. By building on the no-overlap MDD defined by Ciré and van Hoeve, we extract bounds of the time window of the jobs, allowing us to tighten start and end times in time polynomial in the number of nodes of the MDD. Similarly, to bound the size and time-complexity, we limit the width of the MDD to a threshold, creating a relaxed MDD that can also be used to relax the bound-consistent filtering. Through experiments on a sequencing problem with time windows and a just-in-time objective ($1 \mid r_j, d_j, \bar{d}_j \mid \sum E_j + \sum T_j$), we observe that the proposed filtering, even with a threshold on the width, achieves a stronger reduction in the number of nodes visited in the search tree compared to the previously proposed precedence-detection algorithm of Ciré and van Hoeve. The new filtering also appears to be complementary to classical propagation methods for the no-overlap constraint, allowing a substantial reduction in both the number of nodes and the solving time on several instances.

