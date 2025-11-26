---
layout: default
title: Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI
---

# Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI
**arXiv**：[2511.20620v1](https://arxiv.org/abs/2511.20620) · [PDF](https://arxiv.org/pdf/2511.20620.pdf)  
**作者**：Xinhao Liu, Jiaqi Li, Youming Deng, Ruxin Chen, Yingjia Zhang, Yifei Ma, Li Guo, Yiming Li, Jing Zhang, Chen Feng  

**一句话要点**：提出Wanderland框架以解决开放世界具身AI中仿真与现实的差距问题

**关键词**：具身AI, 仿真框架, 几何重建, 视图合成, 导航评估, 开放世界场景

## 3 点简述
- 核心问题：封闭式评估在具身AI中难以复现，仿真与现实存在视觉和几何差距
- 方法要点：开发多传感器捕获、可靠重建和精确几何的实到仿框架
- 实验或效果：展示几何质量影响视图合成和导航策略学习可靠性

## 摘要（原文）

> Reproducible closed-loop evaluation remains a major bottleneck in Embodied AI such as visual navigation. A promising path forward is high-fidelity simulation that combines photorealistic sensor rendering with geometrically grounded interaction in complex, open-world urban environments. Although recent video-3DGS methods ease open-world scene capturing, they are still unsuitable for benchmarking due to large visual and geometric sim-to-real gaps. To address these challenges, we introduce Wanderland, a real-to-sim framework that features multi-sensor capture, reliable reconstruction, accurate geometry, and robust view synthesis. Using this pipeline, we curate a diverse dataset of indoor-outdoor urban scenes and systematically demonstrate how image-only pipelines scale poorly, how geometry quality impacts novel view synthesis, and how all of these adversely affect navigation policy learning and evaluation reliability. Beyond serving as a trusted testbed for embodied navigation, Wanderland's rich raw sensor data further allows benchmarking of 3D reconstruction and novel view synthesis models. Our work establishes a new foundation for reproducible research in open-world embodied AI. Project website is at https://ai4ce.github.io/wanderland/.

