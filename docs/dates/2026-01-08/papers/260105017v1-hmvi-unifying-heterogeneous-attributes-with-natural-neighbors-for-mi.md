---
layout: default
title: HMVI: Unifying Heterogeneous Attributes with Natural Neighbors for Missing Value Inference
---

# HMVI: Unifying Heterogeneous Attributes with Natural Neighbors for Missing Value Inference
**arXiv**：[2601.05017v1](https://arxiv.org/abs/2601.05017) · [PDF](https://arxiv.org/pdf/2601.05017.pdf)  
**作者**：Xiaopeng Luo, Zexi Tan, Zhuowei Wang  

**一句话要点**：提出HMVI方法，通过统一建模异构特征依赖以解决表格数据缺失值推断问题。

**关键词**：缺失值推断, 异构特征建模, 表格数据处理, 机器学习增强, 自然邻居方法

## 3 点简述
- 核心问题：现有方法独立处理数值和分类属性，忽略异构特征间的关键依赖关系。
- 方法要点：在统一框架中显式建模跨类型特征依赖，利用完整和不完整实例进行推断。
- 实验或效果：实验显示优于现有技术，显著提升下游机器学习任务性能，提供鲁棒解决方案。

## 摘要（原文）

> Missing value imputation is a fundamental challenge in machine intelligence, heavily dependent on data completeness. Current imputation methods often handle numerical and categorical attributes independently, overlooking critical interdependencies among heterogeneous features. To address these limitations, we propose a novel imputation approach that explicitly models cross-type feature dependencies within a unified framework. Our method leverages both complete and incomplete instances to ensure accurate and consistent imputation in tabular data. Extensive experimental results demonstrate that the proposed approach achieves superior performance over existing techniques and significantly enhances downstream machine learning tasks, providing a robust solution for real-world systems with missing data.

