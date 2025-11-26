---
layout: default
title: DOGE: Differentiable Bezier Graph Optimization for Road Network Extraction
---

# DOGE: Differentiable Bezier Graph Optimization for Road Network Extraction
**arXiv**：[2511.19850v1](https://arxiv.org/abs/2511.19850) · [PDF](https://arxiv.org/pdf/2511.19850.pdf)  
**作者**：Jiahui Sun, Junran Lu, Jinhui Yin, Yishuo Xu, Yuanqi Li, Yanwen Guo  

**一句话要点**：提出DOGE框架以从分割掩码直接学习贝塞尔图，优化道路网络提取

**关键词**：道路网络提取, 贝塞尔图优化, 可微分渲染, 拓扑适应, 分割掩码学习, 矢量地图生成

## 3 点简述
- 核心问题：现有方法使用折线难以建模道路的曲线几何，且依赖难以构建的矢量真值
- 方法要点：引入可微分贝塞尔图，通过DiffAlign和TopoAdapt模块交替优化几何与拓扑
- 实验或效果：在SpaceNet和CityScale基准上达到新最优，无需曲线真值生成高保真矢量地图

## 摘要（原文）

> Automatic extraction of road networks from aerial imagery is a fundamental task, yet prevailing methods rely on polylines that struggle to model curvilinear geometry. We maintain that road geometry is inherently curve-based and introduce the Bézier Graph, a differentiable parametric curve-based representation. The primary obstacle to this representation is to obtain the difficult-to-construct vector ground-truth (GT). We sidestep this bottleneck by reframing the task as a global optimization problem over the Bézier Graph. Our framework, DOGE, operationalizes this paradigm by learning a parametric Bézier Graph directly from segmentation masks, eliminating the need for curve GT. DOGE holistically optimizes the graph by alternating between two complementary modules: DiffAlign continuously optimizes geometry via differentiable rendering, while TopoAdapt uses discrete operators to refine its topology. Our method sets a new state-of-the-art on the large-scale SpaceNet and CityScale benchmarks, presenting a new paradigm for generating high-fidelity vector maps of road networks. We will release our code and related data.

