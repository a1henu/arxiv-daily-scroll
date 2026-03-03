---
layout: default
title: TiledAttention: a CUDA Tile SDPA Kernel for PyTorch
---

# TiledAttention: a CUDA Tile SDPA Kernel for PyTorch
**arXiv**：[2603.01960v1](https://arxiv.org/abs/2603.01960) · [PDF](https://arxiv.org/pdf/2603.01960.pdf)  
**作者**：Taimur Khan  

**一句话要点**：提出TiledAttention以在PyTorch中实现可编辑的高性能SDPA前向算子，用于GPU研究。

**关键词**：缩放点积注意力, GPU内核优化, PyTorch扩展, CUDA编程, 高性能计算

## 3 点简述
- 核心问题：传统CUDA模板难以修改，阻碍SDPA内核研究的快速迭代。
- 方法要点：基于TileIR实现，支持在线softmax和分块KV流，通过Python调度层直接编辑。
- 实验或效果：在NVIDIA DGX GB10上基准测试，相比标准eager路径有显著加速，提供性能与可定制性的平衡。

## 摘要（原文）

> TiledAttention is a scaled dot-product attention (SDPA) forward operator for SDPA research on NVIDIA GPUs. Implemented in cuTile Python (TileIR) and exposed as a PyTorch-callable function, it is easier to modify than low-level CUDA templates while retaining realistic behavior via online softmax and tiled $K,V$ streaming. The approach is both performant and directly editable at the schedule level from Python (tile shapes, staging, shared-memory layout), enabling rapid, reproducible kernel research without template-heavy CUDA/CUTLASS rewrites. We benchmark TiledAttention on an NVIDIA DGX GB10 node with a reproducible harness and compare against PyTorch SDPA (auto-dispatch) and explicit unfused baselines across sequence length, head dimension, and precision (FP16/BF16). While production fused baselines remain stronger overall, TiledAttention delivers large speedups over standard eager attention paths and is available for direct use within PyTorch workflows, providing a practical balance between performance and customizability.

