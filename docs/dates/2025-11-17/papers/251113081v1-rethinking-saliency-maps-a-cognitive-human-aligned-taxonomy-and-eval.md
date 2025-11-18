---
layout: default
title: Rethinking Saliency Maps: A Cognitive Human Aligned Taxonomy and Evaluation Framework for Explanations
---

# Rethinking Saliency Maps: A Cognitive Human Aligned Taxonomy and Evaluation Framework for Explanations
**arXiv**：[2511.13081v1](https://arxiv.org/abs/2511.13081) · [PDF](https://arxiv.org/pdf/2511.13081.pdf)  
**作者**：Yehonatan Elisha, Seffi Cohen, Oren Barkan, Noam Koenigstein  

**一句话要点**：提出RFxG分类法与评估框架以解决显著图解释与用户意图对齐问题

**关键词**：显著图解释, 解释评估框架, RFxG分类法, 用户意图对齐, 深度学习可解释性

## 3 点简述
- 核心问题：显著图缺乏统一目的定义，难以评估其对用户查询的对齐性
- 方法要点：引入RFxG分类法，基于参考框架和粒度组织解释类型
- 实验或效果：提出四种新指标，评估十种方法，揭示现有指标局限性

## 摘要（原文）

> Saliency maps are widely used for visual explanations in deep learning, but a fundamental lack of consensus persists regarding their intended purpose and alignment with diverse user queries. This ambiguity hinders the effective evaluation and practical utility of explanation methods.We address this gap by introducing the Reference-Frame $\times$ Granularity (RFxG) taxonomy, a principled conceptual framework that organizes saliency explanations along two essential axes:Reference-Frame: Distinguishing between pointwise ("Why this prediction?") and contrastive ("Why this and not an alternative?") explanations.Granularity: Ranging from fine-grained class-level (e.g., "Why Husky?") to coarse-grained group-level (e.g., "Why Dog?") interpretations.Using the RFxG lens, we demonstrate critical limitations in existing evaluation metrics, which overwhelmingly prioritize pointwise faithfulness while neglecting contrastive reasoning and semantic granularity. To systematically assess explanation quality across both RFxG dimensions, we propose four novel faithfulness metrics. Our comprehensive evaluation framework applies these metrics to ten state-of-the-art saliency methods, four model architectures, and three datasets.By advocating a shift toward user-intent-driven evaluation, our work provides both the conceptual foundation and the practical tools necessary to develop visual explanations that are not only faithful to the underlying model behavior but are also meaningfully aligned with the complexity of human understanding and inquiry.

