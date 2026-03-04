---
layout: default
title: Practical FP4 Training for Large-Scale MoE Models on Hopper GPUs
---

# Practical FP4 Training for Large-Scale MoE Models on Hopper GPUs
**arXiv**：[2603.02731v1](https://arxiv.org/abs/2603.02731) · [PDF](https://arxiv.org/pdf/2603.02731.pdf)  
**作者**：Wuyue Zhang, Chongdong Huang, Chunbo You, Cheng Gu, Fengjuan Wang, Mou Sun  

**一句话要点**：提出FP4训练方法以解决Hopper GPU上大规模MoE模型的内存与通信瓶颈

**关键词**：混合专家模型, 低精度训练, GPU优化, 内存压缩, 通信效率, 软件硬件协同设计

## 3 点简述
- 核心问题：Hopper GPU无原生FP4支持，MoE训练受限于激活内存和专家并行通信
- 方法要点：引入直接FP8到FP4量化与反量化，结合缩放感知的行列转换，实现高效FP4压缩
- 实验或效果：在671B参数规模下，减少激活内存14.8%，提升训练吞吐量12.5%，性能媲美FP8基线

## 摘要（原文）

> Training large-scale Mixture-of-Experts (MoE) models is bottlenecked by activation memory and expert-parallel communication, yet FP4 training remains impractical on Hopper-class GPUs without native MXFP4 or NVFP4 support. In this work, we present a training recipe that enables MXFP4 efficiency for MoE models on Hopper architectures without native 4-bit computation support. A central challenge is to integrate FP4 into an existing BF16/FP8 hybrid training pipeline without incurring costly precision round-trips (e.g., FP4 $\leftrightarrow$ BF16 $\leftrightarrow$ FP8). We address this challenge by introducing direct FP8-to-FP4 quantization and de-quantization, together with scaling-aware FP4 row-wise to column-wise conversion, enabling FP4 activations and expert-parallel communication with minimal overhead. Core MoE computations are executed in FP8, while activations and expert-parallel communication are compressed using MXFP4, achieving substantial memory and bandwidth savings without degrading convergence. At the 671B parameter scale, our method achieves end-to-end training performance comparable to strong FP8 baselines, while reducing peak activation memory by 14.8\% (11.8 GB) and improving training throughput by 12.5\%, from 1157 to 1302 tokens per GPU per second. These results show that FP4 efficiency can be practically realized for large-scale MoE training through careful software-hardware co-design, even without native FP4 Tensor Core support.

