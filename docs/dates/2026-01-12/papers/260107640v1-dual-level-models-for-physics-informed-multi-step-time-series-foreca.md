---
layout: default
title: Dual-Level Models for Physics-Informed Multi-Step Time Series Forecasting
---

# Dual-Level Models for Physics-Informed Multi-Step Time Series Forecasting
**arXiv**：[2601.07640v1](https://arxiv.org/abs/2601.07640) · [PDF](https://arxiv.org/pdf/2601.07640.pdf)  
**作者**：Mahdi Nasiri, Johanna Kortelainen, Simo Särkkä  

**一句话要点**：提出双层级物理信息多步时间序列预测方法，以提升动态系统预测精度与泛化能力。

**关键词**：多步时间序列预测, 物理信息神经网络, 概率状态转移模型, 长短期记忆网络, 动态系统建模, 泛化性能

## 3 点简述
- 核心问题：传统机理模型与纯数据驱动方法在动态系统多步预测中存在模型不完整和泛化差的问题。
- 方法要点：第一层用LSTM增强概率状态转移模型预测输入变量，第二层用物理信息神经网络生成多步输出预测。
- 实验或效果：输入预测模型优于传统方法，物理信息神经网络在多个测试案例中展现出更强的泛化与预测性能。

## 摘要（原文）

> This paper develops an approach for multi-step forecasting of dynamical systems by integrating probabilistic input forecasting with physics-informed output prediction. Accurate multi-step forecasting of time series systems is important for the automatic control and optimization of physical processes, enabling more precise decision-making. While mechanistic-based and data-driven machine learning (ML) approaches have been employed for time series forecasting, they face significant limitations. Incomplete knowledge of process mathematical models limits mechanistic-based direct employment, while purely data-driven ML models struggle with dynamic environments, leading to poor generalization. To address these limitations, this paper proposes a dual-level strategy for physics-informed forecasting of dynamical systems. On the first level, input variables are forecast using a hybrid method that integrates a long short-term memory (LSTM) network into probabilistic state transition models (STMs). On the second level, these stochastically predicted inputs are sequentially fed into a physics-informed neural network (PINN) to generate multi-step output predictions. The experimental results of the paper demonstrate that the hybrid input forecasting models achieve a higher log-likelihood and lower mean squared errors (MSE) compared to conventional STMs. Furthermore, the PINNs driven by the input forecasting models outperform their purely data-driven counterparts in terms of MSE and log-likelihood, exhibiting stronger generalization and forecasting performance across multiple test cases.

