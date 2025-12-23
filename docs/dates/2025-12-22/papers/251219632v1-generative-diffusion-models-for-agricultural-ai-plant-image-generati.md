---
layout: default
title: Generative diffusion models for agricultural AI: plant image generation, indoor-to-outdoor translation, and expert preference alignment
---

# Generative diffusion models for agricultural AI: plant image generation, indoor-to-outdoor translation, and expert preference alignment
**arXiv**：[2512.19632v1](https://arxiv.org/abs/2512.19632) · [PDF](https://arxiv.org/pdf/2512.19632.pdf)  
**作者**：Da Tan, Michael Beck, Christopher P. Bidinosti, Robert H. Gulden, Christopher J. Henry  

**一句话要点**：提出基于扩散模型的农业AI生成方法，用于植物图像合成、室内外翻译和专家偏好对齐

**关键词**：扩散模型, 植物图像生成, 室内外图像翻译, 专家偏好对齐, 农业人工智能, 数据增强

## 3 点简述
- 核心问题：农业AI依赖大规模高质量植物图像数据，但野外采集成本高、季节受限
- 方法要点：微调Stable Diffusion生成植物图像，使用DreamBooth进行室内外翻译，基于专家评分进行偏好对齐微调
- 实验或效果：合成图像增强训练数据，提升表型分类和杂草检测准确率，输出更稳定且符合专家偏好

## 摘要（原文）

> The success of agricultural artificial intelligence depends heavily on large, diverse, and high-quality plant image datasets, yet collecting such data in real field conditions is costly, labor intensive, and seasonally constrained. This paper investigates diffusion-based generative modeling to address these challenges through plant image synthesis, indoor-to-outdoor translation, and expert preference aligned fine tuning. First, a Stable Diffusion model is fine tuned on captioned indoor and outdoor plant imagery to generate realistic, text conditioned images of canola and soybean. Evaluation using Inception Score, Frechet Inception Distance, and downstream phenotype classification shows that synthetic images effectively augment training data and improve accuracy. Second, we bridge the gap between high resolution indoor datasets and limited outdoor imagery using DreamBooth-based text inversion and image guided diffusion, generating translated images that enhance weed detection and classification with YOLOv8. Finally, a preference guided fine tuning framework trains a reward model on expert scores and applies reward weighted updates to produce more stable and expert aligned outputs. Together, these components demonstrate a practical pathway toward data efficient generative pipelines for agricultural AI.

