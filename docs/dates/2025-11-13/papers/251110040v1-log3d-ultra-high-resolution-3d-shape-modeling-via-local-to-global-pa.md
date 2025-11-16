---
layout: default
title: LoG3D: Ultra-High-Resolution 3D Shape Modeling via Local-to-Global Partitioning
---

# LoG3D: Ultra-High-Resolution 3D Shape Modeling via Local-to-Global Partitioning
**arXiv**：[2511.10040v1](https://arxiv.org/abs/2511.10040) · [PDF](https://arxiv.org/pdf/2511.10040.pdf)  
**作者**：Xinran Yang, Shuichang Lai, Jiangjing Lyu, Hongjie Li, Bowen Pan, Yuanqi Li, Jie Guo, Zhou Zhengkang, Yanwen Guo  

**一句话要点**：提出LoG3D框架以解决高保真3D建模中复杂拓扑和细节保留的挑战

**关键词**：3D形状建模, 无符号距离场, 局部到全局架构, 超高分辨率, 变分自编码器, 几何细节保留

## 3 点简述
- 核心问题：现有方法难以处理非流形几何和开放表面，导致细节丢失和预处理成本高
- 方法要点：基于无符号距离场，采用局部到全局架构结合3D卷积和稀疏变换器
- 实验或效果：在重建精度和生成质量上达到先进水平，支持高达2048^3的超高分辨率

## 摘要（原文）

> Generating high-fidelity 3D contents remains a fundamental challenge due to the complexity of representing arbitrary topologies-such as open surfaces and intricate internal structures-while preserving geometric details. Prevailing methods based on signed distance fields (SDFs) are hampered by costly watertight preprocessing and struggle with non-manifold geometries, while point-cloud representations often suffer from sampling artifacts and surface discontinuities. To overcome these limitations, we propose a novel 3D variational autoencoder (VAE) framework built upon unsigned distance fields (UDFs)-a more robust and computationally efficient representation that naturally handles complex and incomplete shapes. Our core innovation is a local-to-global (LoG) architecture that processes the UDF by partitioning it into uniform subvolumes, termed UBlocks. This architecture couples 3D convolutions for capturing local detail with sparse transformers for enforcing global coherence. A Pad-Average strategy further ensures smooth transitions at subvolume boundaries during reconstruction. This modular design enables seamless scaling to ultra-high resolutions up to 2048^3-a regime previously unattainable for 3D VAEs. Experiments demonstrate state-of-the-art performance in both reconstruction accuracy and generative quality, yielding superior surface smoothness and geometric flexibility.

