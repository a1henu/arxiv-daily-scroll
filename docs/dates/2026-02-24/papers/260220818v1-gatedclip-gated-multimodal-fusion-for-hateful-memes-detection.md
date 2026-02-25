---
layout: default
title: GatedCLIP: Gated Multimodal Fusion for Hateful Memes Detection
---

# GatedCLIP: Gated Multimodal Fusion for Hateful Memes Detection
**arXiv**：[2602.20818v1](https://arxiv.org/abs/2602.20818) · [PDF](https://arxiv.org/pdf/2602.20818.pdf)  
**作者**：Yingying Guo, Ke Zhang, Zirong Zeng  

**一句话要点**：提出GatedCLIP模型，通过门控多模态融合增强CLIP以检测仇恨表情包

**关键词**：仇恨表情包检测, 多模态融合, 门控机制, 对比学习, CLIP增强

## 3 点简述
- 核心问题：仇恨表情包检测中，良性图像与文本的复杂交互导致有害信息难以识别
- 方法要点：引入学习投影头、动态门控融合机制和对比学习目标，优化多模态特征融合
- 实验或效果：在Hateful Memes数据集上AUROC达0.66，显著优于CLIP基线，仅需35万可训练参数

## 摘要（原文）

> Detecting hateful content in multimodal memes presents unique challenges, as harmful messages often emerge from the complex interplay between benign images and text. We propose GatedCLIP, a Vision-Language model that enhances CLIP's multimodal capabilities with specialized architectural improvements for hateful memes detection. Our approach introduces learned projection heads that map CLIP embeddings to a task-optimized semantic space, a dynamic gated fusion mechanism that adaptively weights visual and textual features, and a contrastive learning objective that maintains cross-modal semantic alignment. Experiments on the Hateful Memes dataset demonstrate that GatedCLIP achieves an AUROC of 0.66, substantially outperforming the CLIP baseline (AUROC 0.49) while maintaining computational efficiency with only 350K trainable parameters.

