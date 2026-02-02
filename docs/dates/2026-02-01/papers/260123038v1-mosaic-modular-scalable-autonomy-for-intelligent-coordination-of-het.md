---
layout: default
title: MOSAIC: Modular Scalable Autonomy for Intelligent Coordination of Heterogeneous Robotic Teams
---

# MOSAIC: Modular Scalable Autonomy for Intelligent Coordination of Heterogeneous Robotic Teams
**arXiv**：[2601.23038v1](https://arxiv.org/abs/2601.23038) · [PDF](https://arxiv.org/pdf/2601.23038.pdf)  
**作者**：David Oberacker, Julia Richer, Philip Arm, Marvin Grosse Besselmann, Lennart Puck, William Talbot, Maximilian Schik, Sabine Bellmann, Tristan Schnell, Hendrik Kolvenbach, Rüdiger Dillmann, Marco Hutter, Arne Roennau  

**一句话要点**：提出MOSAIC框架以解决异构机器人团队在科学探索中的可扩展自主协调问题

**关键词**：多机器人系统, 可扩展自主性, 异构机器人协调, 科学探索, 任务分配

## 3 点简述
- 核心问题：移动机器人在恶劣环境探索中依赖人工遥操作，限制部署规模并需低延迟通信。
- 方法要点：基于兴趣点统一任务抽象和多层自主性，实现单操作员监督下的动态任务分配。
- 实验或效果：在月球勘探模拟实验中，五机器人团队在单操作员下完成82.3%任务，自主率达86%。

## 摘要（原文）

> Mobile robots have become indispensable for exploring hostile environments, such as in space or disaster relief scenarios, but often remain limited to teleoperation by a human operator. This restricts the deployment scale and requires near-continuous low-latency communication between the operator and the robot. We present MOSAIC: a scalable autonomy framework for multi-robot scientific exploration using a unified mission abstraction based on Points of Interest (POIs) and multiple layers of autonomy, enabling supervision by a single operator. The framework dynamically allocates exploration and measurement tasks based on each robot's capabilities, leveraging team-level redundancy and specialization to enable continuous operation. We validated the framework in a space-analog field experiment emulating a lunar prospecting scenario, involving a heterogeneous team of five robots and a single operator. Despite the complete failure of one robot during the mission, the team completed 82.3% of assigned tasks at an Autonomy Ratio of 86%, while the operator workload remained at only 78.2%. These results demonstrate that the proposed framework enables robust, scalable multi-robot scientific exploration with limited operator intervention. We further derive practical lessons learned in robot interoperability, networking architecture, team composition, and operator workload management to inform future multi-robot exploration missions.

