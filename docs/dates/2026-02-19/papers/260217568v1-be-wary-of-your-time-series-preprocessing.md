---
layout: default
title: Be Wary of Your Time Series Preprocessing
---

# Be Wary of Your Time Series Preprocessing
**arXiv**：[2602.17568v1](https://arxiv.org/abs/2602.17568) · [PDF](https://arxiv.org/pdf/2602.17568.pdf)  
**作者**：Sofiane Ennadir, Tianze Wang, Oleg Smirnov, Sahar Asadi, Lele Cao  

**一句话要点**：分析时间序列预处理对Transformer模型表达力的影响，提出理论框架与实证验证

**关键词**：时间序列预处理, Transformer模型, 归一化策略, 表达力分析, 理论框架, 实证验证

## 3 点简述
- 核心问题：时间序列建模中归一化与缩放对Transformer模型表达力的理论影响未充分探索
- 方法要点：提出时间序列表达力框架，量化模型区分输入能力，推导标准与最小-最大缩放的界限
- 实验或效果：在分类和预测基准上验证，无单一归一化方法始终最优，有时省略归一化性能更佳

## 摘要（原文）

> Normalization and scaling are fundamental preprocessing steps in time series modeling, yet their role in Transformer-based models remains underexplored from a theoretical perspective. In this work, we present the first formal analysis of how different normalization strategies, specifically instance-based and global scaling, impact the expressivity of Transformer-based architectures for time series representation learning. We propose a novel expressivity framework tailored to time series, which quantifies a model's ability to distinguish between similar and dissimilar inputs in the representation space. Using this framework, we derive theoretical bounds for two widely used normalization methods: Standard and Min-Max scaling. Our analysis reveals that the choice of normalization strategy can significantly influence the model's representational capacity, depending on the task and data characteristics. We complement our theory with empirical validation on classification and forecasting benchmarks using multiple Transformer-based models. Our results show that no single normalization method consistently outperforms others, and in some cases, omitting normalization entirely leads to superior performance. These findings highlight the critical role of preprocessing in time series learning and motivate the need for more principled normalization strategies tailored to specific tasks and datasets.

