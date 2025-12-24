---
layout: default
title: Improving ML Training Data with Gold-Standard Quality Metrics
---

# Improving ML Training Data with Gold-Standard Quality Metrics
**arXiv**：[2512.20577v1](https://arxiv.org/abs/2512.20577) · [PDF](https://arxiv.org/pdf/2512.20577.pdf)  
**作者**：Leslie Barrett, Michael W. Sherman  

**一句话要点**：提出基于统计方法评估和提升手标训练数据质量，以解决数据质量不一致问题。

**关键词**：训练数据质量, 标注一致性, 统计评估, 机器学习标注, 数据质量控制

## 3 点简述
- 核心问题：手标训练数据质量在标注过程中差异大，但质量控制研究不足。
- 方法要点：使用统计方法测量标注一致性和一致性，通过多轮标注降低方差来提升质量。
- 实验或效果：展示无需每项多标即可收集高质量数据，且标注者适应期可能不足以最小化错误。

## 摘要（原文）

> Hand-tagged training data is essential to many machine learning tasks. However, training data quality control has received little attention in the literature, despite data quality varying considerably with the tagging exercise. We propose methods to evaluate and enhance the quality of hand-tagged training data using statistical approaches to measure tagging consistency and agreement. We show that agreement metrics give more reliable results if recorded over multiple iterations of tagging, where declining variance in such recordings is an indicator of increasing data quality. We also show one way a tagging project can collect high-quality training data without requiring multiple tags for every work item, and that a tagger burn-in period may not be sufficient for minimizing tagger errors.

