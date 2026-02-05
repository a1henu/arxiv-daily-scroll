---
layout: default
title: Multi-Integration of Labels across Categories for Component Identification (MILCCI)
---

# Multi-Integration of Labels across Categories for Component Identification (MILCCI)
**arXiv**：[2602.04270v1](https://arxiv.org/abs/2602.04270) · [PDF](https://arxiv.org/pdf/2602.04270.pdf)  
**作者**：Noga Mudrik, Yuxi Chen, Gal Mishne, Adam S. Charles  

**一句话要点**：提出MILCCI方法以解决多类别标签在时间序列数据中的编码与分离问题

**关键词**：时间序列分析, 多标签集成, 稀疏分解, 跨试验变异性, 可解释组件

## 3 点简述
- 核心问题：多类别标签在重复测量时间序列数据中的编码与分离挑战
- 方法要点：基于稀疏分解，利用标签相似性进行跨试验调整，学习可解释组件
- 实验或效果：通过合成和真实数据（如投票模式、神经元记录）验证性能

## 摘要（原文）

> Many fields collect large-scale temporal data through repeated measurements (trials), where each trial is labeled with a set of metadata variables spanning several categories. For example, a trial in a neuroscience study may be linked to a value from category (a): task difficulty, and category (b): animal choice. A critical challenge in time-series analysis is to understand how these labels are encoded within the multi-trial observations, and disentangle the distinct effect of each label entry across categories. Here, we present MILCCI, a novel data-driven method that i) identifies the interpretable components underlying the data, ii) captures cross-trial variability, and iii) integrates label information to understand each category's representation within the data. MILCCI extends a sparse per-trial decomposition that leverages label similarities within each category to enable subtle, label-driven cross-trial adjustments in component compositions and to distinguish the contribution of each category. MILCCI also learns each component's corresponding temporal trace, which evolves over time within each trial and varies flexibly across trials. We demonstrate MILCCI's performance through both synthetic and real-world examples, including voting patterns, online page view trends, and neuronal recordings.

