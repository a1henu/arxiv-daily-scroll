---
layout: default
title: GPU-Accelerated INT8 Quantization for KV Cache Compression in Large Language Models
---

# GPU-Accelerated INT8 Quantization for KV Cache Compression in Large Language Models
**arXiv**：[2601.04719v1](https://arxiv.org/abs/2601.04719) · [PDF](https://arxiv.org/pdf/2601.04719.pdf)  
**作者**：Maanas Taneja, Purab Shingvi  

**一句话要点**：提出GPU加速的INT8量化方法以压缩大语言模型推理中的KV缓存内存瓶颈

**关键词**：大语言模型推理, KV缓存压缩, INT8量化, GPU加速, CUDA内核优化, 内存效率

## 3 点简述
- KV缓存在大语言模型推理中随序列长度线性增长，成为主要内存瓶颈
- 开发四种CUDA内核变体，实现4倍内存压缩且精度损失极小
- 向量化内核在十亿元素规模下加速达1694倍，重建误差低于0.004

## 摘要（原文）

> The key-value (KV) cache in large language models presents a significant memory bottleneck during inference, growing linearly with sequence length and often exceeding the memory footprint of model weights themselves. We implement and evaluate GPU-accelerated INT8 quantization for KV cache compression, achieving 4$\times$ memory reduction with minimal accuracy degradation. We develop four CUDA kernel variants -- naive, tiled, coarsened, and vectorized -- and benchmark them across realistic workload sizes up to 1 billion elements. Our vectorized kernel achieves up to 1,694$\times$ speedup over CPU baselines while maintaining reconstruction error below 0.004 and attention score error below 0.1 even for 8K-dimensional heads. These results demonstrate that INT8 quantization provides a practical approach for reducing memory pressure in LLM inference with negligible computational overhead (6--58ms) and minimal impact on downstream model behavior

