---
layout: default
title: When Weak LLMs Speak with Confidence, Preference Alignment Gets Stronger
---

# When Weak LLMs Speak with Confidence, Preference Alignment Gets Stronger
**arXiv**：[2603.04968v1](https://arxiv.org/abs/2603.04968) · [PDF](https://arxiv.org/pdf/2603.04968.pdf)  
**作者**：Amirabbas Afzali, Myeongho Jeon, Maria Brbic  

**一句话要点**：提出置信加权偏好优化框架，利用弱大语言模型的高置信样本提升偏好对齐效率

**关键词**：偏好对齐, 置信加权, 弱大语言模型, 成本降低, 样本选择, 优化框架

## 3 点简述
- 核心问题：偏好对齐依赖昂贵人工标注或大规模API模型，成本高
- 方法要点：基于弱大语言模型置信度重加权训练样本，可适配不同优化目标
- 实验或效果：仅用20%人工标注，性能超越标准DPO使用100%标注的模型

## 摘要（原文）

> Preference alignment is an essential step in adapting large language models (LLMs) to human values, but existing approaches typically depend on costly human annotations or large-scale API-based models. We explore whether a weak LLM can instead act as an effective annotator. We surprisingly find that selecting only a subset of a weak LLM's highly confident samples leads to substantially better performance than using full human annotations. Building on this insight, we propose Confidence-Weighted Preference Optimization (CW-PO), a general framework that re-weights training samples by a weak LLM's confidence and can be applied across different preference optimization objectives. Notably, the model aligned by CW-PO with just 20% of human annotations outperforms the model trained with 100% of annotations under standard DPO. These results suggest that weak LLMs, when paired with confidence weighting, can dramatically reduce the cost of preference alignment while even outperforming methods trained on fully human-labeled data.

