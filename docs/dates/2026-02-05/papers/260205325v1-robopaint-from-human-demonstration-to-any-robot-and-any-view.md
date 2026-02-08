---
layout: default
title: RoboPaint: From Human Demonstration to Any Robot and Any View
---

# RoboPaint: From Human Demonstration to Any Robot and Any View
**arXiv**：[2602.05325v1](https://arxiv.org/abs/2602.05325) · [PDF](https://arxiv.org/pdf/2602.05325.pdf)  
**作者**：Jiacheng Fan, Zhiyue Zhao, Yiqian Zhang, Chao Chen, Peide Wang, Hengdi Zhang, Zhengxue Cheng  

**一句话要点**：提出Real-Sim-Real数据管道，从人类演示生成机器人训练数据以解决灵巧操作数据瓶颈

**关键词**：灵巧操作, 数据生成, 触觉感知, 机器人重定向, 视觉-语言-动作模型, 仿真渲染

## 3 点简述
- 核心问题：大规模高保真机器人演示数据是扩展视觉-语言-动作模型在灵巧操作中的关键瓶颈
- 方法要点：通过触觉感知重定向和真实感渲染，将人类演示转换为机器人可执行数据，无需直接遥操作
- 实验或效果：重定向轨迹在10个任务中成功率84%，生成数据训练的VLA策略在代表性任务中平均成功率80%

## 摘要（原文）

> Acquiring large-scale, high-fidelity robot demonstration data remains a critical bottleneck for scaling Vision-Language-Action (VLA) models in dexterous manipulation. We propose a Real-Sim-Real data collection and data editing pipeline that transforms human demonstrations into robot-executable, environment-specific training data without direct robot teleoperation. Standardized data collection rooms are built to capture multimodal human demonstrations (synchronized 3 RGB-D videos, 11 RGB videos, 29-DoF glove joint angles, and 14-channel tactile signals). Based on these human demonstrations, we introduce a tactile-aware retargeting method that maps human hand states to robot dex-hand states via geometry and force-guided optimization. Then the retargeted robot trajectories are rendered in a photorealistic Isaac Sim environment to build robot training data. Real world experiments have demonstrated: (1) The retargeted dex-hand trajectories achieve an 84\% success rate across 10 diverse object manipulation tasks. (2) VLA policies (Pi0.5) trained exclusively on our generated data achieve 80\% average success rate on three representative tasks, i.e., pick-and-place, pushing and pouring. To conclude, robot training data can be efficiently "painted" from human demonstrations using our real-sim-real data pipeline. We offer a scalable, cost-effective alternative to teleoperation with minimal performance loss for complex dexterous manipulation.

