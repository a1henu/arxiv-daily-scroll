---
layout: default
title: CEPAE: Conditional Entropy-Penalized Autoencoders for Time Series Counterfactuals
---

# CEPAE: Conditional Entropy-Penalized Autoencoders for Time Series Counterfactuals
**arXiv**：[2602.15546v1](https://arxiv.org/abs/2602.15546) · [PDF](https://arxiv.org/pdf/2602.15546.pdf)  
**作者**：Tomàs Garriga, Gerard Sanz, Eduard Serrahima de Cambra, Axel Brando  

**一句话要点**：提出条件熵惩罚自编码器以解决时间序列反事实推理问题

**关键词**：时间序列分析, 反事实推理, 自编码器, 条件熵惩罚, 结构因果模型, 变分推理

## 3 点简述
- 核心问题：时间序列反事实推理在金融、医疗等领域对决策至关重要，但现有方法未充分适配时间序列场景。
- 方法要点：基于结构因果模型和变分自编码器，引入条件熵惩罚损失以促进潜在空间解耦表示。
- 实验或效果：在合成、半合成和真实数据集上验证，CEPAE在评估指标上通常优于其他方法。

## 摘要（原文）

> The ability to accurately perform counterfactual inference on time series is crucial for decision-making in fields like finance, healthcare, and marketing, as it allows us to understand the impact of events or treatments on outcomes over time. In this paper, we introduce a new counterfactual inference approach tailored to time series data impacted by market events, which is motivated by an industrial application. Utilizing the abduction-action-prediction procedure and the Structural Causal Model framework, we first adapt methods based on variational autoencoders and adversarial autoencoders, both previously used in counterfactual literature although not in time series settings. Then, we present the Conditional Entropy-Penalized Autoencoder (CEPAE), a novel autoencoder-based approach for counterfactual inference, which employs an entropy penalization loss over the latent space to encourage disentangled data representations. We validate our approach both theoretically and experimentally on synthetic, semi-synthetic, and real-world datasets, showing that CEPAE generally outperforms the other approaches in the evaluated metrics.

