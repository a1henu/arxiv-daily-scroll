---
layout: default
title: A Hierarchical, Model-Based System for High-Performance Humanoid Soccer
---

# A Hierarchical, Model-Based System for High-Performance Humanoid Soccer
**arXiv**：[2512.09431v1](https://arxiv.org/abs/2512.09431) · [PDF](https://arxiv.org/pdf/2512.09431.pdf)  
**作者**：Quanyou Wang, Mingzhang Zhu, Ruochen Hou, Kay Gillespie, Alvin Zhu, Shiqi Wang, Yicheng Wang, Gaberiel I. Fernandez, Yeting Liu, Colin Togashi, Hyunwoo Nam, Aditya Navghare, Alex Xu, Taoyuanmin Zhu, Min Sung Ahn, Arturo Flores Alvarez, Justin Quan, Ethan Hong, Dennis W. Hong  

**一句话要点**：提出硬件与软件创新系统，助力ARTEMIS赢得2024年RoboCup成人尺寸人形足球赛冠军。

**关键词**：人形机器人, RoboCup足球, 硬件设计, 软件系统, 感知定位, 行为管理

## 3 点简述
- 核心问题：在动态对抗的RoboCup比赛中实现高性能人形足球机器人，需兼顾硬件轻量化、高扭矩驱动和软件感知定位集成。
- 方法要点：硬件采用轻质结构、准直驱执行器和专用足部设计；软件结合立体视觉、目标检测与地标融合，集成导航与行为管理。
- 实验或效果：系统在真实比赛中展现快速、精确和战术有效的表现，支持ARTEMIS夺冠，验证了整体设计的鲁棒性。

## 摘要（原文）

> The development of athletic humanoid robots has gained significant attention as advances in actuation, sensing, and control enable increasingly dynamic, real-world capabilities. RoboCup, an international competition of fully autonomous humanoid robots, provides a uniquely challenging benchmark for such systems, culminating in the long-term goal of competing against human soccer players by 2050. This paper presents the hardware and software innovations underlying our team's victory in the RoboCup 2024 Adult-Sized Humanoid Soccer Competition. On the hardware side, we introduce an adult-sized humanoid platform built with lightweight structural components, high-torque quasi-direct-drive actuators, and a specialized foot design that enables powerful in-gait kicks while preserving locomotion robustness. On the software side, we develop an integrated perception and localization framework that combines stereo vision, object detection, and landmark-based fusion to provide reliable estimates of the ball, goals, teammates, and opponents. A mid-level navigation stack then generates collision-aware, dynamically feasible trajectories, while a centralized behavior manager coordinates high-level decision making, role selection, and kick execution based on the evolving game state. The seamless integration of these subsystems results in fast, precise, and tactically effective gameplay, enabling robust performance under the dynamic and adversarial conditions of real matches. This paper presents the design principles, system architecture, and experimental results that contributed to ARTEMIS's success as the 2024 Adult-Sized Humanoid Soccer champion.

