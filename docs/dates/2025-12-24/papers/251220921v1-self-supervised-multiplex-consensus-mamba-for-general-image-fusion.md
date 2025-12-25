---
layout: default
title: Self-supervised Multiplex Consensus Mamba for General Image Fusion
---

# Self-supervised Multiplex Consensus Mamba for General Image Fusion
**arXiv**：[2512.20921v1](https://arxiv.org/abs/2512.20921) · [PDF](https://arxiv.org/pdf/2512.20921.pdf)  
**作者**：Yingying Wang, Rongjin Zhuang, Hui Zheng, Xuanhua He, Ke Cao, Xiaotong Tu, Xinghao Ding  

**一句话要点**：提出SMC-Mamba框架，通过自监督多路共识Mamba实现通用图像融合，提升下游任务性能。

**关键词**：通用图像融合, 自监督学习, Mamba架构, 多模态整合, 下游任务增强

## 3 点简述
- 通用图像融合需处理多任务且不增加复杂度，SMC-Mamba通过MAFE模块增强细节与全局表示，MCCM模块动态整合多模态互补信息。
- 引入BSCL损失函数，在保持高频信息的同时提升下游任务性能，无需额外计算开销。
- 实验表明，在红外-可见光、医学、多焦点和多曝光融合等任务中优于现有方法。

## 摘要（原文）

> Image fusion integrates complementary information from different modalities to generate high-quality fused images, thereby enhancing downstream tasks such as object detection and semantic segmentation. Unlike task-specific techniques that primarily focus on consolidating inter-modal information, general image fusion needs to address a wide range of tasks while improving performance without increasing complexity. To achieve this, we propose SMC-Mamba, a Self-supervised Multiplex Consensus Mamba framework for general image fusion. Specifically, the Modality-Agnostic Feature Enhancement (MAFE) module preserves fine details through adaptive gating and enhances global representations via spatial-channel and frequency-rotational scanning. The Multiplex Consensus Cross-modal Mamba (MCCM) module enables dynamic collaboration among experts, reaching a consensus to efficiently integrate complementary information from multiple modalities. The cross-modal scanning within MCCM further strengthens feature interactions across modalities, facilitating seamless integration of critical information from both sources. Additionally, we introduce a Bi-level Self-supervised Contrastive Learning Loss (BSCL), which preserves high-frequency information without increasing computational overhead while simultaneously boosting performance in downstream tasks. Extensive experiments demonstrate that our approach outperforms state-of-the-art (SOTA) image fusion algorithms in tasks such as infrared-visible, medical, multi-focus, and multi-exposure fusion, as well as downstream visual tasks.

