---
layout: default
title: Low-latency Event-based Object Detection with Spatially-Sparse Linear Attention
---

# Low-latency Event-based Object Detection with Spatially-Sparse Linear Attention
**arXiv**：[2603.06228v1](https://arxiv.org/abs/2603.06228) · [PDF](https://arxiv.org/pdf/2603.06228.pdf)  
**作者**：Haiqing Hao, Zhipeng Sui, Rong Zou, Zijia Dai, Nikola Zubić, Davide Scaramuzza, Wenhui Wang  

**一句话要点**：提出空间稀疏线性注意力以解决事件相机低延迟目标检测中的效率与精度权衡问题

**关键词**：事件相机, 低延迟目标检测, 线性注意力, 空间稀疏性, 异步神经网络, 并行训练

## 3 点简述
- 核心问题：现有异步事件网络在长序列训练和精度提升时面临计算效率与延迟瓶颈
- 方法要点：引入空间稀疏状态激活，通过混合空间分解和分散-计算-聚集训练实现状态级稀疏与并行训练
- 实验或效果：在Gen1和N-Caltech101数据集上达到异步方法最优精度，每事件计算量减少20倍以上

## 摘要（原文）

> Event cameras provide sequential visual data with spatial sparsity and high temporal resolution, making them attractive for low-latency object detection. Existing asynchronous event-based neural networks realize this low-latency advantage by updating predictions event-by-event, but still suffer from two bottlenecks: recurrent architectures are difficult to train efficiently on long sequences, and improving accuracy often increases per-event computation and latency. Linear attention is appealing in this setting because it supports parallel training and recurrent inference. However, standard linear attention updates a global state for every event, yielding a poor accuracy-efficiency trade-off, which is problematic for object detection, where fine-grained representations and thus states are preferred. The key challenge is therefore to introduce sparse state activation that exploits event sparsity while preserving efficient parallel training. We propose Spatially-Sparse Linear Attention (SSLA), which introduces a mixture-of-spaces state decomposition and a scatter-compute-gather training procedure, enabling state-level sparsity as well as training parallelism. Built on SSLA, we develop an end-to-end asynchronous linear attention model, SSLA-Det, for event-based object detection. On Gen1 and N-Caltech101, SSLA-Det achieves state-of-the-art accuracy among asynchronous methods, reaching 0.375 mAP and 0.515 mAP, respectively, while reducing per-event computation by more than 20 times compared to the strongest prior asynchronous baseline, demonstrating the potential of linear attention for low-latency event-based vision.

