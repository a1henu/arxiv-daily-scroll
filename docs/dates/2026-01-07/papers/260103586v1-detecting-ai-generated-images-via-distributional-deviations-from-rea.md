---
layout: default
title: Detecting AI-Generated Images via Distributional Deviations from Real Images
---

# Detecting AI-Generated Images via Distributional Deviations from Real Images
**arXiv**：[2601.03586v1](https://arxiv.org/abs/2601.03586) · [PDF](https://arxiv.org/pdf/2601.03586.pdf)  
**作者**：Yakun Niu, Yingjian Chen, Lei Zhang  

**一句话要点**：提出基于掩码预训练模型微调策略，通过纹理感知掩码机制检测AI生成图像的分布偏差，提升泛化性能。

**关键词**：AI生成图像检测, CLIP模型微调, 纹理感知掩码, 分布偏差分析, 泛化性能提升

## 3 点简述
- 核心问题：现有方法未能充分利用CLIP图像编码器潜力，泛化至未见生成模型的能力有限。
- 方法要点：引入纹理感知掩码机制，在微调中掩码含生成模型特定模式的纹理区域，迫使模型关注分布偏差。
- 实验或效果：在GenImage和UniversalFakeDetect数据集上，仅用少量图像微调即实现高达98.2%和94.6%的平均准确率。

## 摘要（原文）

> The rapid advancement of generative models has significantly enhanced the quality of AI-generated images, raising concerns about misinformation and the erosion of public trust. Detecting AI-generated images has thus become a critical challenge, particularly in terms of generalizing to unseen generative models. Existing methods using frozen pre-trained CLIP models show promise in generalization but treat the image encoder as a basic feature extractor, failing to fully exploit its potential. In this paper, we perform an in-depth analysis of the frozen CLIP image encoder (CLIP-ViT), revealing that it effectively clusters real images in a high-level, abstract feature space. However, it does not truly possess the ability to distinguish between real and AI-generated images. Based on this analysis, we propose a Masking-based Pre-trained model Fine-Tuning (MPFT) strategy, which introduces a Texture-Aware Masking (TAM) mechanism to mask textured areas containing generative model-specific patterns during fine-tuning. This approach compels CLIP-ViT to attend to the "distributional deviations"from authentic images for AI-generated image detection, thereby achieving enhanced generalization performance. Extensive experiments on the GenImage and UniversalFakeDetect datasets demonstrate that our method, fine-tuned with only a minimal number of images, significantly outperforms existing approaches, achieving up to 98.2% and 94.6% average accuracy on the two datasets, respectively.

