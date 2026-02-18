---
layout: default
title: GMAIL: Generative Modality Alignment for generated Image Learning
---

# GMAIL: Generative Modality Alignment for generated Image Learning
**arXiv**：[2602.15368v1](https://arxiv.org/abs/2602.15368) · [PDF](https://arxiv.org/pdf/2602.15368.pdf)  
**作者**：Shentong Mo, Sukmin Yun  

**一句话要点**：提出GMAIL框架，通过模态对齐在潜在空间利用生成图像提升视觉-语言任务性能

**关键词**：生成图像学习, 模态对齐, 视觉-语言模型, 多模态学习, 零样本任务

## 3 点简述
- 核心问题：生成图像与真实图像存在模态差异，直接用作训练数据可能导致模式崩溃
- 方法要点：将生成图像视为独立模态，使用跨模态对齐损失在潜在空间桥接两种模态
- 实验或效果：在图像描述、零样本检索等任务中显著提升性能，并展示正面的数据缩放趋势

## 摘要（原文）

> Generative models have made it possible to synthesize highly realistic images, potentially providing an abundant data source for training machine learning models. Despite the advantages of these synthesizable data sources, the indiscriminate use of generated images as real images for training can even cause mode collapse due to modality discrepancies between real and synthetic domains. In this paper, we propose a novel framework for discriminative use of generated images, coined GMAIL, that explicitly treats generated images as a separate modality from real images. Instead of indiscriminately replacing real images with generated ones in the pixel space, our approach bridges the two distinct modalities in the same latent space through a multi-modal learning approach. To be specific, we first fine-tune a model exclusively on generated images using a cross-modality alignment loss and then employ this aligned model to further train various vision-language models with generated images. By aligning the two modalities, our approach effectively leverages the benefits of recent advances in generative models, thereby boosting the effectiveness of generated image learning across a range of vision-language tasks. Our framework can be easily incorporated with various vision-language models, and we demonstrate its efficacy throughout extensive experiments. For example, our framework significantly improves performance on image captioning, zero-shot image retrieval, zero-shot image classification, and long caption retrieval tasks. It also shows positive generated data scaling trends and notable enhancements in the captioning performance of the large multimodal model, LLaVA.

