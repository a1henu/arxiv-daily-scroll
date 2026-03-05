---
layout: default
title: mlx-vis: GPU-Accelerated Dimensionality Reduction and Visualization on Apple Silicon
---

# mlx-vis: GPU-Accelerated Dimensionality Reduction and Visualization on Apple Silicon
**arXiv**：[2603.04035v1](https://arxiv.org/abs/2603.04035) · [PDF](https://arxiv.org/pdf/2603.04035.pdf)  
**作者**：Han Xiao  

**一句话要点**：提出mlx-vis库，在Apple Silicon上实现GPU加速的降维与可视化

**关键词**：降维算法, GPU加速, Apple Silicon, 可视化渲染, MLX框架

## 3 点简述
- 核心问题：在Apple Silicon上高效执行降维和可视化，依赖MLX框架。
- 方法要点：集成六种降维算法和k近邻图算法，通过fit_transform接口在Metal GPU上运行。
- 实验或效果：在Fashion-MNIST数据集上，嵌入计算2.1-3.8秒，渲染动画1.4秒，全流程3.6-5.2秒完成。

## 摘要（原文）

> mlx-vis is a Python library that implements six dimensionality reduction methods and a k-nearest neighbor graph algorithm entirely in MLX, Apple's array framework for Apple Silicon. The library provides UMAP, t-SNE, PaCMAP, TriMap, DREAMS, CNE, and NNDescent, all executing on Metal GPU through a unified fit_transform interface. Beyond embedding computation, mlx-vis includes a GPU-accelerated circle-splatting renderer that produces scatter plots and smooth animations without matplotlib, composing frames via scatter-add alpha blending on GPU and piping them to hardware H.264 encoding. On Fashion-MNIST with 70,000 points, all methods complete embedding in 2.1-3.8 seconds and render 800-frame animations in 1.4 seconds on an M3 Ultra, with the full pipeline from raw data to rendered video finishing in 3.6-5.2 seconds. The library depends only on MLX and NumPy, is released under the Apache 2.0 license, and is available at https://github.com/hanxiao/mlx-vis.

