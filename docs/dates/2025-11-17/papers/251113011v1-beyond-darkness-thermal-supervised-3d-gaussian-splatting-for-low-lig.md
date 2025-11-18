---
layout: default
title: Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis
---

# Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis
**arXiv**：[2511.13011v1](https://arxiv.org/abs/2511.13011) · [PDF](https://arxiv.org/pdf/2511.13011.pdf)  
**作者**：Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  

**一句话要点**：提出DTGS框架，结合热监督与Retinex分解，解决极低光下新视角合成的退化问题。

**关键词**：新视角合成, 3D高斯泼溅, 低光增强, 热监督, Retinex分解, 多模态重建

## 3 点简述
- 极低光条件下，新视角合成面临几何、颜色和辐射稳定性严重退化。
- DTGS通过循环增强-重建机制，联合优化增强、几何和热监督。
- 在自建RGBT-LOW数据集上，DTGS在辐射一致性、几何保真和颜色稳定性上显著优于基线。

## 摘要（原文）

> Under extremely low-light conditions, novel view synthesis (NVS) faces severe degradation in terms of geometry, color consistency, and radiometric stability. Standard 3D Gaussian Splatting (3DGS) pipelines fail when applied directly to underexposed inputs, as independent enhancement across views causes illumination inconsistencies and geometric distortion. To address this, we present DTGS, a unified framework that tightly couples Retinex-inspired illumination decomposition with thermal-guided 3D Gaussian Splatting for illumination-invariant reconstruction. Unlike prior approaches that treat enhancement as a pre-processing step, DTGS performs joint optimization across enhancement, geometry, and thermal supervision through a cyclic enhancement-reconstruction mechanism. A thermal supervisory branch stabilizes both color restoration and geometry learning by dynamically balancing enhancement, structural, and thermal losses. Moreover, a Retinex-based decomposition module embedded within the 3DGS loop provides physically interpretable reflectance-illumination separation, ensuring consistent color and texture across viewpoints. To evaluate our method, we construct RGBT-LOW, a new multi-view low-light thermal dataset capturing severe illumination degradation. Extensive experiments show that DTGS significantly outperforms existing low-light enhancement and 3D reconstruction baselines, achieving superior radiometric consistency, geometric fidelity, and color stability under extreme illumination.

