---
layout: default
title: PAtt: A Pattern Attention Network for ETA Prediction Using Historical Speed Profiles
---

# PAtt: A Pattern Attention Network for ETA Prediction Using Historical Speed Profiles
**arXiv**：[2601.13793v1](https://arxiv.org/abs/2601.13793) · [PDF](https://arxiv.org/pdf/2601.13793.pdf)  
**作者**：ByeoungDo Kim, JunYeop Na, Kyungwook Tak, JunTae Kim, DongHyeon Kim, Duckky Kim  

**一句话要点**：提出基于历史速度模式的注意力网络PAtt，用于高效准确的ETA预测。

**关键词**：ETA预测, 注意力机制, 时空模式, 历史速度模式, 轻量模型

## 3 点简述
- 核心问题：ETA预测因交通流动态复杂而具挑战性，现有方法计算成本高或未能有效捕获时空模式。
- 方法要点：利用注意力机制提取路线中每个时空点的累积特征，整合道路特性、实时和历史速度模式。
- 实验或效果：在真实驾驶数据集上验证，模型轻量可扩展，性能优于现有基线。

## 摘要（原文）

> In this paper, we propose an ETA model (Estimated Time of Arrival) that leverages an attention mechanism over historical road speed patterns. As autonomous driving and intelligent transportation systems become increasingly prevalent, the need for accurate and reliable ETA estimation has grown, playing a vital role in navigation, mobility planning, and traffic management. However, predicting ETA remains a challenging task due to the dynamic and complex nature of traffic flow. Traditional methods often combine real-time and historical traffic data in simplistic ways, or rely on complex rule-based computations. While recent deep learning models have shown potential, they often require high computational costs and do not effectively capture the spatio-temporal patterns crucial for ETA prediction. ETA prediction inherently involves spatio-temporal causality, and our proposed model addresses this by leveraging attention mechanisms to extract and utilize temporal features accumulated at each spatio-temporal point along a route. This architecture enables efficient and accurate ETA estimation while keeping the model lightweight and scalable. We validate our approach using real-world driving datasets and demonstrate that our approach outperforms existing baselines by effectively integrating road characteristics, real-time traffic conditions, and historical speed patterns in a task-aware manner.

