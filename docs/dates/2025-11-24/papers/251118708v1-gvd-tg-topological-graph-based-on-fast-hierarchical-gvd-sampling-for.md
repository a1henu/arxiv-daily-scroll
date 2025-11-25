---
layout: default
title: GVD-TG: Topological Graph based on Fast Hierarchical GVD Sampling for Robot Exploration
---

# GVD-TG: Topological Graph based on Fast Hierarchical GVD Sampling for Robot Exploration
**arXiv**：[2511.18708v1](https://arxiv.org/abs/2511.18708) · [PDF](https://arxiv.org/pdf/2511.18708.pdf)  
**作者**：Yanbin Li, Canran Xiao, Shenghai Yuan, Peilai Yu, Ziruo Li, Zhiguo Zhang, Wenzheng Chi, Wei Zhang  

**一句话要点**：提出基于分层GVD采样的拓扑图方法以提升机器人探索效率

**关键词**：机器人探索, 拓扑图, 广义Voronoi图, 分层采样, 连通性约束, 前沿提取

## 3 点简述
- 核心问题：实时更新准确且细节丰富的环境拓扑图在机器人探索中仍具挑战
- 方法要点：采用多粒度分层GVD生成、节点聚类与连通性约束，避免无效节点生成
- 实验或效果：通过对比测试验证系统性能优于SOTA方法，提高探索灵活性

## 摘要（原文）

> Topological maps are more suitable than metric maps for robotic exploration tasks. However, real-time updating of accurate and detail-rich environmental topological maps remains a challenge. This paper presents a topological map updating method based on the Generalized Voronoi Diagram (GVD). First, the newly observed areas are denoised to avoid low-efficiency GVD nodes misleading the topological structure. Subsequently, a multi-granularity hierarchical GVD generation method is designed to control the sampling granularity at both global and local levels. This not only ensures the accuracy of the topological structure but also enhances the ability to capture detail features, reduces the probability of path backtracking, and ensures no overlap between GVDs through the maintenance of a coverage map, thereby improving GVD utilization efficiency. Second, a node clustering method with connectivity constraints and a connectivity method based on a switching mechanism are designed to avoid the generation of unreachable nodes and erroneous nodes caused by obstacle attraction. A special cache structure is used to store all connectivity information, thereby improving exploration efficiency. Finally, to address the issue of frontiers misjudgment caused by obstacles within the scope of GVD units, a frontiers extraction method based on morphological dilation is designed to effectively ensure the reachability of frontiers. On this basis, a lightweight cost function is used to assess and switch to the next viewpoint in real time. This allows the robot to quickly adjust its strategy when signs of path backtracking appear, thereby escaping the predicament and increasing exploration flexibility. And the performance of system for exploration task is verified through comparative tests with SOTA methods.

