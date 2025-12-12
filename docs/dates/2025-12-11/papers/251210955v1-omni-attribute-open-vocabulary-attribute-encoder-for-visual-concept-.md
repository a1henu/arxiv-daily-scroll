---
layout: default
title: Omni-Attribute: Open-vocabulary Attribute Encoder for Visual Concept Personalization
---

# Omni-Attribute: Open-vocabulary Attribute Encoder for Visual Concept Personalization
**arXiv**：[2512.10955v1](https://arxiv.org/abs/2512.10955) · [PDF](https://arxiv.org/pdf/2512.10955.pdf)  
**作者**：Tsai-Shien Chen, Aliaksandr Siarohin, Guocheng Gordon Qian, Kuan-Chieh Jackson Wang, Egor Nemchinov, Moayed Haji-Ali, Riza Alp Guler, Willi Menapace, Ivan Skorokhodov, Anil Kag, Jun-Yan Zhu, Sergey Tulyakov  

**一句话要点**：提出Omni-Attribute开放词汇属性编码器，以解决视觉概念个性化中属性纠缠和信息泄漏问题。

**关键词**：视觉概念个性化, 开放词汇属性编码, 属性解缠, 对比学习, 图像生成, 多属性控制

## 3 点简述
- 核心问题：现有方法使用通用图像编码器，导致多个视觉属性纠缠，难以隔离单一属性，引发信息泄漏和不一致合成。
- 方法要点：联合设计数据和模型，包括构建语义链接图像对标注正负属性，以及采用双目标训练平衡生成保真度和对比解缠。
- 实验或效果：在开放词汇属性检索、个性化和组合生成任务中实现最先进性能，验证了编码器的有效性。

## 摘要（原文）

> Visual concept personalization aims to transfer only specific image attributes, such as identity, expression, lighting, and style, into unseen contexts. However, existing methods rely on holistic embeddings from general-purpose image encoders, which entangle multiple visual factors and make it difficult to isolate a single attribute. This often leads to information leakage and incoherent synthesis. To address this limitation, we introduce Omni-Attribute, the first open-vocabulary image attribute encoder designed to learn high-fidelity, attribute-specific representations. Our approach jointly designs the data and model: (i) we curate semantically linked image pairs annotated with positive and negative attributes to explicitly teach the encoder what to preserve or suppress; and (ii) we adopt a dual-objective training paradigm that balances generative fidelity with contrastive disentanglement. The resulting embeddings prove effective for open-vocabulary attribute retrieval, personalization, and compositional generation, achieving state-of-the-art performance across multiple benchmarks.

