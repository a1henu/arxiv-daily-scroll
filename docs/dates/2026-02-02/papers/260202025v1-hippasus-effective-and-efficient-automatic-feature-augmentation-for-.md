---
layout: default
title: Hippasus: Effective and Efficient Automatic Feature Augmentation for Machine Learning Tasks on Relational Data
---

# Hippasus: Effective and Efficient Automatic Feature Augmentation for Machine Learning Tasks on Relational Data
**arXiv**：[2602.02025v1](https://arxiv.org/abs/2602.02025) · [PDF](https://arxiv.org/pdf/2602.02025.pdf)  
**作者**：Serafeim Papadias, Kostas Patroumpas, Dimitrios Skoutas  

**一句话要点**：提出Hippasus框架，通过结合统计信号与LLM语义推理，高效自动增强关系数据特征

**关键词**：特征增强, 关系数据, 连接路径剪枝, 多路连接优化, LLM语义推理, 机器学习特征工程

## 3 点简述
- 核心问题：关系数据特征增强在复杂模式中面临效果与效率的权衡，现有方法难以兼顾。
- 方法要点：结合轻量统计信号与LLM语义推理剪枝连接路径，优化多路连接算法，整合语义与统计特征选择。
- 实验或效果：在公开数据集上，Hippasus比基线方法提升特征增强准确率高达26.8%，同时保持高运行时性能。

## 摘要（原文）

> Machine learning models depend critically on feature quality, yet useful features are often scattered across multiple relational tables. Feature augmentation enriches a base table by discovering and integrating features from related tables through join operations. However, scaling this process to complex schemas with many tables and multi-hop paths remains challenging. Feature augmentation must address three core tasks: identify promising join paths that connect the base table to candidate tables, execute these joins to materialize augmented data, and select the most informative features from the results. Existing approaches face a fundamental tradeoff between effectiveness and efficiency: achieving high accuracy requires exploring many candidate paths, but exhaustive exploration is computationally prohibitive. Some methods compromise by considering only immediate neighbors, limiting their effectiveness, while others employ neural models that require expensive training data and introduce scalability limitations. We present Hippasus, a modular framework that achieves both goals through three key contributions. First, we combine lightweight statistical signals with semantic reasoning from Large Language Models to prune unpromising join paths before execution, focusing computational resources on high-quality candidates. Second, we employ optimized multi-way join algorithms and consolidate features from multiple paths, substantially reducing execution time. Third, we integrate LLM-based semantic understanding with statistical measures to select features that are both semantically meaningful and empirically predictive. Our experimental evaluation on publicly available datasets shows that Hippasus substantially improves feature augmentation accuracy by up to 26.8% over state-of-the-art baselines while also offering high runtime performance.

