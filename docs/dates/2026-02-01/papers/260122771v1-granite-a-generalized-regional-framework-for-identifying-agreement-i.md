---
layout: default
title: GRANITE: A Generalized Regional Framework for Identifying Agreement in Feature-Based Explanations
---

# GRANITE: A Generalized Regional Framework for Identifying Agreement in Feature-Based Explanations
**arXiv**：[2601.22771v1](https://arxiv.org/abs/2601.22771) · [PDF](https://arxiv.org/pdf/2601.22771.pdf)  
**作者**：Julia Herbinger, Gabriel Laberge, Maximilian Muschalik, Yann Pequignot, Marvin N. Wright, Fabian Fumagalli  

**一句话要点**：提出GRANITE框架以解决特征解释方法不一致问题，通过区域划分实现解释对齐。

**关键词**：特征解释方法, 解释一致性, 区域划分框架, 特征交互处理, 可解释人工智能

## 3 点简述
- 核心问题：特征解释方法常因处理特征交互和依赖方式不同而产生冲突解释。
- 方法要点：GRANITE将特征空间划分为最小化交互和分布影响的区域，统一现有区域方法并扩展至特征组。
- 实验或效果：在真实数据集上验证了框架有效性，提供一致且可解释的特征解释工具。

## 摘要（原文）

> Feature-based explanation methods aim to quantify how features influence the model's behavior, either locally or globally, but different methods often disagree, producing conflicting explanations. This disagreement arises primarily from two sources: how feature interactions are handled and how feature dependencies are incorporated. We propose GRANITE, a generalized regional explanation framework that partitions the feature space into regions where interaction and distribution influences are minimized. This approach aligns different explanation methods, yielding more consistent and interpretable explanations. GRANITE unifies existing regional approaches, extends them to feature groups, and introduces a recursive partitioning algorithm to estimate such regions. We demonstrate its effectiveness on real-world datasets, providing a practical tool for consistent and interpretable feature explanations.

