---
layout: default
title: Contrastive Time Series Forecasting with Anomalies
---

# Contrastive Time Series Forecasting with Anomalies
**arXiv**：[2512.11526v1](https://arxiv.org/abs/2512.11526) · [PDF](https://arxiv.org/pdf/2512.11526.pdf)  
**作者**：Joel Ekstrand, Zahra Taghiyarrenani, Slawomir Nowaczyk  

**一句话要点**：提出Co-TSFA框架以解决时间序列预测中异常事件区分问题

**关键词**：时间序列预测, 异常处理, 对比学习, 正则化框架, 分布偏移

## 3 点简述
- 核心问题：标准模型难以区分异常事件对预测的持久或短暂影响，导致过反应或漏检。
- 方法要点：通过输入-输出增强和潜在输出对齐损失，学习忽略无关异常并响应相关分布变化。
- 实验或效果：在交通、电力和现金需求数据集上验证，提升异常条件下性能并保持正常数据准确性。

## 摘要（原文）

> Time series forecasting predicts future values from past data. In real-world settings, some anomalous events have lasting effects and influence the forecast, while others are short-lived and should be ignored. Standard forecasting models fail to make this distinction, often either overreacting to noise or missing persistent shifts. We propose Co-TSFA (Contrastive Time Series Forecasting with Anomalies), a regularization framework that learns when to ignore anomalies and when to respond. Co-TSFA generates input-only and input-output augmentations to model forecast-irrelevant and forecast-relevant anomalies, and introduces a latent-output alignment loss that ties representation changes to forecast changes. This encourages invariance to irrelevant perturbations while preserving sensitivity to meaningful distributional shifts. Experiments on the Traffic and Electricity benchmarks, as well as on a real-world cash-demand dataset, demonstrate that Co-TSFA improves performance under anomalous conditions while maintaining accuracy on normal data. An anonymized GitHub repository with the implementation of Co-TSFA is provided and will be made public upon acceptance.

