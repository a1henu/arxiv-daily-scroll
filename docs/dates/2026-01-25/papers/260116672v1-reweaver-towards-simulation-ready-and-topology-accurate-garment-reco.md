---
layout: default
title: ReWeaver: Towards Simulation-Ready and Topology-Accurate Garment Reconstruction
---

# ReWeaver: Towards Simulation-Ready and Topology-Accurate Garment Reconstruction
**arXiv**：[2601.16672v1](https://arxiv.org/abs/2601.16672) · [PDF](https://arxiv.org/pdf/2601.16672.pdf)  
**作者**：Ming Li, Hui Shan, Kai Zheng, Chentao Shen, Siyu Liu, Yanwei Fu, Zhen Chen, Xiangru Huang  

**一句话要点**：提出ReWeaver框架，从稀疏多视角RGB图像重建拓扑准确的3D服装和缝纫图案，以缩小模拟到现实的差距。

**关键词**：3D服装重建, 拓扑准确重建, 缝纫图案预测, 多视角图像处理, 物理模拟准备, 数据集构建

## 3 点简述
- 现有服装重建方法依赖非结构化表示，难以准确重建服装拓扑和缝纫结构，不适合高保真物理模拟。
- ReWeaver从少至四个输入视角预测缝纫线和面板及其连接性，生成对齐图像的2D-3D结构化表示。
- 构建大规模数据集GCD-TS进行训练，实验显示ReWeaver在拓扑准确性、几何对齐和缝纫一致性方面优于现有方法。

## 摘要（原文）

> High-quality 3D garment reconstruction plays a crucial role in mitigating the sim-to-real gap in applications such as digital avatars, virtual try-on and robotic manipulation. However, existing garment reconstruction methods typically rely on unstructured representations, such as 3D Gaussian Splats, struggling to provide accurate reconstructions of garment topology and sewing structures. As a result, the reconstructed outputs are often unsuitable for high-fidelity physical simulation. We propose ReWeaver, a novel framework for topology-accurate 3D garment and sewing pattern reconstruction from sparse multi-view RGB images. Given as few as four input views, ReWeaver predicts seams and panels as well as their connectivities in both the 2D UV space and the 3D space. The predicted seams and panels align precisely with the multi-view images, yielding structured 2D--3D garment representations suitable for 3D perception, high-fidelity physical simulation, and robotic manipulation. To enable effective training, we construct a large-scale dataset GCD-TS, comprising multi-view RGB images, 3D garment geometries, textured human body meshes and annotated sewing patterns. The dataset contains over 100,000 synthetic samples covering a wide range of complex geometries and topologies. Extensive experiments show that ReWeaver consistently outperforms existing methods in terms of topology accuracy, geometry alignment and seam-panel consistency.

