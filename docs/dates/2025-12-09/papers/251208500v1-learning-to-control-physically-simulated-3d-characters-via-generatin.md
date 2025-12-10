---
layout: default
title: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
---

# Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
**arXiv**：[2512.08500v1](https://arxiv.org/abs/2512.08500) · [PDF](https://arxiv.org/pdf/2512.08500.pdf)  
**作者**：Jianan Li, Xiao Chen, Tao Huang, Tien-Tsin Wong  

**一句话要点**：提出Mimic2DM框架，通过生成和模仿2D运动学习物理模拟3D角色控制，无需3D数据。

**关键词**：2D运动模仿, 物理模拟控制, 变换器生成, 分层控制, 视频数据学习

## 3 点简述
- 核心问题：从视频学习3D角色控制时，现有方法依赖3D运动重建，泛化性差且难以处理复杂场景。
- 方法要点：直接利用2D关键点轨迹训练跟踪策略，结合变换器生成2D参考运动，实现分层控制。
- 实验或效果：在舞蹈、足球运球和动物运动等场景中合成物理合理且多样的运动，无需3D数据。

## 摘要（原文）

> Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

