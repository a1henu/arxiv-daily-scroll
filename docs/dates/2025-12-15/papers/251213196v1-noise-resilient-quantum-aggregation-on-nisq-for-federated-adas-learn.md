---
layout: default
title: Noise-Resilient Quantum Aggregation on NISQ for Federated ADAS Learning
---

# Noise-Resilient Quantum Aggregation on NISQ for Federated ADAS Learning
**arXiv**：[2512.13196v1](https://arxiv.org/abs/2512.13196) · [PDF](https://arxiv.org/pdf/2512.13196.pdf)  
**作者**：Chethana Prasad Kabgere, Sudarshan T S B  

**一句话要点**：提出噪声弹性量子联邦学习框架以解决车载ADAS中联邦学习的噪声、延迟和安全问题。

**关键词**：量子联邦学习, 噪声弹性聚合, 变分量子电路, 车载边缘计算, 模型参数编码, 多服务器协调

## 3 点简述
- 核心问题：传统联邦学习在实时车载网络中易受噪声、延迟和安全约束影响。
- 方法要点：采用变分量子电路在NISQ条件下编码模型参数，实现有界误差收敛和噪声弹性。
- 实验或效果：经验验证显示收敛稳定，梯度方差降低，通信开销减少，噪声容忍度增强。

## 摘要（原文）

> Advanced Driver Assistance Systems (ADAS) increasingly employ Federated Learning (FL) to collaboratively train models across distributed vehicular nodes while preserving data privacy. Yet, conventional FL aggregation remains susceptible to noise, latency, and security constraints inherent to real-time vehicular networks. This paper introduces Noise-Resilient Quantum Federated Learning (NR-QFL), a hybrid quantum-classical framework that enables secure, low-latency aggregation through variational quantum circuits (VQCs) operating under Noisy Intermediate-Scale Quantum (NISQ) conditions. The framework encodes model parameters as quantum states with adaptive gate reparameterization, ensuring bounded-error convergence and provable resilience under Completely Positive Trace-Preserving (CPTP) dynamics. NR-QFL employs quantum entropy-based client selection and multi-server coordination for fairness and stability. Empirical validation shows consistent convergence with reduced gradient variance, lower communication overhead, and enhanced noise tolerance under constrained edge conditions. The framework establishes a scalable foundation for quantum-enhanced federated learning, enabling secure, efficient, and dynamically stable ADAS intelligence at the vehicular edge.

