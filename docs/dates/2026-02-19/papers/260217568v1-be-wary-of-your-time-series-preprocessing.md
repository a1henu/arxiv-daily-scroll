---
layout: default
title: Be Wary of Your Time Series Preprocessing
---

# Be Wary of Your Time Series Preprocessing
**arXiv**：[2602.17568v1](https://arxiv.org/abs/2602.17568) · [PDF](https://arxiv.org/pdf/2602.17568.pdf)  
**作者**：Sofiane Ennadir, Tianze Wang, Oleg Smirnov, Sahar Asadi, Lele Cao  

**一句话要点**：提出时间序列表达性框架，分析归一化策略对Transformer模型的影响

**关键词**：时间序列预处理, 归一化策略, Transformer模型, 表达性分析, 理论界限

## 3 点简述
- 核心问题：归一化策略在时间序列Transformer模型中的理论作用未充分探索
- 方法要点：构建表达性框架，量化模型区分相似与不相似输入的能力
- 实验或效果：实证验证显示无单一最优归一化方法，有时省略归一化效果更佳

## 摘要（原文）

> Normalization and scaling are fundamental preprocessing steps in time series modeling, yet their role in Transformer-based models remains underexplored from a theoretical perspective. In this work, we present the first formal analysis of how different normalization strategies, specifically instance-based and global scaling, impact the expressivity of Transformer-based architectures for time series representation learning. We propose a novel expressivity framework tailored to time series, which quantifies a model's ability to distinguish between similar and dissimilar inputs in the representation space. Using this framework, we derive theoretical bounds for two widely used normalization methods: Standard and Min-Max scaling. Our analysis reveals that the choice of normalization strategy can significantly influence the model's representational capacity, depending on the task and data characteristics. We complement our theory with empirical validation on classification and forecasting benchmarks using multiple Transformer-based models. Our results show that no single normalization method consistently outperforms others, and in some cases, omitting normalization entirely leads to superior performance. These findings highlight the critical role of preprocessing in time series learning and motivate the need for more principled normalization strategies tailored to specific tasks and datasets.

