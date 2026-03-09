---
layout: default
title: Domain-Adaptive Model Merging across Disconnected Modes
---

# Domain-Adaptive Model Merging across Disconnected Modes
**arXiv**：[2603.05957v1](https://arxiv.org/abs/2603.05957) · [PDF](https://arxiv.org/pdf/2603.05957.pdf)  
**作者**：Junming Liu, Yusen Zhang, Rongchao Zhang, Wenkai Zhu, Tian Wu  

**一句话要点**：提出DMM框架以解决跨域模型合并中数据分散与模型差异大的问题

**关键词**：模型合并, 域适应, 知识蒸馏, 数据合成, 多模态学习

## 3 点简述
- 核心问题：数据因隐私或异构无法集中，限制跨域学习与模型训练
- 方法要点：通过三步流程，包括独立训练、相似模型合并和基于伪数据的轻量精炼
- 实验或效果：在单模态和多模态基准测试中，DMM优于现有合并方法

## 摘要（原文）

> Learning across domains is challenging when data cannot be centralized due to privacy or heterogeneity, which limits the ability to train a single comprehensive model. Model merging provides an appealing alternative by consolidating knowledge from multiple specialized models into one, avoiding data sharing and reducing retraining cost. In this work, we present DMM, a data-free model merging framework designed to handle highly divergent models. DMM proceeds in three steps. First, domain-specific models are trained independently. Second, models with high similarity are merged using standard techniques to ensure stability. Third, we synthesize pseudo-data from normalization statistics and distill knowledge from divergent models into the merged model through a lightweight refinement guided by these samples. This approach preserves rare but critical knowledge while maintaining stability. Extensive experiments on unimodal and multimodal benchmarks show that DMM achieves state-of-the-art performance over existing merging methods.

