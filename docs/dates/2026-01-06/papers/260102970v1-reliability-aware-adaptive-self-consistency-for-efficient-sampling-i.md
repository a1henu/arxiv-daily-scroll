---
layout: default
title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning
---

# Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning
**arXiv**：[2601.02970v1](https://arxiv.org/abs/2601.02970) · [PDF](https://arxiv.org/pdf/2601.02970.pdf)  
**作者**：Junseok Kim, Nakyeong Yang, Kyungmin Min, Kyomin Jung  

**一句话要点**：提出可靠性感知自适应自一致性方法，以优化大语言模型推理中的采样效率与准确性平衡。

**关键词**：自适应采样, 推理效率, 置信度聚合, 大语言模型, 自一致性

## 3 点简述
- 核心问题：自适应自一致性方法依赖计数停止规则，导致采样冗余和推理成本高。
- 方法要点：通过两阶段设计，基于响应置信度进行证据充分性判断和聚合，提升采样效率。
- 实验或效果：在多个模型和数据集上实现最佳准确率-成本权衡，推理成本降低高达70%。

## 摘要（原文）

> Self-Consistency improves reasoning reliability through multi-sample aggregation, but incurs substantial inference cost. Adaptive self-consistency methods mitigate this issue by adjusting the sampling budget; however, they rely on count-based stopping rules that treat all responses equally, often leading to unnecessary sampling. We propose Reliability-Aware Adaptive Self-Consistency (ReASC), which addresses this limitation by reframing adaptive sampling from response counting to evidence sufficiency, leveraging response-level confidence for principled information aggregation. ReASC operates in two stages: a single-sample decision stage that resolves instances confidently answerable from a single response, and a reliability-aware accumulation stage that aggregates responses by jointly leveraging their frequency and confidence. Across five models and four datasets, ReASC consistently achieves the best accuracy-cost trade-off compared to existing baselines, yielding improved inference efficiency across model scales from 3B to 27B parameters. As a concrete example, ReASC reduces inference cost by up to 70\% relative to self-consistency while preserving accuracy on GSM8K using Gemma-3-4B-it.

