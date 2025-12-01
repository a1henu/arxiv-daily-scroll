---
layout: default
title: Quantized-Tinyllava: a new multimodal foundation model enables efficient split learning
---

# Quantized-Tinyllava: a new multimodal foundation model enables efficient split learning
**arXiv**：[2511.23402v1](https://arxiv.org/abs/2511.23402) · [PDF](https://arxiv.org/pdf/2511.23402.pdf)  
**作者**：Jiajun Guo, Xin Luo, Jie Liu  

**一句话要点**：提出量化多模态模型结构以降低分割学习中的网络通信成本

**关键词**：分割学习, 多模态模型, 数据压缩, 量化嵌入, 熵编码, 网络通信优化

## 3 点简述
- 核心问题：分割学习中大模型传输高维数据导致高网络通信成本
- 方法要点：结合学习型数据压缩，将嵌入量化为低比特整数以保持性能
- 实验或效果：基于熵编码理论确定离散表示级别，大幅减少传输开销

## 摘要（原文）

> Split learning is well known as a method for resolving data privacy concerns by training a model on distributed devices, thereby avoiding data sharing that raises privacy issues. However, high network communication costs are always an impediment to split learning, especially for large foundation models that require transmitting large amounts of high-dimensional data. To resolve this issue, we present a new multimodal model structure that incorporates a learning-based data compression method, which compresses model embeddings into low-bit integers while preserving the model's performance, greatly reducing the transmission costs between partitions. We then determine the optimal number of discrete representation levels based on a solid theoretical foundation from entropy coding.

