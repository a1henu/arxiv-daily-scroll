---
layout: default
title: Position: The Inevitable End of One-Architecture-Fits-All-Domains in Time Series Forecasting
---

# Position: The Inevitable End of One-Architecture-Fits-All-Domains in Time Series Forecasting
**arXiv**：[2602.01736v1](https://arxiv.org/abs/2602.01736) · [PDF](https://arxiv.org/pdf/2602.01736.pdf)  
**作者**：Qinwei Ma, Jingzhe Shi, Jiahao Qiu, Zaiwen Yang  

**一句话要点**：呼吁时间序列预测领域放弃通用架构研究，转向特定领域或元学习方法

**关键词**：时间序列预测, 神经网络架构, 领域特定方法, 元学习, 通用性冲突, 研究转向

## 3 点简述
- 分析通用时间序列预测神经网络架构的局限性，指出其与特定领域性能的冲突
- 强调通用架构研究已饱和，对金融、天气等实际领域启发有限
- 建议社区聚焦特定领域深度学习或开发通用元学习方法

## 摘要（原文）

> Recent work has questioned the effectiveness and robustness of neural network architectures for time series forecasting tasks. We summarize these concerns and analyze groundly their inherent limitations: i.e. the irreconcilable conflict between single (or few similar) domains SOTA and generalizability over general domains for time series forecasting neural network architecture designs. Moreover, neural networks architectures for general domain time series forecasting are becoming more and more complicated and their performance has almost saturated in recent years. As a result, network architectures developed aiming at fitting general time series domains are almost not inspiring for real world practices for certain single (or few similar) domains such as Finance, Weather, Traffic, etc: each specific domain develops their own methods that rarely utilize advances in neural network architectures of time series community in recent 2-3 years. As a result, we call for the time series community to shift focus away from research on time series neural network architectures for general domains: these researches have become saturated and away from domain-specific SOTAs over time. We should either (1) focus on deep learning methods for certain specific domain(s), or (2) turn to the development of meta-learning methods for general domains.

