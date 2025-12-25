---
layout: default
title: ElfCore: A 28nm Neural Processor Enabling Dynamic Structured Sparse Training and Online Self-Supervised Learning with Activity-Dependent Weight Update
---

# ElfCore: A 28nm Neural Processor Enabling Dynamic Structured Sparse Training and Online Self-Supervised Learning with Activity-Dependent Weight Update
**arXiv**：[2512.21153v1](https://arxiv.org/abs/2512.21153) · [PDF](https://arxiv.org/pdf/2512.21153.pdf)  
**作者**：Zhe Su, Giacomo Indiveri  

**一句话要点**：提出ElfCore处理器，集成动态结构化稀疏训练与在线自监督学习，用于事件驱动传感信号处理。

**关键词**：事件驱动传感信号处理, 动态结构化稀疏训练, 在线自监督学习, 活动依赖权重更新, 低功耗神经网络处理器

## 3 点简述
- 核心问题：事件驱动传感信号处理需高效、低功耗的神经网络处理器。
- 方法要点：集成在线自监督学习、动态结构化稀疏训练和活动依赖权重更新机制。
- 实验或效果：在姿态识别等任务中，功耗降低16倍，内存需求减少3.8倍，网络容量效率提升5.9倍。

## 摘要（原文）

> In this paper, we present ElfCore, a 28nm digital spiking neural network processor tailored for event-driven sensory signal processing. ElfCore is the first to efficiently integrate: (1) a local online self-supervised learning engine that enables multi-layer temporal learning without labeled inputs; (2) a dynamic structured sparse training engine that supports high-accuracy sparse-to-sparse learning; and (3) an activity-dependent sparse weight update mechanism that selectively updates weights based solely on input activity and network dynamics. Demonstrated on tasks including gesture recognition, speech, and biomedical signal processing, ElfCore outperforms state-of-the-art solutions with up to 16X lower power consumption, 3.8X reduced on-chip memory requirements, and 5.9X greater network capacity efficiency.

