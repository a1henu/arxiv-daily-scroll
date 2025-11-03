---
layout: default
title: Modality Alignment across Trees on Heterogeneous Hyperbolic Manifolds
---

# Modality Alignment across Trees on Heterogeneous Hyperbolic Manifolds
**arXiv**：[2510.27391v1](https://arxiv.org/abs/2510.27391) · [PDF](https://arxiv.org/pdf/2510.27391.pdf)  
**作者**：Wu Wei, Xiaomeng Fan, Yuwei Wu, Zhi Gao, Pengxiang Li, Yunde Jia, Mehrtash Harandi  

**一句话要点**：提出跨树对齐方法，在异构双曲流形上对齐视觉与文本的层次特征，以改进模态对齐。

**关键词**：模态对齐, 层次特征, 双曲流形, 跨树对齐, 异构流形, KL距离

## 3 点简述
- 现有方法提取文本层次特征但图像仅用单一特征，导致对齐不对称和次优。
- 构建图像和文本的树状层次特征，嵌入异构双曲流形，并学习中间流形以最小化KL距离对齐。
- 在分类任务实验中，该方法在少样本和跨域设置下优于基线。

## 摘要（原文）

> Modality alignment is critical for vision-language models (VLMs) to
> effectively integrate information across modalities. However, existing methods
> extract hierarchical features from text while representing each image with a
> single feature, leading to asymmetric and suboptimal alignment. To address
> this, we propose Alignment across Trees, a method that constructs and aligns
> tree-like hierarchical features for both image and text modalities.
> Specifically, we introduce a semantic-aware visual feature extraction framework
> that applies a cross-attention mechanism to visual class tokens from
> intermediate Transformer layers, guided by textual cues to extract visual
> features with coarse-to-fine semantics. We then embed the feature trees of the
> two modalities into hyperbolic manifolds with distinct curvatures to
> effectively model their hierarchical structures. To align across the
> heterogeneous hyperbolic manifolds with different curvatures, we formulate a KL
> distance measure between distributions on heterogeneous manifolds, and learn an
> intermediate manifold for manifold alignment by minimizing the distance. We
> prove the existence and uniqueness of the optimal intermediate manifold.
> Experiments on taxonomic open-set classification tasks across multiple image
> datasets demonstrate that our method consistently outperforms strong baselines
> under few-shot and cross-domain settings.

