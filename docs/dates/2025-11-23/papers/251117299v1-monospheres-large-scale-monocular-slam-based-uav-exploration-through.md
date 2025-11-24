---
layout: default
title: MonoSpheres: Large-Scale Monocular SLAM-Based UAV Exploration through Perception-Coupled Mapping and Planning
---

# MonoSpheres: Large-Scale Monocular SLAM-Based UAV Exploration through Perception-Coupled Mapping and Planning
**arXiv**：[2511.17299v1](https://arxiv.org/abs/2511.17299) · [PDF](https://arxiv.org/pdf/2511.17299.pdf)  
**作者**：Tomáš Musil, Matěj Petrlík, Martin Saska  

**一句话要点**：提出MonoSpheres方法，通过感知耦合的建图与规划实现单目SLAM无人机大规模探索

**关键词**：单目SLAM, 无人机探索, 感知耦合规划, 稀疏深度建图, 前沿探索, 不确定性处理

## 3 点简述
- 核心问题：单目相机在未知环境中自主探索时，深度数据稀疏、自由空间间隙和深度不确定性大。
- 方法要点：建图模块过采样纹理稀疏区域，规划模块快速重规划并感知感知航向控制。
- 实验或效果：在真实和模拟环境中广泛评估，首次实现真实世界非结构化户外3D单目探索。

## 摘要（原文）

> Autonomous exploration of unknown environments is a key capability for mobile robots, but it is largely unsolved for robots equipped with only a single monocular camera and no dense range sensors. In this paper, we present a novel approach to monocular vision-based exploration that can safely cover large-scale unstructured indoor and outdoor 3D environments by explicitly accounting for the properties of a sparse monocular SLAM frontend in both mapping and planning. The mapping module solves the problems of sparse depth data, free-space gaps, and large depth uncertainty by oversampling free space in texture-sparse areas and keeping track of obstacle position uncertainty. The planning module handles the added free-space uncertainty through rapid replanning and perception-aware heading control. We further show that frontier-based exploration is possible with sparse monocular depth data when parallax requirements and the possibility of textureless surfaces are taken into account. We evaluate our approach extensively in diverse real-world and simulated environments, including ablation studies. To the best of the authors' knowledge, the proposed method is the first to achieve 3D monocular exploration in real-world unstructured outdoor environments. We open-source our implementation to support future research.

