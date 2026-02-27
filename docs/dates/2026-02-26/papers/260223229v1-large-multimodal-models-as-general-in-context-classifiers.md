---
layout: default
title: Large Multimodal Models as General In-Context Classifiers
---

# Large Multimodal Models as General In-Context Classifiers
**arXiv**：[2602.23229v1](https://arxiv.org/abs/2602.23229) · [PDF](https://arxiv.org/pdf/2602.23229.pdf)  
**作者**：Marco Garosi, Matteo Farina, Alessandro Conti, Massimiliano Mancini, Elisa Ricci  

**一句话要点**：提出CIRCLE方法以提升大型多模态模型在开放世界分类中的上下文学习能力

**关键词**：大型多模态模型, 上下文学习, 开放世界分类, 伪标签迭代, 零样本分类, 多模态分类

## 3 点简述
- 核心问题：大型多模态模型在开放世界分类中受限于不完美的上下文信息
- 方法要点：CIRCLE通过伪标签迭代精炼上下文示例，无需训练
- 实验或效果：CIRCLE在开放世界分类中超越对比视觉语言模型，建立稳健基线

## 摘要（原文）

> Which multimodal model should we use for classification? Previous studies suggest that the answer lies in CLIP-like contrastive Vision-Language Models (VLMs), due to their remarkable performance in zero-shot classification. In contrast, Large Multimodal Models (LMM) are more suitable for complex tasks. In this work, we argue that this answer overlooks an important capability of LMMs: in-context learning. We benchmark state-of-the-art LMMs on diverse datasets for closed-world classification and find that, although their zero-shot performance is lower than CLIP's, LMMs with a few in-context examples can match or even surpass contrastive VLMs with cache-based adapters, their "in-context" equivalent. We extend this analysis to the open-world setting, where the generative nature of LMMs makes them more suitable for the task. In this challenging scenario, LMMs struggle whenever provided with imperfect context information. To address this issue, we propose CIRCLE, a simple training-free method that assigns pseudo-labels to in-context examples, iteratively refining them with the available context itself. Through extensive experiments, we show that CIRCLE establishes a robust baseline for open-world classification, surpassing VLM counterparts and highlighting the potential of LMMs to serve as unified classifiers, and a flexible alternative to specialized models.

