---
layout: default
title: Adaptive Soft Rolling KV Freeze with Entropy-Guided Recovery: Sublinear Memory Growth for Efficient LLM Inference
---

# Adaptive Soft Rolling KV Freeze with Entropy-Guided Recovery: Sublinear Memory Growth for Efficient LLM Inference
**arXiv**：[2512.11221v1](https://arxiv.org/abs/2512.11221) · [PDF](https://arxiv.org/pdf/2512.11221.pdf)  
**作者**：Adilet Metinov, Gulida M. Kudakeeva, Bolotbek uulu Nursultan, Gulnara D. Kabaeva  

**一句话要点**：提出自适应软滚动KV冻结与熵引导恢复框架，以解决长上下文LLM推理中的内存效率问题。

**关键词**：KV缓存优化, 推理效率, 长上下文处理, 训练无关方法, 内存管理, 注意力机制

## 3 点简述
- 核心问题：长上下文LLM推理时KV缓存内存增长快，影响部署效率。
- 方法要点：基于滑动注意力窗口识别低重要性token，可逆软冻结其KV更新，结合熵引导恢复和次线性调度。
- 实验或效果：在LLaMA-3 8B上，主动KV缓存大小减少55-67%，保持生成质量并通过检索测试。

## 摘要（原文）

> We present Adaptive Soft Rolling KV Freeze with Entropy-Guided Recovery (ASR-KF-EGR), a training-free inference-time framework for efficient large language model generation. Our method introduces a reversible soft-freeze mechanism that temporarily suspends key-value (KV) updates for low-importance tokens identified within a sliding attention window. Unlike eviction-based approaches that permanently discard context, ASR-KF-EGR preserves all tokens in off-GPU storage and restores them on demand. We extend the framework with sublinear freeze scheduling, where freeze duration grows sublinearly with repeated low-importance detections, preventing over-aggressive compression. Preliminary experiments on LLaMA-3 8B demonstrate 55-67% reduction in active KV cache size while maintaining generation quality and passing needle-in-haystack retrieval tests. The method is architecture-agnostic, requires no fine-tuning, and provides a practical solution for memory-constrained deployment of long-context LLMs.

