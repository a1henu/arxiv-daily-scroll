---
layout: default
title: Visual Implicit Geometry Transformer for Autonomous Driving
---

# Visual Implicit Geometry Transformer for Autonomous Driving
**arXiv**：[2602.05573v1](https://arxiv.org/abs/2602.05573) · [PDF](https://arxiv.org/pdf/2602.05573.pdf)  
**作者**：Arsenii Shirokov, Mikhail Kuznetsov, Danila Stepochkin, Egor Evdokimov, Daniil Glazkov, Nikolay Patakin, Anton Konushin, Dmitry Senushkin  

**一句话要点**：提出视觉隐式几何变换器，用于自动驾驶中从多视角相机估计连续3D占据场。

**关键词**：自动驾驶几何模型, 3D占据场估计, 自监督学习, 多视图融合, 无校准架构, 鸟瞰图表示

## 3 点简述
- 核心问题：自动驾驶需从多相机视图估计连续3D几何，传统方法依赖校准和标注，难以泛化。
- 方法要点：采用无校准架构和自监督训练，利用图像-LiDAR对，实现多传感器配置的通用几何建模。
- 实验或效果：在五个大规模数据集上训练，点图估计任务达到最佳平均排名，Occ3D-nuScenes基准表现可比监督方法。

## 摘要（原文）

> We introduce the Visual Implicit Geometry Transformer (ViGT), an autonomous driving geometric model that estimates continuous 3D occupancy fields from surround-view camera rigs. ViGT represents a step towards foundational geometric models for autonomous driving, prioritizing scalability, architectural simplicity, and generalization across diverse sensor configurations. Our approach achieves this through a calibration-free architecture, enabling a single model to adapt to different sensor setups. Unlike general-purpose geometric foundational models that focus on pixel-aligned predictions, ViGT estimates a continuous 3D occupancy field in a birds-eye-view (BEV) addressing domain-specific requirements. ViGT naturally infers geometry from multiple camera views into a single metric coordinate frame, providing a common representation for multiple geometric tasks. Unlike most existing occupancy models, we adopt a self-supervised training procedure that leverages synchronized image-LiDAR pairs, eliminating the need for costly manual annotations. We validate the scalability and generalizability of our approach by training our model on a mixture of five large-scale autonomous driving datasets (NuScenes, Waymo, NuPlan, ONCE, and Argoverse) and achieving state-of-the-art performance on the pointmap estimation task, with the best average rank across all evaluated baselines. We further evaluate ViGT on the Occ3D-nuScenes benchmark, where ViGT achieves comparable performance with supervised methods. The source code is publicly available at \href{https://github.com/whesense/ViGT}{https://github.com/whesense/ViGT}.

