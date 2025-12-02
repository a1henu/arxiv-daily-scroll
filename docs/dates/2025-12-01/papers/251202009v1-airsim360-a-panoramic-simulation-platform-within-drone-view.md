---
layout: default
title: AirSim360: A Panoramic Simulation Platform within Drone View
---

# AirSim360: A Panoramic Simulation Platform within Drone View
**arXiv**：[2512.02009v1](https://arxiv.org/abs/2512.02009) · [PDF](https://arxiv.org/pdf/2512.02009.pdf)  
**作者**：Xian Ge, Yuling Pan, Yuhang Zhang, Xiang Li, Weijun Zhang, Dizhe Zhang, Zhaoliang Wan, Xin Lin, Xiangkai Zhang, Juntao Liang, Jason Li, Wenjie Jiang, Bo Du, Ming-Hsuan Yang, Lu Qi  

**一句话要点**：提出AirSim360全景仿真平台，以无人机视角生成大规模全景数据，解决360度理解中数据缺乏问题。

**关键词**：全景仿真, 无人机视角, 空间智能, 数据生成, 行人建模, 导航任务

## 3 点简述
- 核心问题：360度全方位理解领域缺乏大规模多样化数据，限制空间智能发展。
- 方法要点：采用渲染对齐的数据与标注范式，支持像素级几何、语义和实体级理解；集成交互式行人感知系统建模人类行为；自动化轨迹生成支持导航任务。
- 实验或效果：收集超过60K全景样本，通过多任务实验验证平台有效性，并公开平台工具与数据集。

## 摘要（原文）

> The field of 360-degree omnidirectional understanding has been receiving increasing attention for advancing spatial intelligence. However, the lack of large-scale and diverse data remains a major limitation. In this work, we propose AirSim360, a simulation platform for omnidirectional data from aerial viewpoints, enabling wide-ranging scene sampling with drones. Specifically, AirSim360 focuses on three key aspects: a render-aligned data and labeling paradigm for pixel-level geometric, semantic, and entity-level understanding; an interactive pedestrian-aware system for modeling human behavior; and an automated trajectory generation paradigm to support navigation tasks. Furthermore, we collect more than 60K panoramic samples and conduct extensive experiments across various tasks to demonstrate the effectiveness of our simulator. Unlike existing simulators, our work is the first to systematically model the 4D real world under an omnidirectional setting. The entire platform, including the toolkit, plugins, and collected datasets, will be made publicly available at https://insta360-research-team.github.io/AirSim360-website.

