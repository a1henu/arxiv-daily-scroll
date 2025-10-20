---
layout: default
title: FlexiReID: Adaptive Mixture of Expert for Multi-Modal Person Re-Identification
---

# FlexiReID: Adaptive Mixture of Expert for Multi-Modal Person Re-Identification
**arXiv**：[2510.15595v1](https://arxiv.org/abs/2510.15595) · [PDF](https://arxiv.org/pdf/2510.15595.pdf)  
**作者**：Zhen Sun, Lei Tan, Yunhang Shen, Chengmao Cai, Xing Sun, Pingyang Dai, Liujuan Cao, Rongrong Ji  

**一句话要点**：提出FlexiReID框架以支持多模态行人重识别中的任意查询-检索组合

**关键词**：多模态行人重识别, 自适应专家混合, 跨模态查询融合, CIRS-PEDES数据集, 状态性能领先

## 3 点简述
- 核心问题：现有方法不支持多模态行人重识别的任意查询-检索组合，限制实际应用。
- 方法要点：引入自适应专家混合机制和跨模态查询融合模块，动态整合多模态特征。
- 实验或效果：构建CIRS-PEDES数据集，实验显示FlexiReID在复杂场景中性能领先且泛化强。

## 摘要（原文）

> Multimodal person re-identification (Re-ID) aims to match pedestrian images
> across different modalities. However, most existing methods focus on limited
> cross-modal settings and fail to support arbitrary query-retrieval
> combinations, hindering practical deployment. We propose FlexiReID, a flexible
> framework that supports seven retrieval modes across four modalities: rgb,
> infrared, sketches, and text. FlexiReID introduces an adaptive
> mixture-of-experts (MoE) mechanism to dynamically integrate diverse modality
> features and a cross-modal query fusion module to enhance multimodal feature
> extraction. To facilitate comprehensive evaluation, we construct CIRS-PEDES, a
> unified dataset extending four popular Re-ID datasets to include all four
> modalities. Extensive experiments demonstrate that FlexiReID achieves
> state-of-the-art performance and offers strong generalization in complex
> scenarios.

