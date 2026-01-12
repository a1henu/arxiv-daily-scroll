---
layout: default
title: AWaRe-SAC: Proactive Slice Admission Control under Weather-Induced Capacity Uncertainty
---

# AWaRe-SAC: Proactive Slice Admission Control under Weather-Induced Capacity Uncertainty
**arXiv**：[2601.05978v1](https://arxiv.org/abs/2601.05978) · [PDF](https://arxiv.org/pdf/2601.05978.pdf)  
**作者**：Dror Jacoby, Yanzhi Li, Shuyue Yu, Nicola Di Cicco, Hagit Messer, Gil Zussman, Igor Kadota  

**一句话要点**：提出AWaRe-SAC框架，在毫米波x-haul网络中通过主动切片准入控制应对天气不确定性。

**关键词**：毫米波网络, 切片准入控制, 深度学习预测, Q学习, 天气不确定性, x-haul网络

## 3 点简述
- 核心问题：毫米波链路受降雨衰减影响，导致网络容量不确定，难以保证服务质量。
- 方法要点：结合深度学习预测未来网络条件和基于Q学习的主动切片准入控制机制。
- 实验或效果：使用真实数据验证，在动态链路条件下实现长期平均收入提升2-3倍。

## 摘要（原文）

> As emerging applications demand higher throughput and lower latencies, operators are increasingly deploying millimeter-wave (mmWave) links within x-haul transport networks, spanning fronthaul, midhaul, and backhaul segments. However, the inherent susceptibility of mmWave frequencies to weather-related attenuation, particularly rain fading, complicates the maintenance of stringent Quality of Service (QoS) requirements. This creates a critical challenge: making admission decisions under uncertainty regarding future network capacity. To address this, we develop a proactive slice admission control framework for mmWave x-haul networks subject to rain-induced fluctuations. Our objective is to improve network performance, ensure QoS, and optimize revenue, thereby surpassing the limitations of standard reactive approaches. The proposed framework integrates a deep learning predictor of future network conditions with a proactive Q-learning-based slice admission control mechanism. We validate our solution using real-world data from a mmWave x-haul deployment in a dense urban area, incorporating realistic models of link capacity attenuation and dynamic slice demands. Extensive evaluations demonstrate that our proactive solution achieves 2-3x higher long-term average revenue under dynamic link conditions, providing a scalable and resilient framework for adaptive admission control.

