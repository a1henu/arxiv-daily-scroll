---
layout: default
title: Quasar: Quantized Self-Speculative Acceleration for Rapid Inference via Memory-Efficient Verification
---

# Quasar: Quantized Self-Speculative Acceleration for Rapid Inference via Memory-Efficient Verification
**arXiv**：[2603.01399v1](https://arxiv.org/abs/2603.01399) · [PDF](https://arxiv.org/pdf/2603.01399.pdf)  
**作者**：Guang Huang, Zeyi Wen  

**一句话要点**：提出Quasar框架，通过量化验证阶段以解决推测解码中的内存带宽瓶颈问题。

**关键词**：推测解码, 量化推理, 内存优化, 自推测加速, 训练无关框架

## 3 点简述
- 推测解码中验证阶段成为性能瓶颈，受限于内存带宽。
- Quasar采用低比特量化验证，减少内存流量并保持对数分布精度。
- 实验显示Quasar在保持接受长度同时，端到端吞吐量提升1.28倍。

## 摘要（原文）

> Speculative Decoding (SD) has emerged as a premier technique for accelerating Large Language Model (LLM) inference by decoupling token generation into rapid drafting and parallel verification. While recent advancements in self-speculation and lookahead decoding have successfully minimized drafting overhead, they have shifted the primary performance bottleneck to the verification phase. Since verification requires a full forward pass of the target model, it remains strictly memory-bandwidth bound, fundamentally limiting the maximum achievable speedup.In this paper, we introduce \textbf{Quasar} (\textbf{Qua}ntized \textbf{S}elf-speculative \textbf{A}cceleration for \textbf{R}apid Inference), a novel, training-free framework designed to overcome this "memory wall" by employing low-bit quantization specifically for the verification stage. Our empirical analysis reveals that while aggressive structural pruning significantly degrades verification accuracy, quantization-based verification preserves the logit distribution with high fidelity while effectively halving memory traffic. Extensive experiments on state-of-the-art models (e.g., OpenPangu and Qwen3) demonstrate that Quasar maintains a speculative acceptance length comparable to full-precision methods while achieving a $1.28\times$ improvement in end-to-end throughput. Being orthogonal to existing drafting strategies, Quasar offers a generic and efficient pathway to accelerate the verification leg of speculative execution. Code is available at https://github.com/Tom-HG/Quasar.

