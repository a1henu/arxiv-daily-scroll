---
layout: default
title: BronchOpt : Vision-Based Pose Optimization with Fine-Tuned Foundation Models for Accurate Bronchoscopy Navigation
---

# BronchOpt : Vision-Based Pose Optimization with Fine-Tuned Foundation Models for Accurate Bronchoscopy Navigation
**arXiv**：[2511.09443v1](https://arxiv.org/abs/2511.09443) · [PDF](https://arxiv.org/pdf/2511.09443.pdf)  
**作者**：Hongchao Shu, Roger D. Soberanis-Mukul, Jiru Xu, Hao Ding, Morgan Ringel, Mali Shen, Saif Iftekar Sayed, Hedyeh Rafii-Tari, Mathias Unberath  

**一句话要点**：提出基于视觉的位姿优化框架，用于支气管镜导航中的准确2D-3D配准。

**关键词**：支气管镜导航, 2D-3D配准, 视觉位姿优化, 合成基准数据集, 跨域泛化, 可微分渲染

## 3 点简述
- 核心问题：支气管镜导航中因呼吸运动和CT-身体差异导致配准误差，现有方法泛化性差。
- 方法要点：使用微调编码器计算RGB与深度图相似性，通过可微分渲染迭代优化相机位姿。
- 实验或效果：在合成数据上训练，平均平移误差2.65毫米，旋转误差0.19弧度，实现跨域泛化。

## 摘要（原文）

> Accurate intra-operative localization of the bronchoscope tip relative to patient anatomy remains challenging due to respiratory motion, anatomical variability, and CT-to-body divergence that cause deformation and misalignment between intra-operative views and pre-operative CT. Existing vision-based methods often fail to generalize across domains and patients, leading to residual alignment errors. This work establishes a generalizable foundation for bronchoscopy navigation through a robust vision-based framework and a new synthetic benchmark dataset that enables standardized and reproducible evaluation. We propose a vision-based pose optimization framework for frame-wise 2D-3D registration between intra-operative endoscopic views and pre-operative CT anatomy. A fine-tuned modality- and domain-invariant encoder enables direct similarity computation between real endoscopic RGB frames and CT-rendered depth maps, while a differentiable rendering module iteratively refines camera poses through depth consistency. To enhance reproducibility, we introduce the first public synthetic benchmark dataset for bronchoscopy navigation, addressing the lack of paired CT-endoscopy data. Trained exclusively on synthetic data distinct from the benchmark, our model achieves an average translational error of 2.65 mm and a rotational error of 0.19 rad, demonstrating accurate and stable localization. Qualitative results on real patient data further confirm strong cross-domain generalization, achieving consistent frame-wise 2D-3D alignment without domain-specific adaptation. Overall, the proposed framework achieves robust, domain-invariant localization through iterative vision-based optimization, while the new benchmark provides a foundation for standardized progress in vision-based bronchoscopy navigation.

