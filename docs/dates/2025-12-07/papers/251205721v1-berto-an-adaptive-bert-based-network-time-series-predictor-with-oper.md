---
layout: default
title: BERTO: an Adaptive BERT-based Network Time Series Predictor with Operator Preferences in Natural Language
---

# BERTO: an Adaptive BERT-based Network Time Series Predictor with Operator Preferences in Natural Language
**arXiv**：[2512.05721v1](https://arxiv.org/abs/2512.05721) · [PDF](https://arxiv.org/pdf/2512.05721.pdf)  
**作者**：Nitin Priyadarshini Shankar, Vaibhav Singh, Sheetal Kalyani, Christian Maciocco  

**一句话要点**：提出BERTO框架，基于BERT预测蜂窝网络流量并优化能耗，通过自然语言提示平衡节能与性能。

**关键词**：蜂窝网络预测, BERT模型, 能耗优化, 自然语言提示, 平衡损失函数, 智能RAN部署

## 3 点简述
- 核心问题：蜂窝网络中流量预测与能耗优化需平衡节能与服务质量，传统方法难以灵活调整。
- 方法要点：基于Transformer架构，引入平衡损失函数和自然语言提示，允许运营商自定义预测偏好。
- 实验或效果：在真实数据集上，BERTO降低MSE 4.13%，支持1.4 kW功率范围和9倍服务质量变化。

## 摘要（原文）

> We introduce BERTO, a BERT-based framework for traffic prediction and energy optimization in cellular networks. Built on transformer architectures, BERTO delivers high prediction accuracy, while its Balancing Loss Function and prompt-based customization allow operators to adjust the trade-off between power savings and performance. Natural language prompts guide the model to manage underprediction and overprediction in accordance with the operator's intent. Experiments on real-world datasets show that BERTO improves upon existing models with a $4.13$\% reduction in MSE while introducing the feature of balancing competing objectives of power saving and performance through simple natural language inputs, operating over a flexible range of $1.4$ kW in power and up to $9\times$ variation in service quality, making it well suited for intelligent RAN deployments.

