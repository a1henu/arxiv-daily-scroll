---
layout: default
title: PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes
---

# PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes
**arXiv**：[2512.02664v1](https://arxiv.org/abs/2512.02664) · [PDF](https://arxiv.org/pdf/2512.02664.pdf)  
**作者**：Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  

**一句话要点**：提出PolarGuide-GSDR，利用偏振先验与延迟反射解决真实反射场景的3D高斯溅射重建问题。

**关键词**：偏振引导重建, 3D高斯溅射, 反射分离, 实时渲染, 法线估计, 新视角合成

## 3 点简述
- 核心问题：现有方法在反射场景中训练慢、渲染效率低，且依赖材料/视角假设。
- 方法要点：建立偏振与3D高斯溅射的双向耦合机制，先解偏振模糊，再引导法线和球谐表示。
- 实验或效果：在公开和自采数据集上实现高保真反射分离和全场景重建，保持实时渲染性能。

## 摘要（原文）

> Polarization-aware Neural Radiance Fields (NeRF) enable novel view synthesis of specular-reflection scenes but face challenges in slow training, inefficient rendering, and strong dependencies on material/viewpoint assumptions. However, 3D Gaussian Splatting (3DGS) enables real-time rendering yet struggles with accurate reflection reconstruction from reflection-geometry entanglement, adding a deferred reflection module introduces environment map dependence. We address these limitations by proposing PolarGuide-GSDR, a polarization-forward-guided paradigm establishing a bidirectional coupling mechanism between polarization and 3DGS: first 3DGS's geometric priors are leveraged to resolve polarization ambiguity, and then the refined polarization information cues are used to guide 3DGS's normal and spherical harmonic representation. This process achieves high-fidelity reflection separation and full-scene reconstruction without requiring environment maps or restrictive material assumptions. We demonstrate on public and self-collected datasets that PolarGuide-GSDR achieves state-of-the-art performance in specular reconstruction, normal estimation, and novel view synthesis, all while maintaining real-time rendering capabilities. To our knowledge, this is the first framework embedding polarization priors directly into 3DGS optimization, yielding superior interpretability and real-time performance for modeling complex reflective scenes.

