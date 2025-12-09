---
layout: default
title: Enabling Delayed-Full Charging Through Transformer-Based Real-Time-to-Departure Modeling for EV Battery Longevity
---

# Enabling Delayed-Full Charging Through Transformer-Based Real-Time-to-Departure Modeling for EV Battery Longevity
**arXiv**：[2512.07723v1](https://arxiv.org/abs/2512.07723) · [PDF](https://arxiv.org/pdf/2512.07723.pdf)  
**作者**：Yonggeon Lee, Jibin Hwang, Alfred Malengo Kondoro, Juhyun Song, Youngtae Noh  

**一句话要点**：提出基于Transformer的实时到事件模型，以准确预测电动汽车出发时间，延长电池寿命。

**关键词**：电动汽车电池管理, 出发时间预测, Transformer模型, 实时到事件建模, 可持续交通

## 3 点简述
- 核心问题：电动汽车锂离子电池在长时间高荷电状态下易退化，需延迟充满电至出发前。
- 方法要点：将每天离散化为基于网格的令牌序列，利用流式上下文信息预测出发时间，而非仅依赖历史模式。
- 实验或效果：在93名用户的真实世界智能手机数据上评估，模型能有效捕捉个体日常中的不规则出发模式，优于基线。

## 摘要（原文）

> Electric vehicles (EVs) are key to sustainable mobility, yet their lithium-ion batteries (LIBs) degrade more rapidly under prolonged high states of charge (SOC). This can be mitigated by delaying full charging \ours until just before departure, which requires accurate prediction of user departure times. In this work, we propose Transformer-based real-time-to-event (TTE) model for accurate EV departure prediction. Our approach represents each day as a TTE sequence by discretizing time into grid-based tokens. Unlike previous methods primarily dependent on temporal dependency from historical patterns, our method leverages streaming contextual information to predict departures. Evaluation on a real-world study involving 93 users and passive smartphone data demonstrates that our method effectively captures irregular departure patterns within individual routines, outperforming baseline models. These results highlight the potential for practical deployment of the \ours algorithm and its contribution to sustainable transportation systems.

