---
layout: default
title: GS-DMSR: Dynamic Sensitive Multi-scale Manifold Enhancement for Accelerated High-Quality 3D Gaussian Splatting
---

# GS-DMSR: Dynamic Sensitive Multi-scale Manifold Enhancement for Accelerated High-Quality 3D Gaussian Splatting
**arXiv**：[2601.05584v1](https://arxiv.org/abs/2601.05584) · [PDF](https://arxiv.org/pdf/2601.05584.pdf)  
**作者**：Nengbo Lu, Minghua Pan, Shaohua Sun, Yizhou Liang  

**一句话要点**：提出GS-DMSR方法以加速高质量3D动态场景重建，平衡收敛速度与渲染质量。

**关键词**：3D动态场景重建, 高斯泼溅, 自适应梯度聚焦, 多尺度流形增强, 加速渲染

## 3 点简述
- 核心问题：3D动态场景重建中，复杂动态运动场景的高精度建模需平衡模型收敛速度与渲染质量。
- 方法要点：通过动态敏感多尺度流形增强，自适应梯度聚焦和差异化优化策略，提升模型收敛率。
- 实验或效果：在合成数据集上达到96 FPS帧率，有效减少存储开销和训练时间。

## 摘要（原文）

> In the field of 3D dynamic scene reconstruction, how to balance model convergence rate and rendering quality has long been a critical challenge that urgently needs to be addressed, particularly in high-precision modeling of scenes with complex dynamic motions. To tackle this issue, this study proposes the GS-DMSR method. By quantitatively analyzing the dynamic evolution process of Gaussian attributes, this mechanism achieves adaptive gradient focusing, enabling it to dynamically identify significant differences in the motion states of Gaussian models. It then applies differentiated optimization strategies to Gaussian models with varying degrees of significance, thereby significantly improving the model convergence rate. Additionally, this research integrates a multi-scale manifold enhancement module, which leverages the collaborative optimization of an implicit nonlinear decoder and an explicit deformation field to enhance the modeling efficiency for complex deformation scenes. Experimental results demonstrate that this method achieves a frame rate of up to 96 FPS on synthetic datasets, while effectively reducing both storage overhead and training time.Our code and data are available at https://anonymous.4open.science/r/GS-DMSR-2212.

