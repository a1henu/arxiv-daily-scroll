---
layout: default
title: LARM: A Large Articulated-Object Reconstruction Model
---

# LARM: A Large Articulated-Object Reconstruction Model
**arXiv**：[2511.11563v1](https://arxiv.org/abs/2511.11563) · [PDF](https://arxiv.org/pdf/2511.11563.pdf)  
**作者**：Sylvia Yuan, Ruoxi Shi, Xinyue Wei, Xiaoshuai Zhang, Hao Su, Minghua Liu  

**一句话要点**：提出LARM模型，从稀疏视图图像重建3D铰接对象，联合恢复几何、纹理和关节结构。

**关键词**：3D铰接对象重建, 稀疏视图重建, transformer架构, 新视图合成, 关节估计

## 3 点简述
- 现有方法需密集多视图输入和逐实例优化，或前馈方法几何粗糙、缺乏纹理。
- LARM扩展LVSM，使用transformer联合推理相机位姿和铰接变化，实现统一前馈重建。
- 实验显示LARM在新视图合成和3D重建上优于先进方法，生成高质量网格。

## 摘要（原文）

> Modeling 3D articulated objects with realistic geometry, textures, and kinematics is essential for a wide range of applications. However, existing optimization-based reconstruction methods often require dense multi-view inputs and expensive per-instance optimization, limiting their scalability. Recent feedforward approaches offer faster alternatives but frequently produce coarse geometry, lack texture reconstruction, and rely on brittle, complex multi-stage pipelines. We introduce LARM, a unified feedforward framework that reconstructs 3D articulated objects from sparse-view images by jointly recovering detailed geometry, realistic textures, and accurate joint structures. LARM extends LVSM a recent novel view synthesis (NVS) approach for static 3D objects into the articulated setting by jointly reasoning over camera pose and articulation variation using a transformer-based architecture, enabling scalable and accurate novel view synthesis. In addition, LARM generates auxiliary outputs such as depth maps and part masks to facilitate explicit 3D mesh extraction and joint estimation. Our pipeline eliminates the need for dense supervision and supports high-fidelity reconstruction across diverse object categories. Extensive experiments demonstrate that LARM outperforms state-of-the-art methods in both novel view and state synthesis as well as 3D articulated object reconstruction, generating high-quality meshes that closely adhere to the input images. project page: https://sylviayuan-sy.github.io/larm-site/

