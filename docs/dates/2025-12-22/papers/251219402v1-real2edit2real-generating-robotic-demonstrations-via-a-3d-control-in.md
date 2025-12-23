---
layout: default
title: Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface
---

# Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface
**arXiv**：[2512.19402v1](https://arxiv.org/abs/2512.19402) · [PDF](https://arxiv.org/pdf/2512.19402.pdf)  
**作者**：Yujie Zhao, Hongwei Fan, Di Chen, Shengcong Chen, Liliang Chen, Xiaoqi Li, Guanghui Ren, Hao Dong  

**一句话要点**：提出Real2Edit2Real框架，通过3D控制接口生成机器人演示以提升数据效率

**关键词**：机器人演示生成, 3D重建与编辑, 多条件视频生成, 数据效率提升, 空间泛化

## 3 点简述
- 核心问题：机器人学习依赖大规模演示数据，但收集成本高，空间泛化受限
- 方法要点：基于多视角RGB重建3D几何，编辑点云生成新轨迹，并用深度引导视频生成模型合成演示
- 实验或效果：在四任务中，仅用1-5个源演示生成的数据训练策略，性能匹配或超越50个真实演示，数据效率提升10-50倍

## 摘要（原文）

> Recent progress in robot learning has been driven by large-scale datasets and powerful visuomotor policy architectures, yet policy robustness remains limited by the substantial cost of collecting diverse demonstrations, particularly for spatial generalization in manipulation tasks. To reduce repetitive data collection, we present Real2Edit2Real, a framework that generates new demonstrations by bridging 3D editability with 2D visual data through a 3D control interface. Our approach first reconstructs scene geometry from multi-view RGB observations with a metric-scale 3D reconstruction model. Based on the reconstructed geometry, we perform depth-reliable 3D editing on point clouds to generate new manipulation trajectories while geometrically correcting the robot poses to recover physically consistent depth, which serves as a reliable condition for synthesizing new demonstrations. Finally, we propose a multi-conditional video generation model guided by depth as the primary control signal, together with action, edge, and ray maps, to synthesize spatially augmented multi-view manipulation videos. Experiments on four real-world manipulation tasks demonstrate that policies trained on data generated from only 1-5 source demonstrations can match or outperform those trained on 50 real-world demonstrations, improving data efficiency by up to 10-50x. Moreover, experimental results on height and texture editing demonstrate the framework's flexibility and extensibility, indicating its potential to serve as a unified data generation framework.

