---
layout: default
title: Open-Source Based and ETSI Compliant Cooperative, Connected, and Automated Mini-Cars
---

# Open-Source Based and ETSI Compliant Cooperative, Connected, and Automated Mini-Cars
**arXiv**：[2603.06343v1](https://arxiv.org/abs/2603.06343) · [PDF](https://arxiv.org/pdf/2603.06343.pdf)  
**作者**：Lorenzo Farina, Federico Gavioli, Salvatore Iandolo, Francesco Moretti, Giuseppe Perrone, Matteo Piccoli, Francesco Raviglione, Marco Rapelli, Antonio Solida, Paolo Burgio, Carlo Augusto Grazia, Alessandro Bazzi  

**一句话要点**：提出基于开源和ETSI标准的1:10比例协同、自动、连接迷你车平台，以降低实地测试成本。

**关键词**：协同智能交通系统, 开源平台, 迷你车测试, ETSI标准, ROS2, 交叉口碰撞预警

## 3 点简述
- 问题：从仿真到实地测试成本高昂，阻碍协同自动驾驶算法开发。
- 方法：使用Jetson Orin运行ROS2实现自主，Raspberry Pi运行OScar实现ETSI C-ITS标准连接。
- 实验：通过实现交叉口碰撞预警应用验证平台可行性和潜力。

## 摘要（原文）

> The automotive sector is following a revolutionary path from vehicles controlled by humans to vehicles that will be fully automated, fully connected, and ultimately fully cooperative. Along this road, new cooperative algorithms and protocols will be designed and field tested, which represents a great challenge in terms of costs. In this context, in particular, moving from simulations to practical experiments requires huge investments that are not always affordable and may become a barrier in some cases. To solve this issue and provide the community with an intermediate step, we here propose the use of 1:10 scaled cooperative, autonomous, and connected mini-cars. The mini-car is equipped with a Jetson Orin board running the open Robot Operating System 2 (ROS2), sensors for autonomous operations, and a Raspberry Pi board for connectivity mounting the open source Open Stack for Car (OScar). A key aspect of the proposal is the use of OScar, which implements a full ETSI cooperative-intelligent transport systems (C-ITS) compliant stack. The feasibility and potential of the proposed platform is here demonstrated through the implementation of a case study where the Day-1 intersection collision warning (ICW) application is implemented and validated.

