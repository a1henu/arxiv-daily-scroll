---
layout: default
title: Boosting MLLM Spatial Reasoning with Geometrically Referenced 3D Scene Representations
---

# Boosting MLLM Spatial Reasoning with Geometrically Referenced 3D Scene Representations
**arXiv**：[2603.08592v1](https://arxiv.org/abs/2603.08592) · [PDF](https://arxiv.org/pdf/2603.08592.pdf)  
**作者**：Jiangye Yuan, Gowri Kumar, Baoyuan Wang  

**一句话要点**：提出几何参考3D场景表示以增强多模态大语言模型的空间推理能力

**关键词**：3D场景表示, 空间推理, 多模态大语言模型, 零样本学习, 几何参考

## 3 点简述
- 核心问题：多模态大语言模型在3D空间推理方面能力有限
- 方法要点：通过几何参考3D场景表示，将3D几何属性编码为文本参考，无需额外训练
- 实验或效果：在VSI-Bench上提升GPT-5性能8%，空间布局任务提升超11%

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have achieved remarkable success in 2D visual understanding, their ability to reason about 3D space remains limited. To address this gap, we introduce geometrically referenced 3D scene representations (GR3D). Given a set of input images, GR3D annotates objects in the images with unique IDs and encodes their 3D geometric attributes as textual references indexed by these IDs. This representation enables MLLMs to interpret 3D cues using their advanced language-based skills in mathematical reasoning, while concurrently analyzing 2D visual features in a tightly coupled way. We present a simple yet effective approach based on GR3D, which requires no additional training and is readily applicable to different MLLMs. Implemented in a zero-shot setting, our approach boosts GPT-5's performance on VSI-Bench by 8% overall and more than 11% on tasks that rely heavily on spatial layout understanding. Qualitative studies further demonstrate that GR3D empowers MLLMs to perform complex spatial reasoning with highly sparse input views.

