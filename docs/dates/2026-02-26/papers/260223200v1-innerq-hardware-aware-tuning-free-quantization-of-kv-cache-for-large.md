---
layout: default
title: InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models
---

# InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models
**arXiv**：[2602.23200v1](https://arxiv.org/abs/2602.23200) · [PDF](https://arxiv.org/pdf/2602.23200.pdf)  
**作者**：Sayed Mohammadreza Tayaranian Hosseini, Amir Ardakani, Warren J. Gross  

**一句话要点**：提出InnerQ硬件感知KV缓存量化方案，以降低大语言模型解码延迟

**关键词**：KV缓存量化, 硬件感知优化, 大语言模型解码, 内存效率, 分组量化, 解码加速

## 3 点简述
- 核心问题：KV缓存在大语言模型解码中内存占用高，影响长序列生成效率。
- 方法要点：采用内维度分组量化，结合混合量化、高精度窗口和每通道归一化，减少内存访问并加速反量化。
- 实验或效果：在Llama模型上评估，保持GSM8K性能，解码速度提升最高达22%，优于先前方法。

## 摘要（原文）

> Reducing the hardware footprint of large language models (LLMs) during decoding is critical for efficient long-sequence generation. A key bottleneck is the key-value (KV) cache, whose size scales with sequence length and easily dominates the memory footprint of the model. Previous work proposed quantization methods that are focused on compressing the KV cache while maintaining its information. We introduce InnerQ, a hardware-aware KV-cache quantization scheme that lowers decode latency without sacrificing accuracy. InnerQ applies group-wise quantization while grouping the cache matrices over their inner dimension. Unlike previous work that group over the outer dimension, InnerQ aligns dequantization with the vector-matrix multiplication and enables scale factor reuse across GPU compute units. This reduces memory accesses and accelerates dequantization, yielding up to $22\%$ speedup over previous work and up to $88\%$ over half-precision vector-matrix multiplication. To preserve fidelity under aggressive compression, InnerQ incorporates (i) hybrid quantization, selecting symmetric or asymmetric quantization per group based on local statistics; (ii) high-precision windows for both the most recent tokens and the attention sink tokens to mitigate outlier leakage; and (iii) per-channel normalization of the key cache, computed once during prefill and folded into the query to avoid runtime overhead. Our evaluation experiments on Llama models shows that InnerQ maintains a few-shot GSM8K performance comparable to non-quantized KV caches and surpasses prior KV cache quantization methods.

