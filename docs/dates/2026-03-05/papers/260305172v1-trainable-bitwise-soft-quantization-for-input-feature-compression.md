---
layout: default
title: Trainable Bitwise Soft Quantization for Input Feature Compression
---

# Trainable Bitwise Soft Quantization for Input Feature Compression
**arXiv**：[2603.05172v1](https://arxiv.org/abs/2603.05172) · [PDF](https://arxiv.org/pdf/2603.05172.pdf)  
**作者**：Karsten Schrödter, Jan Stenkamp, Nina Herrmann, Fabian Gieseke  

**一句话要点**：提出可训练的比特软量化层以压缩输入特征，解决物联网边缘设备数据传输带宽限制问题。

**关键词**：输入特征压缩, 可训练量化, 比特软量化, 物联网边缘计算, 神经网络优化, 数据传输效率

## 3 点简述
- 核心问题：物联网应用中，边缘设备向远程服务器传输数据面临带宽、延迟和能耗约束，需压缩输入特征以减少数据传输量。
- 方法要点：设计任务特定的可训练量化层，使用sigmoid近似阶跃函数实现可训练阈值，通过比特软量化将每个输入特征量化到用户指定比特数。
- 实验或效果：在多个数据集上，相比32位输入实现5倍至16倍压缩，保持精度接近全精度模型，优于标准量化方法。

## 摘要（原文）

> The growing demand for machine learning applications in the context of the Internet of Things calls for new approaches to optimize the use of limited compute and memory resources. Despite significant progress that has been made w.r.t. reducing model sizes and improving efficiency, many applications still require remote servers to provide the required resources. However, such approaches rely on transmitting data from edge devices to remote servers, which may not always be feasible due to bandwidth, latency, or energy constraints. We propose a task-specific, trainable feature quantization layer that compresses the input features of a neural network. This can significantly reduce the amount of data that needs to be transferred from the device to a remote server. In particular, the layer allows each input feature to be quantized to a user-defined number of bits, enabling a simple on-device compression at the time of data collection. The layer is designed to approximate step functions with sigmoids, enabling trainable quantization thresholds. By concatenating outputs from multiple sigmoids, introduced as bitwise soft quantization, it achieves trainable quantized values when integrated with a neural network. We compare our method to full-precision inference as well as to several quantization baselines. Experiments show that our approach outperforms standard quantization methods, while maintaining accuracy levels close to those of full-precision models. In particular, depending on the dataset, compression factors of $5\times$ to $16\times$ can be achieved compared to $32$-bit input without significant performance loss.

