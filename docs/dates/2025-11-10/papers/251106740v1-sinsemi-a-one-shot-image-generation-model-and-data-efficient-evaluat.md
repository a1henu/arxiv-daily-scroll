---
layout: default
title: SinSEMI: A One-Shot Image Generation Model and Data-Efficient Evaluation Framework for Semiconductor Inspection Equipment
---

# SinSEMI: A One-Shot Image Generation Model and Data-Efficient Evaluation Framework for Semiconductor Inspection Equipment
**arXiv**：[2511.06740v1](https://arxiv.org/abs/2511.06740) · [PDF](https://arxiv.org/pdf/2511.06740.pdf)  
**作者**：ChunLiang Wu, Xiaochun Li  

**一句话要点**：提出SinSEMI单样本图像生成模型以解决半导体检测设备数据稀缺问题

**关键词**：单样本学习, 图像生成, 半导体检测, 流模型, LPIPS引导, 数据高效评估

## 3 点简述
- 半导体设备开发早期缺乏大量光学图像，阻碍AI应用发展
- 采用多尺度流模型和LPIPS能量引导，从单图像生成多样真实图像
- 实验显示SinSEMI在视觉质量、定量指标和下游任务中表现优越

## 摘要（原文）

> In the early stages of semiconductor equipment development, obtaining large
> quantities of raw optical images poses a significant challenge. This data
> scarcity hinder the advancement of AI-powered solutions in semiconductor
> manufacturing. To address this challenge, we introduce SinSEMI, a novel
> one-shot learning approach that generates diverse and highly realistic images
> from single optical image. SinSEMI employs a multi-scale flow-based model
> enhanced with LPIPS (Learned Perceptual Image Patch Similarity) energy guidance
> during sampling, ensuring both perceptual realism and output variety. We also
> introduce a comprehensive evaluation framework tailored for this application,
> which enables a thorough assessment using just two reference images. Through
> the evaluation against multiple one-shot generation techniques, we demonstrate
> SinSEMI's superior performance in visual quality, quantitative measures, and
> downstream tasks. Our experimental results demonstrate that SinSEMI-generated
> images achieve both high fidelity and meaningful diversity, making them
> suitable as training data for semiconductor AI applications.

