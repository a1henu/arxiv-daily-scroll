---
layout: default
title: A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA
---

# A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA
**arXiv**：[2603.05931v1](https://arxiv.org/abs/2603.05931) · [PDF](https://arxiv.org/pdf/2603.05931.pdf)  
**作者**：Neelesh Gupta, Peter Wang, Rajgopal Kannan, Viktor K. Prasanna  

**一句话要点**：提出基于FPGA的持久状态数据流加速器，以解决线性注意力解码在GPU上的内存瓶颈问题。

**关键词**：线性注意力, FPGA加速器, 内存优化, 数据流处理, 循环状态管理, 能效提升

## 3 点简述
- 核心问题：GDN等线性注意力解码在批大小为1时因状态频繁访问HBM而内存受限。
- 方法要点：设计FPGA加速器，将2MB循环状态持久存储于BRAM，实现数据流流水线处理。
- 实验或效果：在AMD Alveo U55C上实现63μs每令牌，比NVIDIA H100 GPU快4.5倍，能效提升达60倍。

## 摘要（原文）

> Gated DeltaNet (GDN) is a linear attention mechanism that replaces the growing KV cache with a fixed-size recurrent state. Hybrid LLMs like Qwen3-Next use 75% GDN layers and achieve competitive accuracy to attention-only models. However, at batch-1, GDN decode is memory-bound on GPUs since the full recurrent state must be round-tripped through HBM every token. We show that this bottleneck is architectural, not algorithmic, as all subquadratic sequence models exhibit arithmetic intensities below 1 FLOP/B at decode time, making them more memory-bound than standard Transformers. We present an FPGA accelerator that eliminates this bottleneck by holding the full 2 MB recurrent state persistently in on-chip BRAM, converting the workload from memory-bound to compute-bound. Our design fuses the GDN recurrence into a five-phase pipelined datapath that performs only one read and one write pass over each state matrix per token, exploits Grouped Value Attention for paired-head parallelism, and overlaps preparation, computation, and output storage via dataflow pipelining. We explore four design points on an AMD Alveo U55C using Vitis HLS, varying head-level parallelism from 2 to 16 value-heads per iteration. Our fastest configuration achieves 63 $μ$s per token, 4.5$\times$ faster than the GPU reference on NVIDIA H100 PCIe. Post-implementation power analysis reports 9.96 W on-chip, yielding up to 60$\times$ greater energy efficiency per token decoded.

