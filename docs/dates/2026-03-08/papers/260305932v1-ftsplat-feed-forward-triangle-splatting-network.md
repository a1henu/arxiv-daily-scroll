---
layout: default
title: FTSplat: Feed-forward Triangle Splatting Network
---

# FTSplat: Feed-forward Triangle Splatting Network
**arXiv**：[2603.05932v1](https://arxiv.org/abs/2603.05932) · [PDF](https://arxiv.org/pdf/2603.05932.pdf)  
**作者**：Xiong Jinlin, Li Can, Shen Jiawei, Qi Zhigang, Sun Lei, Zhao Dongyang  

**一句话要点**：提出前馈三角形生成框架，从多视图图像直接预测连续三角形表面，实现高效三维重建与模拟兼容。

**关键词**：三维重建, 三角形生成, 前馈网络, 多视图图像, 模拟兼容, 几何学习

## 3 点简述
- 核心问题：现有方法如NeRF和3DGS依赖逐场景优化，效率低且缺乏显式几何，限制实时部署与模拟应用。
- 方法要点：设计像素对齐三角形生成模块，结合相对三维点云监督，前馈预测连续三角形表面，无需优化或后处理。
- 实验或效果：实验表明方法高效重建，保持与标准图形和机器人模拟器的无缝兼容，提升几何学习稳定性。

## 摘要（原文）

> High-fidelity three-dimensional (3D) reconstruction is essential for robotics and simulation. While Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) achieve impressive rendering quality, their reliance on time-consuming per-scene optimization limits real-time deployment. Emerging feed-forward Gaussian splatting methods improve efficiency but often lack explicit, manifold geometry required for direct simulation. To address these limitations, we propose a feed-forward framework for triangle primitive generation that directly predicts continuous triangle surfaces from calibrated multi-view images. Our method produces simulation-ready models in a single forward pass, obviating the need for per-scene optimization or post-processing. We introduce a pixel-aligned triangle generation module and incorporate relative 3D point cloud supervision to enhance geometric learning stability and consistency. Experiments demonstrate that our method achieves efficient reconstruction while maintaining seamless compatibility with standard graphics and robotic simulators.

