---
layout: default
title: Group-Invariant Unsupervised Skill Discovery: Symmetry-aware Skill Representations for Generalizable Behavior
---

# Group-Invariant Unsupervised Skill Discovery: Symmetry-aware Skill Representations for Generalizable Behavior
**arXiv**：[2601.14000v1](https://arxiv.org/abs/2601.14000) · [PDF](https://arxiv.org/pdf/2601.14000.pdf)  
**作者**：Junwoo Chang, Joseph Park, Roberto Horowitz, Jongmin Lee, Jongeun Choi  

**一句话要点**：提出群不变技能发现框架，通过嵌入群结构解决物理环境中对称性忽略导致的冗余行为问题。

**关键词**：无监督技能发现, 群不变表示, 对称性嵌入, Wasserstein依赖度量, 强化学习泛化

## 3 点简述
- 核心问题：现有无监督技能发现方法忽略物理环境的几何对称性，导致行为冗余和样本效率低下。
- 方法要点：引入群不变技能发现框架，基于理论保证优化群不变评分函数，确保技能在群变换下系统泛化。
- 实验或效果：在状态和像素基准测试中，相比基线实现更广状态空间覆盖和下游任务学习效率提升。

## 摘要（原文）

> Unsupervised skill discovery aims to acquire behavior primitives that improve exploration and accelerate downstream task learning. However, existing approaches often ignore the geometric symmetries of physical environments, leading to redundant behaviors and sample inefficiency. To address this, we introduce Group-Invariant Skill Discovery (GISD), a framework that explicitly embeds group structure into the skill discovery objective. Our approach is grounded in a theoretical guarantee: we prove that in group-symmetric environments, the standard Wasserstein dependency measure admits a globally optimal solution comprised of an equivariant policy and a group-invariant scoring function. Motivated by this, we formulate the Group-Invariant Wasserstein dependency measure, which restricts the optimization to this symmetry-aware subspace without loss of optimality. Practically, we parameterize the scoring function using a group Fourier representation and define the intrinsic reward via the alignment of equivariant latent features, ensuring that the discovered skills generalize systematically under group transformations. Experiments on state-based and pixel-based locomotion benchmarks demonstrate that GISD achieves broader state-space coverage and improved efficiency in downstream task learning compared to a strong baseline.

