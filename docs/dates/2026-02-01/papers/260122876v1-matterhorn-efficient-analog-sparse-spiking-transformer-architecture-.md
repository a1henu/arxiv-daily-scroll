---
layout: default
title: Matterhorn: Efficient Analog Sparse Spiking Transformer Architecture with Masked Time-To-First-Spike Encoding
---

# Matterhorn: Efficient Analog Sparse Spiking Transformer Architecture with Masked Time-To-First-Spike Encoding
**arXiv**：[2601.22876v1](https://arxiv.org/abs/2601.22876) · [PDF](https://arxiv.org/pdf/2601.22876.pdf)  
**作者**：Zhanglu Yan, Kaiwen Tang, Zixuan Zhu, Zhenyu Bai, Qianhui Liu, Weng-Fai Wong  

**一句话要点**：提出Matterhorn尖峰变压器，集成M-TTFS编码和MSU单元以提升能效

**关键词**：尖峰神经网络, 能效优化, 计算内存, 变压器架构, 模拟计算

## 3 点简述
- 当前SNN能效评估忽略数据移动等硬件成本，导致实际能耗高
- 采用M-TTFS编码减少尖峰移动，MSU单元消除权重访问开销
- 在GLUE基准上实现最高精度，能效提升2.31倍

## 摘要（原文）

> Spiking neural networks (SNNs) have emerged as a promising candidate for energy-efficient LLM inference. However, current energy evaluations for SNNs primarily focus on counting accumulate operations, and fail to account for real-world hardware costs such as data movement, which can consume nearly 80% of the total energy. In this paper, we propose Matterhorn, a spiking transformer that integrates a novel masked time-to-first-spike (M-TTFS) encoding method to reduce spike movement and a memristive synapse unit (MSU) to eliminate weight access overhead. M-TTFS employs a masking strategy that reassigns the zero-energy silent state (a spike train of all 0s) to the most frequent membrane potential rather than the lowest. This aligns the coding scheme with the data distribution, minimizing spike movement energy without information loss. We further propose a `dead zone' strategy that maximizes sparsity by mapping all values within a given range to the silent state. At the hardware level, the MSU utilizes compute-in-memory (CIM) technology to perform analog integration directly within memory, effectively removing weight access costs. On the GLUE benchmark, Matterhorn establishes a new state-of-the-art, surpassing existing SNNs by 1.42% in average accuracy while delivering a 2.31 times improvement in energy efficiency.

