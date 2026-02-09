---
layout: default
title: CORE: Comprehensive Ontological Relation Evaluation for Large Language Models
---

# CORE: Comprehensive Ontological Relation Evaluation for Large Language Models
**arXiv**：[2602.06446v1](https://arxiv.org/abs/2602.06446) · [PDF](https://arxiv.org/pdf/2602.06446.pdf)  
**作者**：Satyam Dwivedi, Sanjukta Ghosh, Shivam Dwivedi, Nishi Kumari, Anil Thakur, Anurag Purushottam, Deepak Alok, Praveen Gatla, Manjuprasad B, Bipasha Patgiri  

**一句话要点**：提出CORE数据集与基准以评估大语言模型在语义无关性推理中的能力

**关键词**：大语言模型评估, 语义关系推理, 无关性检测, 基准数据集, 模型校准误差, 语义崩溃率

## 3 点简述
- 核心问题：现有评估很少测试LLMs区分语义相关与无关关系的能力
- 方法要点：构建包含225K多选题和203题开源基准，覆盖74学科和24语义关系类型
- 实验或效果：29个SOTA LLMs在无关对上准确率显著下降，揭示系统性生成虚假关系

## 摘要（原文）

> Large Language Models (LLMs) perform well on many reasoning benchmarks, yet existing evaluations rarely assess their ability to distinguish between meaningful semantic relations and genuine unrelatedness. We introduce CORE (Comprehensive Ontological Relation Evaluation), a dataset of 225K multiple-choice questions spanning 74 disciplines, together with a general-domain open-source benchmark of 203 rigorously validated questions (Cohen's Kappa = 1.0) covering 24 semantic relation types with equal representation of unrelated pairs. A human baseline from 1,000+ participants achieves 92.6% accuracy (95.1% on unrelated pairs). In contrast, 29 state-of-the-art LLMs achieve 48.25-70.9% overall accuracy, with near-ceiling performance on related pairs (86.5-100%) but severe degradation on unrelated pairs (0-41.35%), despite assigning similar confidence (92-94%). Expected Calibration Error increases 2-4x on unrelated pairs, and a mean semantic collapse rate of 37.6% indicates systematic generation of spurious relations. On the CORE 225K MCQs dataset, accuracy further drops to approximately 2%, highlighting substantial challenges in domain-specific semantic reasoning. We identify unrelatedness reasoning as a critical, under-evaluated frontier for LLM evaluation and safety.

