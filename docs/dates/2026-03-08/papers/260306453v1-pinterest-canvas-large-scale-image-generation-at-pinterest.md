---
layout: default
title: Pinterest Canvas: Large-Scale Image Generation at Pinterest
---

# Pinterest Canvas: Large-Scale Image Generation at Pinterest
**arXiv**：[2603.06453v1](https://arxiv.org/abs/2603.06453) · [PDF](https://arxiv.org/pdf/2603.06453.pdf)  
**作者**：Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  

**一句话要点**：提出Pinterest Canvas系统，通过基础扩散模型与任务特定微调支持大规模图像编辑与增强。

**关键词**：大规模图像生成, 扩散模型, 任务特定微调, 图像编辑, 在线实验

## 3 点简述
- 问题：通用图像生成模型难以通过提示或简单推理适应严格产品需求。
- 方法：先训练基础扩散模型，再针对下游任务快速微调专用变体。
- 效果：在线A/B实验显示增强图像提升18.0%和12.5%参与度，优于第三方模型。

## 摘要（原文）

> While recent image generation models demonstrate a remarkable ability to handle a wide variety of image generation tasks, this flexibility makes them hard to control via prompting or simple inference adaptation alone, rendering them unsuitable for use cases with strict product requirements. In this paper, we introduce Pinterest Canvas, our large-scale image generation system built to support image editing and enhancement use cases at Pinterest. Canvas is first trained on a diverse, multimodal dataset to produce a foundational diffusion model with broad image-editing capabilities. However, rather than relying on one generic model to handle every downstream task, we instead rapidly fine-tune variants of this base model on task-specific datasets, producing specialized models for individual use cases. We describe key components of Canvas and summarize our best practices for dataset curation, training, and inference. We also showcase task-specific variants through case studies on background enhancement and aspect-ratio outpainting, highlighting how we tackle their specific product requirements. Online A/B experiments demonstrate that our enhanced images receive a significant 18.0% and 12.5% engagement lift, respectively, and comparisons with human raters further validate that our models outperform third-party models on these tasks. Finally, we showcase other Canvas variants, including multi-image scene synthesis and image-to-video generation, demonstrating that our approach can generalize to a wide variety of potential downstream tasks.

