---
layout: default
title: ZipMoE: Efficient On-Device MoE Serving via Lossless Compression and Cache-Affinity Scheduling
---

# ZipMoE: Efficient On-Device MoE Serving via Lossless Compression and Cache-Affinity Scheduling
**arXiv**：[2601.21198v1](https://arxiv.org/abs/2601.21198) · [PDF](https://arxiv.org/pdf/2601.21198.pdf)  
**作者**：Yuchen Yang, Yaru Zhao, Pu Yang, Shaowei Wang, Zhi-Hua Zhou  

**一句话要点**：提出ZipMoE系统，通过无损压缩和缓存亲和调度实现高效边缘设备MoE服务。

**关键词**：边缘计算, MoE架构, 无损压缩, 缓存调度, 推理优化, 系统设计

## 3 点简述
- MoE架构在边缘设备部署时面临内存占用过高问题，需无损保持模型行为。
- ZipMoE结合硬件特性和参数冗余，采用缓存调度协同设计，将推理从I/O瓶颈转向计算中心。
- 实验显示，ZipMoE在边缘平台上显著降低延迟并提升吞吐量，优于现有系统。

## 摘要（原文）

> While Mixture-of-Experts (MoE) architectures substantially bolster the expressive power of large-language models, their prohibitive memory footprint severely impedes the practical deployment on resource-constrained edge devices, especially when model behavior must be preserved without relying on lossy quantization. In this paper, we present ZipMoE, an efficient and semantically lossless on-device MoE serving system. ZipMoE exploits the synergy between the hardware properties of edge devices and the statistical redundancy inherent to MoE parameters via a caching-scheduling co-design with provable performance guarantee. Fundamentally, our design shifts the paradigm of on-device MoE inference from an I/O-bound bottleneck to a compute-centric workflow that enables efficient parallelization. We implement a prototype of ZipMoE and conduct extensive experiments on representative edge computing platforms using popular open-source MoE models and real-world workloads. Our evaluation reveals that ZipMoE achieves up to $72.77\%$ inference latency reduction and up to $6.76\times$ higher throughput than the state-of-the-art systems.

