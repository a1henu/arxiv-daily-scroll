---
layout: default
title: Compiler-First State Space Duality and Portable $O(1)$ Autoregressive Caching for Inference
---

# Compiler-First State Space Duality and Portable $O(1)$ Autoregressive Caching for Inference
**arXiv**：[2603.09555v1](https://arxiv.org/abs/2603.09555) · [PDF](https://arxiv.org/pdf/2603.09555.pdf)  
**作者**：Cosmo Santoni  

**一句话要点**：提出基于XLA的状态空间模型编译器优先方法，实现跨平台高效推理与O(1)自回归缓存。

**关键词**：状态空间模型, 编译器优化, 跨平台推理, 自回归缓存, XLA, 硬件无关性

## 3 点简述
- 核心问题：状态空间模型依赖NVIDIA硬件和定制内核，限制可移植性和优化。
- 方法要点：利用Mamba-2状态空间对偶性，映射到XLA融合和分块优化，无需手写内核。
- 实验或效果：在CPU、GPU、TPU上运行，TPU v6e达到140 TFLOPS预填充和64%带宽利用率解码。

## 摘要（原文）

> State-space model releases are typically coupled to fused CUDA and Triton kernels, inheriting a hard dependency on NVIDIA hardware. We show that Mamba-2's state space duality algorithm -- diagonal state structure, chunkable recurrence, and einsum-dominated compute with static control flow -- maps cleanly onto what XLA's fusion and tiling passes actually optimise, making custom kernels optional rather than required. We implement the full inference path (prefill, cached autoregressive decoding) as shaped standard primitives under XLA, without hand-written kernels, and realise the architecture's theoretical $O(1)$ state management as a compiled on-device cache requiring no host synchronisation during generation. The implementation runs unmodified on CPU, NVIDIA GPU, and Google Cloud TPU from a single JAX source. On TPU v6e across five model scales (130M--2.7B parameters), XLA-generated code reaches approximately 140 TFLOPS on single-stream prefill ($15%$ MFU) and up to $64%$ bandwidth utilisation on decode. Greedy decoding matches the PyTorch/CUDA reference token-for-token across 64 steps, with hidden-state agreement within float32 rounding tolerance. The pattern transfers to any SSM recurrence satisfying the same structural conditions, on any platform with a mature XLA backend. The implementation is publicly available at https://github.com/CosmoNaught/mamba2-jax and merged into the Bonsai JAX model library.

