---
layout: default
title: EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education
---

# EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education
**arXiv**：[2603.03066v1](https://arxiv.org/abs/2603.03066) · [PDF](https://arxiv.org/pdf/2603.03066.pdf)  
**作者**：Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  

**一句话要点**：提出EduVQA基准与S2D-MoE模块，评估教育场景下AI生成视频的质量与提示对齐。

**关键词**：AI生成视频质量评估, 教育视频基准, 提示对齐, 细粒度标注, 混合专家模块

## 3 点简述
- 核心问题：AI生成视频在教育中缺乏针对数学概念学习的质量评估基准。
- 方法要点：构建EduAIGV-1k数据集，包含细粒度标注，并设计S2D-MoE模块增强子维度依赖。
- 实验或效果：EduVQA在感知质量和提示对齐评估上优于现有VQA基线。

## 摘要（原文）

> While AI-generated content (AIGC) models have achieved remarkable success in generating photorealistic videos, their potential to support visual, story-driven learning in education remains largely untapped. To close this gap, we present EduAIGV-1k, the first benchmark dataset and evaluation framework dedicated to assessing the quality of AI-generated videos (AIGVs) designed to teach foundational math concepts, such as numbers and geometry, to young learners. EduAIGV-1k contains 1,130 short videos produced by ten state-of-the-art text-to-video (T2V) models using 113 pedagogy-oriented prompts. Each video is accompanied by rich, fine-grained annotations along two complementary axes: (1) Perceptual quality, disentangled into spatial and temporal fidelity, and (2) Prompt alignment, labeled at the word-level and sentence-level to quantify the degree to which each mathematical concept in the prompt is accurately grounded in the generated video. These fine-grained annotations transform each video into a multi-dimensional, interpretable supervision signal, far beyond a single quality score. Leveraging this dense feedback, we introduce EduVQA for both perceptual and alignment quality assessment of AIGVs. In particular, we propose a Structured 2D Mixture-of-Experts (S2D-MoE) module, which enhances the dependency between overall quality and each sub-dimension by shared experts and dynamic 2D gating matrix. Extensive experiments show our EduVQA consistently outperforms existing VQA baselines. Both our dataset and code will be publicly available.

