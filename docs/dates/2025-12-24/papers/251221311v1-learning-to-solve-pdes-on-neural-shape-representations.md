---
layout: default
title: Learning to Solve PDEs on Neural Shape Representations
---

# Learning to Solve PDEs on Neural Shape Representations
**arXiv**：[2512.21311v1](https://arxiv.org/abs/2512.21311) · [PDF](https://arxiv.org/pdf/2512.21311.pdf)  
**作者**：Lilian Welschinger, Yilin Liu, Zican Wang, Niloy Mitra  

**一句话要点**：提出基于神经形状表示的局部更新算子以直接求解表面偏微分方程

**关键词**：神经形状表示, 表面偏微分方程求解, 无网格方法, 局部更新算子, 端到端工作流

## 3 点简述
- 核心问题：传统PDE求解器依赖网格，与神经形状表示不匹配，阻碍端到端工作流
- 方法要点：设计无网格方法，学习基于局部形状属性的更新算子，实现直接求解
- 实验或效果：在基准测试和真实神经资产上表现接近有限元法，支持跨形状泛化

## 摘要（原文）

> Solving partial differential equations (PDEs) on shapes underpins many shape analysis and engineering tasks; yet, prevailing PDE solvers operate on polygonal/triangle meshes while modern 3D assets increasingly live as neural representations. This mismatch leaves no suitable method to solve surface PDEs directly within the neural domain, forcing explicit mesh extraction or per-instance residual training, preventing end-to-end workflows. We present a novel, mesh-free formulation that learns a local update operator conditioned on neural (local) shape attributes, enabling surface PDEs to be solved directly where the (neural) data lives. The operator integrates naturally with prevalent neural surface representations, is trained once on a single representative shape, and generalizes across shape and topology variations, enabling accurate, fast inference without explicit meshing or per-instance optimization while preserving differentiability. Across analytic benchmarks (heat equation and Poisson solve on sphere) and real neural assets across different representations, our method slightly outperforms CPM while remaining reasonably close to FEM, and, to our knowledge, delivers the first end-to-end pipeline that solves surface PDEs on both neural and classical surface representations. Code will be released on acceptance.

