---
layout: default
title: Distributed Dynamic Invariant Causal Prediction in Environmental Time Series
---

# Distributed Dynamic Invariant Causal Prediction in Environmental Time Series
**arXiv**：[2603.02902v1](https://arxiv.org/abs/2603.02902) · [PDF](https://arxiv.org/pdf/2603.02902.pdf)  
**作者**：Ziruo Hao, Tao Yang, Xiaofeng Wu, Bo Hu  

**一句话要点**：提出DisDy-ICPT框架以解决分布式时序中动态不变因果预测问题

**关键词**：分布式学习, 动态因果预测, 不变因果推断, 时序分析, 环境监测

## 3 点简述
- 核心问题：现有方法在分布式时序中缺乏结合环境属性的动态不变因果分析
- 方法要点：无需数据通信，学习动态因果并缓解空间混杂变量
- 实验或效果：在合成和真实环境数据集上优于基线，预测稳定性和准确性更高

## 摘要（原文）

> The extraction of invariant causal relationships from time series data with environmental attributes is critical for robust decision-making in domains such as climate science and environmental monitoring. However, existing methods either emphasize dynamic causal analysis without leveraging environmental contexts or focus on static invariant causal inference, leaving a gap in distributed temporal settings. In this paper, we propose Distributed Dynamic Invariant Causal Prediction in Time-series (DisDy-ICPT), a novel framework that learns dynamic causal relationships over time while mitigating spatial confounding variables without requiring data communication. We theoretically prove that DisDy-ICPT recovers stable causal predictors within a bounded number of communication rounds under standard sampling assumptions. Empirical evaluations on synthetic benchmarks and environment-segmented real-world datasets show that DisDy-ICPT achieves superior predictive stability and accuracy compared to baseline methods A and B. Our approach offers promising applications in carbon monitoring and weather forecasting. Future work will extend DisDy-ICPT to online learning scenarios.

