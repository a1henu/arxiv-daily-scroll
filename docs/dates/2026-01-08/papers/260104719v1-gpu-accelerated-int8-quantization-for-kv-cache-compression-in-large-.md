---
layout: default
title: GPU-Accelerated INT8 Quantization for KV Cache Compression in Large Language Models
---

# GPU-Accelerated INT8 Quantization for KV Cache Compression in Large Language Models
**arXiv**：[2601.04719v1](https://arxiv.org/abs/2601.04719) · [PDF](https://arxiv.org/pdf/2601.04719.pdf)  
**作者**：Maanas Taneja, Purab Shingvi  

**一句话要点**：提出GPU加速INT8量化以压缩大语言模型KV缓存，减少内存占用并保持精度

**关键词**：大语言模型, KV缓存压缩, INT8量化, GPU加速, 推理优化, 内存效率

## 3 点简述
- KV缓存在大语言模型推理中导致内存瓶颈，随序列长度线性增长
- 开发四种CUDA内核变体，实现GPU加速INT8量化，压缩内存4倍
- 实验显示向量化内核加速达1694倍，重建误差低于0.004，对模型行为影响小

## 摘要（原文）

> The key-value (KV) cache in large language models presents a significant memory bottleneck during inference, growing linearly with sequence length and often exceeding the memory footprint of model weights themselves. We implement and evaluate GPU-accelerated INT8 quantization for KV cache compression, achieving 4$\times$ memory reduction with minimal accuracy degradation. We develop four CUDA kernel variants -- naive, tiled, coarsened, and vectorized -- and benchmark them across realistic workload sizes up to 1 billion elements. Our vectorized kernel achieves up to 1,694$\times$ speedup over CPU baselines while maintaining reconstruction error below 0.004 and attention score error below 0.1 even for 8K-dimensional heads. These results demonstrate that INT8 quantization provides a practical approach for reducing memory pressure in LLM inference with negligible computational overhead (6--58ms) and minimal impact on downstream model behavior

