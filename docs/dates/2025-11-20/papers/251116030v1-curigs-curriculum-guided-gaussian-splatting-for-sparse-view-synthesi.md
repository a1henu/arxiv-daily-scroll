---
layout: default
title: CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis
---

# CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis
**arXiv**：[2511.16030v1](https://arxiv.org/abs/2511.16030) · [PDF](https://arxiv.org/pdf/2511.16030.pdf)  
**作者**：Zijian Wu, Mingfeng Jiang, Zidian Lin, Ying Song, Hanjie Ma, Qun Wu, Dongping Zhang, Guiyang Pu  

**一句话要点**：提出课程引导高斯泼溅框架以解决稀疏视图合成中的过拟合问题

**关键词**：稀疏视图合成, 3D高斯泼溅, 课程学习, 学生视图生成, 多信号评估, 深度相关正则化

## 3 点简述
- 核心问题：稀疏视图下3D高斯泼溅因监督不足和视角覆盖有限易过拟合
- 方法要点：通过学生视图生成和课程调度逐步增强训练，结合深度相关与多信号评估
- 实验或效果：在合成和真实稀疏场景中渲染保真度和几何一致性优于现有方法

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has recently emerged as an efficient, high-fidelity representation for real-time scene reconstruction and rendering. However, extending 3DGS to sparse-view settings remains challenging because of supervision scarcity and overfitting caused by limited viewpoint coverage. In this paper, we present CuriGS, a curriculum-guided framework for sparse-view 3D reconstruction using 3DGS. CuriGS addresses the core challenge of sparse-view synthesis by introducing student views: pseudo-views sampled around ground-truth poses (teacher). For each teacher, we generate multiple groups of student views with different perturbation levels. During training, we follow a curriculum schedule that gradually unlocks higher perturbation level, randomly sampling candidate students from the active level to assist training. Each sampled student is regularized via depth-correlation and co-regularization, and evaluated using a multi-signal metric that combines SSIM, LPIPS, and an image-quality measure. For every teacher and perturbation level, we periodically retain the best-performing students and promote those that satisfy a predefined quality threshold to the training set, resulting in a stable augmentation of sparse training views. Experimental results show that CuriGS outperforms state-of-the-art baselines in both rendering fidelity and geometric consistency across various synthetic and real sparse-view scenes. Project page: https://zijian1026.github.io/CuriGS/

