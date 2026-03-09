---
layout: default
title: Moving Through Clutter: Scaling Data Collection and Benchmarking for 3D Scene-Aware Humanoid Locomotion via Virtual Reality
---

# Moving Through Clutter: Scaling Data Collection and Benchmarking for 3D Scene-Aware Humanoid Locomotion via Virtual Reality
**arXiv**：[2603.05993v1](https://arxiv.org/abs/2603.05993) · [PDF](https://arxiv.org/pdf/2603.05993.pdf)  
**作者**：Beichen Wang, Yuanjie Lu, Linji Wang, Liuchuan Yu, Xuesu Xiao  

**一句话要点**：提出基于VR的MTC框架，用于在杂乱3D环境中收集和评估人形机器人场景感知运动数据。

**关键词**：人形机器人运动, 虚拟现实数据收集, 场景感知控制, 杂乱环境导航, 运动重定向, 基准评估

## 3 点简述
- 核心问题：人形机器人在杂乱3D环境中的运动研究不足，缺乏公开数据集耦合全身运动与场景几何。
- 方法要点：通过VR沉浸式导航捕获人体运动，自动重定向到人形机器人模型，并程序化生成可控杂乱度的场景。
- 实验或效果：编译了包含348条轨迹和145个场景的数据集，引入量化环境杂乱度和运动性能的基准。

## 摘要（原文）

> Recent advances in humanoid locomotion have enabled dynamic behaviors such as dancing, martial arts, and parkour, yet these capabilities are predominantly demonstrated in open, flat, and obstacle-free settings. In contrast, real-world environments such as homes, offices, and public spaces, are densely cluttered, three-dimensional, and geometrically constrained, requiring scene-aware whole-body coordination, precise balance control, and reasoning over spatial constraints imposed by furniture and household objects. However, humanoid locomotion in cluttered 3D environments remains underexplored, and no public dataset systematically couples full-body human locomotion with the scene geometry that shapes it. To address this gap, we present Moving Through Clutter (MTC), an opensource Virtual Reality (VR) based data collection and evaluation framework for scene-aware humanoid locomotion in cluttered environments. Our system procedurally generates scenes with controllable clutter levels and captures embodiment-consistent, whole-body human motion through immersive VR navigation, which is then automatically retargeted to a humanoid robot model. We further introduce benchmarks that quantify environment clutter level and locomotion performance, including stability and collision safety. Using this framework, we compile a dataset of 348 trajectories across 145 diverse 3D cluttered scenes. The dataset provides a foundation for studying geometry-induced adaptation in humanoid locomotion and developing scene-aware planning and control methods.

