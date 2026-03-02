---
layout: default
title: Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation
---

# Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation
**arXiv**：[2602.23814v1](https://arxiv.org/abs/2602.23814) · [PDF](https://arxiv.org/pdf/2602.23814.pdf)  
**作者**：Chongyang Xu, Haipeng Li, Shen Cheng, Jingyu Hu, Haoqiang Fan, Ziliang Feng, Shuaicheng Liu  

**一句话要点**：提出基于3D几何先验的动作-几何预测框架，用于双手机器人操作

**关键词**：双手机器人操作, 3D几何预测, 扩散模型, RGB观测, 点图生成, 空间推理

## 3 点简述
- 核心问题：双手机器人操作需3D几何推理，现有方法依赖2D特征或难获取的点云，空间感知有限。
- 方法要点：利用预训练3D几何基础模型，融合几何感知潜在、2D语义特征和本体感知，用扩散模型联合预测未来动作块和3D潜在解码为密集点图。
- 实验或效果：在仿真和真实机器人上评估，优于2D和点云基线，在操作成功率、双臂协调和3D空间预测精度上达到先进水平。

## 摘要（原文）

> Bimanual manipulation requires policies that can reason about 3D geometry, anticipate how it evolves under action, and generate smooth, coordinated motions. However, existing methods typically rely on 2D features with limited spatial awareness, or require explicit point clouds that are difficult to obtain reliably in real-world settings. At the same time, recent 3D geometric foundation models show that accurate and diverse 3D structure can be reconstructed directly from RGB images in a fast and robust manner. We leverage this opportunity and propose a framework that builds bimanual manipulation directly on a pre-trained 3D geometric foundation model. Our policy fuses geometry-aware latents, 2D semantic features, and proprioception into a unified state representation, and uses diffusion model to jointly predict a future action chunk and a future 3D latent that decodes into a dense pointmap. By explicitly predicting how the 3D scene will evolve together with the action sequence, the policy gains strong spatial understanding and predictive capability using only RGB observations. We evaluate our method both in simulation on the RoboTwin benchmark and in real-world robot executions. Our approach consistently outperforms 2D-based and point-cloud-based baselines, achieving state-of-the-art performance in manipulation success, inter-arm coordination, and 3D spatial prediction accuracy. Code is available at https://github.com/Chongyang-99/GAP.git.

