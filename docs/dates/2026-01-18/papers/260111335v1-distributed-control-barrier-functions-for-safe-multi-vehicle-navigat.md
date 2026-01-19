---
layout: default
title: Distributed Control Barrier Functions for Safe Multi-Vehicle Navigation in Heterogeneous USV Fleets
---

# Distributed Control Barrier Functions for Safe Multi-Vehicle Navigation in Heterogeneous USV Fleets
**arXiv**：[2601.11335v1](https://arxiv.org/abs/2601.11335) · [PDF](https://arxiv.org/pdf/2601.11335.pdf)  
**作者**：Tyler Paine, Brendan Long, Jeremy Wenger, Michael DeFilippo, James Usevitch, Michael Benjamin  

**一句话要点**：提出分布式控制屏障函数方法，以解决异构无人船队安全导航中的碰撞避免问题。

**关键词**：分布式控制, 控制屏障函数, 无人船导航, 碰撞避免, 异构系统, 安全控制

## 3 点简述
- 核心问题：异构无人船队因决策与控制差异及实时信息共享限制，碰撞避免复杂化。
- 方法要点：基于控制屏障函数理论，为每艘船添加最坏情况假设的安全控制过滤器。
- 实验或效果：仿真与真实实验验证方法有效，结合COLREGS行为提升安全与效率。

## 摘要（原文）

> Collision avoidance in heterogeneous fleets of uncrewed vessels is challenging because the decision-making processes and controllers often differ between platforms, and it is further complicated by the limitations on sharing trajectories and control values in real-time. This paper presents a pragmatic approach that addresses these issues by adding a control filter on each autonomous vehicle that assumes worst-case behavior from other contacts, including crewed vessels. This distributed safety control filter is developed using control barrier function (CBF) theory and the application is clearly described to ensure explainability of these safety-critical methods. This work compares the worst-case CBF approach with a Collision Regulations (COLREGS) behavior-based approach in simulated encounters. Real-world experiments with three different uncrewed vessels and a human operated vessel were performed to confirm the approach is effective across a range of platforms and is robust to uncooperative behavior from human operators. Results show that combining both CBF methods and COLREGS behaviors achieves the best safety and efficiency.

