---
layout: default
title: SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors
---

# SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors
**arXiv**：[2602.02000v1](https://arxiv.org/abs/2602.02000) · [PDF](https://arxiv.org/pdf/2602.02000.pdf)  
**作者**：Bing He, Jingnan Gao, Yunuo Chen, Ning Cao, Gang Chen, Zhengxue Cheng, Li Song, Wenjun Zhang  

**一句话要点**：提出SurfSplat框架，基于2D高斯泼溅和表面连续性先验，解决稀疏图像3D重建中的几何不连续问题。

**关键词**：3D场景重建, 高斯泼溅, 表面连续性先验, 稀疏图像输入, 高分辨率评估

## 3 点简述
- 核心问题：现有方法基于3D高斯泼溅重建稀疏图像3D场景时，常产生离散、颜色偏差的点云，几何不连续，近看有严重伪影。
- 方法要点：采用2D高斯泼溅基元增强各向异性和几何精度，结合表面连续性先验和强制alpha混合策略，重建连贯几何与忠实纹理。
- 实验或效果：在RealEstate10K等数据集上，标准指标和新指标HRRC均优于先前方法，实现高保真重建。

## 摘要（原文）

> Reconstructing 3D scenes from sparse images remains a challenging task due to the difficulty of recovering accurate geometry and texture without optimization. Recent approaches leverage generalizable models to generate 3D scenes using 3D Gaussian Splatting (3DGS) primitive. However, they often fail to produce continuous surfaces and instead yield discrete, color-biased point clouds that appear plausible at normal resolution but reveal severe artifacts under close-up views. To address this issue, we present SurfSplat, a feedforward framework based on 2D Gaussian Splatting (2DGS) primitive, which provides stronger anisotropy and higher geometric precision. By incorporating a surface continuity prior and a forced alpha blending strategy, SurfSplat reconstructs coherent geometry together with faithful textures. Furthermore, we introduce High-Resolution Rendering Consistency (HRRC), a new evaluation metric designed to evaluate high-resolution reconstruction quality. Extensive experiments on RealEstate10K, DL3DV, and ScanNet demonstrate that SurfSplat consistently outperforms prior methods on both standard metrics and HRRC, establishing a robust solution for high-fidelity 3D reconstruction from sparse inputs. Project page: https://hebing-sjtu.github.io/SurfSplat-website/

