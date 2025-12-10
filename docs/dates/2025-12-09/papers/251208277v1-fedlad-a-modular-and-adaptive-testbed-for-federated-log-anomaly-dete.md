---
layout: default
title: FedLAD: A Modular and Adaptive Testbed for Federated Log Anomaly Detection
---

# FedLAD: A Modular and Adaptive Testbed for Federated Log Anomaly Detection
**arXiv**：[2512.08277v1](https://arxiv.org/abs/2512.08277) · [PDF](https://arxiv.org/pdf/2512.08277.pdf)  
**作者**：Yihan Liao, Jacky Keung, Zhenyu Mao, Jingyu Zhang, Jialong Li  

**一句话要点**：提出FedLAD测试平台，以解决联邦学习中日志异常检测缺乏专用工具的问题。

**关键词**：联邦学习, 日志异常检测, 测试平台, 模块化设计, 自适应控制

## 3 点简述
- 核心问题：现有日志异常检测方法依赖集中训练，不适用于隐私约束和日志分散的场景。
- 方法要点：FedLAD支持模块化集成多种模型、数据集和聚合策略，并提供自监控、自配置和自适应控制功能。
- 实验或效果：平台促进可复现和可扩展的实验，为未来研究奠定基础，代码已开源。

## 摘要（原文）

> Log-based anomaly detection (LAD) is critical for ensuring the reliability of large-scale distributed systems. However, most existing LAD approaches assume centralized training, which is often impractical due to privacy constraints and the decentralized nature of system logs. While federated learning (FL) offers a promising alternative, there is a lack of dedicated testbeds tailored to the needs of LAD in federated settings. To address this, we present FedLAD, a unified platform for training and evaluating LAD models under FL constraints. FedLAD supports plug-and-play integration of diverse LAD models, benchmark datasets, and aggregation strategies, while offering runtime support for validation logging (self-monitoring), parameter tuning (self-configuration), and adaptive strategy control (self-adaptation). By enabling reproducible and scalable experimentation, FedLAD bridges the gap between FL frameworks and LAD requirements, providing a solid foundation for future research. Project code is publicly available at: https://github.com/AA-cityu/FedLAD.

