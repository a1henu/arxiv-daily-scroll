---
layout: default
title: Single-Stage Huffman Encoder for ML Compression
---

# Single-Stage Huffman Encoder for ML Compression
**arXiv**：[2601.10673v1](https://arxiv.org/abs/2601.10673) · [PDF](https://arxiv.org/pdf/2601.10673.pdf)  
**作者**：Aditya Agrawal, Albert Magyar, Hiteshwar Eswaraiah, Patrick Sheridan, Pradeep Janedula, Ravi Krishnan Venkatesan, Krishna Nair, Ravi Iyer  

**一句话要点**：提出单阶段哈夫曼编码器以解决大语言模型分布式训练中的网络带宽瓶颈问题。

**关键词**：哈夫曼编码, 无损压缩, 大语言模型, 分布式训练, 网络带宽优化, 实时压缩

## 3 点简述
- 核心问题：传统哈夫曼编码的三阶段设计在延迟敏感场景（如芯片间通信）中引入计算、延迟和数据开销。
- 方法要点：使用基于历史数据平均概率分布的固定码本，消除动态频率分析和码本传输开销。
- 实验或效果：在Gemma 2B模型中，压缩率接近逐分片哈夫曼编码和理想香农压缩性，实现高效实时压缩。

## 摘要（原文）

> Training and serving Large Language Models (LLMs) require partitioning data across multiple accelerators, where collective operations are frequently bottlenecked by network bandwidth. Lossless compression using Huffman codes is an effective way to alleviate the issue, however, its three-stage design requiring on-the-fly frequency analysis, codebook generation and transmission of codebook along with data introduces computational, latency and data overheads which are prohibitive for latency-sensitive scenarios such as die-to-die communication. This paper proposes a single-stage Huffman encoder that eliminates these overheads by using fixed codebooks derived from the average probability distribution of previous data batches. Through our analysis of the Gemma 2B model, we demonstrate that tensors exhibit high statistical similarity across layers and shards. Using this approach we achieve compression within 0.5% of per-shard Huffman coding and within 1% of the ideal Shannon compressibility, enabling efficient on-the-fly compression.

