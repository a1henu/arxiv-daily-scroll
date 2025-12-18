---
layout: default
title: In Pursuit of Pixel Supervision for Visual Pre-training
---

# In Pursuit of Pixel Supervision for Visual Pre-training
**arXiv**：[2512.15715v1](https://arxiv.org/abs/2512.15715) · [PDF](https://arxiv.org/pdf/2512.15715.pdf)  
**作者**：Lihe Yang, Shang-Wen Li, Yang Li, Xinjie Lei, Dong Wang, Abdelrahman Mohamed, Hengshuang Zhao, Hu Xu  

**一句话要点**：提出增强掩码自编码器Pixio，通过像素监督预训练提升下游任务性能

**关键词**：像素监督, 掩码自编码器, 自监督学习, 视觉预训练, 下游任务

## 3 点简述
- 核心问题：像素级自监督学习在视觉预训练中是否仍具竞争力，需更高效方法。
- 方法要点：基于掩码自编码器，引入更具挑战的预训练任务和更强架构，使用自筛选策略训练。
- 实验或效果：在深度估计、3D重建等任务中表现优异，匹配或超越DINOv3。

## 摘要（原文）

> At the most basic level, pixels are the source of the visual information through which we perceive the world. Pixels contain information at all levels, ranging from low-level attributes to high-level concepts. Autoencoders represent a classical and long-standing paradigm for learning representations from pixels or other raw inputs. In this work, we demonstrate that autoencoder-based self-supervised learning remains competitive today and can produce strong representations for downstream tasks, while remaining simple, stable, and efficient. Our model, codenamed "Pixio", is an enhanced masked autoencoder (MAE) with more challenging pre-training tasks and more capable architectures. The model is trained on 2B web-crawled images with a self-curation strategy with minimal human curation. Pixio performs competitively across a wide range of downstream tasks in the wild, including monocular depth estimation (e.g., Depth Anything), feed-forward 3D reconstruction (i.e., MapAnything), semantic segmentation, and robot learning, outperforming or matching DINOv3 trained at similar scales. Our results suggest that pixel-space self-supervised learning can serve as a promising alternative and a complement to latent-space approaches.

