---
layout: default
title: Towards Scalable Pre-training of Visual Tokenizers for Generation
---

# Towards Scalable Pre-training of Visual Tokenizers for Generation
**arXiv**：[2512.13687v1](https://arxiv.org/abs/2512.13687) · [PDF](https://arxiv.org/pdf/2512.13687.pdf)  
**作者**：Jingfeng Yao, Yuda Song, Yucong Zhou, Xinggang Wang  

**一句话要点**：提出VTP框架以解决视觉分词器预训练中的扩展性问题，提升生成质量。

**关键词**：视觉分词器, 预训练扩展性, 生成模型, 语义表示, 联合优化

## 3 点简述
- 核心问题：传统基于重建的视觉分词器预训练导致潜在空间偏向低级信息，生成性能随计算投入提升有限。
- 方法要点：VTP框架联合优化图像-文本对比、自监督和重建损失，强调高层语义表示。
- 实验或效果：大规模预训练后，VTP在生成任务中实现更快收敛和显著性能提升，扩展性优于传统方法。

## 摘要（原文）

> The quality of the latent space in visual tokenizers (e.g., VAEs) is crucial for modern generative models. However, the standard reconstruction-based training paradigm produces a latent space that is biased towards low-level information, leading to a foundation flaw: better pixel-level accuracy does not lead to higher-quality generation. This implies that pouring extensive compute into visual tokenizer pre-training translates poorly to improved performance in generation. We identify this as the ``pre-training scaling problem`` and suggest a necessary shift: to be effective for generation, a latent space must concisely represent high-level semantics. We present VTP, a unified visual tokenizer pre-training framework, pioneering the joint optimization of image-text contrastive, self-supervised, and reconstruction losses. Our large-scale study reveals two principal findings: (1) understanding is a key driver of generation, and (2) much better scaling properties, where generative performance scales effectively with compute, parameters, and data allocated to the pretraining of the visual tokenizer. After large-scale pre-training, our tokenizer delivers a competitive profile (78.2 zero-shot accuracy and 0.36 rFID on ImageNet) and 4.1 times faster convergence on generation compared to advanced distillation methods. More importantly, it scales effectively: without modifying standard DiT training specs, solely investing more FLOPS in pretraining VTP achieves 65.8\% FID improvement in downstream generation, while conventional autoencoder stagnates very early at 1/10 FLOPS. Our pre-trained models are available at https://github.com/MiniMax-AI/VTP.

