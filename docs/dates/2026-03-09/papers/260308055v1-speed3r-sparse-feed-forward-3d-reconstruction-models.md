---
layout: default
title: Speed3R: Sparse Feed-forward 3D Reconstruction Models
---

# Speed3R: Sparse Feed-forward 3D Reconstruction Models
**arXiv**：[2603.08055v1](https://arxiv.org/abs/2603.08055) · [PDF](https://arxiv.org/pdf/2603.08055.pdf)  
**作者**：Weining Ren, Xiao Tan, Kai Han  

**一句话要点**：提出Speed3R稀疏前馈3D重建模型，通过双分支注意力机制解决密集注意力计算瓶颈，实现高效大规模场景建模。

**关键词**：3D重建, 稀疏注意力, 前馈模型, 运动恢复结构, 计算效率, 大规模场景建模

## 3 点简述
- 核心问题：现有前馈3D重建模型依赖密集注意力，导致二次复杂度计算瓶颈，严重限制推理速度。
- 方法要点：受运动恢复结构启发，采用双分支注意力机制，压缩分支提供粗粒度上下文先验，选择分支仅对信息量最大的图像令牌进行细粒度注意力。
- 实验或效果：在1000视图序列上实现12.4倍推理加速，几何精度损失可控，在标准基准测试中验证了高效高质量重建。

## 摘要（原文）

> While recent feed-forward 3D reconstruction models accelerate 3D reconstruction by jointly inferring dense geometry and camera poses in a single pass, their reliance on dense attention imposes a quadratic complexity, creating a prohibitive computational bottleneck that severely limits inference speed. To resolve this, we introduce Speed3R, an end-to-end trainable model inspired by the core principle of Structure-from-Motion: that a sparse set of keypoints is sufficient for robust pose estimation. Speed3R features a dual-branch attention mechanism where a compression branch creates a coarse contextual prior to guide a selection branch, which performs fine-grained attention only on the most informative image tokens. This strategy mimics the efficiency of traditional keypoint matching, achieving a remarkable 12.4x inference speedup on 1000-view sequences, while introducing a minimal, controlled trade-off in geometric accuracy. Validated on standard benchmarks with both VGGT and $π^3$ backbones, our method delivers high-quality reconstructions at a fraction of computational cost, paving the way for efficient large-scale scene modeling.

