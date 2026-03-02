---
layout: default
title: A Reliable Indoor Navigation System for Humans Using AR-based Technique
---

# A Reliable Indoor Navigation System for Humans Using AR-based Technique
**arXiv**：[2602.23706v1](https://arxiv.org/abs/2602.23706) · [PDF](https://arxiv.org/pdf/2602.23706.pdf)  
**作者**：Vijay U. Rathod, Manav S. Sharma, Shambhavi Verma, Aadi Joshi, Sachin Aage, Sujal Shahane  

**一句话要点**：提出基于AR和A*算法的室内导航系统，以解决校园和小区域导航不可靠问题。

**关键词**：室内导航, 增强现实, A*算法, 路径规划, 环境建模, 用户体验

## 3 点简述
- 核心问题：室内导航缺乏可靠系统，依赖静态标识或地图，导致用户困惑和耗时。
- 方法要点：使用Vuforia Area Target进行环境建模，结合AI导航的NavMesh组件和A*算法计算最短路径。
- 实验或效果：相比传统方法，显著提升导航准确性、用户体验和效率，但需优化NavMesh以适应大型或动态环境。

## 摘要（原文）

> Reliable navigation systems are not available indoors, such as in campuses and small areas. Users must depend on confusing, time-consuming static signage or floor maps. In this paper, an AR-based technique has been applied to campus and small-site navigation, where Vuforia Area Target is used for environment modeling. AI navigation's NavMesh component is used for navigation purposes, and the A* algorithm is used within this component for shortest path calculation. Compared to Dijkstra's algorithm, it can reach a solution about two to three times faster for smaller search spaces. In many cases, Dijkstra's algorithm has difficulty performing well in high-complexity environments where memory usage grows and processing times increase. Compared to older approaches such as GPS, real-time processing and AR overlays can be combined to provide intuitive directions for users while dynamically updating the path in response to environmental changes. Experimental results indicate significantly improved navigation accuracy, better user experience, and greater efficiency compared to traditional methods. These results show that AR technology integrated with existing pathfinding algorithms is feasible and scalable, making it a user-friendly solution for indoor navigation. Although highly effective in limited and defined indoor spaces, further optimization of NavMesh is required for large or highly dynamic environments.

