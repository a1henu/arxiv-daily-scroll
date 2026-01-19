---
layout: default
title: Context-Aware Semantic Segmentation via Stage-Wise Attention
---

# Context-Aware Semantic Segmentation via Stage-Wise Attention
**arXiv**：[2601.11310v1](https://arxiv.org/abs/2601.11310) · [PDF](https://arxiv.org/pdf/2601.11310.pdf)  
**作者**：Antoine Carreaud, Elias Naha, Arthur Chansel, Nina Lahellec, Jan Skaloud, Adrien Gressin  

**一句话要点**：提出CASWiT以解决超高分辨率图像语义分割中Transformer内存限制问题

**关键词**：语义分割, 超高分辨率图像, Transformer架构, 双分支网络, 交叉注意力融合, SimMIM预训练

## 3 点简述
- 核心问题：Transformer在超高分辨率图像分割中内存随token数平方增长，限制上下文范围或空间分辨率。
- 方法要点：采用双分支Swin架构，通过上下文编码器捕获长程依赖，高分辨率编码器提取细节，交叉尺度融合模块注入全局线索。
- 实验或效果：在IGN FLAIR-HUB数据集上达到65.83% mIoU，优于RGB基线1.78点；在URUR数据集上超越当前SoTA 0.9%。

## 摘要（原文）

> Semantic ultra high resolution image (UHR) segmentation is essential in remote sensing applications such as aerial mapping and environmental monitoring. Transformer-based models struggle in this setting because memory grows quadratically with token count, constraining either the contextual scope or the spatial resolution. We introduce CASWiT (Context-Aware Stage-Wise Transformer), a dual-branch, Swin-based architecture that injects global cues into fine-grained UHR features. A context encoder processes a downsampled neighborhood to capture long-range dependencies, while a high resolution encoder extracts detailed features from UHR patches. A cross-scale fusion module, combining cross-attention and gated feature injection, enriches high-resolution tokens with context. Beyond architecture, we propose a SimMIM-style pretraining. We mask 75% of the high-resolution image tokens and the low-resolution center region that spatially corresponds to the UHR patch, then train the shared dual-encoder with small decoder to reconstruct the UHR initial image. Extensive experiments on the large-scale IGN FLAIR-HUB aerial dataset demonstrate the effectiveness of CASWiT. Our method achieves 65.83% mIoU, outperforming RGB baselines by 1.78 points. On URUR, CASWiT achieves 49.1% mIoU, surpassing the current SoTA by +0.9% under the official evaluation protocol. All codes are provided on: https://huggingface.co/collections/heig-vd-geo/caswit.

