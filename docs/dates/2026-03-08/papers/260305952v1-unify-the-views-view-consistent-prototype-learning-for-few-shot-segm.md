---
layout: default
title: Unify the Views: View-Consistent Prototype Learning for Few-Shot Segmentation
---

# Unify the Views: View-Consistent Prototype Learning for Few-Shot Segmentation
**arXiv**：[2603.05952v1](https://arxiv.org/abs/2603.05952) · [PDF](https://arxiv.org/pdf/2603.05952.pdf)  
**作者**：Hongli Liu, Yu Wang, Shengjie Zhao  

**一句话要点**：提出VINE框架，通过视图一致原型学习解决少样本分割中的结构错位和跨视图不一致问题。

**关键词**：少样本分割, 视图一致性, 原型学习, 空间-视图图, 掩码交叉注意力, SAM解码器

## 3 点简述
- 核心问题：少样本分割在视角变化下存在结构错位和跨视图不一致，导致分割精度下降。
- 方法要点：引入空间-视图图联合建模结构一致性和前景判别，利用特征差异增强类别对比，通过掩码交叉注意力集成特征生成一致原型。
- 实验或效果：在多个少样本分割基准测试中验证有效性，尤其在视角变化和复杂结构场景下表现稳健。

## 摘要（原文）

> Few-shot segmentation (FSS) has gained significant attention for its ability to generalize to novel classes with limited supervision, yet remains challenged by structural misalignment and cross-view inconsistency under large appearance or viewpoint variations. This paper tackles these challenges by introducing VINE (View-Informed NEtwork), a unified framework that jointly models structural consistency and foreground discrimination to refine class-specific prototypes. Specifically, VINE introduces a spatial-view graph on backbone features, where the spatial graph captures local geometric topology and the view graph connects features from different perspectives to propagate view-invariant structural semantics. To further alleviate foreground ambiguity, we derive a discriminative prior from the support-query feature discrepancy to capture category-specific contrast, which reweights SAM features by emphasizing salient regions and recalibrates backbone activations for improved structural focus. The foreground-enhanced SAM features and structurally enriched ResNet features are progressively integrated through masked cross-attention, yielding class-consistent prototypes used as adaptive prompts for the SAM decoder to generate accurate masks. Extensive experiments on multiple FSS benchmarks validate the effectiveness and robustness of VINE, particularly under challenging scenarios with viewpoint shifts and complex structures. The code is available at https://github.com/HongliLiu1/VINE-main.

