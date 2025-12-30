---
layout: default
title: Beyond Coverage Path Planning: Can UAV Swarms Perfect Scattered Regions Inspections?
---

# Beyond Coverage Path Planning: Can UAV Swarms Perfect Scattered Regions Inspections?
**arXiv**：[2512.23257v1](https://arxiv.org/abs/2512.23257) · [PDF](https://arxiv.org/pdf/2512.23257.pdf)  
**作者**：Socratis Gkelios, Savvas D. Apostolidis, Pavlos Ch. Kapoutsis, Elias B. Kosmatopoulos, Athanasios Ch. Kapoutsis  

**一句话要点**：提出多无人机分散区域快速巡检方法mUDAI，以优化无人机群对非连接兴趣区域的检查效率。

**关键词**：无人机巡检, 路径规划优化, 分散区域检查, 多无人机协同, 资源效率

## 3 点简述
- 核心问题：无人机电池限制和传统覆盖路径规划在检查多个非连接兴趣区域时效率低下。
- 方法要点：mUDAI方法通过双重优化计算最佳图像采集位置和无人机轨迹，平衡数据分辨率与操作时间。
- 实验或效果：结合仿真和真实部署验证，mUDAI能提高操作效率并保持高质量数据采集，适用于安全评估等场景。

## 摘要（原文）

> Unmanned Aerial Vehicles (UAVs) have revolutionized inspection tasks by offering a safer, more efficient, and flexible alternative to traditional methods. However, battery limitations often constrain their effectiveness, necessitating the development of optimized flight paths and data collection techniques. While existing approaches like coverage path planning (CPP) ensure comprehensive data collection, they can be inefficient, especially when inspecting multiple non connected Regions of Interest (ROIs). This paper introduces the Fast Inspection of Scattered Regions (FISR) problem and proposes a novel solution, the multi UAV Disjoint Areas Inspection (mUDAI) method. The introduced approach implements a two fold optimization procedure, for calculating the best image capturing positions and the most efficient UAV trajectories, balancing data resolution and operational time, minimizing redundant data collection and resource consumption. The mUDAI method is designed to enable rapid, efficient inspections of scattered ROIs, making it ideal for applications such as security infrastructure assessments, agricultural inspections, and emergency site evaluations. A combination of simulated evaluations and real world deployments is used to validate and quantify the method's ability to improve operational efficiency while preserving high quality data capture, demonstrating its effectiveness in real world operations. An open source Python implementation of the mUDAI method can be found on GitHub (https://github.com/soc12/mUDAI) and the collected and processed data from the real world experiments are all hosted on Zenodo (https://zenodo.org/records/13866483). Finally, this online platform (https://sites.google.com/view/mudai-platform/) allows interested readers to interact with the mUDAI method and generate their own multi UAV FISR missions.

