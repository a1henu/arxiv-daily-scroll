---
layout: default
title: Symmetry Informative and Agnostic Feature Disentanglement for 3D Shapes
---

# Symmetry Informative and Agnostic Feature Disentanglement for 3D Shapes
**arXiv**：[2601.14804v1](https://arxiv.org/abs/2601.14804) · [PDF](https://arxiv.org/pdf/2601.14804.pdf)  
**作者**：Tobias Weißberg, Weikang Wang, Paul Roetzer, Nafie El Amrani, Florian Bernard  

**一句话要点**：提出对称信息与无关特征解耦方法以改进三维形状描述符

**关键词**：三维形状分析, 特征解耦, 对称感知, 形状描述符, 特征细化

## 3 点简述
- 核心问题：现有对称感知描述符仅提取一维特征，忽略其他语义信息且噪声大。
- 方法要点：设计特征解耦框架，同时提取对称信息特征和对称无关特征，并引入特征细化技术提升鲁棒性。
- 实验或效果：在内在对称检测、左右分类和形状匹配等任务中，定性和定量评估均优于现有方法。

## 摘要（原文）

> Shape descriptors, i.e., per-vertex features of 3D meshes or point clouds, are fundamental to shape analysis. Historically, various handcrafted geometry-aware descriptors and feature refinement techniques have been proposed. Recently, several studies have initiated a new research direction by leveraging features from image foundation models to create semantics-aware descriptors, demonstrating advantages across tasks like shape matching, editing, and segmentation. Symmetry, another key concept in shape analysis, has also attracted increasing attention. Consequently, constructing symmetry-aware shape descriptors is a natural progression. Although the recent method $χ$ (Wang et al., 2025) successfully extracted symmetry-informative features from semantic-aware descriptors, its features are only one-dimensional, neglecting other valuable semantic information. Furthermore, the extracted symmetry-informative feature is usually noisy and yields small misclassified patches. To address these gaps, we propose a feature disentanglement approach which is simultaneously symmetry informative and symmetry agnostic. Further, we propose a feature refinement technique to improve the robustness of predicted symmetry informative features. Extensive experiments, including intrinsic symmetry detection, left/right classification, and shape matching, demonstrate the effectiveness of our proposed framework compared to various state-of-the-art methods, both qualitatively and quantitatively.

