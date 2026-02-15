---
layout: default
title: Resource-Aware Deployment Optimization for Collaborative Intrusion Detection in Layered Networks
---

# Resource-Aware Deployment Optimization for Collaborative Intrusion Detection in Layered Networks
**arXiv**：[2602.11851v1](https://arxiv.org/abs/2602.11851) · [PDF](https://arxiv.org/pdf/2602.11851.pdf)  
**作者**：André García Gómez, Ines Rieger, Wolfgang Hotwagner, Max Landauer, Markus Wurzenberger, Florian Skopik, Edgar Weippl  

**一句话要点**：提出资源感知的协作入侵检测框架，以优化分布式网络中的检测器部署。

**关键词**：协作入侵检测, 资源优化, 分布式网络, 动态部署, 边缘计算

## 3 点简述
- 核心问题：分布式关键基础设施需适应动态环境，现有CIDS架构部署灵活性不足。
- 方法要点：基于节点资源和数据类型动态优化检测器分配，实现低计算开销的快速适配。
- 实验或效果：使用真实网络攻击数据集评估，在边缘设备上实现自适应高效入侵检测。

## 摘要（原文）

> Collaborative Intrusion Detection Systems (CIDS) are increasingly adopted to counter cyberattacks, as their collaborative nature enables them to adapt to diverse scenarios across heterogeneous environments. As distributed critical infrastructure operates in rapidly evolving environments, such as drones in both civil and military domains, there is a growing need for CIDS architectures that can flexibly accommodate these dynamic changes. In this study, we propose a novel CIDS framework designed for easy deployment across diverse distributed environments. The framework dynamically optimizes detector allocation per node based on available resources and data types, enabling rapid adaptation to new operational scenarios with minimal computational overhead. We first conducted a comprehensive literature review to identify key characteristics of existing CIDS architectures. Based on these insights and real-world use cases, we developed our CIDS framework, which we evaluated using several distributed datasets that feature different attack chains and network topologies. Notably, we introduce a public dataset based on a realistic cyberattack targeting a ground drone aimed at sabotaging critical infrastructure. Experimental results demonstrate that the proposed CIDS framework can achieve adaptive, efficient intrusion detection in distributed settings, automatically reconfiguring detectors to maintain an optimal configuration, without requiring heavy computation, since all experiments were conducted on edge devices.

