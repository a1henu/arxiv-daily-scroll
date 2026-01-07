---
layout: default
title: Robust Mesh Saliency GT Acquisition in VR via View Cone Sampling and Geometric Smoothing
---

# Robust Mesh Saliency GT Acquisition in VR via View Cone Sampling and Geometric Smoothing
**arXiv**：[2601.02721v1](https://arxiv.org/abs/2601.02721) · [PDF](https://arxiv.org/pdf/2601.02721.pdf)  
**作者**：Guoquan Zheng, Jie Hao, Huiyu Duan, Yongming Han, Liang Yuan, Dong Zhang, Guangtao Zhai  

**一句话要点**：提出基于视锥采样和几何平滑的鲁棒框架，以解决VR中3D网格显著性GT获取的拓扑不一致问题。

**关键词**：3D网格显著性, 虚拟现实, 视锥采样, 几何平滑, 流形约束, 眼动追踪

## 3 点简述
- 核心问题：现有VR眼动追踪方法依赖单射线采样和欧氏平滑，导致纹理注意力和信号泄漏，忽略3D几何拓扑差异。
- 方法要点：引入视锥采样模拟人眼中央凹感受野，并开发混合流形-欧氏约束扩散算法，融合流形测地约束以确保拓扑一致的显著性传播。
- 实验或效果：框架通过减轻“拓扑短路”和混叠，提供高保真3D注意力获取范式，为3D网格显著性研究提供更准确鲁棒的基线。

## 摘要（原文）

> Reliable 3D mesh saliency ground truth (GT) is essential for human-centric visual modeling in virtual reality (VR). However, current 3D mesh saliency GT acquisition methods are generally consistent with 2D image methods, ignoring the differences between 3D geometry topology and 2D image array. Current VR eye-tracking pipelines rely on single ray sampling and Euclidean smoothing, triggering texture attention and signal leakage across gaps. This paper proposes a robust framework to address these limitations. We first introduce a view cone sampling (VCS) strategy, which simulates the human foveal receptive field via Gaussian-distributed ray bundles to improve sampling robustness for complex topologies. Furthermore, a hybrid Manifold-Euclidean constrained diffusion (HCD) algorithm is developed, fusing manifold geodesic constraints with Euclidean scales to ensure topologically-consistent saliency propagation. By mitigating "topological short-circuits" and aliasing, our framework provides a high-fidelity 3D attention acquisition paradigm that aligns with natural human perception, offering a more accurate and robust baseline for 3D mesh saliency research.

