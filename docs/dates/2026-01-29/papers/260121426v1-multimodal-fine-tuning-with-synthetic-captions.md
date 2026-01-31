---
layout: default
title: MultiModal Fine-tuning with Synthetic Captions
---

# MultiModal Fine-tuning with Synthetic Captions
**arXiv**：[2601.21426v1](https://arxiv.org/abs/2601.21426) · [PDF](https://arxiv.org/pdf/2601.21426.pdf)  
**作者**：Shohei Enomoto, Shin'ya Yamaguchi  

**一句话要点**：提出基于合成字幕的多模态微调方法，以解决预训练与微调间的模态不匹配问题。

**关键词**：多模态微调, 合成字幕生成, 监督对比损失, 图像分类, 少样本学习, 数据集增强

## 3 点简述
- 核心问题：预训练已转向多模态，但微调仍以单模态为主，限制了预训练表示的优势。
- 方法要点：使用多模态大语言模型生成合成图像字幕，将单模态数据集转换为多模态，并引入监督对比损失和类平均文本嵌入推理技术。
- 实验或效果：在13个图像分类基准测试中超越基线方法，尤其在少样本学习场景下提升显著。

## 摘要（原文）

> In this paper, we address a fundamental gap between pre-training and fine-tuning of deep neural networks: while pre-training has shifted from unimodal to multimodal learning with enhanced visual understanding, fine-tuning predominantly remains unimodal, limiting the benefits of rich pre-trained representations. To bridge this gap, we propose a novel approach that transforms unimodal datasets into multimodal ones using Multimodal Large Language Models (MLLMs) to generate synthetic image captions for fine-tuning models with a multimodal objective. Our method employs carefully designed prompts incorporating class labels and domain context to produce high-quality captions tailored for classification tasks. Furthermore, we introduce a supervised contrastive loss function that explicitly encourages clustering of same-class representations during fine-tuning, along with a new inference technique that leverages class-averaged text embeddings from multiple synthetic captions per image. Extensive experiments across 13 image classification benchmarks demonstrate that our approach outperforms baseline methods, with particularly significant improvements in few-shot learning scenarios. Our work establishes a new paradigm for dataset enhancement that effectively bridges the gap between multimodal pre-training and fine-tuning. Our code is available at https://github.com/s-enmt/MMFT.

