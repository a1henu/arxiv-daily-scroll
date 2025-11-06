---
layout: default
title: Decoupling Augmentation Bias in Prompt Learning for Vision-Language Models
---

# Decoupling Augmentation Bias in Prompt Learning for Vision-Language Models
**arXiv**：[2511.03367v1](https://arxiv.org/abs/2511.03367) · [PDF](https://arxiv.org/pdf/2511.03367.pdf)  
**作者**：Gahyeon Kim, Sohee Kim, Seokju Lee  

**一句话要点**：提出AAPL方法，通过解耦增强偏差提升视觉语言模型的提示学习泛化能力

**关键词**：提示学习, 视觉语言模型, 数据增强, 泛化能力, 对抗学习

## 3 点简述
- 核心问题：现有提示学习方法如CoCoOp泛化能力不足，未充分利用图像增强
- 方法要点：引入对抗性令牌嵌入，解耦增强引入的表面变化与类别语义表示
- 实验或效果：在11个基准数据集上，AAPL在多种设置中优于现有方法

## 摘要（原文）

> Recent advances in large-scale vision and language models have led to
> significant progress in zero-shot learning tasks. Methods such as CoOp and
> CoCoOp have shown that replacing handcrafted prompts with learnable vectors,
> known as prompt learning, can result in improved performance. However, these
> models often struggle to generalize to entirely unseen categories. While
> traditional zero-shot learning techniques benefit from various data
> augmentation strategies, prompt learning has primarily focused on text-based
> modifications, leaving the potential of image-based augmentation largely
> unexplored. In this work, we explore how image-level augmentations,
> particularly those that introduce attribute-specific variations, can support
> and enhance prompt learning. Our analysis examines the interaction between
> these augmentations and soft prompt frameworks, revealing their potential to
> improve generalization. We also identify a limitation in existing methods, such
> as CoCoOp, which do not provide explicit guidance for learning prompts that
> focus on semantically meaningful visual features. To address this, we propose
> Adding Attributes to Prompt Learning, AAPL, a novel method that introduces
> adversarial token embeddings to decouple superficial visual variations
> introduced by augmentation from class-relevant semantic representations. This
> decoupling enables the learned prompts to concentrate on visually
> discriminative features that align with the target categories. We conduct
> comprehensive experiments on eleven benchmark datasets, and AAPL consistently
> outperforms existing methods across few-shot, zero-shot, cross-dataset, and
> domain generalization settings. Our source code is publicly available at:
> https://github.com/Gahyeonkim09/AAPL

