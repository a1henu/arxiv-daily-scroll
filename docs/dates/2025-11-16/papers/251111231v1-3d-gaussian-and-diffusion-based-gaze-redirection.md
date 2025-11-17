---
layout: default
title: 3D Gaussian and Diffusion-Based Gaze Redirection
---

# 3D Gaussian and Diffusion-Based Gaze Redirection
**arXiv**：[2511.11231v1](https://arxiv.org/abs/2511.11231) · [PDF](https://arxiv.org/pdf/2511.11231.pdf)  
**作者**：Abiram Panchalingam, Indu Bodala, Stuart Middleton  

**一句话要点**：提出DiT-Gaze框架以增强3D视线重定向的保真度和准确性

**关键词**：视线重定向, 扩散变换器, 3D高斯溅射, 弱监督学习, 正交约束损失, 合成数据生成

## 3 点简述
- 核心问题：现有3D高斯溅射模型在渲染细微连续视线转移时存在困难
- 方法要点：结合扩散变换器、弱监督策略和正交约束损失提升合成质量
- 实验或效果：在感知质量和重定向精度上达到新SOTA，误差降低至6.353度

## 摘要（原文）

> High-fidelity gaze redirection is critical for generating augmented data to improve the generalization of gaze estimators. 3D Gaussian Splatting (3DGS) models like GazeGaussian represent the state-of-the-art but can struggle with rendering subtle, continuous gaze shifts. In this paper, we propose DiT-Gaze, a framework that enhances 3D gaze redirection models using a novel combination of Diffusion Transformer (DiT), weak supervision across gaze angles, and an orthogonality constraint loss. DiT allows higher-fidelity image synthesis, while our weak supervision strategy using synthetically generated intermediate gaze angles provides a smooth manifold of gaze directions during training. The orthogonality constraint loss mathematically enforces the disentanglement of internal representations for gaze, head pose, and expression. Comprehensive experiments show that DiT-Gaze sets a new state-of-the-art in both perceptual quality and redirection accuracy, reducing the state-of-the-art gaze error by 4.1% to 6.353 degrees, providing a superior method for creating synthetic training data. Our code and models will be made available for the research community to benchmark against.

