---
layout: default
title: HyperAlign: Hyperbolic Entailment Cones for Adaptive Text-to-Image Alignment Assessment
---

# HyperAlign: Hyperbolic Entailment Cones for Adaptive Text-to-Image Alignment Assessment
**arXiv**：[2601.04614v1](https://arxiv.org/abs/2601.04614) · [PDF](https://arxiv.org/pdf/2601.04614.pdf)  
**作者**：Wenzhi Chen, Bo Hu, Leida Li, Lihuo He, Wen Lu, Xinbo Gao  

**一句话要点**：提出HyperAlign框架，基于双曲蕴含几何自适应评估文本到图像生成的对齐度

**关键词**：文本到图像对齐评估, 双曲几何, 自适应调制, 蕴含建模, CLIP特征映射

## 3 点简述
- 核心问题：现有方法依赖欧氏空间度量，忽略语义对齐的结构性，且缺乏对不同样本的自适应能力
- 方法要点：将CLIP特征映射到双曲空间，设计动态监督蕴含建模机制，并引入自适应调制回归器校准相似度
- 实验或效果：在单数据库评估和跨数据库泛化任务中表现优异，验证双曲几何建模的有效性

## 摘要（原文）

> With the rapid development of text-to-image generation technology, accurately assessing the alignment between generated images and text prompts has become a critical challenge. Existing methods rely on Euclidean space metrics, neglecting the structured nature of semantic alignment, while lacking adaptive capabilities for different samples. To address these limitations, we propose HyperAlign, an adaptive text-to-image alignment assessment framework based on hyperbolic entailment geometry. First, we extract Euclidean features using CLIP and map them to hyperbolic space. Second, we design a dynamic-supervision entailment modeling mechanism that transforms discrete entailment logic into continuous geometric structure supervision. Finally, we propose an adaptive modulation regressor that utilizes hyperbolic geometric features to generate sample-level modulation parameters, adaptively calibrating Euclidean cosine similarity to predict the final score. HyperAlign achieves highly competitive performance on both single database evaluation and cross-database generalization tasks, fully validating the effectiveness of hyperbolic geometric modeling for image-text alignment assessment.

