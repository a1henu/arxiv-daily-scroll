---
layout: default
title: Closing the Loop: A Control-Theoretic Framework for Provably Stable Time Series Forecasting with LLMs
---

# Closing the Loop: A Control-Theoretic Framework for Provably Stable Time Series Forecasting with LLMs
**arXiv**：[2602.12756v1](https://arxiv.org/abs/2602.12756) · [PDF](https://arxiv.org/pdf/2602.12756.pdf)  
**作者**：Xingyu Zhang, Hanyun Du, Zeen Song, Jianqi Zhang, Changwen Zheng, Wenwen Qiang  

**一句话要点**：提出F-LLM闭环框架，利用控制理论解决大语言模型在时间序列预测中的误差累积问题。

**关键词**：时间序列预测, 大语言模型, 控制理论, 闭环框架, 误差累积, 稳定性保证

## 3 点简述
- 核心问题：现有大语言模型在时间序列预测中采用开环自回归策略，导致误差累积和轨迹漂移。
- 方法要点：引入控制理论，设计闭环框架F-LLM，通过可学习残差估计器和反馈控制器主动稳定预测轨迹。
- 实验或效果：理论证明闭环机制确保误差有界，实验显示F-LLM显著减少误差传播，在基准测试中表现良好。

## 摘要（原文）

> Large Language Models (LLMs) have recently shown exceptional potential in time series forecasting, leveraging their inherent sequential reasoning capabilities to model complex temporal dynamics. However, existing approaches typically employ a naive autoregressive generation strategy. We identify a critical theoretical flaw in this paradigm: during inference, the model operates in an open-loop manner, consuming its own generated outputs recursively. This leads to inevitable error accumulation (exposure bias), where minor early deviations cascade into significant trajectory drift over long horizons. In this paper, we reformulate autoregressive forecasting through the lens of control theory, proposing \textbf{F-LLM} (Feedback-driven LLM), a novel closed-loop framework. Unlike standard methods that passively propagate errors, F-LLM actively stabilizes the trajectory via a learnable residual estimator (Observer) and a feedback controller. Furthermore, we provide a theoretical guarantee that our closed-loop mechanism ensures uniformly bounded error, provided the base model satisfies a local Lipschitz constraint. Extensive experiments demonstrate that F-LLM significantly mitigates error propagation, achieving good performance on time series benchmarks.

