---
layout: default
title: Efficient Hierarchical Any-Angle Path Planning on Multi-Resolution 3D Grids
---

# Efficient Hierarchical Any-Angle Path Planning on Multi-Resolution 3D Grids
**arXiv**：[2602.21174v1](https://arxiv.org/abs/2602.21174) · [PDF](https://arxiv.org/pdf/2602.21174.pdf)  
**作者**：Victor Reijgwart, Cesar Cadena, Roland Siegwart, Lionel Ott  

**一句话要点**：提出基于多分辨率3D网格的层次化任意角度路径规划方法，以解决大规模高分辨率地图中的计算可扩展性问题。

**关键词**：路径规划, 多分辨率网格, 任意角度规划, 计算可扩展性, 3D环境导航

## 3 点简述
- 核心问题：传统搜索方法如A*在大规模高分辨率地图中面临计算可扩展性挑战，而采样和轨迹优化方法未充分利用地图的显式连通性信息。
- 方法要点：利用多分辨率表示，结合任意角度规划的最优性和完备性，通过连接障碍物角点生成直线段路径，提高计算效率。
- 实验或效果：在真实和合成环境中进行广泛实验，证明该方法在解质量和速度上优于基于采样的方法，并开源框架以促进社区研究。

## 摘要（原文）

> Hierarchical, multi-resolution volumetric mapping approaches are widely used to represent large and complex environments as they can efficiently capture their occupancy and connectivity information. Yet widely used path planning methods such as sampling and trajectory optimization do not exploit this explicit connectivity information, and search-based methods such as A* suffer from scalability issues in large-scale high-resolution maps. In many applications, Euclidean shortest paths form the underpinning of the navigation system. For such applications, any-angle planning methods, which find optimal paths by connecting corners of obstacles with straight-line segments, provide a simple and efficient solution. In this paper, we present a method that has the optimality and completeness properties of any-angle planners while overcoming computational tractability issues common to search-based methods by exploiting multi-resolution representations. Extensive experiments on real and synthetic environments demonstrate the proposed approach's solution quality and speed, outperforming even sampling-based methods. The framework is open-sourced to allow the robotics and planning community to build on our research.

