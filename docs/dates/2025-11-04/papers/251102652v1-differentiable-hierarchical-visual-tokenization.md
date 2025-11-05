---
layout: default
title: Differentiable Hierarchical Visual Tokenization
---

# Differentiable Hierarchical Visual Tokenization
**arXiv**：[2511.02652v1](https://arxiv.org/abs/2511.02652) · [PDF](https://arxiv.org/pdf/2511.02652.pdf)  
**作者**：Marius Aasan, Martine Hjelkrem-Tan, Nico Catalano, Changkyu Choi, Adín Ramírez Rivera  

**一句话要点**：提出可微分分层视觉分词器，以解决ViT固定补丁忽略图像结构的问题。

**关键词**：视觉Transformer, 可微分分词, 分层模型选择, 图像分类, 密集预测, 光栅矢量转换

## 3 点简述
- 核心问题：ViT依赖固定补丁分词，忽略图像空间和语义结构。
- 方法要点：使用分层模型选择和信息准则，实现端到端可微分分词。
- 实验或效果：在图像分类和密集预测任务中表现竞争性，支持光栅到矢量转换。

## 摘要（原文）

> Vision Transformers rely on fixed patch tokens that ignore the spatial and
> semantic structure of images. In this work, we introduce an end-to-end
> differentiable tokenizer that adapts to image content with pixel-level
> granularity while remaining backward-compatible with existing architectures for
> retrofitting pretrained models. Our method uses hierarchical model selection
> with information criteria to provide competitive performance in both
> image-level classification and dense-prediction tasks, and even supports
> out-of-the-box raster-to-vector conversion.

