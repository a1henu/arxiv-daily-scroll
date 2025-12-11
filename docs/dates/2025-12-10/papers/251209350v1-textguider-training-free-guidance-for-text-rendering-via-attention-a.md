---
layout: default
title: TextGuider: Training-Free Guidance for Text Rendering via Attention Alignment
---

# TextGuider: Training-Free Guidance for Text Rendering via Attention Alignment
**arXiv**：[2512.09350v1](https://arxiv.org/abs/2512.09350) · [PDF](https://arxiv.org/pdf/2512.09350.pdf)  
**作者**：Kanghyun Baek, Sangyub Lee, Jin Young Choi, Jaewoo Song, Daemin Park, Jooyoung Choi, Chaehun Shin, Bohyung Han, Sungroh Yoon  

**一句话要点**：提出TextGuider以解决扩散模型文本渲染中的文本缺失问题

**关键词**：文本渲染, 扩散模型, 注意力对齐, 训练免费方法, 文本缺失问题

## 3 点简述
- 核心问题：扩散模型在文本渲染中常出现文本部分或完全缺失，现有方法对此关注不足。
- 方法要点：通过分析MM-DiT模型的注意力模式，在去噪早期阶段应用基于新损失函数的潜在引导，对齐文本内容令牌与图像区域。
- 实验或效果：在测试时文本渲染中达到最先进性能，显著提升召回率，并在OCR准确率和CLIP分数上表现强劲。

## 摘要（原文）

> Despite recent advances, diffusion-based text-to-image models still struggle with accurate text rendering. Several studies have proposed fine-tuning or training-free refinement methods for accurate text rendering. However, the critical issue of text omission, where the desired text is partially or entirely missing, remains largely overlooked. In this work, we propose TextGuider, a novel training-free method that encourages accurate and complete text appearance by aligning textual content tokens and text regions in the image. Specifically, we analyze attention patterns in MM-DiT models, particularly for text-related tokens intended to be rendered in the image. Leveraging this observation, we apply latent guidance during the early stage of denoising steps based on two loss functions that we introduce. Our method achieves state-of-the-art performance in test-time text rendering, with significant gains in recall and strong results in OCR accuracy and CLIP score.

