---
layout: default
title: Count Every Rotation and Every Rotation Counts: Exploring Drone Dynamics via Propeller Sensing
---

# Count Every Rotation and Every Rotation Counts: Exploring Drone Dynamics via Propeller Sensing
**arXiv**：[2511.13100v1](https://arxiv.org/abs/2511.13100) · [PDF](https://arxiv.org/pdf/2511.13100.pdf)  
**作者**：Xuecheng Chen, Jingao Xu, Wenhua Ding, Haoyang Wang, Xinyu Luo, Ruiyang Duan, Jialong Chen, Xueqian Wang, Yunhao Liu, Xinlei Chen  

**一句话要点**：提出基于事件相机的无人机螺旋桨转速感知系统，以提升地面非接触式无人机感知性能。

**关键词**：无人机感知, 事件相机, 螺旋桨转速估计, 非接触式传感, 动态推断

## 3 点简述
- 核心问题：无人机应用中，地面非接触式感知无人机面临挑战，需高精度实时监测。
- 方法要点：利用事件相机估计螺旋桨转速，通过降噪和动态推断实现无人机状态感知。
- 实验或效果：在真实交付场景中，实现3ms延迟、0.23%转速误差和96.5%命令推断精度。

## 摘要（原文）

> As drone-based applications proliferate, paramount contactless sensing of airborne drones from the ground becomes indispensable. This work demonstrates concentrating on propeller rotational speed will substantially improve drone sensing performance and proposes an event-camera-based solution, \sysname. \sysname features two components: \textit{Count Every Rotation} achieves accurate, real-time propeller speed estimation by mitigating ultra-high sensitivity of event cameras to environmental noise. \textit{Every Rotation Counts} leverages these speeds to infer both internal and external drone dynamics. Extensive evaluations in real-world drone delivery scenarios show that \sysname achieves a sensing latency of 3$ms$ and a rotational speed estimation error of merely 0.23\%. Additionally, \sysname infers drone flight commands with 96.5\% precision and improves drone tracking accuracy by over 22\% when combined with other sensing modalities. \textit{ Demo: {\color{blue}https://eventpro25.github.io/EventPro/.} }

