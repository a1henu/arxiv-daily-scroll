---
layout: default
title: GR-Diffusion: 3D Gaussian Representation Meets Diffusion in Whole-Body PET Reconstruction
---

# GR-Diffusion: 3D Gaussian Representation Meets Diffusion in Whole-Body PET Reconstruction
**arXiv**：[2602.11653v1](https://arxiv.org/abs/2602.11653) · [PDF](https://arxiv.org/pdf/2602.11653.pdf)  
**作者**：Mengxiao Geng, Zijie Chen, Ran Hong, Bingxuan Li, Qiegen Liu  

**一句话要点**：提出GR-Diffusion框架，结合3D高斯表示与扩散模型以提升低剂量全身PET重建质量

**关键词**：PET重建, 3D高斯表示, 扩散模型, 低剂量成像, 全身扫描, 分层引导

## 3 点简述
- 核心问题：PET重建因稀疏采样和逆问题病态性导致噪声放大、结构模糊和细节丢失
- 方法要点：利用3D高斯表示生成参考图像，通过分层引导机制在扩散过程中整合几何先验
- 实验或效果：在UDPET和临床数据集上优于现有方法，增强图像质量并保留生理细节

## 摘要（原文）

> Positron emission tomography (PET) reconstruction is a critical challenge in molecular imaging, often hampered by noise amplification, structural blurring, and detail loss due to sparse sampling and the ill-posed nature of inverse problems. The three-dimensional discrete Gaussian representation (GR), which efficiently encodes 3D scenes using parameterized discrete Gaussian distributions, has shown promise in computer vision. In this work, we pro-pose a novel GR-Diffusion framework that synergistically integrates the geometric priors of GR with the generative power of diffusion models for 3D low-dose whole-body PET reconstruction. GR-Diffusion employs GR to generate a reference 3D PET image from projection data, establishing a physically grounded and structurally explicit benchmark that overcomes the low-pass limitations of conventional point-based or voxel-based methods. This reference image serves as a dual guide during the diffusion process, ensuring both global consistency and local accuracy. Specifically, we employ a hierarchical guidance mechanism based on the GR reference. Fine-grained guidance leverages differences to refine local details, while coarse-grained guidance uses multi-scale difference maps to correct deviations. This strategy allows the diffusion model to sequentially integrate the strong geometric prior from GR and recover sub-voxel information. Experimental results on the UDPET and Clinical datasets with varying dose levels show that GR-Diffusion outperforms state-of-the-art methods in enhancing 3D whole-body PET image quality and preserving physiological details.

