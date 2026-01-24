---
layout: default
title: Zero-Shot Product Attribute Labeling with Vision-Language Models: A Three-Tier Evaluation Framework
---

# Zero-Shot Product Attribute Labeling with Vision-Language Models: A Three-Tier Evaluation Framework
**arXiv**：[2601.15711v1](https://arxiv.org/abs/2601.15711) · [PDF](https://arxiv.org/pdf/2601.15711.pdf)  
**作者**：Shubham Shukla, Kunal Sonalkar  

**一句话要点**：提出三层次评估框架以解决时尚属性零标注中条件属性的检测与分类问题

**关键词**：零样本学习, 视觉语言模型, 时尚属性标注, 条件属性检测, 评估框架, 细粒度分类

## 3 点简述
- 核心问题：时尚属性常为条件性，需先检测适用性再分类，现有评估不足。
- 方法要点：引入三层次框架，分解为整体性能、适用性检测和细粒度分类评估。
- 实验或效果：在DeepFashion-MultiModal上测试九种VLMs，零-shot性能提升三倍，但适用性检测是瓶颈。

## 摘要（原文）

> Fine-grained attribute prediction is essential for fashion retail applications including catalog enrichment, visual search, and recommendation systems. Vision-Language Models (VLMs) offer zero-shot prediction without task-specific training, yet their systematic evaluation on multi-attribute fashion tasks remains underexplored. A key challenge is that fashion attributes are often conditional. For example, "outer fabric" is undefined when no outer garment is visible. This requires models to detect attribute applicability before attempting classification. We introduce a three-tier evaluation framework that decomposes this challenge: (1) overall task performance across all classes (including NA class: suggesting attribute is not applicable) for all attributes, (2) attribute applicability detection, and (3) fine-grained classification when attributes are determinable. Using DeepFashion-MultiModal, which explicitly defines NA (meaning attribute doesn't exist or is not visible) within attribute label spaces, we benchmark nine VLMs spanning flagship (GPT-5, Gemini 2.5 Pro), efficient (GPT-5 Mini, Gemini 2.5 Flash), and ultra-efficient tiers (GPT-5 Nano, Gemini 2.5 Flash-Lite) against classifiers trained on pretrained Fashion-CLIP embeddings on 5,000 images across 18 attributes. Our findings reveal that: (1) zero-shot VLMs achieve 64.0% macro-F1, a threefold improvement over logistic regression on pretrained Fashion-CLIP embeddings; (2) VLMs excel at fine-grained classification (Tier 3: 70.8% F1) but struggle with applicability detection (Tier 2: 34.1% NA-F1), identifying a key bottleneck; (3) efficient models achieve over 90% of flagship performance at lower cost, offering practical deployment paths. This diagnostic framework enables practitioners to pinpoint whether errors stem from visibility detection or classification, guiding targeted improvements for production systems.

