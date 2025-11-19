---
layout: default
title: Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction
---

# Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction
**arXiv**：[2511.14540v1](https://arxiv.org/abs/2511.14540) · [PDF](https://arxiv.org/pdf/2511.14540.pdf)  
**作者**：Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  

**一句话要点**：提出交互感知4D高斯泼溅方法以重建动态手-物交互场景

**关键词**：动态3D重建, 高斯泼溅, 手-物交互, 交互感知建模, 无先验学习

## 3 点简述
- 核心问题：无先验下同时建模手-物交互的几何与外观，处理遮挡和边缘模糊。
- 方法要点：引入交互感知高斯和动态场，结合手信息优化对象变形与运动。
- 实验效果：超越现有动态3D-GS方法，在交互重建中达到最优性能。

## 摘要（原文）

> This paper focuses on a challenging setting of simultaneously modeling geometry and appearance of hand-object interaction scenes without any object priors. We follow the trend of dynamic 3D Gaussian Splatting based methods, and address several significant challenges. To model complex hand-object interaction with mutual occlusion and edge blur, we present interaction-aware hand-object Gaussians with newly introduced optimizable parameters aiming to adopt piecewise linear hypothesis for clearer structural representation. Moreover, considering the complementarity and tightness of hand shape and object shape during interaction dynamics, we incorporate hand information into object deformation field, constructing interaction-aware dynamic fields to model flexible motions. To further address difficulties in the optimization process, we propose a progressive strategy that handles dynamic regions and static background step by step. Correspondingly, explicit regularizations are designed to stabilize the hand-object representations for smooth motion transition, physical interaction reality, and coherent lighting. Experiments show that our approach surpasses existing dynamic 3D-GS-based methods and achieves state-of-the-art performance in reconstructing dynamic hand-object interaction.

