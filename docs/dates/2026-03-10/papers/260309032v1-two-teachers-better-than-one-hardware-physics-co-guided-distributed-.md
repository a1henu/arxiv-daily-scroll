---
layout: default
title: Two Teachers Better Than One: Hardware-Physics Co-Guided Distributed Scientific Machine Learning
---

# Two Teachers Better Than One: Hardware-Physics Co-Guided Distributed Scientific Machine Learning
**arXiv**：[2603.09032v1](https://arxiv.org/abs/2603.09032) · [PDF](https://arxiv.org/pdf/2603.09032.pdf)  
**作者**：Yuchen Yuan, Junhuan Yang, Hao Wan, Yipei Liu, Hanhan Wu, Youzuo Lin, Lei Yang  

**一句话要点**：提出硬件与物理协同引导的分布式科学机器学习框架EPIC，以解决广域传感中通信延迟与能耗高的问题。

**关键词**：分布式科学机器学习, 硬件物理协同引导, 全波形反演, 通信优化, 跨注意力机制, 轻量级编码

## 3 点简述
- 核心问题：集中式科学机器学习在广域传感中因高通信延迟和能耗不实用，且分布式模型易破坏物理原理导致性能下降。
- 方法要点：EPIC在终端设备进行轻量级本地编码，在中心节点进行物理感知解码，通过传输紧凑潜在特征和跨注意力机制捕获波场耦合。
- 实验或效果：在分布式测试床和OpenFWI数据集上评估，EPIC降低延迟8.9倍、通信能耗33.8倍，并在多数数据集上提升重建保真度。

## 摘要（原文）

> Scientific machine learning (SciML) is increasingly applied to in-field processing, controlling, and monitoring; however, wide-area sensing, real-time demands, and strict energy and reliability constraints make centralized SciML implementation impractical. Most SciML models assume raw data aggregation at a central node, incurring prohibitively high communication latency and energy costs; yet, distributing models developed for general-purpose ML often breaks essential physical principles, resulting in degraded performance. To address these challenges, we introduce EPIC, a hardware- and physics-co-guided distributed SciML framework, using full-waveform inversion (FWI) as a representative task. EPIC performs lightweight local encoding on end devices and physics-aware decoding at a central node. By transmitting compact latent features rather than high-volume raw data and by using cross-attention to capture inter-receiver wavefield coupling, EPIC significantly reduces communication cost while preserving physical fidelity. Evaluated on a distributed testbed with five end devices and one central node, and across 10 datasets from OpenFWI, EPIC reduces latency by 8.9$\times$ and communication energy by 33.8$\times$, while even improving reconstruction fidelity on 8 out of 10 datasets.

