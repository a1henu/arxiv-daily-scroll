---
layout: default
title: Temporal-Conditioned Normalizing Flows for Multivariate Time Series Anomaly Detection
---

# Temporal-Conditioned Normalizing Flows for Multivariate Time Series Anomaly Detection
**arXiv**：[2603.09490v1](https://arxiv.org/abs/2603.09490) · [PDF](https://arxiv.org/pdf/2603.09490.pdf)  
**作者**：David Baumgartner, Helge Langseth, Kenth Engø-Monsen, Heri Ramampiaro  

**一句话要点**：提出时序条件归一化流以解决多元时间序列异常检测问题

**关键词**：多元时间序列, 异常检测, 归一化流, 时序建模, 概率分布, 自回归方法

## 3 点简述
- 核心问题：时间序列异常检测需建模复杂时序依赖与不确定性
- 方法要点：基于先前观测条件归一化流，捕获动态并生成准确概率分布
- 实验或效果：在多样数据集上评估，相比现有方法展现良好准确性与鲁棒性

## 摘要（原文）

> This paper introduces temporal-conditioned normalizing flows (tcNF), a novel framework that addresses anomaly detection in time series data with accurate modeling of temporal dependencies and uncertainty. By conditioning normalizing flows on previous observations, tcNF effectively captures complex temporal dynamics and generates accurate probability distributions of expected behavior. This autoregressive approach enables robust anomaly detection by identifying low-probability events within the learned distribution. We evaluate tcNF on diverse datasets, demonstrating good accuracy and robustness compared to existing methods. A comprehensive analysis of strengths and limitations and open-source code is provided to facilitate reproducibility and future research.

