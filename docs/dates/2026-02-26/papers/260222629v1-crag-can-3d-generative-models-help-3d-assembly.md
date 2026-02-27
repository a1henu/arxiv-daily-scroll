---
layout: default
title: CRAG: Can 3D Generative Models Help 3D Assembly?
---

# CRAG: Can 3D Generative Models Help 3D Assembly?
**arXiv**：[2602.22629v1](https://arxiv.org/abs/2602.22629) · [PDF](https://arxiv.org/pdf/2602.22629.pdf)  
**作者**：Zeyu Jiang, Sihang Li, Siqi Tan, Chenyang Xu, Juexiao Zhang, Julia Galway-Witham, Xue Wang, Scott A. Williams, Radu Iovita, Chen Feng, Jing Zhang  

**一句话要点**：提出CRAG方法，通过联合装配与生成解决3D物体组装问题

**关键词**：3D组装, 生成模型, 结构推理, 形状补全, 姿态估计

## 3 点简述
- 核心问题：现有3D组装方法仅依赖刚性变换，无法处理缺失几何部分
- 方法要点：将组装与生成结合，利用结构先验和整体形状上下文相互增强
- 实验或效果：在多样几何、不同部件数和缺失部件场景中实现先进性能

## 摘要（原文）

> Most existing 3D assembly methods treat the problem as pure pose estimation, rearranging observed parts via rigid transformations. In contrast, human assembly naturally couples structural reasoning with holistic shape inference. Inspired by this intuition, we reformulate 3D assembly as a joint problem of assembly and generation. We show that these two processes are mutually reinforcing: assembly provides part-level structural priors for generation, while generation injects holistic shape context that resolves ambiguities in assembly. Unlike prior methods that cannot synthesize missing geometry, we propose CRAG, which simultaneously generates plausible complete shapes and predicts poses for input parts. Extensive experiments demonstrate state-of-the-art performance across in-the-wild objects with diverse geometries, varying part counts, and missing pieces. Our code and models will be released.

