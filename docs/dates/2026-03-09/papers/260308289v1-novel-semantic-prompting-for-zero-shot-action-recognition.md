---
layout: default
title: Novel Semantic Prompting for Zero-Shot Action Recognition
---

# Novel Semantic Prompting for Zero-Shot Action Recognition
**arXiv**：[2603.08289v1](https://arxiv.org/abs/2603.08289) · [PDF](https://arxiv.org/pdf/2603.08289.pdf)  
**作者**：Salman Iqbal, Waheed Rehman  

**一句话要点**：提出SP-CLIP框架，通过结构化语义提示增强预训练视觉语言模型，以提升零样本动作识别性能。

**关键词**：零样本动作识别, 语义提示, 视觉语言模型, 结构化提示, 多抽象层次, 轻量框架

## 3 点简述
- 核心问题：零样本动作识别依赖语义描述，但现有方法多关注时序建模或架构调整，语义提示信号未充分探索。
- 方法要点：引入SP-CLIP，使用多抽象层次（如意图、运动、物体交互）的结构化语义提示，无需修改视觉编码器或学习额外参数。
- 实验或效果：在标准基准测试中，语义提示显著提升零样本动作识别，尤其对细粒度和组合动作有效，保持模型效率和泛化性。

## 摘要（原文）

> Zero-shot action recognition relies on transferring knowledge from vision-language models to unseen actions using semantic descriptions. While recent methods focus on temporal modeling or architectural adaptations to handle video data, we argue that semantic prompting alone provides a strong and underexplored signal for zero-shot action understanding. We introduce SP-CLIP, a lightweight framework that augments frozen vision-language models with structured semantic prompts describing actions at multiple levels of abstraction, such as intent, motion, and object interaction. Without modifying the visual encoder or learning additional parameters, SP-CLIP aligns video representations with enriched textual semantics through prompt aggregation and consistency scoring. Experiments across standard benchmarks show that semantic prompting substantially improves zero-shot action recognition, particularly for fine-grained and compositional actions, while preserving the efficiency and generalization of pretrained models.

