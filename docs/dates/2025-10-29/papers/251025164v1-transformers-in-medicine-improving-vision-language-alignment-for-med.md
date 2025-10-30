---
layout: default
title: Transformers in Medicine: Improving Vision-Language Alignment for Medical Image Captioning
---

# Transformers in Medicine: Improving Vision-Language Alignment for Medical Image Captioning
**arXiv**：[2510.25164v1](https://arxiv.org/abs/2510.25164) · [PDF](https://arxiv.org/pdf/2510.25164.pdf)  
**作者**：Yogesh Thakku Suresh, Vishwajeet Shivaji Hogale, Luca-Alexandru Zamfira, Anandavardhana Hegde  

**一句话要点**：提出基于Transformer的多模态框架，以改进医学MRI图像描述中的视觉-语言对齐。

**关键词**：医学图像描述, 视觉-语言对齐, Transformer架构, MRI图像分析, 对比学习

## 3 点简述
- 核心问题：医学MRI图像描述中视觉与文本语义对齐不足，影响临床相关性。
- 方法要点：结合DEiT-Small视觉Transformer、MediCareBERT和LSTM解码器，使用混合损失和对比推理。
- 实验或效果：在MultiCaRe数据集上验证，专注脑部MRI提升描述准确性和语义对齐。

## 摘要（原文）

> We present a transformer-based multimodal framework for generating clinically
> relevant captions for MRI scans. Our system combines a DEiT-Small vision
> transformer as an image encoder, MediCareBERT for caption embedding, and a
> custom LSTM-based decoder. The architecture is designed to semantically align
> image and textual embeddings, using hybrid cosine-MSE loss and contrastive
> inference via vector similarity. We benchmark our method on the MultiCaRe
> dataset, comparing performance on filtered brain-only MRIs versus general MRI
> images against state-of-the-art medical image captioning methods including
> BLIP, R2GenGPT, and recent transformer-based approaches. Results show that
> focusing on domain-specific data improves caption accuracy and semantic
> alignment. Our work proposes a scalable, interpretable solution for automated
> medical image reporting.

