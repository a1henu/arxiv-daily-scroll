---
layout: default
title: RUMPL: Ray-Based Transformers for Universal Multi-View 2D to 3D Human Pose Lifting
---

# RUMPL: Ray-Based Transformers for Universal Multi-View 2D to 3D Human Pose Lifting
**arXiv**：[2512.15488v1](https://arxiv.org/abs/2512.15488) · [PDF](https://arxiv.org/pdf/2512.15488.pdf)  
**作者**：Seyed Abolfazl Ghasemzadeh, Alexandre Alahi, Christophe De Vleeschouwer  

**一句话要点**：提出RUMPL，基于射线表示和Transformer，实现通用多视图2D到3D人体姿态提升。

**关键词**：多视图姿态估计, 3D人体姿态提升, 射线表示, Transformer, 通用部署

## 3 点简述
- 核心问题：多视图3D姿态估计因遮挡和投影模糊而困难，且缺乏真实世界大规模数据。
- 方法要点：引入3D射线表示2D关键点，使模型独立于相机标定和视图数量，无需重训练。
- 实验或效果：在多个基准测试中，相比三角测量和基于图像的Transformer基线，MPJPE降低超过50%。

## 摘要（原文）

> Estimating 3D human poses from 2D images remains challenging due to occlusions and projective ambiguity. Multi-view learning-based approaches mitigate these issues but often fail to generalize to real-world scenarios, as large-scale multi-view datasets with 3D ground truth are scarce and captured under constrained conditions. To overcome this limitation, recent methods rely on 2D pose estimation combined with 2D-to-3D pose lifting trained on synthetic data. Building on our previous MPL framework, we propose RUMPL, a transformer-based 3D pose lifter that introduces a 3D ray-based representation of 2D keypoints. This formulation makes the model independent of camera calibration and the number of views, enabling universal deployment across arbitrary multi-view configurations without retraining or fine-tuning. A new View Fusion Transformer leverages learned fused-ray tokens to aggregate information along rays, further improving multi-view consistency. Extensive experiments demonstrate that RUMPL reduces MPJPE by up to 53% compared to triangulation and over 60% compared to transformer-based image-representation baselines. Results on new benchmarks, including in-the-wild multi-view and multi-person datasets, confirm its robustness and scalability. The framework's source code is available at https://github.com/aghasemzadeh/OpenRUMPL

