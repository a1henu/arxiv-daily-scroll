---
layout: default
title: How to rewrite the stars: Mapping your orchard over time through constellations of fruits
---

# How to rewrite the stars: Mapping your orchard over time through constellations of fruits
**arXiv**：[2602.04722v1](https://arxiv.org/abs/2602.04722) · [PDF](https://arxiv.org/pdf/2602.04722.pdf)  
**作者**：Gonçalo P. Matos, Carlos Santiago, João P. Costeira, Ricardo L. Saldanha, Ernesto M. Morgado  

**一句话要点**：提出基于3D质心星座的方法，以匹配不同时间视频中的果实，解决果园果实生长跟踪问题。

**关键词**：果实跟踪, 3D点云匹配, 果园地图构建, 计算机视觉, 精准农业, 机器人导航

## 3 点简述
- 核心问题：匹配不同日期视频中的同一果实，以跟踪生长，现有方法依赖固定相机位置或GPS数据。
- 方法要点：使用3D质心星座和稀疏点云描述符，匹配星座而非单个果实，处理非刚性、遮挡和特征少的情况。
- 实验或效果：方法成功匹配果实，构建果园地图，支持6DoF相机定位，用于机器人自主导航和选择性采摘。

## 摘要（原文）

> Following crop growth through the vegetative cycle allows farmers to predict fruit setting and yield in early stages, but it is a laborious and non-scalable task if performed by a human who has to manually measure fruit sizes with a caliper or dendrometers. In recent years, computer vision has been used to automate several tasks in precision agriculture, such as detecting and counting fruits, and estimating their size. However, the fundamental problem of matching the exact same fruits from one video, collected on a given date, to the fruits visible in another video, collected on a later date, which is needed to track fruits' growth through time, remains to be solved. Few attempts were made, but they either assume that the camera always starts from the same known position and that there are sufficiently distinct features to match, or they used other sources of data like GPS. Here we propose a new paradigm to tackle this problem, based on constellations of 3D centroids, and introduce a descriptor for very sparse 3D point clouds that can be used to match fruits across videos. Matching constellations instead of individual fruits is key to deal with non-rigidity, occlusions and challenging imagery with few distinct visual features to track. The results show that the proposed method can be successfully used to match fruits across videos and through time, and also to build an orchard map and later use it to locate the camera pose in 6DoF, thus providing a method for autonomous navigation of robots in the orchard and for selective fruit picking, for example.

