---
layout: default
title: LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding
---

# LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding
**arXiv**：[2602.04541v1](https://arxiv.org/abs/2602.04541) · [PDF](https://arxiv.org/pdf/2602.04541.pdf)  
**作者**：Gang Lin, Dongfang Li, Zhuoen Chen, Yukun Shi, Xuhui Chen, Baotian Hu, Min Zhang  

**一句话要点**：提出LycheeDecode，通过混合头稀疏解码加速长上下文LLM推理

**关键词**：长上下文推理, 稀疏注意力, 键值缓存优化, LLM加速, 混合头机制

## 3 点简述
- 核心问题：长上下文LLM解码时键值缓存膨胀导致内存和延迟成本高。
- 方法要点：基于HardKuma的细粒度混合头注意力机制，动态识别关键令牌并重用。
- 实验效果：在128K上下文长度下实现最高2.7倍加速，生成质量媲美或超越全注意力基线。

## 摘要（原文）

> The proliferation of long-context large language models (LLMs) exposes a key bottleneck: the rapidly expanding key-value cache during decoding, which imposes heavy memory and latency costs. While recent approaches attempt to alleviate this by sharing a single set of crucial tokens across layers, such coarse-grained sharing undermines model performance by neglecting the functional diversity of attention heads. To address this, we propose LycheeDecode, an efficient decoding method centered on a fine-grained hybrid-head attention mechanism that employs a hardware-efficient top-k selection strategy. Specifically, the novel HardKuma-based mechanism partitions attention heads into a small subset of retrieval heads that dynamically identify crucial tokens and a majority of sparse heads that reuse them for efficient computation. Through extensive experiments on leading models like Llama3 and Qwen3 across diverse benchmarks for long-context understanding (e.g., LongBench, RULER) and complex reasoning (e.g., AIME24, OlympiadBench), we demonstrate that LycheeDecode achieves generative quality comparable to, and at times surpassing even the full-attention baseline. Crucially, this is accomplished with up to a 2.7x speedup at a 128K context length. By preserving the functional diversity of attention heads, our fine-grained strategy overcomes the performance bottlenecks of existing methods, providing a powerful and validated pathway to both efficient and high-quality long-context LLM inference.

