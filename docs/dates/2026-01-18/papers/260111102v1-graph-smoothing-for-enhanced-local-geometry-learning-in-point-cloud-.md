---
layout: default
title: Graph Smoothing for Enhanced Local Geometry Learning in Point Cloud Analysis
---

# Graph Smoothing for Enhanced Local Geometry Learning in Point Cloud Analysis
**arXiv**：[2601.11102v1](https://arxiv.org/abs/2601.11102) · [PDF](https://arxiv.org/pdf/2601.11102.pdf)  
**作者**：Shangbo Yuan, Jie Xu, Ping Hu, Xiaofeng Zhu, Na Zhao  

**一句话要点**：提出图平滑与增强局部几何学习模块以优化点云分析中的图结构问题

**关键词**：点云分析, 图平滑, 局部几何学习, 自适应几何描述子, 圆柱坐标变换, 三维视觉

## 3 点简述
- 核心问题：传统图方法在边界点稀疏连接和交叉区域噪声连接上存在结构缺陷
- 方法要点：引入图平滑模块优化图结构，结合自适应几何描述子和圆柱坐标变换增强局部几何特征
- 实验或效果：在真实数据集上验证了方法在分类、部件分割和语义分割任务中的有效性

## 摘要（原文）

> Graph-based methods have proven to be effective in capturing relationships among points for 3D point cloud analysis. However, these methods often suffer from suboptimal graph structures, particularly due to sparse connections at boundary points and noisy connections in junction areas. To address these challenges, we propose a novel method that integrates a graph smoothing module with an enhanced local geometry learning module. Specifically, we identify the limitations of conventional graph structures, particularly in handling boundary points and junction areas. In response, we introduce a graph smoothing module designed to optimize the graph structure and minimize the negative impact of unreliable sparse and noisy connections. Based on the optimized graph structure, we improve the feature extract function with local geometry information. These include shape features derived from adaptive geometric descriptors based on eigenvectors and distribution features obtained through cylindrical coordinate transformation. Experimental results on real-world datasets validate the effectiveness of our method in various point cloud learning tasks, i.e., classification, part segmentation, and semantic segmentation.

