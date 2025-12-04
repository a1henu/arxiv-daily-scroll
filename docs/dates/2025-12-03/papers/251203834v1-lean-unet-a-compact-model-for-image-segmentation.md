---
layout: default
title: Lean Unet: A Compact Model for Image Segmentation
---

# Lean Unet: A Compact Model for Image Segmentation
**arXiv**：[2512.03834v1](https://arxiv.org/abs/2512.03834) · [PDF](https://arxiv.org/pdf/2512.03834.pdf)  
**作者**：Ture Hassler, Ida Åkerholm, Marcus Nordström, Gabriele Balletti, Orcun Goksel  

**一句话要点**：提出紧凑型LUnet架构以解决Unet内存占用大和推理延迟高的问题

**关键词**：图像分割, Unet架构, 模型压缩, 医学影像, 通道剪枝, 轻量模型

## 3 点简述
- Unet及其变体在图像分割中内存需求大，限制训练批次和增加推理延迟
- 通过分析剪枝，假设最终结构是关键，提出通道数不随分辨率减半而翻倍的紧凑架构
- 在MRI和CT数据集上，LUnet参数减少超30倍，性能与传统Unet和剪枝网络相当

## 摘要（原文）

> Unet and its variations have been standard in semantic image segmentation, especially for computer assisted radiology. Current Unet architectures iteratively downsample spatial resolution while increasing channel dimensions to preserve information content. Such a structure demands a large memory footprint, limiting training batch sizes and increasing inference latency. Channel pruning compresses Unet architecture without accuracy loss, but requires lengthy optimization and may not generalize across tasks and datasets. By investigating Unet pruning, we hypothesize that the final structure is the crucial factor, not the channel selection strategy of pruning. Based on our observations, we propose a lean Unet architecture (LUnet) with a compact, flat hierarchy where channels are not doubled as resolution is halved. We evaluate on a public MRI dataset allowing comparable reporting, as well as on two internal CT datasets. We show that a state-of-the-art pruning solution (STAMP) mainly prunes from the layers with the highest number of channels. Comparatively, simply eliminating a random channel at the pruning-identified layer or at the largest layer achieves similar or better performance. Our proposed LUnet with fixed architectures and over 30 times fewer parameters achieves performance comparable to both conventional Unet counterparts and data-adaptively pruned networks. The proposed lean Unet with constant channel count across layers requires far fewer parameters while achieving performance superior to standard Unet for the same total number of parameters. Skip connections allow Unet bottleneck channels to be largely reduced, unlike standard encoder-decoder architectures requiring increased bottleneck channels for information propagation.

