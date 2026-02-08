---
layout: default
title: Smoothness Errors in Dynamics Models and How to Avoid Them
---

# Smoothness Errors in Dynamics Models and How to Avoid Them
**arXiv**：[2602.05352v1](https://arxiv.org/abs/2602.05352) · [PDF](https://arxiv.org/pdf/2602.05352.pdf)  
**作者**：Edward Berman, Luisa Li, Jung Yeon Park, Robin Walters  

**一句话要点**：提出松弛酉卷积以平衡平滑度，提升物理系统动态建模性能

**关键词**：图神经网络, 偏微分方程, 动态建模, 平滑度误差, 酉卷积, 网格学习

## 3 点简述
- 核心问题：图神经网络在表面PDE建模中因过度平滑而性能受限，酉卷积可能过度约束自然平滑过程
- 方法要点：系统研究GNN平滑效应，证明酉卷积有害，提出松弛酉卷积并推广至网格
- 实验或效果：在热方程、波动方程和天气预报任务中，优于网格感知Transformer和等变神经网络等基线

## 摘要（原文）

> Modern neural networks have shown promise for solving partial differential equations over surfaces, often by discretizing the surface as a mesh and learning with a mesh-aware graph neural network. However, graph neural networks suffer from oversmoothing, where a node's features become increasingly similar to those of its neighbors. Unitary graph convolutions, which are mathematically constrained to preserve smoothness, have been proposed to address this issue. Despite this, in many physical systems, such as diffusion processes, smoothness naturally increases and unitarity may be overconstraining. In this paper, we systematically study the smoothing effects of different GNNs for dynamics modeling and prove that unitary convolutions hurt performance for such tasks. We propose relaxed unitary convolutions that balance smoothness preservation with the natural smoothing required for physical systems. We also generalize unitary and relaxed unitary convolutions from graphs to meshes. In experiments on PDEs such as the heat and wave equations over complex meshes and on weather forecasting, we find that our method outperforms several strong baselines, including mesh-aware transformers and equivariant neural networks.

