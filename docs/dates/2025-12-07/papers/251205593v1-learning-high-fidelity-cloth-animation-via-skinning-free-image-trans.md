---
layout: default
title: Learning High-Fidelity Cloth Animation via Skinning-Free Image Transfer
---

# Learning High-Fidelity Cloth Animation via Skinning-Free Image Transfer
**arXiv**：[2512.05593v1](https://arxiv.org/abs/2512.05593) · [PDF](https://arxiv.org/pdf/2512.05593.pdf)  
**作者**：Rong Wang, Wei Mao, Changsheng Lu, Hongdong Li  

**一句话要点**：提出免蒙皮图像转移方法以生成高保真3D服装动画

**关键词**：3D服装动画, 图像转移, 高频细节恢复, 免蒙皮方法, 虚拟试穿

## 3 点简述
- 核心问题：现有基于线性混合蒙皮的方法在服装变形时易产生形状错位，影响高频皱纹恢复。
- 方法要点：独立估计顶点位置和法线以解耦低频形状与高频细节，通过图像转移利用预训练模型提升视觉质量。
- 实验或效果：在多种服装类型上显著提升动画质量，恢复更精细皱纹，优于现有方法。

## 摘要（原文）

> We present a novel method for generating 3D garment deformations from given body poses, which is key to a wide range of applications, including virtual try-on and extended reality. To simplify the cloth dynamics, existing methods mostly rely on linear blend skinning to obtain low-frequency posed garment shape and only regress high-frequency wrinkles. However, due to the lack of explicit skinning supervision, such skinning-based approach often produces misaligned shapes when posing the garment, consequently corrupts the high-frequency signals and fails to recover high-fidelity wrinkles. To tackle this issue, we propose a skinning-free approach by independently estimating posed (i) vertex position for low-frequency posed garment shape, and (ii) vertex normal for high-frequency local wrinkle details. In this way, each frequency modality can be effectively decoupled and directly supervised by the geometry of the deformed garment. To further improve the visual quality of animation, we propose to encode both vertex attributes as rendered texture images, so that 3D garment deformation can be equivalently achieved via 2D image transfer. This enables us to leverage powerful pretrained image models to recover fine-grained visual details in wrinkles, while maintaining superior scalability for garments of diverse topologies without relying on manual UV partition. Finally, we propose a multimodal fusion to incorporate constraints from both frequency modalities and robustly recover deformed 3D garments from transferred images. Extensive experiments show that our method significantly improves animation quality on various garment types and recovers finer wrinkles than state-of-the-art methods.

