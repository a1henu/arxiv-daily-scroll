---
layout: default
title: Quality-guided UAV Surface Exploration for 3D Reconstruction
---

# Quality-guided UAV Surface Exploration for 3D Reconstruction
**arXiv**：[2511.20353v1](https://arxiv.org/abs/2511.20353) · [PDF](https://arxiv.org/pdf/2511.20353.pdf)  
**作者**：Benjamin Sportich, Kenza Boubakri, Olivier Simonin, Alessandro Renzaglia  

**一句话要点**：提出基于重建质量引导的无人机表面探索框架，用于高效3D重建

**关键词**：无人机探索, 3D重建, NBV规划, TSDF表示, 自适应视点选择

## 3 点简述
- 核心问题：无人机自主探索中，现有规划策略未充分考虑重建质量与用户需求差异。
- 方法要点：引入模块化NBV规划，利用TSDF不确定性自适应生成和选择视点。
- 实验效果：仿真验证显示，在覆盖度、地图质量和路径效率上优于传统方法。

## 摘要（原文）

> Reasons for mapping an unknown environment with autonomous robots are wide-ranging, but in practice, they are often overlooked when developing planning strategies. Rapid information gathering and comprehensive structural assessment of buildings have different requirements and therefore necessitate distinct methodologies. In this paper, we propose a novel modular Next-Best-View (NBV) planning framework for aerial robots that explicitly uses a reconstruction quality objective to guide the exploration planning. In particular, our approach introduces new and efficient methods for view generation and selection of viewpoint candidates that are adaptive to the user-defined quality requirements, fully exploiting the uncertainty encoded in a Truncated Signed Distance field (TSDF) representation of the environment. This results in informed and efficient exploration decisions tailored towards the predetermined objective. Finally, we validate our method via extensive simulations in realistic environments. We demonstrate that it successfully adjusts its behavior to the user goal while consistently outperforming conventional NBV strategies in terms of coverage, quality of the final 3D map and path efficiency.

