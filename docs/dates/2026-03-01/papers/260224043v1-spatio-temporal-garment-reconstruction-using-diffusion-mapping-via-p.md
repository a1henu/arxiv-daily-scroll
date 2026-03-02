---
layout: default
title: Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates
---

# Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates
**arXiv**：[2602.24043v1](https://arxiv.org/abs/2602.24043) · [PDF](https://arxiv.org/pdf/2602.24043.pdf)  
**作者**：Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  

**一句话要点**：提出基于扩散映射与图案坐标的时空服装重建框架，用于单图像和视频的高保真3D服装重建。

**关键词**：3D服装重建, 扩散模型, 时空一致性, UV映射, 单目视觉, 虚拟试穿

## 3 点简述
- 核心问题：从单目图像和视频重建3D服装，特别是宽松服装的几何细节，仍具挑战性。
- 方法要点：结合隐式缝纫图案与生成扩散模型，在UV空间学习形状先验，并通过映射模型关联像素、UV坐标和3D几何。
- 实验或效果：在合成数据训练下，泛化至真实图像，在紧身和宽松服装上优于现有方法，支持纹理编辑和动画应用。

## 摘要（原文）

> Reconstructing 3D clothed humans from monocular images and videos is a fundamental problem with applications in virtual try-on, avatar creation, and mixed reality. Despite significant progress in human body recovery, accurately reconstructing garment geometry, particularly for loose-fitting clothing, remains an open challenge. We propose a unified framework for high-fidelity 3D garment reconstruction from both single images and video sequences. Our approach combines Implicit Sewing Patterns (ISP) with a generative diffusion model to learn expressive garment shape priors in 2D UV space. Leveraging these priors, we introduce a mapping model that establishes correspondences between image pixels, UV pattern coordinates, and 3D geometry, enabling accurate and detailed garment reconstruction from single images. We further extend this formulation to dynamic reconstruction by introducing a spatio-temporal diffusion scheme with test-time guidance to enforce long-range temporal consistency. We also develop analytic projection-based constraints that preserve image-aligned geometry in visible regions while enforcing coherent completion in occluded areas over time. Although trained exclusively on synthetically simulated cloth data, our method generalizes well to real-world imagery and consistently outperforms existing approaches on both tight- and loose-fitting garments. The reconstructed garments preserve fine geometric detail while exhibiting realistic dynamic motion, supporting downstream applications such as texture editing, garment retargeting, and animation.

