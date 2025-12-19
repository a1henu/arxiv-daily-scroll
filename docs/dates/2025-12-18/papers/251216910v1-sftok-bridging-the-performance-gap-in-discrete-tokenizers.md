---
layout: default
title: SFTok: Bridging the Performance Gap in Discrete Tokenizers
---

# SFTok: Bridging the Performance Gap in Discrete Tokenizers
**arXiv**：[2512.16910v1](https://arxiv.org/abs/2512.16910) · [PDF](https://arxiv.org/pdf/2512.16910.pdf)  
**作者**：Qihang Rao, Borui Zhang, Wenzhao Zheng, Jie Zhou, Jiwen Lu  

**一句话要点**：提出SFTok离散分词器以解决多模态模型中离散分词器性能不足的问题。

**关键词**：离散分词器, 图像重建, 多模态模型, 自强制训练, 去偏拟合

## 3 点简述
- 核心问题：离散分词器在图像重建质量上落后于连续分词器，限制其在多模态系统中的应用。
- 方法要点：采用自强制引导视觉重建和去偏拟合训练策略，解决多步迭代过程中的训练-推理不一致性。
- 实验或效果：在ImageNet上实现rFID=1.21的先进重建质量，并在类到图像生成任务中达到gFID=2.29的优异性能。

## 摘要（原文）

> Recent advances in multimodal models highlight the pivotal role of image tokenization in high-resolution image generation. By compressing images into compact latent representations, tokenizers enable generative models to operate in lower-dimensional spaces, thereby improving computational efficiency and reducing complexity. Discrete tokenizers naturally align with the autoregressive paradigm but still lag behind continuous ones, limiting their adoption in multimodal systems. To address this, we propose \textbf{SFTok}, a discrete tokenizer that incorporates a multi-step iterative mechanism for precise reconstruction. By integrating \textbf{self-forcing guided visual reconstruction} and \textbf{debias-and-fitting training strategy}, SFTok resolves the training-inference inconsistency in multi-step process, significantly enhancing image reconstruction quality. At a high compression rate of only 64 tokens per image, SFTok achieves state-of-the-art reconstruction quality on ImageNet (rFID = 1.21) and demonstrates exceptional performance in class-to-image generation tasks (gFID = 2.29).

