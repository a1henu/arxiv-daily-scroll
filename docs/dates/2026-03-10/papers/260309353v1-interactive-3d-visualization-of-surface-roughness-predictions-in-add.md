---
layout: default
title: Interactive 3D visualization of surface roughness predictions in additive manufacturing: A data-driven framework
---

# Interactive 3D visualization of surface roughness predictions in additive manufacturing: A data-driven framework
**arXiv**：[2603.09353v1](https://arxiv.org/abs/2603.09353) · [PDF](https://arxiv.org/pdf/2603.09353.pdf)  
**作者**：Engin Deniz Erkan, Elif Surer, Ulas Yaman  

**一句话要点**：提出数据驱动框架以预测增材制造表面粗糙度，并开发交互式3D可视化决策支持界面。

**关键词**：增材制造, 表面粗糙度预测, 数据驱动框架, 条件生成对抗网络, 交互式3D可视化, 决策支持系统

## 3 点简述
- 核心问题：增材制造中表面粗糙度受打印参数和局部表面倾斜度影响，难以在工艺规划中预测。
- 方法要点：使用多层感知机回归器预测粗糙度，并采用条件生成对抗网络扩充数据以提高性能。
- 实验或效果：基于87个样本的1566个测量数据训练模型，开发Web界面实现交互式3D粗糙度可视化。

## 摘要（原文）

> Surface roughness in Material Extrusion Additive Manufacturing varies across a part and is difficult to anticipate during process planning because it depends on both printing parameters and local surface inclination, which governs the staircase effect. A data-driven framework is presented to predict the arithmetic mean roughness (Ra) prior to fabrication using process parameters and surface angle. A structured experimental dataset was created using a three-level Box-Behnken design: 87 specimens were printed, each with multiple planar faces spanning different inclination angles, yielding 1566 Ra measurements acquired with a contact profilometer. A multilayer perceptron regressor was trained to capture nonlinear relationships between manufacturing conditions, inclination, and Ra. To mitigate limited experimental data, a conditional generative adversarial network was used to generate additional condition-specific tabular samples, thereby improving predictive performance. Model performance was assessed on a hold-out test set. A web-based decision-support interface was also developed to enable interactive process planning by loading a 3D model, specifying printing parameters, and adjusting the part's orientation. The system computes face-wise inclination from the model geometry and visualizes predicted Ra as an interactive colormap over the surface, enabling rapid identification of regions prone to high roughness and immediate comparison of parameter and orientation choices.

