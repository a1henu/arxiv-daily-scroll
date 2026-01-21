---
layout: default
title: Resilient Routing: Risk-Aware Dynamic Routing in Smart Logistics via Spatiotemporal Graph Learning
---

# Resilient Routing: Risk-Aware Dynamic Routing in Smart Logistics via Spatiotemporal Graph Learning
**arXiv**：[2601.13632v1](https://arxiv.org/abs/2601.13632) · [PDF](https://arxiv.org/pdf/2601.13632.pdf)  
**作者**：Zhiming Xue, Sichen Zhao, Yalun Qi, Xianling Zeng, Zihan Yu  

**一句话要点**：提出风险感知动态路由框架，通过时空图学习优化智能物流路径规划以应对拥堵和需求波动。

**关键词**：智能物流, 时空图神经网络, 动态路由, 风险预测, 组合优化

## 3 点简述
- 核心问题：传统静态路由策略难以应对物流网络中的交通拥堵和需求波动，影响供应链韧性。
- 方法要点：结合时空图神经网络与组合优化，利用GCN和GRU预测拥堵风险，动态调整路径权重。
- 实验或效果：在真实物联网数据集上验证，高拥堵场景下风险暴露降低19.3%，运输距离仅增2.1%。

## 摘要（原文）

> With the rapid development of the e-commerce industry, the logistics network is experiencing unprecedented pressure. The traditional static routing strategy most time cannot tolerate the traffic congestion and fluctuating retail demand. In this paper, we propose a Risk-Aware Dynamic Routing(RADR) framework which integrates Spatiotemporal Graph Neural Networks (ST-GNN) with combinatorial optimization. We first construct a logistics topology graph by using the discrete GPS data using spatial clustering methods. Subsequently, a hybrid deep learning model combining Graph Convolutional Network (GCN) and Gated Recurrent Unit (GRU) is adopted to extract spatial correlations and temporal dependencies for predicting future congestion risks. These prediction results are then integrated into a dynamic edge weight mechanism to perform path planning. We evaluated the framework on the Smart Logistics Dataset 2024, which contains real-world Internet of Things(IoT) sensor data. The experimental results show that the RADR algorithm significantly enhances the resilience of the supply chain. Particularly in the case study of high congestion scenarios, our method reduces the potential congestion risk exposure by 19.3% while only increasing the transportation distance by 2.1%. This empirical evidence confirms that the proposed data-driven approach can effectively balance delivery efficiency and operational safety.

