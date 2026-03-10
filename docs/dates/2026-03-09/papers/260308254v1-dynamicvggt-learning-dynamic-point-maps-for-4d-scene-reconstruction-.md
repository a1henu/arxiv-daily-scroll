---
layout: default
title: DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving
---

# DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving
**arXiv**：[2603.08254v1](https://arxiv.org/abs/2603.08254) · [PDF](https://arxiv.org/pdf/2603.08254.pdf)  
**作者**：Zhuolin He, Jing Li, Guanghao Li, Xiaolei Chen, Jiacheng Tang, Siyang Zhang, Zhounan Jin, Feipeng Cai, Bin Li, Jian Pu, Jia Cai, Xiangyang Xue  

**一句话要点**：提出DynamicVGGT框架，通过动态点映射和运动建模实现自动驾驶中的4D动态场景重建。

**关键词**：4D场景重建, 动态点映射, 自动驾驶, 前馈模型, 运动建模, 高斯溅射

## 3 点简述
- 核心问题：自动驾驶中动态场景重建因时间变化、移动物体和复杂动态而具挑战性，现有前馈3D模型难以捕捉动态运动。
- 方法要点：扩展VGGT至动态4D重建，联合预测当前和未来点映射，引入运动感知时间注意力模块和动态3D高斯溅射头以建模点运动。
- 实验或效果：在自动驾驶数据集上，DynamicVGGT在重建精度上显著优于现有方法，实现鲁棒的前馈4D动态场景重建。

## 摘要（原文）

> Dynamic scene reconstruction in autonomous driving remains a fundamental challenge due to significant temporal variations, moving objects, and complex scene dynamics. Existing feed-forward 3D models have demonstrated strong performance in static reconstruction but still struggle to capture dynamic motion. To address these limitations, we propose DynamicVGGT, a unified feed-forward framework that extends VGGT from static 3D perception to dynamic 4D reconstruction. Our goal is to model point motion within feed-forward 3D models in a dynamic and temporally coherent manner. To this end, we jointly predict the current and future point maps within a shared reference coordinate system, allowing the model to implicitly learn dynamic point representations through temporal correspondence. To efficiently capture temporal dependencies, we introduce a Motion-aware Temporal Attention (MTA) module that learns motion continuity. Furthermore, we design a Dynamic 3D Gaussian Splatting Head that explicitly models point motion by predicting Gaussian velocities using learnable motion tokens under scene flow supervision. It refines dynamic geometry through continuous 3D Gaussian optimization. Extensive experiments on autonomous driving datasets demonstrate that DynamicVGGT significantly outperforms existing methods in reconstruction accuracy, achieving robust feed-forward 4D dynamic scene reconstruction under complex driving scenarios.

