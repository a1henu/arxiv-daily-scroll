---
layout: default
title: Ego: Embedding-Guided Personalization of Vision-Language Models
---

# Ego: Embedding-Guided Personalization of Vision-Language Models
**arXiv**：[2603.09771v1](https://arxiv.org/abs/2603.09771) · [PDF](https://arxiv.org/pdf/2603.09771.pdf)  
**作者**：Soroush Seifi, Simon Gardier, Vaggelis Dorovatas, Daniel Olmeda Reino, Rahaf Aljundi  

**一句话要点**：提出Ego方法，利用模型内部注意力机制提取视觉令牌以实现视觉语言模型的高效个性化。

**关键词**：视觉语言模型个性化, 注意力机制, 视觉令牌提取, 多概念个性化, 视频个性化

## 3 点简述
- 核心问题：现有视觉语言模型个性化方法依赖额外训练或外部模块，限制通用性和部署效率。
- 方法要点：通过模型内部注意力提取代表目标概念的视觉令牌，作为记忆以在测试中召回和描述。
- 实验或效果：在单概念、多概念和视频个性化设置中评估，显示性能提升且开销最小。

## 摘要（原文）

> AI assistants that support humans in daily life are becoming increasingly feasible, driven by the rapid advancements in multimodal language models. A key challenge lies in overcoming the generic nature of these models to deliver personalized experiences. Existing approaches to personalizing large vision language models often rely on additional training stages, which limit generality and scalability, or on engineered pipelines with external pre-trained modules, which hinder deployment efficiency. In this work, we propose an efficient personalization method that leverages the model's inherent ability to capture personalized concepts. Specifically, we extract visual tokens that predominantly represent the target concept by utilizing the model's internal attention mechanisms. These tokens serve as a memory of that specific concept, enabling the model to recall and describe it when it appears in test images. We conduct a comprehensive and unified evaluation of our approach and SOTA methods across various personalization settings including single-concept, multi-concept, and video personalization, demonstrating strong performance gains with minimal personalization overhead.

