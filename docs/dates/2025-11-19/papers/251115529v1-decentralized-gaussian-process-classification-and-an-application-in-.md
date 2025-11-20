---
layout: default
title: Decentralized Gaussian Process Classification and an Application in Subsea Robotics
---

# Decentralized Gaussian Process Classification and an Application in Subsea Robotics
**arXiv**：[2511.15529v1](https://arxiv.org/abs/2511.15529) · [PDF](https://arxiv.org/pdf/2511.15529.pdf)  
**作者**：Yifei Gao, Hans J. He, Daniel J. Stilwell, James McMahon  

**一句话要点**：提出去中心化高斯过程分类与数据共享策略，以解决水下机器人通信不确定性。

**关键词**：去中心化分类, 高斯过程, 水下机器人, 声学通信, 数据共享策略, 实时地图构建

## 3 点简述
- 核心问题：水下机器人团队在受限声学通信环境下，实时构建通信成功概率地图。
- 方法要点：设计数据共享策略，选择测量值共享，实现去中心化分类。
- 实验或效果：使用真实声学数据验证，策略在水下环境中有效。

## 摘要（原文）

> Teams of cooperating autonomous underwater vehicles (AUVs) rely on acoustic communication for coordination, yet this communication medium is constrained by limited range, multi-path effects, and low bandwidth. One way to address the uncertainty associated with acoustic communication is to learn the communication environment in real-time. We address the challenge of a team of robots building a map of the probability of communication success from one location to another in real-time. This is a decentralized classification problem -- communication events are either successful or unsuccessful -- where AUVs share a subset of their communication measurements to build the map. The main contribution of this work is a rigorously derived data sharing policy that selects measurements to be shared among AUVs. We experimentally validate our proposed sharing policy using real acoustic communication data collected from teams of Virginia Tech 690 AUVs, demonstrating its effectiveness in underwater environments.

