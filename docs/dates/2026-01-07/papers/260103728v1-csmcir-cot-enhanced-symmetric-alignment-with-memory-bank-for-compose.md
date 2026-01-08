---
layout: default
title: CSMCIR: CoT-Enhanced Symmetric Alignment with Memory Bank for Composed Image Retrieval
---

# CSMCIR: CoT-Enhanced Symmetric Alignment with Memory Bank for Composed Image Retrieval
**arXiv**：[2601.03728v1](https://arxiv.org/abs/2601.03728) · [PDF](https://arxiv.org/pdf/2601.03728.pdf)  
**作者**：Zhipeng Qian, Zihan Liang, Yufei Ma, Ben Chen, Huangyu Dai, Yiwei Ma, Jiayi Ji, Chenyi Lei, Han Li, Xiaoshuai Sun  

**一句话要点**：提出CSMCIR框架，通过对称架构与记忆库解决组合图像检索中的表示空间碎片化问题。

**关键词**：组合图像检索, 表示空间对齐, 对称架构, 思维链提示, 动态记忆库

## 3 点简述
- 核心问题：现有方法因异构模态编码导致表示空间碎片化，限制检索性能。
- 方法要点：采用多级思维链提示、对称双塔架构和动态记忆库，实现高效查询-目标对齐。
- 实验或效果：在四个基准数据集上达到最先进性能，并验证了各组件有效性。

## 摘要（原文）

> Composed Image Retrieval (CIR) enables users to search for target images using both a reference image and manipulation text, offering substantial advantages over single-modality retrieval systems. However, existing CIR methods suffer from representation space fragmentation: queries and targets comprise heterogeneous modalities and are processed by distinct encoders, forcing models to bridge misaligned representation spaces only through post-hoc alignment, which fundamentally limits retrieval performance. This architectural asymmetry manifests as three distinct, well-separated clusters in the feature space, directly demonstrating how heterogeneous modalities create fundamentally misaligned representation spaces from initialization. In this work, we propose CSMCIR, a unified representation framework that achieves efficient query-target alignment through three synergistic components. First, we introduce a Multi-level Chain-of-Thought (MCoT) prompting strategy that guides Multimodal Large Language Models to generate discriminative, semantically compatible captions for target images, establishing modal symmetry. Building upon this, we design a symmetric dual-tower architecture where both query and target sides utilize the identical shared-parameter Q-Former for cross-modal encoding, ensuring consistent feature representations and further reducing the alignment gap. Finally, this architectural symmetry enables an entropy-based, temporally dynamic Memory Bank strategy that provides high-quality negative samples while maintaining consistency with the evolving model state. Extensive experiments on four benchmark datasets demonstrate that our CSMCIR achieves state-of-the-art performance with superior training efficiency. Comprehensive ablation studies further validate the effectiveness of each proposed component.

