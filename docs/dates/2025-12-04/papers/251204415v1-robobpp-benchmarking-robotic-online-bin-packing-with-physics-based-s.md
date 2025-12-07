---
layout: default
title: RoboBPP: Benchmarking Robotic Online Bin Packing with Physics-based Simulation
---

# RoboBPP: Benchmarking Robotic Online Bin Packing with Physics-based Simulation
**arXiv**：[2512.04415v1](https://arxiv.org/abs/2512.04415) · [PDF](https://arxiv.org/pdf/2512.04415.pdf)  
**作者**：Zhoufeng Wang, Hang Zhao, Juzhan Xu, Shishun Zhang, Zeyu Xiong, Ruizhen Hu, Chenyang Zhu, Kai Xu  

**一句话要点**：提出RoboBPP基准系统，通过物理仿真解决机器人在线装箱的物理可行性与标准化评估问题。

**关键词**：机器人装箱, 物理仿真, 基准测试, 工业自动化, 在线优化

## 3 点简述
- 核心问题：机器人在线装箱领域缺乏统一基准，物理可行性和真实数据不足阻碍进展。
- 方法要点：集成物理仿真器模拟真实工业流程，引入真实工业数据集和扩展评估指标。
- 实验或效果：提供开源基准系统，包含可视化工具和在线排行榜，支持可复现研究。

## 摘要（原文）

> Physical feasibility in 3D bin packing is a key requirement in modern industrial logistics and robotic automation. With the growing adoption of industrial automation, online bin packing has gained increasing attention. However, inconsistencies in problem settings, test datasets, and evaluation metrics have hindered progress in the field, and there is a lack of a comprehensive benchmarking system. Direct testing on real hardware is costly, and building a realistic simulation environment is also challenging. To address these limitations, we introduce RoboBPP, a benchmarking system designed for robotic online bin packing. RoboBPP integrates a physics-based simulator to assess physical feasibility. In our simulation environment, we introduce a robotic arm and boxes at real-world scales to replicate real industrial packing workflows. By simulating conditions that arise in real industrial applications, we ensure that evaluated algorithms are practically deployable. In addition, prior studies often rely on synthetic datasets whose distributions differ from real-world industrial data. To address this issue, we collect three datasets from real industrial workflows, including assembly-line production, logistics packing, and furniture manufacturing. The benchmark comprises three carefully designed test settings and extends existing evaluation metrics with new metrics for structural stability and operational safety. We design a scoring system and derive a range of insights from the evaluation results. RoboBPP is fully open-source and is equipped with visualization tools and an online leaderboard, providing a reproducible and extensible foundation for future research and industrial applications (https://robot-bin-packing-benchmark.github.io).

