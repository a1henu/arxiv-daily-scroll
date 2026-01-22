---
layout: default
title: Place with Intention: An Empirical Attendance Predictive Study of Expo 2025 Osaka, Kansai, Japan
---

# Place with Intention: An Empirical Attendance Predictive Study of Expo 2025 Osaka, Kansai, Japan
**arXiv**：[2601.14570v1](https://arxiv.org/abs/2601.14570) · [PDF](https://arxiv.org/pdf/2601.14570.pdf)  
**作者**：Xiaojie Yang, Dizhi Huang, Hangli Ge, Masahiro Sano, Takeaki Ohdake, Kazuma Hatano, Noboru Koshizuka  

**一句话要点**：提出基于Transformer的框架，利用预约动态预测2025大阪世博会日参观人数，以解决历史数据不足时多源数据不可靠的问题。

**关键词**：参观人数预测, Transformer框架, 预约动态, 世博会管理, 多通道建模

## 3 点简述
- 核心问题：大规模国际活动如世博会的日参观人数预测，传统方法依赖多源外部数据，在历史数据不足时准确性受限。
- 方法要点：设计Transformer框架，以预约动态（如票务预订和更新）作为参观意图的代理，避免多源数据整合的复杂性。
- 实验或效果：在单通道和双通道（东、西门分开）设置下评估，分开建模东、西门能提升准确性，尤其在短中期预测中效果显著。

## 摘要（原文）

> Accurate forecasting of daily attendance is vital for managing transportation, crowd flows, and services at large-scale international events such as Expo 2025 Osaka, Kansai, Japan. However, existing approaches often rely on multi-source external data (such as weather, traffic, and social media) to improve accuracy, which can lead to unreliable results when historical data are insufficient. To address these challenges, we propose a Transformer-based framework that leverages reservation dynamics, i.e., ticket bookings and subsequent updates within a time window, as a proxy for visitors' attendance intentions, under the assumption that such intentions are eventually reflected in reservation patterns. This design avoids the complexity of multi-source integration while still capturing external influences like weather and promotions implicitly embedded in reservation dynamics. We construct a dataset combining entrance records and reservation dynamics and evaluate the model under both single-channel (total attendance) and two-channel (separated by East and West gates) settings. Results show that separately modeling East and West gates consistently improves accuracy, particularly for short- and medium-term horizons. Ablation studies further confirm the importance of the encoder-decoder structure, inverse-style embedding, and adaptive fusion module. Overall, our findings indicate that reservation dynamics offer a practical and informative foundation for attendance forecasting in large-scale international events.

