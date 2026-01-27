---
layout: default
title: PPISP: Physically-Plausible Compensation and Control of Photometric Variations in Radiance Field Reconstruction
---

# PPISP: Physically-Plausible Compensation and Control of Photometric Variations in Radiance Field Reconstruction
**arXiv**：[2601.18336v1](https://arxiv.org/abs/2601.18336) · [PDF](https://arxiv.org/pdf/2601.18336.pdf)  
**作者**：Isaac Deutsch, Nicolas Moënne-Loccoz, Gavriel State, Zan Gojcic  

**一句话要点**：提出PPISP模块以解决多视图重建中相机光学和ISP变化导致的色彩不一致问题

**关键词**：多视图重建, 辐射场重建, 图像信号处理, 物理可解释模型, 新视角合成, 色彩校正

## 3 点简述
- 核心问题：多视图3D重建对相机光学特性和图像信号处理变化敏感，现有方法缺乏物理基础且泛化性差
- 方法要点：通过物理可解释变换分离相机固有和捕获依赖效应，训练控制器预测新视角ISP参数
- 实验或效果：在标准基准测试中达到最先进性能，支持无真实图像的新视角评估和元数据集成

## 摘要（原文）

> Multi-view 3D reconstruction methods remain highly sensitive to photometric inconsistencies arising from camera optical characteristics and variations in image signal processing (ISP). Existing mitigation strategies such as per-frame latent variables or affine color corrections lack physical grounding and generalize poorly to novel views. We propose the Physically-Plausible ISP (PPISP) correction module, which disentangles camera-intrinsic and capture-dependent effects through physically based and interpretable transformations. A dedicated PPISP controller, trained on the input views, predicts ISP parameters for novel viewpoints, analogous to auto exposure and auto white balance in real cameras. This design enables realistic and fair evaluation on novel views without access to ground-truth images. PPISP achieves SoTA performance on standard benchmarks, while providing intuitive control and supporting the integration of metadata when available. The source code is available at: https://github.com/nv-tlabs/ppisp

