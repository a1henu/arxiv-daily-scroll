---
layout: default
title: SeeThrough3D: Occlusion Aware 3D Control in Text-to-Image Generation
---

# SeeThrough3D: Occlusion Aware 3D Control in Text-to-Image Generation
**arXiv**：[2602.23359v1](https://arxiv.org/abs/2602.23359) · [PDF](https://arxiv.org/pdf/2602.23359.pdf)  
**作者**：Vaibhav Agrawal, Rishubh Parihar, Pradhaan Bhat, Ravi Kiran Sarvadevabhatla, R. Venkatesh Babu  

**一句话要点**：提出SeeThrough3D以解决3D布局条件生成中的遮挡推理问题

**关键词**：3D布局条件生成, 遮挡推理, 文本到图像生成, 视觉令牌, 掩码自注意力, 合成数据集

## 3 点简述
- 核心问题：现有方法在3D布局条件生成中常忽略精确的物体间遮挡建模，导致几何和尺度不一致
- 方法要点：引入遮挡感知3D场景表示（OSCR），通过半透明3D框渲染编码隐藏区域，结合视觉令牌和掩码自注意力实现精确控制
- 实验或效果：在合成数据集上训练，能泛化到未见物体类别，实现逼真遮挡和一致相机控制的3D布局生成

## 摘要（原文）

> We identify occlusion reasoning as a fundamental yet overlooked aspect for 3D layout-conditioned generation. It is essential for synthesizing partially occluded objects with depth-consistent geometry and scale. While existing methods can generate realistic scenes that follow input layouts, they often fail to model precise inter-object occlusions. We propose SeeThrough3D, a model for 3D layout conditioned generation that explicitly models occlusions. We introduce an occlusion-aware 3D scene representation (OSCR), where objects are depicted as translucent 3D boxes placed within a virtual environment and rendered from desired camera viewpoint. The transparency encodes hidden object regions, enabling the model to reason about occlusions, while the rendered viewpoint provides explicit camera control during generation. We condition a pretrained flow based text-to-image image generation model by introducing a set of visual tokens derived from our rendered 3D representation. Furthermore, we apply masked self-attention to accurately bind each object bounding box to its corresponding textual description, enabling accurate generation of multiple objects without object attribute mixing. To train the model, we construct a synthetic dataset with diverse multi-object scenes with strong inter-object occlusions. SeeThrough3D generalizes effectively to unseen object categories and enables precise 3D layout control with realistic occlusions and consistent camera control.

