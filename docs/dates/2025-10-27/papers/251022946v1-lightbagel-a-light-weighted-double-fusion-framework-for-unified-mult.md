---
layout: default
title: LightBagel: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation
---

# LightBagel: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation
**arXiv**：[2510.22946v1](https://arxiv.org/abs/2510.22946) · [PDF](https://arxiv.org/pdf/2510.22946.pdf)  
**作者**：Zeyu Wang, Zilong Chen, Chenhui Gou, Feng Li, Chaorui Deng, Deyao Zhu, Kunchang Li, Weihao Yu, Haoqin Tu, Haoqi Fan, Cihang Xie  

**一句话要点**：提出LightBagel框架，通过双融合机制高效统一多模态理解与生成。

**关键词**：多模态融合, 轻量级框架, 自注意力机制, 统一模型, 高效训练

## 3 点简述
- 问题：统一多模态模型训练资源消耗大，需从零开始构建。
- 方法：保留原模型块，插入多模态自注意力块实现双融合。
- 效果：仅用35B tokens训练，在多个基准测试中取得强结果。

## 摘要（原文）

> Unified multimodal models have recently shown remarkable gains in both
> capability and versatility, yet most leading systems are still trained from
> scratch and require substantial computational resources. In this paper, we show
> that competitive performance can be obtained far more efficiently by
> strategically fusing publicly available models specialized for either
> generation or understanding. Our key design is to retain the original blocks
> while additionally interleaving multimodal self-attention blocks throughout the
> networks. This double fusion mechanism (1) effectively enables rich multi-modal
> fusion while largely preserving the original strengths of the base models, and
> (2) catalyzes synergistic fusion of high-level semantic representations from
> the understanding encoder with low-level spatial signals from the generation
> encoder. By training with only ~ 35B tokens, this approach achieves strong
> results across multiple benchmarks: 0.91 on GenEval for compositional
> text-to-image generation, 82.16 on DPG-Bench for complex text-to-image
> generation, 6.06 on GEditBench, and 3.77 on ImgEdit-Bench for image editing. By
> fully releasing the entire suite of code, model weights, and datasets, we hope
> to support future research on unified multimodal modeling.

