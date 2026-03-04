---
layout: default
title: Beyond Factual Correctness: Mitigating Preference-Inconsistent Explanations in Explainable Recommendation
---

# Beyond Factual Correctness: Mitigating Preference-Inconsistent Explanations in Explainable Recommendation
**arXiv**：[2603.03080v1](https://arxiv.org/abs/2603.03080) · [PDF](https://arxiv.org/pdf/2603.03080.pdf)  
**作者**：Chengkai Wang, Baisong Liu  

**一句话要点**：提出PURE框架以解决可解释推荐中偏好不一致解释的问题

**关键词**：可解释推荐, 偏好对齐, 多跳推理, LLM生成, 用户意图建模, 事实基础

## 3 点简述
- 核心问题：LLM生成解释虽事实正确，但可能基于与用户历史偏好冲突的属性，导致逻辑有效但不可信
- 方法要点：采用选择-生成范式，通过用户意图、特异性和多样性指导，选择事实基础且偏好对齐的多跳推理路径作为证据
- 实验或效果：在三个真实数据集上，PURE减少偏好不一致解释和事实幻觉，同时保持推荐准确性、解释质量和推理效率

## 摘要（原文）

> LLM-based explainable recommenders can produce fluent explanations that are factually correct, yet still justify items using attributes that conflict with a user's historical preferences. Such preference-inconsistent explanations yield logically valid but unconvincing reasoning and are largely missed by standard hallucination or faithfulness metrics. We formalize this failure mode and propose PURE, a preference-aware reasoning framework following a select-then-generate paradigm. Instead of only improving generation, PURE intervenes in evidence selection, it selects a compact set of multi-hop item-centric reasoning paths that are both factually grounded and aligned with user preference structure, guided by user intent, specificity, and diversity to suppress generic, weakly personalized evidence. The selected evidence is then injected into LLM generation via structure-aware prompting that preserves relational constraints. To measure preference inconsistency, we introduce a feature-level, user-centric evaluation metric that reveals misalignment overlooked by factuality-based measures. Experiments on three real-world datasets show that PURE consistently reduces preference-inconsistent explanations and factual hallucinations while maintaining competitive recommendation accuracy, explanation quality, and inference efficiency. These results highlight that trustworthy explanations require not only factual correctness but also justification aligned with user preferences.

