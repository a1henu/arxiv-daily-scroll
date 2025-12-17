---
layout: default
title: DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos
---

# DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos
**arXiv**：[2512.14217v1](https://arxiv.org/abs/2512.14217) · [PDF](https://arxiv.org/pdf/2512.14217.pdf)  
**作者**：Yang Bai, Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Ziyuan Liu, Gitta Kutyniok  

**一句话要点**：提出DRAW2ACT框架，通过深度感知轨迹条件视频生成提升机器人演示的可控性与一致性。

**关键词**：视频生成, 机器人演示, 深度感知, 轨迹条件, 多模态学习, 扩散模型

## 3 点简述
- 核心问题：视频扩散模型在机器人操作中可控性不足，现有方法依赖2D轨迹或单模态条件。
- 方法要点：从轨迹提取深度、语义等多正交表示，注入扩散模型，并联合生成对齐的RGB和深度视频。
- 实验或效果：在多个基准测试中，DRAW2ACT实现更高视觉保真度和操作成功率。

## 摘要（原文）

> Video diffusion models provide powerful real-world simulators for embodied AI but remain limited in controllability for robotic manipulation. Recent works on trajectory-conditioned video generation address this gap but often rely on 2D trajectories or single modality conditioning, which restricts their ability to produce controllable and consistent robotic demonstrations. We present DRAW2ACT, a depth-aware trajectory-conditioned video generation framework that extracts multiple orthogonal representations from the input trajectory, capturing depth, semantics, shape and motion, and injects them into the diffusion model. Moreover, we propose to jointly generate spatially aligned RGB and depth videos, leveraging cross-modality attention mechanisms and depth supervision to enhance the spatio-temporal consistency. Finally, we introduce a multimodal policy model conditioned on the generated RGB and depth sequences to regress the robot's joint angles. Experiments on Bridge V2, Berkeley Autolab, and simulation benchmarks show that DRAW2ACT achieves superior visual fidelity and consistency while yielding higher manipulation success rates compared to existing baselines.

