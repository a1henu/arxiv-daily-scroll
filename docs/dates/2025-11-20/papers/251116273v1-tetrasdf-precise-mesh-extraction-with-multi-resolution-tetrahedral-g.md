---
layout: default
title: TetraSDF: Precise Mesh Extraction with Multi-resolution Tetrahedral Grid
---

# TetraSDF: Precise Mesh Extraction with Multi-resolution Tetrahedral Grid
**arXiv**：[2511.16273v1](https://arxiv.org/abs/2511.16273) · [PDF](https://arxiv.org/pdf/2511.16273.pdf)  
**作者**：Seonghun Oh, Youngjung Uh, Jin-Hwa Kim  

**一句话要点**：提出TetraSDF框架以精确提取神经SDF的网格

**关键词**：神经符号距离函数, 网格提取, 四面体网格, 解析方法, 多分辨率编码

## 3 点简述
- 神经SDF网格提取存在离散化误差或仅适用于简单MLP的问题
- 使用多分辨率四面体位置编码和固定分析输入预处理器实现精确解析提取
- 在多个基准测试中，SDF重建精度高，网格自一致性强，运行效率实用

## 摘要（原文）

> Extracting meshes that exactly match the zero-level set of neural signed distance functions (SDFs) remains challenging. Sampling-based methods introduce discretization error, while continuous piecewise affine (CPWA) analytic approaches apply only to plain ReLU MLPs. We present TetraSDF, a precise analytic meshing framework for SDFs represented by a ReLU MLP composed with a multi-resolution tetrahedral positional encoder. The encoder's barycentric interpolation preserves global CPWA structure, enabling us to track ReLU linear regions within an encoder-induced polyhedral complex. A fixed analytic input preconditioner derived from the encoder's metric further reduces directional bias and stabilizes training. Across multiple benchmarks, TetraSDF matches or surpasses existing grid-based encoders in SDF reconstruction accuracy, and its analytic extractor produces highly self-consistent meshes that remain faithful to the learned isosurfaces, all with practical runtime and memory efficiency.

