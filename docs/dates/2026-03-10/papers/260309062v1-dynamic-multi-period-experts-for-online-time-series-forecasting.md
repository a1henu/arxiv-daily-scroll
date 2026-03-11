---
layout: default
title: Dynamic Multi-period Experts for Online Time Series Forecasting
---

# Dynamic Multi-period Experts for Online Time Series Forecasting
**arXiv**：[2603.09062v1](https://arxiv.org/abs/2603.09062) · [PDF](https://arxiv.org/pdf/2603.09062.pdf)  
**作者**：Seungha Hong, Sukang Chae, Suyeon Kim, Sanghwan Jang, Hwanjo Yu  

**一句话要点**：提出DynaME框架以解决在线时间序列预测中的概念漂移问题

**关键词**：在线时间序列预测, 概念漂移, 动态专家系统, 重现漂移, 新兴漂移, 混合框架

## 3 点简述
- 核心问题：现有方法将概念漂移视为单一现象，难以适应其双重性质。
- 方法要点：将概念漂移分为重现漂移和新兴漂移，分别用动态专家委员会和稳定专家处理。
- 实验或效果：在多个基准数据集上验证，DynaME显著优于现有基线方法。

## 摘要（原文）

> Online Time Series Forecasting (OTSF) requires models to continuously adapt to concept drift. However, existing methods often treat concept drift as a monolithic phenomenon. To address this limitation, we first redefine concept drift by categorizing it into two distinct types: Recurring Drift, where previously seen patterns reappear, and Emergent Drift, where entirely new patterns emerge. We then propose DynaME (Dynamic Multi-period Experts), a novel hybrid framework designed to effectively address this dual nature of drift. For Recurring Drift, DynaME employs a committee of specialized experts that are dynamically fitted to the most relevant historical periodic patterns at each time step. For Emergent Drift, the framework detects high-uncertainty scenarios and shifts reliance to a stable, general expert. Extensive experiments on several benchmark datasets and backbones demonstrate that DynaME effectively adapts to both concept drifts and significantly outperforms existing baselines.

