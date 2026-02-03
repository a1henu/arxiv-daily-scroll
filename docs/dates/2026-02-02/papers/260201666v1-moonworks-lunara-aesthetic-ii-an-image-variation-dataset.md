---
layout: default
title: Moonworks Lunara Aesthetic II: An Image Variation Dataset
---

# Moonworks Lunara Aesthetic II: An Image Variation Dataset
**arXiv**：[2602.01666v1](https://arxiv.org/abs/2602.01666) · [PDF](https://arxiv.org/pdf/2602.01666.pdf)  
**作者**：Yan Wang, Partho Hassan, Samiha Sadeka, Nada Soliman, M M Sayeef Abdullah, Sabit Hassan  

**一句话要点**：提出Lunara Aesthetic II数据集以支持图像生成与编辑系统中上下文一致性的评估与学习

**关键词**：图像变体数据集, 上下文一致性, 身份保持, 美学评分, 图像生成评估, 图像编辑系统

## 3 点简述
- 核心问题：现代图像生成与编辑系统缺乏上下文一致性评估的标准化数据集
- 方法要点：基于Moonworks原创艺术与照片，构建2,854个锚点链接的变体对，应用光照、天气等变换并保持身份稳定
- 实验或效果：数据集展示高身份稳定性、强目标属性实现和超越大规模网络数据集的稳健美学评分

## 摘要（原文）

> We introduce Lunara Aesthetic II, a publicly released, ethically sourced image dataset designed to support controlled evaluation and learning of contextual consistency in modern image generation and editing systems. The dataset comprises 2,854 anchor-linked variation pairs derived from original art and photographs created by Moonworks. Each variation pair applies contextual transformations, such as illumination, weather, viewpoint, scene composition, color tone, or mood; while preserving a stable underlying identity. Lunara Aesthetic II operationalizes identity-preserving contextual variation as a supervision signal while also retaining Lunara's signature high aesthetic scores. Results show high identity stability, strong target attribute realization, and a robust aesthetic profile that exceeds large-scale web datasets. Released under the Apache 2.0 license, Lunara Aesthetic II is intended for benchmarking, fine-tuning, and analysis of contextual generalization, identity preservation, and edit robustness in image generation and image-to-image systems with interpretable, relational supervision. The dataset is publicly available at: https://huggingface.co/datasets/moonworks/lunara-aesthetic-image-variations.

