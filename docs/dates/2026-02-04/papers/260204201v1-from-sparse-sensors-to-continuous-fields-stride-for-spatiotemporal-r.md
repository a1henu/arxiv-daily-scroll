---
layout: default
title: From Sparse Sensors to Continuous Fields: STRIDE for Spatiotemporal Reconstruction
---

# From Sparse Sensors to Continuous Fields: STRIDE for Spatiotemporal Reconstruction
**arXiv**：[2602.04201v1](https://arxiv.org/abs/2602.04201) · [PDF](https://arxiv.org/pdf/2602.04201.pdf)  
**作者**：Yanjie Tong, Peng Chen  

**一句话要点**：提出STRIDE框架，通过隐式神经表示从稀疏传感器重建连续时空场

**关键词**：时空场重建, 隐式神经表示, 稀疏传感器, 参数PDE, 超分辨率, 噪声鲁棒性

## 3 点简述
- 核心问题：从稀疏点传感器测量重建高维时空场，现有方法泛化性差或依赖网格化解码器。
- 方法要点：两阶段框架，时间编码器映射测量到潜状态，调制隐式神经表示解码器在任意位置重建场。
- 实验或效果：在混沌动力学和波传播基准上优于基线，支持超分辨率，对噪声鲁棒。

## 摘要（原文）

> Reconstructing high-dimensional spatiotemporal fields from sparse point-sensor measurements is a central challenge in learning parametric PDE dynamics. Existing approaches often struggle to generalize across trajectories and parameter settings, or rely on discretization-tied decoders that do not naturally transfer across meshes and resolutions. We propose STRIDE (Spatio-Temporal Recurrent Implicit DEcoder), a two-stage framework that maps a short window of sensor measurements to a latent state with a temporal encoder and reconstructs the field at arbitrary query locations with a modulated implicit neural representation (INR) decoder. Using the Fourier Multi-Component and Multi-Layer Neural Network (FMMNN) as the INR backbone improves representation of complex spatial fields and yields more stable optimization than sine-based INRs. We provide a conditional theoretical justification: under stable delay observability of point measurements on a low-dimensional parametric invariant set, the reconstruction operator factors through a finite-dimensional embedding, making STRIDE-type architectures natural approximators. Experiments on four challenging benchmarks spanning chaotic dynamics and wave propagation show that STRIDE outperforms strong baselines under extremely sparse sensing, supports super-resolution, and remains robust to noise.

