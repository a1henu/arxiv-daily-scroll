---
layout: default
title: FlexLLM: Composable HLS Library for Flexible Hybrid LLM Accelerator Design
---

# FlexLLM: Composable HLS Library for Flexible Hybrid LLM Accelerator Design
**arXiv**：[2601.15710v1](https://arxiv.org/abs/2601.15710) · [PDF](https://arxiv.org/pdf/2601.15710.pdf)  
**作者**：Jiahao Zhang, Zifan He, Nicholas Fraser, Michaela Blott, Yizhou Sun, Jason Cong  

**一句话要点**：提出FlexLLM可组合HLS库，用于快速开发面向LLM推理的混合加速器设计。

**关键词**：LLM加速器, 可组合HLS库, 阶段定制化推理, 混合数据流, 硬件高效量化, 长上下文处理

## 3 点简述
- 核心问题：LLM推理加速器设计复杂，需灵活支持预填充和解码阶段的不同优化。
- 方法要点：提供可组合HLS库，支持阶段定制化推理、混合数据流和量化套件。
- 实验或效果：在FPGA上实现优于GPU的加速、能效和长上下文处理能力。

## 摘要（原文）

> We present FlexLLM, a composable High-Level Synthesis (HLS) library for rapid development of domain-specific LLM accelerators. FlexLLM exposes key architectural degrees of freedom for stage-customized inference, enabling hybrid designs that tailor temporal reuse and spatial dataflow differently for prefill and decode, and provides a comprehensive quantization suite to support accurate low-bit deployment. Using FlexLLM, we build a complete inference system for the Llama-3.2 1B model in under two months with only 1K lines of code. The system includes: (1) a stage-customized accelerator with hardware-efficient quantization (12.68 WikiText-2 PPL) surpassing SpinQuant baseline, and (2) a Hierarchical Memory Transformer (HMT) plug-in for efficient long-context processing. On the AMD U280 FPGA at 16nm, the accelerator achieves 1.29$\times$ end-to-end speedup, 1.64$\times$ higher decode throughput, and 3.14$\times$ better energy efficiency than an NVIDIA A100 GPU (7nm) running BF16 inference; projected results on the V80 FPGA at 7nm reach 4.71$\times$, 6.55$\times$, and 4.13$\times$, respectively. In long-context scenarios, integrating the HMT plug-in reduces prefill latency by 23.23$\times$ and extends the context window by 64$\times$, delivering 1.10$\times$/4.86$\times$ lower end-to-end latency and 5.21$\times$/6.27$\times$ higher energy efficiency on the U280/V80 compared to the A100 baseline. FlexLLM thus bridges algorithmic innovation in LLM inference and high-performance accelerators with minimal manual effort.

