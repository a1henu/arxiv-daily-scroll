---
layout: default
title: Larger than memory image processing
---

# Larger than memory image processing
**arXiv**：[2601.18407v1](https://arxiv.org/abs/2601.18407) · [PDF](https://arxiv.org/pdf/2601.18407.pdf)  
**作者**：Jon Sporring, David Stansby  

**一句话要点**：提出基于切片流式架构的领域特定语言，以解决超大规模图像处理中的I/O瓶颈问题。

**关键词**：超大规模图像处理, I/O优化, 流式架构, 领域特定语言, 内存管理, 图像分析

## 3 点简述
- 核心问题：处理PB级图像数据时性能受I/O限制，需最小化磁盘访问。
- 方法要点：采用切片流式架构，结合扫描执行和重叠感知分块，减少冗余数据读取。
- 实验或效果：通过DSL自动优化流水线，实现近线性I/O扫描和可预测内存占用，提升吞吐量。

## 摘要（原文）

> This report addresses larger-than-memory image analysis for petascale datasets such as 1.4 PB electron-microscopy volumes and 150 TB human-organ atlases. We argue that performance is fundamentally I/O-bound. We show that structuring analysis as streaming passes over data is crucial. For 3D volumes, two representations are popular: stacks of 2D slices (e.g., directories or multi-page TIFF) and 3D chunked layouts (e.g., Zarr/HDF5). While for a few algorithms, chunked layout on disk is crucial to keep disk I/O at a minimum, we show how the slice-based streaming architecture can be built on top of either image representation in a manner that minimizes disk I/O. This is in particular advantageous for algorithms relying on neighbouring values, since the slicing streaming architecture is 1D, which implies that there are only 2 possible sweeping orders, both of which are aligned with the order in which images are read from the disk. This is in contrast to 3D chunks, in which any sweep cannot be done without accessing each chunk at least 9 times. We formalize this with sweep-based execution (natural 2D/3D orders), windowed operations, and overlap-aware tiling to minimize redundant access. Building on these principles, we introduce a domain-specific language (DSL) that encodes algorithms with intrinsic knowledge of their optimal streaming and memory use; the DSL performs compile-time and run-time pipeline analyses to automatically select window sizes, fuse stages, tee and zip streams, and schedule passes for limited-RAM machines, yielding near-linear I/O scans and predictable memory footprints. The approach integrates with existing tooling for segmentation and morphology but reframes pre/post-processing as pipelines that privilege sequential read/write patterns, delivering substantial throughput gains for extremely large images without requiring full-volume residency in memory.

