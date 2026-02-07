---
layout: default
title: From Bench to Flight: Translating Drone Impact Tests into Operational Safety Limits
---

# From Bench to Flight: Translating Drone Impact Tests into Operational Safety Limits
**arXiv**：[2602.05922v1](https://arxiv.org/abs/2602.05922) · [PDF](https://arxiv.org/pdf/2602.05922.pdf)  
**作者**：Aziz Mohamed Mili, Louis Catar, Paul Gérard, Ilyass Tabiai, David St-Onge  

**一句话要点**：提出端到端工具链，将无人机冲击测试转化为运行时安全限制，以保障室内近人操作安全。

**关键词**：无人机安全, 冲击测试, 数据驱动模型, 运行时限制, 室内操作, ROS2节点

## 3 点简述
- 室内微型飞行器近人操作缺乏基于冲击风险的运动限制调优方法。
- 开发可复制的冲击测试装置与数据驱动模型，将速度映射为冲击参数。
- 验证工具链在商用无人机上，在满足力约束的同时保持任务吞吐量。

## 摘要（原文）

> Indoor micro-aerial vehicles (MAVs) are increasingly used for tasks that require close proximity to people, yet practitioners lack practical methods to tune motion limits based on measured impact risk. We present an end-to-end, open toolchain that converts benchtop impact tests into deployable safety governors for drones. First, we describe a compact and replicable impact rig and protocol for capturing force-time profiles across drone classes and contact surfaces. Second, we provide data-driven models that map pre-impact speed to impulse and contact duration, enabling direct computation of speed bounds for a target force limit. Third, we release scripts and a ROS2 node that enforce these bounds online and log compliance, with support for facility-specific policies. We validate the workflow on multiple commercial off-the-shelf quadrotors and representative indoor assets, demonstrating that the derived governors preserve task throughput while meeting force constraints specified by safety stakeholders. Our contribution is a practical bridge from measured impacts to runtime limits, with shareable datasets, code, and a repeatable process that teams can adopt to certify indoor MAV operations near humans.

