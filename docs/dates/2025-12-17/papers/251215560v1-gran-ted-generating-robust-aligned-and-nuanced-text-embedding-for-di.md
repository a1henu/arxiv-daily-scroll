---
layout: default
title: GRAN-TED: Generating Robust, Aligned, and Nuanced Text Embedding for Diffusion Models
---

# GRAN-TED: Generating Robust, Aligned, and Nuanced Text Embedding for Diffusion Models
**arXiv**：[2512.15560v1](https://arxiv.org/abs/2512.15560) · [PDF](https://arxiv.org/pdf/2512.15560.pdf)  
**作者**：Bozhou Li, Sihan Yang, Yushuo Guan, Ruichuan An, Xinlong Chen, Yang Shi, Pengfei Wan, Wentao Zhang, Yuanxing zhang  

**一句话要点**：提出GRAN-TED范式以解决扩散模型中文本编码器评估与优化难题

**关键词**：文本编码器, 扩散模型, 文本到图像生成, 文本到视频生成, 评估基准, 多模态训练

## 3 点简述
- 核心问题：缺乏高效评估框架和预训练语言模型适配视觉合成的困难
- 方法要点：引入TED-6K基准和两阶段训练范式，包括多模态大语言模型微调和层加权
- 实验或效果：GRAN-TED在TED-6K上表现优异，并在文本到图像/视频生成中带来性能提升

## 摘要（原文）

> The text encoder is a critical component of text-to-image and text-to-video diffusion models, fundamentally determining the semantic fidelity of the generated content. However, its development has been hindered by two major challenges: the lack of an efficient evaluation framework that reliably predicts downstream generation performance, and the difficulty of effectively adapting pretrained language models for visual synthesis. To address these issues, we introduce GRAN-TED, a paradigm to Generate Robust, Aligned, and Nuanced Text Embeddings for Diffusion models. Our contribution is twofold. First, we propose TED-6K, a novel text-only benchmark that enables efficient and robust assessment of an encoder's representational quality without requiring costly end-to-end model training. We demonstrate that performance on TED-6K, standardized via a lightweight, unified adapter, strongly correlates with an encoder's effectiveness in downstream generation tasks. Second, guided by this validated framework, we develop a superior text encoder using a novel two-stage training paradigm. This process involves an initial fine-tuning stage on a Multimodal Large Language Model for better visual representation, followed by a layer-wise weighting method to extract more nuanced and potent text features. Our experiments show that the resulting GRAN-TED encoder not only achieves state-of-the-art performance on TED-6K but also leads to demonstrable performance gains in text-to-image and text-to-video generation. Our code is available at the following link: https://anonymous.4open.science/r/GRAN-TED-4FCC/.

