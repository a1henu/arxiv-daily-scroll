---
layout: default
title: VLM in a flash: I/O-Efficient Sparsification of Vision-Language Model via Neuron Chunking
---

# VLM in a flash: I/O-Efficient Sparsification of Vision-Language Model via Neuron Chunking
**arXiv**：[2511.18692v1](https://arxiv.org/abs/2511.18692) · [PDF](https://arxiv.org/pdf/2511.18692.pdf)  
**作者**：Kichang Yang, Seonjun Kim, Minjae Kim, Nairan Zhang, Chi Zhang, Youngki Lee  

**一句话要点**：提出神经元分块方法以优化视觉语言模型在边缘设备上的I/O效率

**关键词**：视觉语言模型, I/O优化, 激活稀疏化, 边缘计算, 神经元分块

## 3 点简述
- 核心问题：传统激活稀疏化仅基于神经元重要性，忽略存储访问模式对闪存性能的影响。
- 方法要点：通过分块操作，结合神经元重要性和访问连续性，选择高效用块以减少I/O开销。
- 实验或效果：在Jetson设备上，I/O效率提升最高达4.65倍和5.76倍。

## 摘要（原文）

> Edge deployment of large Vision-Language Models (VLMs) increasingly relies on flash-based weight offloading, where activation sparsification is used to reduce I/O overhead. However, conventional sparsification remains model-centric, selecting neurons solely by activation magnitude and neglecting how access patterns influence flash performance. We present Neuron Chunking, an I/O-efficient sparsification strategy that operates on chunks (i.e., groups of contiguous neurons in memory) and couples neuron importance with storage access cost. The method models I/O latency through a lightweight abstraction of access contiguity and selects chunks with high utility, defined as neuron importance normalized by estimated latency. By aligning sparsification decisions with the underlying storage behavior, Neuron Chunking improves I/O efficiency by up to 4.65x and 5.76x on Jetson Orin Nano and Jetson AGX Orin, respectively.

