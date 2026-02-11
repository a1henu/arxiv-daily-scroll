---
layout: default
title: ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge
---

# ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge
**arXiv**：[2602.09839v1](https://arxiv.org/abs/2602.09839) · [PDF](https://arxiv.org/pdf/2602.09839.pdf)  
**作者**：Yijie Lin, Guofeng Ding, Haochen Zhou, Haobin Li, Mouxing Yang, Xi Peng  

**一句话要点**：提出ARK基准以评估多模态检索在专业知识和复杂推理方面的性能

**关键词**：多模态检索, 推理技能, 知识域, 困难负样本, 视觉数据类型, 基准评估

## 3 点简述
- 现有基准缺乏对专业知识和复杂推理的诊断，ARK从知识域和推理技能两个维度填补此空白
- ARK包含16种视觉数据类型，使用单模态和多模态查询，并设计针对性困难负样本以避免捷径匹配
- 评估23个检索模型显示知识密集和推理密集检索存在显著差距，简单增强方法有改进但仍有提升空间

## 摘要（原文）

> Existing multimodal retrieval benchmarks largely emphasize semantic matching on daily-life images and offer limited diagnostics of professional knowledge and complex reasoning. To address this gap, we introduce ARK, a benchmark designed to analyze multimodal retrieval from two complementary perspectives: (i) knowledge domains (five domains with 17 subtypes), which characterize the content and expertise retrieval relies on, and (ii) reasoning skills (six categories), which characterize the type of inference over multimodal evidence required to identify the correct candidate. Specifically, ARK evaluates retrieval with both unimodal and multimodal queries and candidates, covering 16 heterogeneous visual data types. To avoid shortcut matching during evaluation, most queries are paired with targeted hard negatives that require multi-step reasoning. We evaluate 23 representative text-based and multimodal retrievers on ARK and observe a pronounced gap between knowledge-intensive and reasoning-intensive retrieval, with fine-grained visual and spatial reasoning emerging as persistent bottlenecks. We further show that simple enhancements such as re-ranking and rewriting yield consistent improvements, but substantial headroom remains.

