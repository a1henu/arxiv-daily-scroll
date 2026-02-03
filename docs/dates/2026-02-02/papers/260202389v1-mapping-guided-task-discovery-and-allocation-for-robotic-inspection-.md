---
layout: default
title: Mapping-Guided Task Discovery and Allocation for Robotic Inspection of Underwater Structures
---

# Mapping-Guided Task Discovery and Allocation for Robotic Inspection of Underwater Structures
**arXiv**：[2602.02389v1](https://arxiv.org/abs/2602.02389) · [PDF](https://arxiv.org/pdf/2602.02389.pdf)  
**作者**：Marina Ruediger, Ashis G. Banerjee  

**一句话要点**：提出基于SLAM数据的任务发现与分配方法，以优化水下结构多机器人巡检

**关键词**：水下机器人巡检, 任务发现与分配, SLAM数据优化, 多机器人系统, 结构缺陷检测

## 3 点简述
- 核心问题：水下结构巡检中，无先验几何知识时如何生成和优化多机器人任务
- 方法要点：利用SLAM网格生成任务，通过关键点评分和距离剪枝进行优化，考虑硬件和环境因素
- 实验或效果：通过水下测试验证算法有效性，并与Voronoi分区和Boustrophedon模式比较覆盖效果

## 摘要（原文）

> Task generation for underwater multi-robot inspections without prior knowledge of existing geometry can be achieved and optimized through examination of simultaneous localization and mapping (SLAM) data. By considering hardware parameters and environmental conditions, a set of tasks is generated from SLAM meshes and optimized through expected keypoint scores and distance-based pruning. In-water tests are used to demonstrate the effectiveness of the algorithm and determine the appropriate parameters. These results are compared to simulated Voronoi partitions and boustrophedon patterns for inspection coverage on a model of the test environment. The key benefits of the presented task discovery method include adaptability to unexpected geometry and distributions that maintain coverage while focusing on areas more likely to present defects or damage.

