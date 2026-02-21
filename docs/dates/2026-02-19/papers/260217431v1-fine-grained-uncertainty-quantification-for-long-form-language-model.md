---
layout: default
title: Fine-Grained Uncertainty Quantification for Long-Form Language Model Outputs: A Comparative Study
---

# Fine-Grained Uncertainty Quantification for Long-Form Language Model Outputs: A Comparative Study
**arXiv**：[2602.17431v1](https://arxiv.org/abs/2602.17431) · [PDF](https://arxiv.org/pdf/2602.17431.pdf)  
**作者**：Dylan Bouchard, Mohit Singh Chauhan, Viren Bajaj, David Skarbrevik  

**一句话要点**：提出细粒度不确定性量化框架以解决长文本语言模型输出的幻觉检测问题

**关键词**：不确定性量化, 长文本生成, 幻觉检测, 一致性评分, 事实性改进, 黑盒方法

## 3 点简述
- 核心问题：现有不确定性量化方法针对短文本设计，在长文本生成中泛化不佳
- 方法要点：基于响应分解、单元级评分和响应级聚合的三阶段分类法，形式化一致性黑盒评分器
- 实验或效果：在多个模型和数据集上验证，claim-response蕴含评分表现最佳，不确定性感知解码提升事实性

## 摘要（原文）

> Uncertainty quantification has emerged as an effective approach to closed-book hallucination detection for LLMs, but existing methods are largely designed for short-form outputs and do not generalize well to long-form generation. We introduce a taxonomy for fine-grained uncertainty quantification in long-form LLM outputs that distinguishes methods by design choices at three stages: response decomposition, unit-level scoring, and response-level aggregation. We formalize several families of consistency-based black-box scorers, providing generalizations and extensions of existing methods. In our experiments across multiple LLMs and datasets, we find 1) claim-response entailment consistently performs better or on par with more complex claim-level scorers, 2) claim-level scoring generally yields better results than sentence-level scoring, and 3) uncertainty-aware decoding is highly effective for improving the factuality of long-form outputs. Our framework clarifies relationships between prior methods, enables apples-to-apples comparisons, and provides practical guidance for selecting components for fine-grained UQ.

