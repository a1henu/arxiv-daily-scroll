---
layout: default
title: LADY: Linear Attention for Autonomous Driving Efficiency without Transformers
---

# LADY: Linear Attention for Autonomous Driving Efficiency without Transformers
**arXiv**：[2512.15038v1](https://arxiv.org/abs/2512.15038) · [PDF](https://arxiv.org/pdf/2512.15038.pdf)  
**作者**：Jihao Huang, Xi Xia, Zhiyuan Li, Tianle Liu, Jingke Wang, Junbo Chen, Tengju Ye  

**一句话要点**：提出LADY线性注意力模型以解决自动驾驶中Transformer计算效率低的问题

**关键词**：自动驾驶, 线性注意力, 端到端学习, 计算效率, 跨模态融合, 边缘部署

## 3 点简述
- 核心问题：Transformer在自动驾驶中因二次注意力成本限制长时空序列建模，影响边缘部署。
- 方法要点：LADY采用全线性注意力，支持恒定计算成本的长期上下文融合和跨模态交互。
- 实验或效果：在NAVSIM和Bench2Drive基准上实现SOTA性能，计算成本显著降低，边缘设备验证可行。

## 摘要（原文）

> End-to-end paradigms have demonstrated great potential for autonomous driving. Additionally, most existing methods are built upon Transformer architectures. However, transformers incur a quadratic attention cost, limiting their ability to model long spatial and temporal sequences-particularly on resource-constrained edge platforms. As autonomous driving inherently demands efficient temporal modeling, this challenge severely limits their deployment and real-time performance. Recently, linear attention mechanisms have gained increasing attention due to their superior spatiotemporal complexity. However, existing linear attention architectures are limited to self-attention, lacking support for cross-modal and cross-temporal interactions-both crucial for autonomous driving. In this work, we propose LADY, the first fully linear attention-based generative model for end-to-end autonomous driving. LADY enables fusion of long-range temporal context at inference with constant computational and memory costs, regardless of the history length of camera and LiDAR features. Additionally, we introduce a lightweight linear cross-attention mechanism that enables effective cross-modal information exchange. Experiments on the NAVSIM and Bench2Drive benchmarks demonstrate that LADY achieves state-of-the-art performance with constant-time and memory complexity, offering improved planning performance and significantly reduced computational cost. Additionally, the model has been deployed and validated on edge devices, demonstrating its practicality in resource-limited scenarios.

