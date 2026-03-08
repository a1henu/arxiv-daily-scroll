---
layout: default
title: From Code to Road: A Vehicle-in-the-Loop and Digital Twin-Based Framework for Central Car Server Testing in Autonomous Driving
---

# From Code to Road: A Vehicle-in-the-Loop and Digital Twin-Based Framework for Central Car Server Testing in Autonomous Driving
**arXiv**：[2603.05279v1](https://arxiv.org/abs/2603.05279) · [PDF](https://arxiv.org/pdf/2603.05279.pdf)  
**作者**：Chengdong Wu, Sven Kirchner, Nils Purschke, Axel Torschmied, Norbert Kroth, Yinglei Song, André Schamschurko, Erik Leo Haß, Kuo-Yi Chao, Yi Zhang, Nenad Petrovic, Alois C. Knoll  

**一句话要点**：提出基于车辆在环与数字孪生的中央汽车服务器测试框架，以解决自动驾驶集中式架构验证难题。

**关键词**：车辆在环测试, 数字孪生, 自动驾驶验证, 集中式电子电气架构, 虚拟-物理集成

## 3 点简述
- 核心问题：纯虚拟仿真难以准确捕捉所有现实因素，影响自动驾驶软件测试效果。
- 方法要点：结合物理测试车辆与同步虚拟副本，实现安全、可重复、现实的虚拟-物理集成测试。
- 实验或效果：案例研究验证框架在不同测试场景中的有效性，减少早期硬件集成需求。

## 摘要（原文）

> Simulation is one of the most essential parts in the development stage of automotive software. However, purely virtual simulations often struggle to accurately capture all real-world factors due to limitations in modeling. To address this challenge, this work presents a test framework for automotive software on the centralized E/E architecture, which is a central car server in our case, based on Vehicle-in-the-Loop (ViL) and digital twin technology. The framework couples a physical test vehicle on a dynamometer test bench with its synchronized virtual counterpart in a simulation environment. Our approach provides a safe, reproducible, realistic, and cost-effective platform for validating autonomous driving algorithms with a centralized architecture. This test method eliminates the need to test individual physical ECUs and their communication protocols separately. In contrast to traditional ViL methods, the proposed framework runs the full autonomous driving software directly on the vehicle hardware after the simulation process, eliminating flashing and intermediate layers while enabling seamless virtual-physical integration and accurately reflecting centralized E/E behavior. In addition, incorporating mixed testing in both simulated and physical environments reduces the need for full hardware integration during the early stages of automotive development. Experimental case studies demonstrate the effectiveness of the framework in different test scenarios. These findings highlight the potential to reduce development and integration efforts for testing autonomous driving pipelines in the future.

