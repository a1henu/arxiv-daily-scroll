---
layout: default
title: PINGS-X: Physics-Informed Normalized Gaussian Splatting with Axes Alignment for Efficient Super-Resolution of 4D Flow MRI
---

# PINGS-X: Physics-Informed Normalized Gaussian Splatting with Axes Alignment for Efficient Super-Resolution of 4D Flow MRI
**arXiv**：[2511.11048v1](https://arxiv.org/abs/2511.11048) · [PDF](https://arxiv.org/pdf/2511.11048.pdf)  
**作者**：Sun Jo, Seok Young Hong, JinHyun Kim, Seungmin Kang, Ahjin Choi, Don-Gwan An, Simon Song, Je Hyeong Hong  

**一句话要点**：提出PINGS-X框架，通过轴对齐高斯表示高效实现4D流MRI超分辨率

**关键词**：4D流MRI超分辨率, 物理信息神经网络, 高斯溅射, 轴对齐表示, 计算流体动力学, 训练效率优化

## 3 点简述
- 4D流MRI高分辨率需求与扫描时间矛盾，限制心血管疾病早期诊断
- 采用归一化高斯溅射和轴对齐高斯，简化训练并保证收敛性
- 实验显示在CFD和真实数据上训练时间减少，超分辨率精度提升

## 摘要（原文）

> 4D flow magnetic resonance imaging (MRI) is a reliable, non-invasive approach for estimating blood flow velocities, vital for cardiovascular diagnostics. Unlike conventional MRI focused on anatomical structures, 4D flow MRI requires high spatiotemporal resolution for early detection of critical conditions such as stenosis or aneurysms. However, achieving such resolution typically results in prolonged scan times, creating a trade-off between acquisition speed and prediction accuracy. Recent studies have leveraged physics-informed neural networks (PINNs) for super-resolution of MRI data, but their practical applicability is limited as the prohibitively slow training process must be performed for each patient. To overcome this limitation, we propose PINGS-X, a novel framework modeling high-resolution flow velocities using axes-aligned spatiotemporal Gaussian representations. Inspired by the effectiveness of 3D Gaussian splatting (3DGS) in novel view synthesis, PINGS-X extends this concept through several non-trivial novel innovations: (i) normalized Gaussian splatting with a formal convergence guarantee, (ii) axes-aligned Gaussians that simplify training for high-dimensional data while preserving accuracy and the convergence guarantee, and (iii) a Gaussian merging procedure to prevent degenerate solutions and boost computational efficiency. Experimental results on computational fluid dynamics (CFD) and real 4D flow MRI datasets demonstrate that PINGS-X substantially reduces training time while achieving superior super-resolution accuracy. Our code and datasets are available at https://github.com/SpatialAILab/PINGS-X.

