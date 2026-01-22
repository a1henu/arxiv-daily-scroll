---
layout: default
title: Fast-ULCNet: A fast and ultra low complexity network for single-channel speech enhancement
---

# Fast-ULCNet: A fast and ultra low complexity network for single-channel speech enhancement
**arXiv**：[2601.14925v1](https://arxiv.org/abs/2601.14925) · [PDF](https://arxiv.org/pdf/2601.14925.pdf)  
**作者**：Nicolás Arrieta Larraza, Niels de Koeijer  

**一句话要点**：提出Fast-ULCNet以在资源受限设备上实现低延迟和低复杂度的单通道语音增强

**关键词**：单通道语音增强, 低复杂度网络, FastGRNN, 状态漂移缓解, 嵌入式设备

## 3 点简述
- 核心问题：单通道语音增强在嵌入式设备中需低延迟和低复杂度设计
- 方法要点：将ULCNet的GRU层替换为FastGRNNs，并引入可训练互补滤波器缓解状态漂移
- 实验或效果：模型大小减半，延迟降低34%，性能与原ULCNet相当

## 摘要（原文）

> Single-channel speech enhancement algorithms are often used in resource-constrained embedded devices, where low latency and low complexity designs gain more importance. In recent years, researchers have proposed a wide variety of novel solutions to this problem. In particular, a recent deep learning model named ULCNet is among the state-of-the-art approaches in this domain. This paper proposes an adaptation of ULCNet, by replacing its GRU layers with FastGRNNs, to reduce both computational latency and complexity. Furthermore, this paper shows empirical evidence on the performance decay of FastGRNNs in long audio signals during inference due to internal state drifting, and proposes a novel approach based on a trainable complementary filter to mitigate it. The resulting model, Fast-ULCNet, performs on par with the state-of-the-art original ULCNet architecture on a speech enhancement task, while reducing its model size by more than half and decreasing its latency by 34% on average.

