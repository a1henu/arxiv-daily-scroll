---
layout: default
title: SoftDTW-CUDA-Torch: Memory-Efficient GPU-Accelerated Soft Dynamic Time Warping for PyTorch
---

# SoftDTW-CUDA-Torch: Memory-Efficient GPU-Accelerated Soft Dynamic Time Warping for PyTorch
**arXiv**：[2602.17206v1](https://arxiv.org/abs/2602.17206) · [PDF](https://arxiv.org/pdf/2602.17206.pdf)  
**作者**：Ron Shapira Weber, Oren Freifeld  

**一句话要点**：提出SoftDTW-CUDA-Torch库，解决GPU上SoftDTW的序列长度限制、数值不稳定性和内存消耗问题。

**关键词**：SoftDTW, GPU加速, PyTorch库, 内存优化, 动态时间规整

## 3 点简述
- 现有GPU实现存在序列长度上限1024、反向传播数值不稳定和内存消耗大等限制。
- 采用分块反对角线核执行、对数空间反向传播和融合距离计算模式以提升性能。
- 支持任意序列长度、PyTorch自动微分和Soft-DTW重心计算，内存减少高达98%。

## 摘要（原文）

> We present softdtw-cuda-torch, an open-source PyTorch library for computing Soft Dynamic Time Warping (SoftDTW) on GPUs. Our implementation addresses three key limitations of existing GPU implementations of SoftDTW: a hard sequence-length cap of 1024, numerical instability in the backward pass for small smoothing parameters, and excessive GPU memory consumption from materializing pairwise distance tensors. We introduce (1) tiled anti-diagonal kernel execution that removes the sequence-length constraint, (2) a log-space back-ward pass that prevents floating-point overflow, and (3) a fused distance-computation mode that eliminates the O(BN M ) intermediate distance tensor, achieving up to 98% memory reduction compared to prior work. The library supports arbitrary sequence lengths, full PyTorch autograd integration, and Soft-DTW Barycenter computation. Code is available at https://github.com/BGU-CS-VIL/sdtw-cuda-torch.

