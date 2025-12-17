---
layout: default
title: A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks
---

# A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks
**arXiv**：[2512.14297v1](https://arxiv.org/abs/2512.14297) · [PDF](https://arxiv.org/pdf/2512.14297.pdf)  
**作者**：Agrippina Mwangi, León Navarro-Hilfiker, Lukasz Brewka, Mikkel Gryning, Elena Fumagalli, Madeleine Gibescu  

**一句话要点**：提出基于阈值触发深度Q网络的自主修复框架，以提升软件定义工业物联网边缘网络的韧性。

**关键词**：软件定义网络, 深度强化学习, 自主修复, 工业物联网, 边缘计算, 网络韧性

## 3 点简述
- 核心问题：随机中断（如流量突发和交换机热波动）导致服务降级，违反工业标准要求。
- 方法要点：使用深度强化学习代理实时检测、分析和缓解网络中断，自适应调整路由和资源分配。
- 实验或效果：在仿真测试中，恢复性能提升53.84%，优于现有方法，并保持交换机热稳定性。

## 摘要（原文）

> Stochastic disruptions such as flash events arising from benign traffic bursts and switch thermal fluctuations are major contributors to intermittent service degradation in software-defined industrial networks. These events violate IEC~61850-derived quality-of-service requirements and user-defined service-level agreements, hindering the reliable and timely delivery of control, monitoring, and best-effort traffic in IEC~61400-25-compliant wind power plants. Failure to maintain these requirements often results in delayed or lost control signals, reduced operational efficiency, and increased risk of wind turbine generator downtime.
>   To address these challenges, this study proposes a threshold-triggered Deep Q-Network self-healing agent that autonomically detects, analyzes, and mitigates network disruptions while adapting routing behavior and resource allocation in real time. The proposed agent was trained, validated, and tested on an emulated tri-clustered switch network deployed in a cloud-based proof-of-concept testbed.
>   Simulation results show that the proposed agent improves disruption recovery performance by 53.84% compared to a baseline shortest-path and load-balanced routing approach and outperforms state-of-the-art methods, including the Adaptive Network-based Fuzzy Inference System by 13.1% and the Deep Q-Network and traffic prediction-based routing optimization method by 21.5%, in a super-spine leaf data-plane architecture.
>   Additionally, the agent maintains switch thermal stability by proactively initiating external rack cooling when required. These findings highlight the potential of deep reinforcement learning in building resilience in software-defined industrial networks deployed in mission-critical, time-sensitive application scenarios.

