---
layout: default
title: GenDA: Generative Data Assimilation on Complex Urban Areas via Classifier-Free Diffusion Guidance
---

# GenDA: Generative Data Assimilation on Complex Urban Areas via Classifier-Free Diffusion Guidance
**arXiv**：[2601.11440v1](https://arxiv.org/abs/2601.11440) · [PDF](https://arxiv.org/pdf/2601.11440.pdf)  
**作者**：Francisco Giral, Álvaro Manzano, Ignacio Gómez, Ricardo Vinuesa, Soledad Le Clainche  

**一句话要点**：提出GenDA框架，通过无分类器扩散引导实现复杂城市区域的风场高分辨率重建

**关键词**：生成式数据同化, 风场重建, 扩散模型, 图神经网络, 城市流体动力学, 稀疏观测

## 3 点简述
- 核心问题：城市风场重建在稀疏传感器数据下具有挑战性，影响空气质量评估和行人舒适度分析。
- 方法要点：采用多尺度图扩散架构，结合几何感知先验和传感器条件分支，实现障碍物感知重建和跨未见几何的泛化。
- 实验或效果：在真实城市邻域RANS模拟中，相比基线方法，RRMSE降低25-57%，SSIM提高23-33%。

## 摘要（原文）

> Urban wind flow reconstruction is essential for assessing air quality, heat dispersion, and pedestrian comfort, yet remains challenging when only sparse sensor data are available. We propose GenDA, a generative data assimilation framework that reconstructs high-resolution wind fields on unstructured meshes from limited observations. The model employs a multiscale graph-based diffusion architecture trained on computational fluid dynamics (CFD) simulations and interprets classifier-free guidance as a learned posterior reconstruction mechanism: the unconditional branch learns a geometry-aware flow prior, while the sensor-conditioned branch injects observational constraints during sampling. This formulation enables obstacle-aware reconstruction and generalization across unseen geometries, wind directions, and mesh resolutions without retraining. We consider both sparse fixed sensors and trajectory-based observations using the same reconstruction procedure. When evaluated against supervised graph neural network (GNN) baselines and classical reduced-order data assimilation methods, GenDA reduces the relative root-mean-square error (RRMSE) by 25-57% and increases the structural similarity index (SSIM) by 23-33% across the tested meshes. Experiments are conducted on Reynolds-averaged Navier-Stokes (RANS) simulations of a real urban neighbourhood in Bristol, United Kingdom, at a characteristic Reynolds number of $\mathrm{Re}\approx2\times10^{7}$, featuring complex building geometry and irregular terrain. The proposed framework provides a scalable path toward generative, geometry-aware data assimilation for environmental monitoring in complex domains.

