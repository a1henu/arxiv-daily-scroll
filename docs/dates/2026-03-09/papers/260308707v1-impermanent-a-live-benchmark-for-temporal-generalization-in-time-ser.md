---
layout: default
title: Impermanent: A Live Benchmark for Temporal Generalization in Time Series Forecasting
---

# Impermanent: A Live Benchmark for Temporal Generalization in Time Series Forecasting
**arXiv**：[2603.08707v1](https://arxiv.org/abs/2603.08707) · [PDF](https://arxiv.org/pdf/2603.08707.pdf)  
**作者**：Azul Garza, Renée Rosillo, Rodrigo Mendoza-Smith, David Salinas, Andrew Robert Williams, Arjun Ashok, Mononito Goswami, José Martín Juárez  

**一句话要点**：提出Impermanent实时基准以评估时间序列预测模型在开放世界时间变化下的泛化能力

**关键词**：时间序列预测, 实时基准, 泛化评估, 分布偏移, 开源活动数据, 性能稳定性

## 3 点简述
- 核心问题：现有基准使用静态训练-测试分割，易导致数据污染和性能虚高，无法有效评估基础模型的泛化能力。
- 方法要点：引入实时基准，通过连续更新的数据流进行顺序评分，研究时间鲁棒性、分布偏移和性能稳定性。
- 实验或效果：基于GitHub开源活动构建数据集，聚焦400个顶级仓库，提供标准化协议和排行榜，支持可复现的持续比较。

## 摘要（原文）

> Recent advances in time-series forecasting increasingly rely on pre-trained foundation-style models. While these models often claim broad generalization, existing evaluation protocols provide limited evidence. Indeed, most current benchmarks use static train-test splits that can easily lead to contamination as foundation models can inadvertently train on test data or perform model selection using test scores, which can inflate performance. We introduce Impermanent, a live benchmark that evaluates forecasting models under open-world temporal change by scoring forecasts sequentially over time on continuously updated data streams, enabling the study of temporal robustness, distributional shift, and performance stability rather than one-off accuracy on a frozen test set. Impermanent is instantiated on GitHub open-source activity, providing a naturally live and highly non-stationary dataset shaped by releases, shifting contributor behavior, platform/tooling changes, and external events. We focus on the top 400 repositories by star count and construct time series from issues opened, pull requests opened, push events, and new stargazers, evaluated over a rolling window with daily updates, alongside standardized protocols and leaderboards for reproducible, ongoing comparison. By shifting evaluation from static accuracy to sustained performance, Impermanent takes a concrete step toward assessing when and whether foundation-level generalization in time-series forecasting can be meaningfully claimed. Code and a live dashboard are available at https://github.com/TimeCopilot/impermanent and https://impermanent.timecopilot.dev.

