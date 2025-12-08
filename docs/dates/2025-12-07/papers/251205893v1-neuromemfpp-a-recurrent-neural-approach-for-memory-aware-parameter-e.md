---
layout: default
title: NeuroMemFPP: A recurrent neural approach for memory-aware parameter estimation in fractional Poisson process
---

# NeuroMemFPP: A recurrent neural approach for memory-aware parameter estimation in fractional Poisson process
**arXiv**：[2512.05893v1](https://arxiv.org/abs/2512.05893) · [PDF](https://arxiv.org/pdf/2512.05893.pdf)  
**作者**：Neha Gupta, Aditya Maheshwari  

**一句话要点**：提出基于循环神经网络的框架，用于估计具有记忆性的分数泊松过程参数

**关键词**：分数泊松过程, 参数估计, 循环神经网络, 长短期记忆网络, 时间序列分析

## 3 点简述
- 核心问题：分数泊松过程参数估计，需处理事件到达的记忆和长程依赖性
- 方法要点：使用LSTM网络从到达时间间隔序列中估计参数μ和β，建模时间依赖
- 实验或效果：在合成数据上MSE降低约55.3%，在紧急呼叫和股票交易数据中有效跟踪模式

## 摘要（原文）

> In this paper, we propose a recurrent neural network (RNN)-based framework for estimating the parameters of the fractional Poisson process (FPP), which models event arrivals with memory and long-range dependence. The Long Short-Term Memory (LSTM) network estimates the key parameters $μ>0$ and $β\in(0,1)$ from sequences of inter-arrival times, effectively modeling their temporal dependencies. Our experiments on synthetic data show that the proposed approach reduces the mean squared error (MSE) by about 55.3\% compared to the traditional method of moments (MOM) and performs reliably across different training conditions. We tested the method on two real-world high-frequency datasets: emergency call records from Montgomery County, PA, and AAPL stock trading data. The results show that the LSTM can effectively track daily patterns and parameter changes, indicating its effectiveness on real-world data with complex time dependencies.

