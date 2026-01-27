---
layout: default
title: Conformal Prediction Algorithms for Time Series Forecasting: Methods and Benchmark
---

# Conformal Prediction Algorithms for Time Series Forecasting: Methods and Benchmark
**arXiv**：[2601.18509v1](https://arxiv.org/abs/2601.18509) · [PDF](https://arxiv.org/pdf/2601.18509.pdf)  
**作者**：Andro Sabashvili  

**一句话要点**：综述时间序列预测的保形预测算法，解决非交换性挑战并基准测试方法

**关键词**：时间序列预测, 保形预测, 不确定性量化, 非交换性处理, 算法基准测试, 在线学习

## 3 点简述
- 核心问题：时间序列的时序依赖性违反保形预测的交换性假设，影响不确定性量化可靠性。
- 方法要点：分类评述算法，包括放宽交换性假设、重定义数据单元、建模残差动态和在线学习适应分布漂移。
- 实验或效果：基准测试方法在真实数据上的计算效率和实际性能，强调实用表现。

## 摘要（原文）

> Reliable uncertainty quantification is of critical importance in time series forecasting, yet traditional methods often rely on restrictive distributional assumptions. Conformal prediction (CP) has emerged as a promising distribution-free framework for generating prediction intervals with rigorous theoretical guarantees. However, applying CP to sequential data presents a primary challenge: the temporal dependencies inherent in time series fundamentally violate the core assumption of data exchangeability, upon which standard CP guarantees are built. This review critically examines the main categories of algorithmic solutions designed to address this conflict. We survey and benchmark methods that relax the exchangeability assumption, those that redefine the data unit to be a collection of independent time series, approaches that explicitly model the dynamics of the prediction residuals, and online learning algorithms that adapt to distribution shifts to maintain long-run coverage. By synthesizing these approaches, we highlight computational efficiency and practical performance on real-world data.

