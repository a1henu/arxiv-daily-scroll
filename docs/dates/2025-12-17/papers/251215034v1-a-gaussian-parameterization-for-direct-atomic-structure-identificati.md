---
layout: default
title: A Gaussian Parameterization for Direct Atomic Structure Identification in Electron Tomography
---

# A Gaussian Parameterization for Direct Atomic Structure Identification in Electron Tomography
**arXiv**：[2512.15034v1](https://arxiv.org/abs/2512.15034) · [PDF](https://arxiv.org/pdf/2512.15034.pdf)  
**作者**：Nalini M. Singh, Tiffany Chien, Arthur R. C. McCray, Colin Ophus, Laura Waller  

**一句话要点**：提出高斯参数化方法，直接求解原子位置以改进电子断层扫描中的结构识别

**关键词**：原子电子断层扫描, 高斯参数化, 直接结构识别, 材料表征, 透射电子显微镜

## 3 点简述
- 核心问题：传统原子电子断层扫描需先重建体积再后处理，易受成像伪影影响。
- 方法要点：将原子结构参数化为高斯函数集合，直接学习原子位置和属性，引入物理先验。
- 实验或效果：模拟和实验数据验证方法对伪影的鲁棒性，适用于材料表征与分析。

## 摘要（原文）

> Atomic electron tomography (AET) enables the determination of 3D atomic structures by acquiring a sequence of 2D tomographic projection measurements of a particle and then computationally solving for its underlying 3D representation. Classical tomography algorithms solve for an intermediate volumetric representation that is post-processed into the atomic structure of interest. In this paper, we reformulate the tomographic inverse problem to solve directly for the locations and properties of individual atoms. We parameterize an atomic structure as a collection of Gaussians, whose positions and properties are learnable. This representation imparts a strong physical prior on the learned structure, which we show yields improved robustness to real-world imaging artifacts. Simulated experiments and a proof-of-concept result on experimentally-acquired data confirm our method's potential for practical applications in materials characterization and analysis with Transmission Electron Microscopy (TEM). Our code is available at https://github.com/nalinimsingh/gaussian-atoms.

