---
layout: default
title: GaussianFluent: Gaussian Simulation for Dynamic Scenes with Mixed Materials
---

# GaussianFluent: Gaussian Simulation for Dynamic Scenes with Mixed Materials
**arXiv**：[2601.09265v1](https://arxiv.org/abs/2601.09265) · [PDF](https://arxiv.org/pdf/2601.09265.pdf)  
**作者**：Bei Huang, Yixin Chen, Ruijie Lu, Gang Zeng, Hongbin Zha, Yuru Pei, Siyuan Huang  

**一句话要点**：提出GaussianFluent框架，通过生成内部高斯和优化CD-MPM实现混合材料动态场景的实时仿真与渲染。

**关键词**：3D高斯溅射, 脆性断裂仿真, 混合材料仿真, 实时渲染, 连续损伤材料点法

## 3 点简述
- 核心问题：3D高斯溅射缺乏体积内部纹理和脆性断裂仿真方法，限制动态场景应用。
- 方法要点：利用生成模型合成逼真内部高斯，集成优化CD-MPM实现高速脆性断裂仿真。
- 实验或效果：支持混合材料和多阶段断裂，实现照片级实时渲染，适用于VR和机器人等下游应用。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a prominent 3D representation for high-fidelity and real-time rendering. Prior work has coupled physics simulation with Gaussians, but predominantly targets soft, deformable materials, leaving brittle fracture largely unresolved. This stems from two key obstacles: the lack of volumetric interiors with coherent textures in GS representation, and the absence of fracture-aware simulation methods for Gaussians. To address these challenges, we introduce GaussianFluent, a unified framework for realistic simulation and rendering of dynamic object states. First, it synthesizes photorealistic interiors by densifying internal Gaussians guided by generative models. Second, it integrates an optimized Continuum Damage Material Point Method (CD-MPM) to enable brittle fracture simulation at remarkably high speed. Our approach handles complex scenarios including mixed-material objects and multi-stage fracture propagation, achieving results infeasible with previous methods. Experiments clearly demonstrate GaussianFluent's capability for photo-realistic, real-time rendering with structurally consistent interiors, highlighting its potential for downstream application, such as VR and Robotics.

