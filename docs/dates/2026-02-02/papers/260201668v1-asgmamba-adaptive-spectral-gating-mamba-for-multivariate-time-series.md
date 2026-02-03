---
layout: default
title: ASGMamba: Adaptive Spectral Gating Mamba for Multivariate Time Series Forecasting
---

# ASGMamba: Adaptive Spectral Gating Mamba for Multivariate Time Series Forecasting
**arXiv**：[2602.01668v1](https://arxiv.org/abs/2602.01668) · [PDF](https://arxiv.org/pdf/2602.01668.pdf)  
**作者**：Qianyang Li, Xingjun Zhang, Shaoxun Wang, Jia Wei, Yueqi Xing  

**一句话要点**：提出ASGMamba框架，通过自适应谱门控机制解决长序列多元时间序列预测中的噪声干扰与计算效率问题。

**关键词**：多元时间序列预测, 自适应谱门控, 状态空间模型, 长序列预测, 计算效率优化, 资源受限环境

## 3 点简述
- 核心问题：Transformer模型复杂度高，线性状态空间模型易受高频噪声影响，导致状态容量浪费。
- 方法要点：集成自适应谱门控机制动态过滤噪声，结合多尺度架构和节点嵌入捕获物理特性。
- 实验或效果：在九个基准测试中达到最先进精度，保持线性复杂度并显著降低内存使用。

## 摘要（原文）

> Long-term multivariate time series forecasting (LTSF) plays a crucial role in various high-performance computing applications, including real-time energy grid management and large-scale traffic flow simulation. However, existing solutions face a dilemma: Transformer-based models suffer from quadratic complexity, limiting their scalability on long sequences, while linear State Space Models (SSMs) often struggle to distinguish valuable signals from high-frequency noise, leading to wasted state capacity. To bridge this gap, we propose ASGMamba, an efficient forecasting framework designed for resource-constrained supercomputing environments. ASGMamba integrates a lightweight Adaptive Spectral Gating (ASG) mechanism that dynamically filters noise based on local spectral energy, enabling the Mamba backbone to focus its state evolution on robust temporal dynamics. Furthermore, we introduce a hierarchical multi-scale architecture with variable-specific Node Embeddings to capture diverse physical characteristics. Extensive experiments on nine benchmarks demonstrate that ASGMamba achieves state-of-the-art accuracy. While keeping strictly $$\mathcal{O}(L)$$ complexity we significantly reduce the memory usage on long-horizon tasks, thus establishing ASGMamba as a scalable solution for high-throughput forecasting in resource limited environments.The code is available at https://github.com/hit636/ASGMamba

