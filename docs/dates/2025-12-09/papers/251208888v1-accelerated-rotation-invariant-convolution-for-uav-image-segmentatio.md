---
layout: default
title: Accelerated Rotation-Invariant Convolution for UAV Image Segmentation
---

# Accelerated Rotation-Invariant Convolution for UAV Image Segmentation
**arXiv**：[2512.08888v1](https://arxiv.org/abs/2512.08888) · [PDF](https://arxiv.org/pdf/2512.08888.pdf)  
**作者**：Manduhu Manduhu, Alexander Dow, Gerard Dooly, James Riordan  

**一句话要点**：提出GPU优化的旋转不变卷积框架，以高效处理无人机图像分割中的任意方向目标。

**关键词**：旋转不变卷积, 无人机图像分割, GPU优化, 计算效率, 内存优化

## 3 点简述
- 核心问题：传统卷积在无人机图像分割中缺乏旋转不变性，导致精度下降且计算成本高。
- 方法要点：通过结构化数据共享消除im2col步骤，减少内存流量和计算冗余，支持多方向和任意角度卷积。
- 实验或效果：相比CUDNN，训练速度提升20-55%，能耗降低15-45%，在U-Net中精度提升达6%。

## 摘要（原文）

> Rotation invariance is essential for precise, object-level segmentation in UAV aerial imagery, where targets can have arbitrary orientations and exhibit fine-scale details. Conventional segmentation architectures like U-Net rely on convolution operators that are not rotation-invariant, leading to degraded segmentation accuracy across varying viewpoints. Rotation invariance can be achieved by expanding the filter bank across multiple orientations; however, this will significantly increase computational cost and memory traffic. In this paper, we introduce a GPU-optimized rotation-invariant convolution framework that eliminates the traditional data-lowering (im2col) step required for matrix-multiplication-based convolution. By exploiting structured data sharing among symmetrically rotated filters, our method achieves multi-orientation convolution with greatly reduced memory traffic and computational redundancy. We further generalize the approach to accelerate convolution with arbitrary (non-symmetric) rotation angles.
>   Across extensive benchmarks, the proposed convolution achieves 20--55% faster training and 15--45% lower energy consumption than CUDNN, while maintaining accuracy comparable to state-of-the-art rotation-invariant methods. In the eight-orientation setting, our approach achieves up to 45% speedup and 41% energy savings on 256\(\times\)256 inputs, and 32% speedup and 23% lower energy usage on 1024\(\times\)1024 inputs. Integrated into a U-Net segmentation model, the framework yields up to 6% improvement in accuracy over the non-rotation-aware baseline. These results demonstrate that the proposed method provides an effective and highly efficient alternative to existing rotation-invariant CNN frameworks.

