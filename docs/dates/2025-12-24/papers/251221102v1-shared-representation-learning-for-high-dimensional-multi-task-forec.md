---
layout: default
title: Shared Representation Learning for High-Dimensional Multi-Task Forecasting under Resource Contention in Cloud-Native Backends
---

# Shared Representation Learning for High-Dimensional Multi-Task Forecasting under Resource Contention in Cloud-Native Backends
**arXiv**：[2512.21102v1](https://arxiv.org/abs/2512.21102) · [PDF](https://arxiv.org/pdf/2512.21102.pdf)  
**作者**：Zixiao Huang, Jixiao Yang, Sijia Li, Chi Zhang, Jinyu Chen, Chengda Xu  

**一句话要点**：提出统一预测框架以解决云原生后端高维多任务时序预测问题

**关键词**：时序预测, 云原生系统, 多任务学习, 共享表示学习, 资源竞争, 动态调整机制

## 3 点简述
- 核心问题：云原生后端系统在高动态负载、耦合指标和并行任务下的预测需求
- 方法要点：构建共享编码结构、状态融合机制和跨任务结构传播模块
- 实验或效果：在多种误差指标上表现优异，验证了框架的有效性和适应性

## 摘要（原文）

> This study proposes a unified forecasting framework for high-dimensional multi-task time series to meet the prediction demands of cloud native backend systems operating under highly dynamic loads, coupled metrics, and parallel tasks. The method builds a shared encoding structure to represent diverse monitoring indicators in a unified manner and employs a state fusion mechanism to capture trend changes and local disturbances across different time scales. A cross-task structural propagation module is introduced to model potential dependencies among nodes, enabling the model to understand complex structural patterns formed by resource contention, link interactions, and changes in service topology. To enhance adaptability to non-stationary behaviors, the framework incorporates a dynamic adjustment mechanism that automatically regulates internal feature flows according to system state changes, ensuring stable predictions in the presence of sudden load shifts, topology drift, and resource jitter. The experimental evaluation compares multiple models across various metrics and verifies the effectiveness of the framework through analyses of hyperparameter sensitivity, environmental sensitivity, and data sensitivity. The results show that the proposed method achieves superior performance on several error metrics and provides more accurate representations of future states under different operating conditions. Overall, the unified forecasting framework offers reliable predictive capability for high-dimensional, multi-task, and strongly dynamic environments in cloud native systems and provides essential technical support for intelligent backend management.

