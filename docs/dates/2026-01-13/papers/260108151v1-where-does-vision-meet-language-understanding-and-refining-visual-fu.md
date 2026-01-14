---
layout: default
title: Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention
---

# Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention
**arXiv**：[2601.08151v1](https://arxiv.org/abs/2601.08151) · [PDF](https://arxiv.org/pdf/2601.08151.pdf)  
**作者**：Shezheng Song, Shasha Li, Jie Yu  

**一句话要点**：提出对比注意力框架以优化多模态大语言模型中的视觉-语言融合

**关键词**：多模态大语言模型, 视觉-语言融合, 注意力机制, 层间分析, 对比学习

## 3 点简述
- 核心问题：MLLMs内部视觉与文本信息融合机制不明确，影响模型理解能力。
- 方法要点：通过层间掩码分析揭示融合演化，并设计无训练对比注意力框架突出关键注意力转移。
- 实验或效果：在多个MLLMs和基准测试中验证分析，提升多模态推理性能。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language understanding, yet how they internally integrate visual and textual information remains poorly understood. To bridge this gap, we perform a systematic layer-wise masking analysis across multiple architectures, revealing how visual-text fusion evolves within MLLMs. The results show that fusion emerges at several specific layers rather than being uniformly distributed across the network, and certain models exhibit a late-stage "review" phenomenon where visual signals are reactivated before output generation. Besides, we further analyze layer-wise attention evolution and observe persistent high-attention noise on irrelevant regions, along with gradually increasing attention on text-aligned areas. Guided by these insights, we introduce a training-free contrastive attention framework that models the transformation between early fusion and final layers to highlight meaningful attention shifts. Extensive experiments across various MLLMs and benchmarks validate our analysis and demonstrate that the proposed approach improves multimodal reasoning performance. Code will be released.

