---
layout: default
title: AlignDrive: Aligned Lateral-Longitudinal Planning for End-to-End Autonomous Driving
---

# AlignDrive: Aligned Lateral-Longitudinal Planning for End-to-End Autonomous Driving
**arXiv**：[2601.01762v1](https://arxiv.org/abs/2601.01762) · [PDF](https://arxiv.org/pdf/2601.01762.pdf)  
**作者**：Yanhao Wu, Haoyang Zhang, Fei He, Rui Wu, Congpei Qiu, Liang Gao, Wei Ke, Tong Zhang  

**一句话要点**：提出AlignDrive框架，通过级联设计解决端到端自动驾驶中横向与纵向规划协调问题

**关键词**：端到端自动驾驶, 横向纵向规划, 路径条件化, 级联框架, 数据增强, 安全关键事件

## 3 点简述
- 核心问题：现有端到端模型并行预测横向与纵向规划，易导致路径与速度不协调及静态信息冗余编码
- 方法要点：引入路径条件化纵向规划，基于驾驶路径预测纵向位移，简化推理并增强横向纵向耦合
- 实验或效果：在Bench2Drive基准测试中，驾驶分数达89.07%，成功率73.18%，显著提升协调性与安全性

## 摘要（原文）

> End-to-end autonomous driving has rapidly progressed, enabling joint perception and planning in complex environments. In the planning stage, state-of-the-art (SOTA) end-to-end autonomous driving models decouple planning into parallel lateral and longitudinal predictions. While effective, this parallel design can lead to i) coordination failures between the planned path and speed, and ii) underutilization of the drive path as a prior for longitudinal planning, thus redundantly encoding static information. To address this, we propose a novel cascaded framework that explicitly conditions longitudinal planning on the drive path, enabling coordinated and collision-aware lateral and longitudinal planning. Specifically, we introduce a path-conditioned formulation that explicitly incorporates the drive path into longitudinal planning. Building on this, the model predicts longitudinal displacements along the drive path rather than full 2D trajectory waypoints. This design simplifies longitudinal reasoning and more tightly couples it with lateral planning. Additionally, we introduce a planning-oriented data augmentation strategy that simulates rare safety-critical events, such as vehicle cut-ins, by adding agents and relabeling longitudinal targets to avoid collision. Evaluated on the challenging Bench2Drive benchmark, our method sets a new SOTA, achieving a driving score of 89.07 and a success rate of 73.18%, demonstrating significantly improved coordination and safety

