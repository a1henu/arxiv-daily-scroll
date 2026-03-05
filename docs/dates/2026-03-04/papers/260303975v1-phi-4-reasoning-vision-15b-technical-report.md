---
layout: default
title: Phi-4-reasoning-vision-15B Technical Report
---

# Phi-4-reasoning-vision-15B Technical Report
**arXiv**：[2603.03975v1](https://arxiv.org/abs/2603.03975) · [PDF](https://arxiv.org/pdf/2603.03975.pdf)  
**作者**：Jyoti Aneja, Michael Harrison, Neel Joshi, Tyler LaBonte, John Langford, Eduardo Salinas  

**一句话要点**：提出Phi-4-reasoning-vision-15B，通过架构优化与数据策展实现高效多模态推理

**关键词**：多模态推理, 数据策展, 动态分辨率编码, 科学数学推理, 用户界面理解, 开放权重模型

## 3 点简述
- 核心问题：构建更小、高效的多模态推理模型，以降低训练和推理成本
- 方法要点：采用高分辨率动态编码器、混合推理与非推理数据及显式模式标记
- 实验或效果：在视觉语言任务中表现竞争性，尤其在科学数学推理和界面理解方面突出

## 摘要（原文）

> We present Phi-4-reasoning-vision-15B, a compact open-weight multimodal reasoning model, and share the motivations, design choices, experiments, and learnings that informed its development. Our goal is to contribute practical insight to the research community on building smaller, efficient multimodal reasoning models and to share the result of these learnings as an open-weight model that is good at common vision and language tasks and excels at scientific and mathematical reasoning and understanding user interfaces. Our contributions include demonstrating that careful architecture choices and rigorous data curation enable smaller, open-weight multimodal models to achieve competitive performance with significantly less training and inference-time compute and tokens. The most substantial improvements come from systematic filtering, error correction, and synthetic augmentation -- reinforcing that data quality remains the primary lever for model performance. Systematic ablations show that high-resolution, dynamic-resolution encoders yield consistent improvements, as accurate perception is a prerequisite for high-quality reasoning. Finally, a hybrid mix of reasoning and non-reasoning data with explicit mode tokens allows a single model to deliver fast direct answers for simpler tasks and chain-of-thought reasoning for complex problems.

