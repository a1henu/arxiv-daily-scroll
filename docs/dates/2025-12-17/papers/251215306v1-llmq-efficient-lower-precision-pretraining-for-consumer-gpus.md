---
layout: default
title: LLMQ: Efficient Lower-Precision Pretraining for Consumer GPUs
---

# LLMQ: Efficient Lower-Precision Pretraining for Consumer GPUs
**arXiv**：[2512.15306v1](https://arxiv.org/abs/2512.15306) · [PDF](https://arxiv.org/pdf/2512.15306.pdf)  
**作者**：Erik Schultheis, Dan Alistarh  

**一句话要点**：提出LLMQ以在消费级GPU上高效训练中等规模语言模型

**关键词**：低精度训练, 消费级GPU, 语言模型训练, CUDA优化, 内存管理

## 3 点简述
- 针对消费级GPU内存有限和通信慢的问题
- 采用激活检查点、卸载和基于复制引擎的集合通信等优化
- 在单张16GB显卡上训练7B模型，4张RTX 4090上训练32B模型，保持约50% FLOP利用率

## 摘要（原文）

> We present LLMQ, an end-to-end CUDA/C++ implementation for medium-sized language-model training, e.g. 3B to 32B parameters, on affordable, commodity GPUs. These devices are characterized by low memory availability and slow communication compared to datacentre-grade GPUs. Consequently, we showcase a range of optimizations that target these bottlenecks, including activation checkpointing, offloading, and copy-engine based collectives. LLMQ is able to train or fine-tune a 7B model on a single 16GB mid-range gaming card, or a 32B model on a workstation equipped with 4 RTX 4090s. This is achieved while executing a standard 8-bit training pipeline, without additional algorithmic approximations, and maintaining FLOP utilization of around 50%. The efficiency of LLMQ rivals that of production-scale systems on much more expensive cloud-grade GPUs.

