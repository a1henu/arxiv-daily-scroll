---
layout: default
title: LOOKAT: Lookup-Optimized Key-Attention for Memory-Efficient Transformers
---

# LOOKAT: Lookup-Optimized Key-Attention for Memory-Efficient Transformers
**arXiv**：[2601.10155v1](https://arxiv.org/abs/2601.10155) · [PDF](https://arxiv.org/pdf/2601.10155.pdf)  
**作者**：Aryan Karmore  

**一句话要点**：提出LOOKAT方法，通过查找优化键注意力实现内存高效Transformer，以在边缘设备部署大语言模型。

**关键词**：KV缓存压缩, 乘积量化, 查找表注意力, 内存高效Transformer, 边缘设备部署, 秩相关分析

## 3 点简述
- 核心问题：现有KV缓存量化方法压缩存储但未减少带宽，因注意力计算需将INT4/INT8键反量化为FP16。
- 方法要点：将键向量分解为子空间，应用乘积量化和非对称距离计算，通过查找表计算注意力表，将注意力从内存受限转为计算受限。
- 实验或效果：在GPT-2上实现64倍压缩（95.7%输出保真度）和32倍压缩（95.0%保真度），无需架构更改或训练，秩相关ρ>0.95。

## 摘要（原文）

> Compressing the KV cache is a required step to deploy large language models on edge devices. Current quantization methods compress storage but fail to reduce bandwidth as attention calculation requires dequantizing keys from INT4/INT8 to FP16 before use. We observe that attention scoring is mathematically equivalent to the inner product similarity search and we can apply some compression techniques from vector databases to compress KV-cache better. We propose LOOKAT, which applies product quantization and asymmetric distance computation, to transformer architecture by decomposing key vectors into subspaces, learning codebooks and computing attention tables via lookup tables. This transforms attention from memory-bound to compute-bound. LOOKAT achieves 64 $\times$ compression at 95.7\% output fidelity and 32 $\times$ compression at 95.0\% fidelity when tested on GPT-2. LOOKAT requires no architecture changes or training while maintaining rank correlation $ρ> 0.95$. Theoretical analysis confirms that rank correlation degrades as $O(d_k/mK)$, with guarantees validated across sequence lengths up to 1024 tokens.

