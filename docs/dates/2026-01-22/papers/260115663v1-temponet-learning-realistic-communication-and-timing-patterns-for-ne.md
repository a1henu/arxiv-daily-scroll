---
layout: default
title: TempoNet: Learning Realistic Communication and Timing Patterns for Network Traffic Simulation
---

# TempoNet: Learning Realistic Communication and Timing Patterns for Network Traffic Simulation
**arXiv**：[2601.15663v1](https://arxiv.org/abs/2601.15663) · [PDF](https://arxiv.org/pdf/2601.15663.pdf)  
**作者**：Kristen Moore, Diksha Goel, Cody James Christopher, Zhen Wang, Minjune Kim, Ahmed Ibrahim, Ahmad Mohsin, Seyit Camtepe  

**一句话要点**：提出TempoNet以解决网络流量模拟中真实良性背景流量生成的挑战

**关键词**：网络流量模拟, 生成模型, 时间点过程, 入侵检测, 多任务学习

## 3 点简述
- 核心问题：真实网络流量模拟中，良性背景流量的复杂时序和通信动态难以生成
- 方法要点：结合多任务学习和多标记时间点过程，联合建模到达时间和包头字段
- 实验或效果：在真实数据集上验证，生成流量用于入侵检测模型训练效果接近真实数据

## 摘要（原文）

> Realistic network traffic simulation is critical for evaluating intrusion detection systems, stress-testing network protocols, and constructing high-fidelity environments for cybersecurity training. While attack traffic can often be layered into training environments using red-teaming or replay methods, generating authentic benign background traffic remains a core challenge -- particularly in simulating the complex temporal and communication dynamics of real-world networks. This paper introduces TempoNet, a novel generative model that combines multi-task learning with multi-mark temporal point processes to jointly model inter-arrival times and all packet- and flow-header fields. TempoNet captures fine-grained timing patterns and higher-order correlations such as host-pair behavior and seasonal trends, addressing key limitations of GAN-, LLM-, and Bayesian-based methods that fail to reproduce structured temporal variation. TempoNet produces temporally consistent, high-fidelity traces, validated on real-world datasets. Furthermore, we show that intrusion detection models trained on TempoNet-generated background traffic perform comparably to those trained on real data, validating its utility for real-world security applications.

