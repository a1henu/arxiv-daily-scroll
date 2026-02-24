---
layout: default
title: Monocular Mesh Recovery and Body Measurement of Female Saanen Goats
---

# Monocular Mesh Recovery and Body Measurement of Female Saanen Goats
**arXiv**：[2602.19896v1](https://arxiv.org/abs/2602.19896) · [PDF](https://arxiv.org/pdf/2602.19896.pdf)  
**作者**：Bo Jin, Shichao Zhao, Jin Lyu, Bin Zhang, Tao Yu, Liang An, Yebin Liu, Meili Wang  

**一句话要点**：提出SaanenGoat参数化模型，实现单目RGBD输入下雌性萨能山羊的3D重建与自动体尺测量。

**关键词**：3D重建, 参数化模型, 体尺测量, 精准畜牧业, 多视图融合, 山羊数据集

## 3 点简述
- 核心问题：现有方法缺乏山羊专用真实3D数据，影响基于体尺的产奶潜力评估。
- 方法要点：构建FemaleSaanenGoat数据集，开发多视图融合和参数化模型SaanenGoat，增强骨骼关节和乳房表示。
- 实验或效果：实现六项关键体尺的自动测量，在3D重建和体尺测量中展示高精度。

## 摘要（原文）

> The lactation performance of Saanen dairy goats, renowned for their high milk yield, is intrinsically linked to their body size, making accurate 3D body measurement essential for assessing milk production potential, yet existing reconstruction methods lack goat-specific authentic 3D data. To address this limitation, we establish the FemaleSaanenGoat dataset containing synchronized eight-view RGBD videos of 55 female Saanen goats (6-18 months). Using multi-view DynamicFusion, we fuse noisy, non-rigid point cloud sequences into high-fidelity 3D scans, overcoming challenges from irregular surfaces and rapid movement. Based on these scans, we develop SaanenGoat, a parametric 3D shape model specifically designed for female Saanen goats. This model features a refined template with 41 skeletal joints and enhanced udder representation, registered with our scan data. A comprehensive shape space constructed from 48 goats enables precise representation of diverse individual variations. With the help of SaanenGoat model, we get high-precision 3D reconstruction from single-view RGBD input, and achieve automated measurement of six critical body dimensions: body length, height, chest width, chest girth, hip width, and hip height. Experimental results demonstrate the superior accuracy of our method in both 3D reconstruction and body measurement, presenting a novel paradigm for large-scale 3D vision applications in precision livestock farming.

