---
layout: default
title: OptMap: Geometric Map Distillation via Submodular Maximization
---

# OptMap: Geometric Map Distillation via Submodular Maximization
**arXiv**：[2512.07775v1](https://arxiv.org/abs/2512.07775) · [PDF](https://arxiv.org/pdf/2512.07775.pdf)  
**作者**：David Thorne, Nathan Chan, Christa S. Robison, Philip R. Osteen, Brett T. Lopez  

**一句话要点**：提出OptMap几何地图蒸馏算法，通过子模最大化实现实时应用特定地图生成

**关键词**：几何地图蒸馏, 子模最大化, LiDAR SLAM, 实时地图生成, 组合优化

## 3 点简述
- 核心问题：LiDAR数据丰富，但选择信息丰富、大小受限的地图是NP-hard组合优化问题
- 方法要点：利用子模奖励函数量化信息性，采用动态重排序流式子模算法减少输入集大小和顺序偏差
- 实验或效果：在开源和自定义数据集上测试，强调长时映射会话，计算需求最小，提供ROS包

## 摘要（原文）

> Autonomous robots rely on geometric maps to inform a diverse set of perception and decision-making algorithms. As autonomy requires reasoning and planning on multiple scales of the environment, each algorithm may require a different map for optimal performance. Light Detection And Ranging (LiDAR) sensors generate an abundance of geometric data to satisfy these diverse requirements, but selecting informative, size-constrained maps is computationally challenging as it requires solving an NP-hard combinatorial optimization. In this work we present OptMap: a geometric map distillation algorithm which achieves real-time, application-specific map generation via multiple theoretical and algorithmic innovations. A central feature is the maximization of set functions that exhibit diminishing returns, i.e., submodularity, using polynomial-time algorithms with provably near-optimal solutions. We formulate a novel submodular reward function which quantifies informativeness, reduces input set sizes, and minimizes bias in sequentially collected datasets. Further, we propose a dynamically reordered streaming submodular algorithm which improves empirical solution quality and addresses input order bias via an online approximation of the value of all scans. Testing was conducted on open-source and custom datasets with an emphasis on long-duration mapping sessions, highlighting OptMap's minimal computation requirements. Open-source ROS1 and ROS2 packages are available and can be used alongside any LiDAR SLAM algorithm.

