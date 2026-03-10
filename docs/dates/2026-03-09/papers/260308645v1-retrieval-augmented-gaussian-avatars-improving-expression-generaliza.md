---
layout: default
title: Retrieval-Augmented Gaussian Avatars: Improving Expression Generalization
---

# Retrieval-Augmented Gaussian Avatars: Improving Expression Generalization
**arXiv**：[2603.08645v1](https://arxiv.org/abs/2603.08645) · [PDF](https://arxiv.org/pdf/2603.08645.pdf)  
**作者**：Matan Levy, Gavriel Habib, Issar Tzachor, Dvir Samuel, Rami Ben-Ari, Nir Darshan, Or Litany, Dani Lischinski  

**一句话要点**：提出检索增强训练方法RAF，提升无模板头部虚拟化身的表情泛化能力

**关键词**：头部虚拟化身, 表情泛化, 检索增强, 无模板动画, 身份解耦, 训练增强

## 3 点简述
- 核心问题：无模板头部虚拟化身因训练数据表情有限，泛化能力不足，易受分布外表情影响
- 方法要点：构建大型无标签表情库，训练时用检索的最近邻表情替换部分特征，增强身份与表情解耦
- 实验或效果：在NeRSemble基准测试中，RAF在自驱动和跨驱动场景下均提升表情保真度

## 摘要（原文）

> Template-free animatable head avatars can achieve high visual fidelity by learning expression-dependent facial deformation directly from a subject's capture, avoiding parametric face templates and hand-designed blendshape spaces. However, since learned deformation is supervised only by the expressions observed for a single identity, these models suffer from limited expression coverage and often struggle when driven by motions that deviate from the training distribution. We introduce RAF (Retrieval-Augmented Faces), a simple training-time augmentation designed for template-free head avatars that learn deformation from data. RAF constructs a large unlabeled expression bank and, during training, replaces a subset of the subject's expression features with nearest-neighbor expressions retrieved from this bank while still reconstructing the subject's original frames. This exposes the deformation field to a broader range of expression conditions, encouraging stronger identity-expression decoupling and improving robustness to expression distribution shift without requiring paired cross-identity data, additional annotations, or architectural changes. We further analyze how retrieval augmentation increases expression diversity and validate retrieval quality with a user study showing that retrieved neighbors are perceptually closer in expression and pose. Experiments on the NeRSemble benchmark demonstrate that RAF consistently improves expression fidelity over the baseline, in both self-driving and cross-driving scenarios.

