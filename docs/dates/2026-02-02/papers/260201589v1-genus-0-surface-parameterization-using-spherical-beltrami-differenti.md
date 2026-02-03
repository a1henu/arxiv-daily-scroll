---
layout: default
title: Genus-0 Surface Parameterization using Spherical Beltrami Differentials
---

# Genus-0 Surface Parameterization using Spherical Beltrami Differentials
**arXiv**：[2602.01589v1](https://arxiv.org/abs/2602.01589) · [PDF](https://arxiv.org/pdf/2602.01589.pdf)  
**作者**：Zhehao Xu, Lok Ming Lui  

**一句话要点**：提出球面Beltrami微分框架BOOST，优化球面自映射以解决任务驱动映射中的失真与双射权衡问题。

**关键词**：球面参数化, Beltrami微分, 神经优化, 几何处理, 脑皮层配准, 双射映射

## 3 点简述
- 核心问题：球面参数化在满足任务目标、保持双射性和控制几何失真间存在权衡。
- 方法要点：引入球面Beltrami微分表示，基于SBN提出神经优化框架BOOST，通过显式接缝约束确保全局一致性。
- 实验或效果：在大变形地标匹配和强度配准中验证有效性，应用于脑皮层配准，提升任务保真度并控制失真。

## 摘要（原文）

> Spherical surface parameterization is a fundamental tool in geometry processing and imaging science. For a genus-0 closed surface, many efficient algorithms can map the surface to the sphere; consequently, a broad class of task-driven genus-0 mapping problems can be reduced to constructing a high-quality spherical self-map. However, existing approaches often face a trade-off between satisfying task objectives (e.g., landmark or feature alignment), maintaining bijectivity, and controlling geometric distortion. We introduce the Spherical Beltrami Differential (SBD), a two-chart representation of quasiconformal self-maps of the sphere, and establish its correspondence with spherical homeomorphisms up to conformal automorphisms. Building on the Spectral Beltrami Network (SBN), we propose a neural optimization framework BOOST that optimizes two Beltrami fields on hemispherical stereographic charts and enforces global consistency through explicit seam-aware constraints. Experiments on large-deformation landmark matching and intensity-based spherical registration demonstrate the effectiveness of our proposed framework. We further apply the method to brain cortical surface registration, aligning sulcal landmarks and jointly matching cortical sulci depth maps, showing improved task fidelity with controlled distortion and robust bijective behavior.

