---
layout: default
title: A Generic Service-Oriented Function Offloading Framework for Connected Automated Vehicles
---

# A Generic Service-Oriented Function Offloading Framework for Connected Automated Vehicles
**arXiv**：[2602.08799v1](https://arxiv.org/abs/2602.08799) · [PDF](https://arxiv.org/pdf/2602.08799.pdf)  
**作者**：Robin Dehler, Michael Buchholz  

**一句话要点**：提出面向服务的通用函数卸载框架，以提升联网自动驾驶车辆的计算效率与服务质量。

**关键词**：函数卸载, 联网自动驾驶车辆, 服务质量, 轨迹规划, 多接入边缘计算

## 3 点简述
- 核心问题：联网自动驾驶车辆计算能力与能源有限，需通过任务卸载平衡本地与远程计算。
- 方法要点：设计通用框架，支持不同卸载决策算法与服务质量要求，并基于位置进行高效卸载。
- 实验或效果：在轨迹规划用例中，通过仿真和实际应用验证框架能保证服务质量并提升计算效率。

## 摘要（原文）

> Function offloading is a promising solution to address limitations concerning computational capacity and available energy of Connected Automated Vehicles~(CAVs) or other autonomous robots by distributing computational tasks between local and remote computing devices in form of distributed services. This paper presents a generic function offloading framework that can be used to offload an arbitrary set of computational tasks with a focus on autonomous driving. To provide flexibility, the function offloading framework is designed to incorporate different offloading decision making algorithms and quality of service~(QoS) requirements that can be adjusted to different scenarios or the objectives of the CAVs. With a focus on the applicability, we propose an efficient location-based approach, where the decision whether tasks are processed locally or remotely depends on the location of the CAV. We apply the proposed framework on the use case of service-oriented trajectory planning, where we offload the trajectory planning task of CAVs to a Multi-Access Edge Computing~(MEC) server. The evaluation is conducted in both simulation and real-world application. It demonstrates the potential of the function offloading framework to guarantee the QoS for trajectory planning while improving the computational efficiency of the CAVs. Moreover, the simulation results also show the adaptability of the framework to diverse scenarios involving simultaneous offloading requests from multiple CAVs.

