---
layout: default
title: Kernel Alignment-based Multi-view Unsupervised Feature Selection with Sample-level Adaptive Graph Learning
---

# Kernel Alignment-based Multi-view Unsupervised Feature Selection with Sample-level Adaptive Graph Learning
**arXiv**：[2601.07288v1](https://arxiv.org/abs/2601.07288) · [PDF](https://arxiv.org/pdf/2601.07288.pdf)  
**作者**：Yalan Tan, Yanyong Huang, Zongxin Shen, Dongjie Wang, Fengmao Lv, Tianrui Li  

**一句话要点**：提出KAFUSE方法，通过核对齐和样本级自适应图学习解决多视图无监督特征选择中的非线性依赖和局部结构不准确问题。

**关键词**：多视图学习, 无监督特征选择, 核对齐, 自适应图学习, 样本级融合, 非线性依赖

## 3 点简述
- 核心问题：现有方法忽视特征间的非线性依赖，且图融合时样本权重固定，导致特征冗余和局部结构表征不准确。
- 方法要点：使用核对齐减少线性和非线性特征冗余，通过样本级自适应图学习融合多视图相似性图，提升局部结构准确性。
- 实验或效果：在真实多视图数据集上验证，KAFUSE优于现有先进方法，实现特征选择与结构学习的相互增强。

## 摘要（原文）

> Although multi-view unsupervised feature selection (MUFS) has demonstrated success in dimensionality reduction for unlabeled multi-view data, most existing methods reduce feature redundancy by focusing on linear correlations among features but often overlook complex nonlinear dependencies. This limits the effectiveness of feature selection. In addition, existing methods fuse similarity graphs from multiple views by employing sample-invariant weights to preserve local structure. However, this process fails to account for differences in local neighborhood clarity among samples within each view, thereby hindering accurate characterization of the intrinsic local structure of the data. In this paper, we propose a Kernel Alignment-based multi-view unsupervised FeatUre selection with Sample-level adaptive graph lEarning method (KAFUSE) to address these issues. Specifically, we first employ kernel alignment with an orthogonal constraint to reduce feature redundancy in both linear and nonlinear relationships. Then, a cross-view consistent similarity graph is learned by applying sample-level fusion to each slice of a tensor formed by stacking similarity graphs from different views, which automatically adjusts the view weights for each sample during fusion. These two steps are integrated into a unified model for feature selection, enabling mutual enhancement between them. Extensive experiments on real multi-view datasets demonstrate the superiority of KAFUSE over state-of-the-art methods.

