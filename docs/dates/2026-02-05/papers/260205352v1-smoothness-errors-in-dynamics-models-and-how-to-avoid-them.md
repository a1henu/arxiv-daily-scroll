---
layout: default
title: Smoothness Errors in Dynamics Models and How to Avoid Them
---

# Smoothness Errors in Dynamics Models and How to Avoid Them
**arXiv**：[2602.05352v1](https://arxiv.org/abs/2602.05352) · [PDF](https://arxiv.org/pdf/2602.05352.pdf)  
**作者**：Edward Berman, Luisa Li, Jung Yeon Park, Robin Walters  

**一句话要点**：提出松弛酉卷积以平衡平滑性，提升动态建模性能

**关键词**：图神经网络, 动态建模, 平滑性误差, 松弛酉卷积, 偏微分方程求解, 天气预报

## 3 点简述
- 核心问题：图神经网络在动态建模中因过度平滑或酉卷积约束过强而性能下降
- 方法要点：引入松弛酉卷积，在保持平滑性与自然平滑需求间取得平衡
- 实验或效果：在热方程、波动方程和天气预报任务中优于基线方法

## 摘要（原文）

> Modern neural networks have shown promise for solving partial differential equations over surfaces, often by discretizing the surface as a mesh and learning with a mesh-aware graph neural network. However, graph neural networks suffer from oversmoothing, where a node's features become increasingly similar to those of its neighbors. Unitary graph convolutions, which are mathematically constrained to preserve smoothness, have been proposed to address this issue. Despite this, in many physical systems, such as diffusion processes, smoothness naturally increases and unitarity may be overconstraining. In this paper, we systematically study the smoothing effects of different GNNs for dynamics modeling and prove that unitary convolutions hurt performance for such tasks. We propose relaxed unitary convolutions that balance smoothness preservation with the natural smoothing required for physical systems. We also generalize unitary and relaxed unitary convolutions from graphs to meshes. In experiments on PDEs such as the heat and wave equations over complex meshes and on weather forecasting, we find that our method outperforms several strong baselines, including mesh-aware transformers and equivariant neural networks.

