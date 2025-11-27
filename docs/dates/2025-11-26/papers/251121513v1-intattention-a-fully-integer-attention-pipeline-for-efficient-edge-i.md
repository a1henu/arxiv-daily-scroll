---
layout: default
title: IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference
---

# IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference
**arXiv**：[2511.21513v1](https://arxiv.org/abs/2511.21513) · [PDF](https://arxiv.org/pdf/2511.21513.pdf)  
**作者**：Wanli Zhong, Haibo Feng, Zirui Zhou, Hanyang Peng, Shiqi Yu  

**一句话要点**：提出IntAttention全整数注意力管道，解决边缘设备Transformer推理中softmax瓶颈问题

**关键词**：整数注意力, 边缘推理, Transformer优化, 软最大量化, 硬件加速

## 3 点简述
- 核心问题：INT8量化中softmax阶段需浮点计算，导致延迟和能耗瓶颈，占注意力延迟高达65%
- 方法要点：使用IndexSoftmax硬件友好算子，结合查找表近似和整数归一化，实现全整数处理
- 实验或效果：在Armv8 CPU上，相比FP16基线提速3.7倍、能耗降61%，精度与基线相当

## 摘要（原文）

> Deploying Transformer models on edge devices is limited by latency and energy budgets. While INT8 quantization effectively accelerates the primary matrix multiplications, it exposes the softmax as the dominant bottleneck. This stage incurs a costly dequantize-softmax-requantize detour, which can account for up to 65% of total attention latency and disrupts the end-to-end integer dataflow critical for edge hardware efficiency. To address this limitation, we present IntAttention, the first fully integer, plug-and-play attention pipeline without retraining. At the core of our approach lies IndexSoftmax, a hardware-friendly operator that replaces floating-point exponentials entirely within the integer domain. IntAttention integrates sparsity-aware clipping, a 32-entry lookup-table approximation, and direct integer normalization, thereby eliminating all datatype conversion overhead. We evaluate IntAttention and demonstrate consistent and substantial gains. Our method achieves up to 3.7x speedup and 61% energy reduction over FP16 baselines and 2.0x faster than conventional INT8 attention pipelines on Armv8 CPUs. These gains are achieved with high-fidelity accuracy comparable to baselines across diverse language and vision models, enabling practical and efficient Transformer inference on commodity edge devices. Code will be released in later version of this work.

