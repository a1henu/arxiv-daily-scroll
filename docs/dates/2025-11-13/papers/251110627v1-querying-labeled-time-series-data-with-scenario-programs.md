---
layout: default
title: Querying Labeled Time Series Data with Scenario Programs
---

# Querying Labeled Time Series Data with Scenario Programs
**arXiv**：[2511.10627v1](https://arxiv.org/abs/2511.10627) · [PDF](https://arxiv.org/pdf/2511.10627.pdf)  
**作者**：Edward Kim, Devan Shanker, Varun Bharadwaj, Hongbeen Park, Jinkyu Kim, Hazem Torfah, Daniel J Fremont, Sanjit A Seshia  

**一句话要点**：提出基于场景程序的查询算法以验证仿真失败场景在真实数据中的可复现性

**关键词**：时间序列查询, 场景程序, 仿真验证, 自动驾驶安全, 传感器数据匹配

## 3 点简述
- 核心问题：仿真发现的自动驾驶失败场景是否能在真实系统中复现，存在仿真与现实差距。
- 方法要点：定义时间序列数据与抽象场景的匹配，使用Scenic语言开发高效查询算法。
- 实验或效果：算法比商业视觉大模型更准确、快数个数量级，可扩展处理长时间序列数据。

## 摘要（原文）

> Simulation-based testing has become a crucial complement to road testing for ensuring the safety of cyber physical systems (CPS). As a result, significant research efforts have been directed toward identifying failure scenarios within simulation environments. However, a critical question remains. Are the AV failure scenarios discovered in simulation reproducible on actual systems in the real world? The sim-to-real gap caused by differences between simulated and real sensor data means that failure scenarios identified in simulation might either be artifacts of synthetic sensor data or actual issues that also occur with real sensor data. To address this, an effective approach to validating simulated failure scenarios is to locate occurrences of these scenarios within real-world datasets and verify whether the failure persists on the datasets. To this end, we introduce a formal definition of how labeled time series sensor data can match an abstract scenario, represented as a scenario program using the Scenic probabilistic programming language. We present a querying algorithm that, given a scenario program and a labeled dataset, identifies the subset of data that matches the specified scenario. Our experiment shows that our algorithm is more accurate and orders of magnitude faster in querying scenarios than the state-of-the-art commercial vision large language models, and can scale with the duration of queried time series data.

