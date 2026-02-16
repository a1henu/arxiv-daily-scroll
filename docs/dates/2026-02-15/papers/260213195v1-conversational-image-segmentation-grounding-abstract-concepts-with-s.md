---
layout: default
title: Conversational Image Segmentation: Grounding Abstract Concepts with Scalable Supervision
---

# Conversational Image Segmentation: Grounding Abstract Concepts with Scalable Supervision
**arXiv**：[2602.13195v1](https://arxiv.org/abs/2602.13195) · [PDF](https://arxiv.org/pdf/2602.13195.pdf)  
**作者**：Aadarsh Sahoo, Georgia Gkioxari  

**一句话要点**：提出对话式图像分割以解决抽象概念与像素级掩码的关联问题

**关键词**：对话式图像分割, 抽象概念定位, 无监督数据生成, 语言引导分割, 功能推理

## 3 点简述
- 核心问题：现有指称图像定位忽略功能与物理推理，如安全存储刀具的位置
- 方法要点：融合分割先验与语言理解，并开发无监督数据引擎生成提示-掩码对
- 实验或效果：在ConverSeg基准上显著提升，同时保持现有语言引导分割基准的强性能

## 摘要（原文）

> Conversational image segmentation grounds abstract, intent-driven concepts into pixel-accurate masks. Prior work on referring image grounding focuses on categorical and spatial queries (e.g., "left-most apple") and overlooks functional and physical reasoning (e.g., "where can I safely store the knife?"). We address this gap and introduce Conversational Image Segmentation (CIS) and ConverSeg, a benchmark spanning entities, spatial relations, intent, affordances, functions, safety, and physical reasoning. We also present ConverSeg-Net, which fuses strong segmentation priors with language understanding, and an AI-powered data engine that generates prompt-mask pairs without human supervision. We show that current language-guided segmentation models are inadequate for CIS, while ConverSeg-Net trained on our data engine achieves significant gains on ConverSeg and maintains strong performance on existing language-guided segmentation benchmarks. Project webpage: https://glab-caltech.github.io/converseg/

