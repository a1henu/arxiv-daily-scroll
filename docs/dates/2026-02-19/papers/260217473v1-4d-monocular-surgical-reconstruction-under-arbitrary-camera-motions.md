---
layout: default
title: 4D Monocular Surgical Reconstruction under Arbitrary Camera Motions
---

# 4D Monocular Surgical Reconstruction under Arbitrary Camera Motions
**arXiv**：[2602.17473v1](https://arxiv.org/abs/2602.17473) · [PDF](https://arxiv.org/pdf/2602.17473.pdf)  
**作者**：Jiwei Shan, Zeyu Cai, Cheng-Tai Hsieh, Yirui Li, Hao Liu, Lijun Han, Hesheng Wang, Shing Shin Cheng  

**一句话要点**：提出Local-EndoGS框架，用于单目内窥镜视频在任意相机运动下的高质量4D重建。

**关键词**：4D重建, 单目内窥镜, 相机运动, 变形场景, 高斯溅射, 多视图几何

## 3 点简述
- 核心问题：现有方法依赖固定视角或深度先验，难以处理单目序列中的大相机运动。
- 方法要点：采用渐进式窗口全局表示，结合粗到细策略和物理先验，提升重建鲁棒性。
- 实验或效果：在三个公开数据集上，外观和几何质量均优于现有方法，消融实验验证关键设计。

## 摘要（原文）

> Reconstructing deformable surgical scenes from endoscopic videos is challenging and clinically important. Recent state-of-the-art methods based on implicit neural representations or 3D Gaussian splatting have made notable progress. However, most are designed for deformable scenes with fixed endoscope viewpoints and rely on stereo depth priors or accurate structure-from-motion for initialization and optimization, limiting their ability to handle monocular sequences with large camera motion in real clinical settings. To address this, we propose Local-EndoGS, a high-quality 4D reconstruction framework for monocular endoscopic sequences with arbitrary camera motion. Local-EndoGS introduces a progressive, window-based global representation that allocates local deformable scene models to each observed window, enabling scalability to long sequences with substantial motion. To overcome unreliable initialization without stereo depth or accurate structure-from-motion, we design a coarse-to-fine strategy integrating multi-view geometry, cross-window information, and monocular depth priors, providing a robust foundation for optimization. We further incorporate long-range 2D pixel trajectory constraints and physical motion priors to improve deformation plausibility. Experiments on three public endoscopic datasets with deformable scenes and varying camera motions show that Local-EndoGS consistently outperforms state-of-the-art methods in appearance quality and geometry. Ablation studies validate the effectiveness of our key designs. Code will be released upon acceptance at: https://github.com/IRMVLab/Local-EndoGS.

