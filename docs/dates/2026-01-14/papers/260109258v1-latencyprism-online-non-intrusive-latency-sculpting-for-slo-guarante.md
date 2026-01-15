---
layout: default
title: LatencyPrism: Online Non-intrusive Latency Sculpting for SLO-Guaranteed LLM Inference
---

# LatencyPrism: Online Non-intrusive Latency Sculpting for SLO-Guaranteed LLM Inference
**arXiv**：[2601.09258v1](https://arxiv.org/abs/2601.09258) · [PDF](https://arxiv.org/pdf/2601.09258.pdf)  
**作者**：Du Yin, Jiayi Ren, Xiayu Sun, Tianyao Zhou, Haizhu Zhou, Ruiyan Ma, Danyang Zhang  

**一句话要点**：提出LatencyPrism系统以解决分布式LLM推理中非侵入式实时延迟监控与SLO保障问题

**关键词**：LLM推理延迟, 非侵入式监控, SLO保障, 分布式系统, 异常检测, 实时分析

## 3 点简述
- 核心问题：分布式LLM推理环境动态复杂，现有侵入式方法难以实时分析延迟，影响SLO保障。
- 方法要点：设计零侵入多平台延迟雕刻系统，无需代码修改或服务重启，实现批级实时监控与异常预警。
- 实验或效果：部署数千XPU超半年，毫秒级预警，区分工作负载变化与异常，F1分数达0.98。

## 摘要（原文）

> LLM inference latency critically determines user experience and operational costs, directly impacting throughput under SLO constraints. Even brief latency spikes degrade service quality despite acceptable average performance. However, distributed inference environments featuring diverse software frameworks and XPU architectures combined with dynamic workloads make latency analysis challenging. Constrained by intrusive designs that necessitate service restarts or even suspension, and by hardware-bound implementations that fail to adapt to heterogeneous inference environments, existing AI profiling methods are often inadequate for real-time production analysis.
>   We present LatencyPrism, the first zero-intrusion multi-platform latency sculpting system. It aims to break down the inference latency across pipeline, proactively alert on inference latency anomalies, and guarantee adherence to SLOs, all without requiring code modifications or service restarts. LatencyPrism has been deployed across thousands of XPUs for over six months. It enables low-overhead real-time monitoring at batch level with alerts triggered in milliseconds. This approach distinguishes between workload-driven latency variations and anomalies indicating underlying issues with an F1-score of 0.98. We also conduct extensive experiments and investigations into root cause analysis to demonstrate LatencyPrism's capability.

