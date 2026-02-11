---
layout: default
title: Unbalanced optimal transport for robust longitudinal lesion evolution with registration-aware and appearance-guided priors
---

# Unbalanced optimal transport for robust longitudinal lesion evolution with registration-aware and appearance-guided priors
**arXiv**：[2602.09933v1](https://arxiv.org/abs/2602.09933) · [PDF](https://arxiv.org/pdf/2602.09933.pdf)  
**作者**：Melika Qahqaie, Dominik Neumann, Tobias Heimann, Andreas Maier, Veronika A. Zimmer  

**一句话要点**：提出基于不平衡最优传输的配准感知匹配器，以解决纵向CT中病灶演化对应问题。

**关键词**：不平衡最优传输, 纵向病灶演化, 配准感知匹配, CT图像分析, 病灶对应

## 3 点简述
- 核心问题：纵向CT中病灶出现、消失、合并或分裂时，标准几何匹配器难以建立可靠对应。
- 方法要点：结合几何、配准信任和外观一致性，通过不平衡最优传输适应病灶质量变化。
- 实验或效果：在纵向CT数据上，相比仅距离基线，提升了边缘检测精度、召回率和病灶图组件F1分数。

## 摘要（原文）

> Evaluating lesion evolution in longitudinal CT scans of can cer patients is essential for assessing treatment response, yet establishing reliable lesion correspondence across time remains challenging. Standard bipartite matchers, which rely on geometric proximity, struggle when lesions appear, disappear, merge, or split. We propose a registration-aware matcher based on unbalanced optimal transport (UOT) that accommodates unequal lesion mass and adapts priors to patient-level tumor-load changes. Our transport cost blends (i) size-normalized geometry, (ii) local registration trust from the deformation-field Jacobian, and (iii) optional patch-level appearance consistency. The resulting transport plan is sparsified by relative pruning, yielding one-to-one matches as well as new, disappearing, merging, and splitting lesions without retraining or heuristic rules. On longitudinal CT data, our approach achieves consistently higher edge-detection precision and recall, improved lesion-state recall, and superior lesion-graph component F1 scores versus distance-only baselines.

