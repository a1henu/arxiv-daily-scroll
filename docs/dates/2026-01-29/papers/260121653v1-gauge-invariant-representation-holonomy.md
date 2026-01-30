---
layout: default
title: Gauge-invariant representation holonomy
---

# Gauge-invariant representation holonomy
**arXiv**：[2601.21653v1](https://arxiv.org/abs/2601.21653) · [PDF](https://arxiv.org/pdf/2601.21653.pdf)  
**作者**：Vasileios Sevetlidis, George Pavlidis  

**一句话要点**：提出表示全纯性以量化深度网络表示沿输入路径的几何变化，超越点相似性度量。

**关键词**：表示几何, 规范不变性, 全纯性, 深度网络诊断, 鲁棒性分析, 特征演化

## 3 点简述
- 现有相似性度量如CKA或SVCCA仅捕获激活集的点重叠，忽略表示沿输入路径的变化。
- 表示全纯性通过测量特征在输入空间小环路上平行传输累积的“扭曲”，提供规范不变统计量。
- 实验显示全纯性随环路半径增加，区分CKA相似模型，并与对抗和腐败鲁棒性相关。

## 摘要（原文）

> Deep networks learn internal representations whose geometry--how features bend, rotate, and evolve--affects both generalization and robustness. Existing similarity measures such as CKA or SVCCA capture pointwise overlap between activation sets, but miss how representations change along input paths. Two models may appear nearly identical under these metrics yet respond very differently to perturbations or adversarial stress. We introduce representation holonomy, a gauge-invariant statistic that measures this path dependence. Conceptually, holonomy quantifies the "twist" accumulated when features are parallel-transported around a small loop in input space: flat representations yield zero holonomy, while nonzero values reveal hidden curvature. Our estimator fixes gauge through global whitening, aligns neighborhoods using shared subspaces and rotation-only Procrustes, and embeds the result back to the full feature space. We prove invariance to orthogonal (and affine, post-whitening) transformations, establish a linear null for affine layers, and show that holonomy vanishes at small radii. Empirically, holonomy increases with loop radius, separates models that appear similar under CKA, and correlates with adversarial and corruption robustness. It also tracks training dynamics as features form and stabilize. Together, these results position representation holonomy as a practical and scalable diagnostic for probing the geometric structure of learned representations beyond pointwise similarity.

