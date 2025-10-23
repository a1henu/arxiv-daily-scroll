---
layout: default
title: AegisRF: Adversarial Perturbations Guided with Sensitivity for Protecting Intellectual Property of Neural Radiance Fields
---

# AegisRF: Adversarial Perturbations Guided with Sensitivity for Protecting Intellectual Property of Neural Radiance Fields
**arXiv**：[2510.19371v1](https://arxiv.org/abs/2510.19371) · [PDF](https://arxiv.org/pdf/2510.19371.pdf)  
**作者**：Woo Jae Kim, Kyu Beom Han, Yoonki Cho, Youngju Na, Junsik Jung, Sooel Son, Sung-eui Yoon  

**一句话要点**：提出AegisRF框架以保护神经辐射场知识产权，通过对抗扰动破坏未授权使用

**关键词**：神经辐射场保护, 对抗扰动, 知识产权安全, 几何扰动约束, 多任务评估

## 3 点简述
- 核心问题：神经辐射场易受未授权使用，现有方法避免几何扰动以防渲染质量下降
- 方法要点：引入可学习敏感度场，自适应约束几何扰动，保持渲染质量同时注入对抗扰动
- 实验或效果：在多种下游任务中验证通用性，如多视图图像分类，保持高视觉保真度

## 摘要（原文）

> As Neural Radiance Fields (NeRFs) have emerged as a powerful tool for 3D
> scene representation and novel view synthesis, protecting their intellectual
> property (IP) from unauthorized use is becoming increasingly crucial. In this
> work, we aim to protect the IP of NeRFs by injecting adversarial perturbations
> that disrupt their unauthorized applications. However, perturbing the 3D
> geometry of NeRFs can easily deform the underlying scene structure and thus
> substantially degrade the rendering quality, which has led existing attempts to
> avoid geometric perturbations or restrict them to explicit spaces like meshes.
> To overcome this limitation, we introduce a learnable sensitivity to quantify
> the spatially varying impact of geometric perturbations on rendering quality.
> Building upon this, we propose AegisRF, a novel framework that consists of a
> Perturbation Field, which injects adversarial perturbations into the
> pre-rendering outputs (color and volume density) of NeRF models to fool an
> unauthorized downstream target model, and a Sensitivity Field, which learns the
> sensitivity to adaptively constrain geometric perturbations, preserving
> rendering quality while disrupting unauthorized use. Our experimental
> evaluations demonstrate the generalized applicability of AegisRF across diverse
> downstream tasks and modalities, including multi-view image classification and
> voxel-based 3D localization, while maintaining high visual fidelity. Codes are
> available at https://github.com/wkim97/AegisRF.

