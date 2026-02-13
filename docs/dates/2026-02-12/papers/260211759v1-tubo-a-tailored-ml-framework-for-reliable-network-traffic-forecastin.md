---
layout: default
title: TUBO: A Tailored ML Framework for Reliable Network Traffic Forecasting
---

# TUBO: A Tailored ML Framework for Reliable Network Traffic Forecasting
**arXiv**：[2602.11759v1](https://arxiv.org/abs/2602.11759) · [PDF](https://arxiv.org/pdf/2602.11759.pdf)  
**作者**：Zhihang Yuan, Leyang Xue, Waleed Ahsan, Mahesh K. Marina  

**一句话要点**：提出TUBO框架以解决网络流量预测中突发性和复杂模式导致的可靠性问题

**关键词**：网络流量预测, 机器学习框架, 不确定性量化, 突发处理, 模型选择, 主动流量工程

## 3 点简述
- 核心问题：现有深度学习模型难以有效处理网络流量的突发性和复杂模式，导致预测可靠性不足
- 方法要点：TUBO包含突发处理和模型选择组件，提供确定性预测和量化不确定性
- 实验或效果：在三个真实数据集上，TUBO预测精度提升4倍，突发预测准确率达94%，下游应用提升吞吐量

## 摘要（原文）

> Traffic forecasting based network operation optimization and management offers enormous promise but also presents significant challenges from traffic forecasting perspective. While deep learning models have proven to be relatively more effective than traditional statistical methods for time series forecasting, their reliability is not satisfactory due to their inability to effectively handle unique characteristics of network traffic. In particular, the burst and complex traffic patterns makes the existing models less reliable, as each type of deep learning model has limited capability in capturing traffic patterns. To address this issue, we introduce TUBO, a novel machine learning framework custom designed for reliable network traffic forecasting. TUBO features two key components: burst processing for handling significant traffic fluctuations and model selection for adapting to varying traffic patterns using a pool of models. A standout feature of TUBO is its ability to provide deterministic predictions along with quantified uncertainty, which serves as a cue for identifying the most reliable forecasts. Evaluations on three real-world network demand matrix (DM) datasets (Abilene, GEANT, and CERNET) show that TUBO significantly outperforms existing methods on forecasting accuracy (by 4 times), and also achieves up to 94% accuracy in burst occurrence forecasting. Furthermore, we also consider traffic demand forecasting based proactive traffic engineering (TE) as a downstream use case. Our results show that compared to reactive approaches and proactive TE using the best existing DM forecasting methods, proactive TE powered by TUBO improves aggregated throughput by 9 times and 3 times, respectively.

