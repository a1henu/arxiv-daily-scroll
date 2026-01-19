---
layout: default
title: SUG-Occ: An Explicit Semantics and Uncertainty Guided Sparse Learning Framework for Real-Time 3D Occupancy Prediction
---

# SUG-Occ: An Explicit Semantics and Uncertainty Guided Sparse Learning Framework for Real-Time 3D Occupancy Prediction
**arXiv**：[2601.11396v1](https://arxiv.org/abs/2601.11396) · [PDF](https://arxiv.org/pdf/2601.11396.pdf)  
**作者**：Hanlin Wu, Pengfei Lin, Ehsan Javanmardi, Nanren Bao, Bo Qian, Hao Si, Manabu Tsukada  

**一句话要点**：提出SUG-Occ框架，通过语义和不确定性引导的稀疏学习实现实时3D占用预测

**关键词**：3D语义占用预测, 稀疏学习, 实时感知, 自动驾驶, 不确定性引导, 级联稀疏卷积

## 3 点简述
- 核心问题：3D语义占用预测计算和内存开销大，阻碍实时部署。
- 方法要点：利用语义和不确定性先验抑制自由空间投影，设计级联稀疏完成模块和基于OCR的掩码解码器。
- 实验或效果：在SemanticKITTI基准上，准确率提升7.34%，效率提升57.8%。

## 摘要（原文）

> As autonomous driving moves toward full scene understanding, 3D semantic occupancy prediction has emerged as a crucial perception task, offering voxel-level semantics beyond traditional detection and segmentation paradigms. However, such a refined representation for scene understanding incurs prohibitive computation and memory overhead, posing a major barrier to practical real-time deployment. To address this, we propose SUG-Occ, an explicit Semantics and Uncertainty Guided Sparse Learning Enabled 3D Occupancy Prediction Framework, which exploits the inherent sparsity of 3D scenes to reduce redundant computation while maintaining geometric and semantic completeness. Specifically, we first utilize semantic and uncertainty priors to suppress projections from free space during view transformation while employing an explicit unsigned distance encoding to enhance geometric consistency, producing a structurally consistent sparse 3D representation. Secondly, we design an cascade sparse completion module via hyper cross sparse convolution and generative upsampling to enable efficiently coarse-to-fine reasoning. Finally, we devise an object contextual representation (OCR) based mask decoder that aggregates global semantic context from sparse features and refines voxel-wise predictions via lightweight query-context interactions, avoiding expensive attention operations over volumetric features. Extensive experiments on SemanticKITTI benchmark demonstrate that the proposed approach outperforms the baselines, achieving a 7.34/% improvement in accuracy and a 57.8\% gain in efficiency.

