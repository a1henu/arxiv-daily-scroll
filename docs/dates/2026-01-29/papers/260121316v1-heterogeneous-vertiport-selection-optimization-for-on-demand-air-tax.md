---
layout: default
title: Heterogeneous Vertiport Selection Optimization for On-Demand Air Taxi Services: A Deep Reinforcement Learning Approach
---

# Heterogeneous Vertiport Selection Optimization for On-Demand Air Taxi Services: A Deep Reinforcement Learning Approach
**arXiv**：[2601.21316v1](https://arxiv.org/abs/2601.21316) · [PDF](https://arxiv.org/pdf/2601.21316.pdf)  
**作者**：Aoyu Pang, Maonan Wang, Zifan Sha, Wenwei Yue, Changle Li, Chung Shue Chen, Man-On Pun  

**一句话要点**：提出统一空陆移动协调框架，通过深度强化学习优化垂直起降机场选择以提升按需空中出租车服务效率。

**关键词**：城市空中移动, 深度强化学习, 垂直起降机场选择, 空陆移动协调, V2X通信, 多模态交通优化

## 3 点简述
- 核心问题：现有研究缺乏对空陆移动系统中乘客最优集成路由策略的系统探索，难以实现高效无缝门到门旅行。
- 方法要点：构建统一优化模型，结合深度强化学习和V2X通信，动态规划空中出租车路线和垂直起降机场选择。
- 实验或效果：相比传统比例分配方法，平均旅行时间减少34%，提升了整体旅行效率。

## 摘要（原文）

> Urban Air Mobility (UAM) has emerged as a transformative solution to alleviate urban congestion by utilizing low-altitude airspace, thereby reducing pressure on ground transportation networks. To enable truly efficient and seamless door-to-door travel experiences, UAM requires close integration with existing ground transportation infrastructure. However, current research on optimal integrated routing strategies for passengers in air-ground mobility systems remains limited, with a lack of systematic exploration.To address this gap, we first propose a unified optimization model that integrates strategy selection for both air and ground transportation. This model captures the dynamic characteristics of multimodal transport networks and incorporates real-time traffic conditions alongside passenger decision-making behavior. Building on this model, we propose a Unified Air-Ground Mobility Coordination (UAGMC) framework, which leverages deep reinforcement learning (RL) and Vehicle-to-Everything (V2X) communication to optimize vertiport selection and dynamically plan air taxi routes. Experimental results demonstrate that UAGMC achieves a 34\% reduction in average travel time compared to conventional proportional allocation methods, enhancing overall travel efficiency and providing novel insights into the integration and optimization of multimodal transportation systems. This work lays a solid foundation for advancing intelligent urban mobility solutions through the coordination of air and ground transportation modes. The related code can be found at https://github.com/Traffic-Alpha/UAGMC.

