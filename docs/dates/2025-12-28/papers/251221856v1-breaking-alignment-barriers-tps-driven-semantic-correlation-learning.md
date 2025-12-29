---
layout: default
title: Breaking Alignment Barriers: TPS-Driven Semantic Correlation Learning for Alignment-Free RGB-T Salient Object Detection
---

# Breaking Alignment Barriers: TPS-Driven Semantic Correlation Learning for Alignment-Free RGB-T Salient Object Detection
**arXiv**：[2512.21856v1](https://arxiv.org/abs/2512.21856) · [PDF](https://arxiv.org/pdf/2512.21856.pdf)  
**作者**：Lupiao Hu, Fasheng Wang, Fangmei Chen, Fuming Sun, Haojie Li  

**一句话要点**：提出TPS-SCL网络以解决未对齐RGB-T图像对的显著目标检测问题

**关键词**：RGB-T显著目标检测, 未对齐图像处理, 薄板样条对齐, 跨模态学习, 轻量级网络

## 3 点简述
- 核心问题：现有方法依赖对齐数据集，在未对齐真实场景中性能下降
- 方法要点：使用双流MobileViT编码器、TPS对齐模块和语义约束模块建模跨模态相关性
- 实验或效果：在多个数据集上达到轻量级SOTA，优于主流RGB-T SOD方法

## 摘要（原文）

> Existing RGB-T salient object detection methods predominantly rely on manually aligned and annotated datasets, struggling to handle real-world scenarios with raw, unaligned RGB-T image pairs. In practical applications, due to significant cross-modal disparities such as spatial misalignment, scale variations, and viewpoint shifts, the performance of current methods drastically deteriorates on unaligned datasets. To address this issue, we propose an efficient RGB-T SOD method for real-world unaligned image pairs, termed Thin-Plate Spline-driven Semantic Correlation Learning Network (TPS-SCL). We employ a dual-stream MobileViT as the encoder, combined with efficient Mamba scanning mechanisms, to effectively model correlations between the two modalities while maintaining low parameter counts and computational overhead. To suppress interference from redundant background information during alignment, we design a Semantic Correlation Constraint Module (SCCM) to hierarchically constrain salient features. Furthermore, we introduce a Thin-Plate Spline Alignment Module (TPSAM) to mitigate spatial discrepancies between modalities. Additionally, a Cross-Modal Correlation Module (CMCM) is incorporated to fully explore and integrate inter-modal dependencies, enhancing detection performance. Extensive experiments on various datasets demonstrate that TPS-SCL attains state-of-the-art (SOTA) performance among existing lightweight SOD methods and outperforms mainstream RGB-T SOD approaches.

