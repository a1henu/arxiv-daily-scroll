---
layout: default
title: LitS: A novel Neighborhood Descriptor for Point Clouds
---

# LitS: A novel Neighborhood Descriptor for Point Clouds
**arXiv**：[2602.04838v1](https://arxiv.org/abs/2602.04838) · [PDF](https://arxiv.org/pdf/2602.04838.pdf)  
**作者**：Jonatan B. Bastos, Francisco F. Rivera, Oscar G. Lorenzo, David L. Vilariño, José C. Cabaleiro, Alberto M. Esmorís, Tomás F. Pena  

**一句话要点**：提出LitS点云邻域描述符，用于捕捉局部几何结构并适应密度变化和噪声。

**关键词**：点云分析, 邻域描述符, 局部几何, 方向性统计, 鲁棒性, 分段常数函数

## 3 点简述
- 核心问题：点云分析依赖邻域描述符以准确表征局部几何，现有方法可能对密度变化和噪声敏感。
- 方法要点：LitS是基于单位圆的分段常数函数，通过方向性锥形区域统计邻居数量，提供两种版本和可调参数。
- 实验或效果：LitS能捕捉点排列细节，对密度变化和噪声具有鲁棒性，适用于多种点云类型。

## 摘要（原文）

> With the advancement of 3D scanning technologies, point clouds have become fundamental for representing 3D spatial data, with applications that span across various scientific and technological fields. Practical analysis of this data depends crucially on available neighborhood descriptors to accurately characterize the local geometries of the point cloud. This paper introduces LitS, a novel neighborhood descriptor for 2D and 3D point clouds. LitS are piecewise constant functions on the unit circle that allow points to keep track of their surroundings. Each element in LitS' domain represents a direction with respect to a local reference system. Once constructed, evaluating LitS at any given direction gives us information about the number of neighbors in a cone-like region centered around that same direction. Thus, LitS conveys a lot of information about the local neighborhood of a point, which can be leveraged to gain global structural understanding by analyzing how LitS changes between close points. In addition, LitS comes in two versions ('regular' and 'cumulative') and has two parameters, allowing them to adapt to various contexts and types of point clouds. Overall, they are a versatile neighborhood descriptor, capable of capturing the nuances of local point arrangements and resilient to common point cloud data issues such as variable density and noise.

