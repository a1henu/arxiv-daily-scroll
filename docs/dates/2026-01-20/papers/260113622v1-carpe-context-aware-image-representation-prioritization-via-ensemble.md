---
layout: default
title: CARPE: Context-Aware Image Representation Prioritization via Ensemble for Large Vision-Language Models
---

# CARPE: Context-Aware Image Representation Prioritization via Ensemble for Large Vision-Language Models
**arXiv**：[2601.13622v1](https://arxiv.org/abs/2601.13622) · [PDF](https://arxiv.org/pdf/2601.13622.pdf)  
**作者**：Donghee Lee, Rui Cai, Zhe Zhao  

**一句话要点**：提出CARPE框架以解决大型视觉语言模型在图像分类等视觉中心任务中表现不佳的问题

**关键词**：大型视觉语言模型, 图像分类, 上下文感知集成, 视觉集成层, 模态加权, 模型无关框架

## 3 点简述
- 核心问题：大型视觉语言模型在图像分类等视觉中心任务中表现不如其基础视觉编码器，如CLIP模型
- 方法要点：通过视觉集成层和上下文感知集成策略，自适应加权视觉和文本模态，优先图像表示或依赖语言模型推理
- 实验或效果：在图像分类和视觉语言基准测试中实现一致改进，提升泛化能力

## 摘要（原文）

> Recent advancements in Large Vision-Language Models (LVLMs) have pushed them closer to becoming general-purpose assistants. Despite their strong performance, LVLMs still struggle with vision-centric tasks such as image classification, underperforming compared to their base vision encoders, which are often CLIP-based models. To address this limitation, we propose Context-Aware Image Representation Prioritization via Ensemble (CARPE), a novel, model-agnostic framework which introduces vision-integration layers and a context-aware ensemble strategy to identify when to prioritize image representations or rely on the reasoning capabilities of the language model. This design enhances the model's ability to adaptively weight visual and textual modalities and enables the model to capture various aspects of image representations, leading to consistent improvements in generalization across classification and vision-language benchmarks. Extensive experiments demonstrate that CARPE not only improves performance on image classification benchmarks but also enhances results across various vision-language benchmarks. Finally, CARPE is designed to be effectively integrated with most open-source LVLMs that consist of a vision encoder and a language model, ensuring its adaptability across diverse architectures.

