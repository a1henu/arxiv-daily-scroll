---
layout: default
title: Geospatial-Reasoning-Driven Vocabulary-Agnostic Remote Sensing Semantic Segmentation
---

# Geospatial-Reasoning-Driven Vocabulary-Agnostic Remote Sensing Semantic Segmentation
**arXiv**：[2602.08206v1](https://arxiv.org/abs/2602.08206) · [PDF](https://arxiv.org/pdf/2602.08206.pdf)  
**作者**：Chufeng Zhou, Jian Wang, Xinyuan Liu, Xiaokang Zhang  

**一句话要点**：提出地理空间推理思维链框架以解决遥感开放词汇语义分割中的语义模糊问题

**关键词**：遥感语义分割, 开放词汇识别, 地理空间推理, 多模态大语言模型, 知识蒸馏, 实例推理

## 3 点简述
- 核心问题：现有遥感开放词汇分割方法依赖外观特征映射，缺乏地理空间上下文感知，导致相似光谱特征但不同语义的地物类别混淆。
- 方法要点：设计离线知识蒸馏和在线实例推理双流协作框架，通过宏场景锚定、视觉特征解耦和知识驱动决策合成生成图像自适应词汇。
- 实验或效果：在LoveDA和GID5基准测试中验证了方法的优越性，实现像素级地理语义对齐。

## 摘要（原文）

> Open-vocabulary semantic segmentation has emerged as a promising research direction in remote sensing, enabling the recognition of diverse land-cover types beyond pre-defined category sets. However, existing methods predominantly rely on the passive mapping of visual features and textual embeddings. This ``appearance-based" paradigm lacks geospatial contextual awareness, leading to severe semantic ambiguity and misclassification when encountering land-cover classes with similar spectral features but distinct semantic attributes. To address this, we propose a Geospatial Reasoning Chain-of-Thought (GR-CoT) framework designed to enhance the scene understanding capabilities of Multimodal Large Language Models (MLLMs), thereby guiding open-vocabulary segmentation models toward precise mapping. The framework comprises two collaborative components: an offline knowledge distillation stream and an online instance reasoning stream. The offline stream establishes fine-grained category interpretation standards to resolve semantic conflicts between similar land-cover types. During online inference, the framework executes a sequential reasoning process involving macro-scenario anchoring, visual feature decoupling, and knowledge-driven decision synthesis. This process generates an image-adaptive vocabulary that guides downstream models to achieve pixel-level alignment with correct geographical semantics. Extensive experiments on the LoveDA and GID5 benchmarks demonstrate the superiority of our approach.

