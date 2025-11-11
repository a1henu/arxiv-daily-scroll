---
layout: default
title: NOVO: Bridging LLaVA and SAM with Visual-only Prompts for Reasoning Segmentation
---

# NOVO: Bridging LLaVA and SAM with Visual-only Prompts for Reasoning Segmentation
**arXiv**：[2511.06651v1](https://arxiv.org/abs/2511.06651) · [PDF](https://arxiv.org/pdf/2511.06651.pdf)  
**作者**：Kyung-Yoon Yoon, Yeong-Jun Cho  

**一句话要点**：提出NOVO框架，通过视觉提示桥接视觉语言模型与分割模型，实现推理分割。

**关键词**：推理分割, 视觉提示, Segment Anything Model, 视觉语言模型, 无训练细化, 实例分割

## 3 点简述
- 核心问题：现有方法依赖文本嵌入，限制了分割模型与视觉语言模型的直接集成。
- 方法要点：NOVO从VLM输出生成粗掩码和点提示，兼容SAM并引入无训练细化模块。
- 实验效果：在RISeg基准上实现SOTA性能，提升分割质量和可扩展性。

## 摘要（原文）

> In this study, we propose NOVO (NO text, Visual-Only prompts), a novel
> framework that bridges vision-language models (VLMs) and segmentation models
> through visual-only prompts. Unlike prior approaches that feed text-derived SEG
> token embeddings into segmentation models, NOVO instead generates a coarse mask
> and point prompts from the VLM output. These visual prompts are compatible with
> the Segment Anything Model (SAM), preserving alignment with its pretrained
> capabilities. To further enhance boundary quality and enable instance-level
> segmentation, we introduce a training-free refinement module that reduces
> visual artifacts and improves the quality of segmentation masks. We also
> present RISeg, a new benchmark comprising 918 images, 2,533 instance-level
> masks, and diverse reasoning queries to evaluate this task. Experiments
> demonstrate that NOVO achieves state-of-the-art performance across multiple
> metrics and model sizes, demonstrating its effectiveness and scalability in
> reasoning segmentation.

