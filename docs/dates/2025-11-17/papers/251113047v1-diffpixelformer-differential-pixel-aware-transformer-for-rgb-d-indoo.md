---
layout: default
title: DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation
---

# DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation
**arXiv**：[2511.13047v1](https://arxiv.org/abs/2511.13047) · [PDF](https://arxiv.org/pdf/2511.13047.pdf)  
**作者**：Yan Gong, Jianli Lu, Yongsheng Gao, Jie Zhao, Xiaojuan Zhang, Susanto Rahardja  

**一句话要点**：提出DiffPixelFormer以解决RGB-D室内场景分割中的特征对齐和表示问题

**关键词**：RGB-D融合, Transformer模型, 室内语义分割, 跨模态对齐, 动态融合策略

## 3 点简述
- RGB-D融合方法依赖计算密集型跨注意力，特征关系建模不足导致对齐不精确
- 核心IIMIB模块通过自注意力捕获模态内依赖，DSIM模块解耦模态特定和共享线索
- 在SUN RGB-D和NYUDv2基准上mIoU达54.28%和59.95%，优于DFormer-L

## 摘要（原文）

> Indoor semantic segmentation is fundamental to computer vision and robotics, supporting applications such as autonomous navigation, augmented reality, and smart environments. Although RGB-D fusion leverages complementary appearance and geometric cues, existing methods often depend on computationally intensive cross-attention mechanisms and insufficiently model intra- and inter-modal feature relationships, resulting in imprecise feature alignment and limited discriminative representation. To address these challenges, we propose DiffPixelFormer, a differential pixel-aware Transformer for RGB-D indoor scene segmentation that simultaneously enhances intra-modal representations and models inter-modal interactions. At its core, the Intra-Inter Modal Interaction Block (IIMIB) captures intra-modal long-range dependencies via self-attention and models inter-modal interactions with the Differential-Shared Inter-Modal (DSIM) module to disentangle modality-specific and shared cues, enabling fine-grained, pixel-level cross-modal alignment. Furthermore, a dynamic fusion strategy balances modality contributions and fully exploits RGB-D information according to scene characteristics. Extensive experiments on the SUN RGB-D and NYUDv2 benchmarks demonstrate that DiffPixelFormer-L achieves mIoU scores of 54.28% and 59.95%, outperforming DFormer-L by 1.78% and 2.75%, respectively. Code is available at https://github.com/gongyan1/DiffPixelFormer.

