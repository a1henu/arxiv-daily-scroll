---
layout: default
title: A Beacon Based Solution for Autonomous UUVs GNSS-Denied Stealthy Navigation
---

# A Beacon Based Solution for Autonomous UUVs GNSS-Denied Stealthy Navigation
**arXiv**：[2601.15802v1](https://arxiv.org/abs/2601.15802) · [PDF](https://arxiv.org/pdf/2601.15802.pdf)  
**作者**：Alexandre Albore, Humbert Fiorino, Damien Pellier  

**一句话要点**：提出基于信标的解决方案，用于自主无人水下航行器在GNSS拒止环境下的隐蔽导航

**关键词**：自主无人水下航行器, GNSS拒止导航, 信标网络, 声学定位, 分层路径规划, 隐蔽操作

## 3 点简述
- 核心问题：自主无人水下航行器在沿海区域需隐蔽导航，但无法依赖GNSS或支援船只，面临定位与路径规划挑战
- 方法要点：通过空中或水面无人机部署信标网络，建立合成地标，利用声学信号进行定位，并结合分层规划器生成自适应路径
- 实验或效果：未知，论文未提及具体实验或效果数据

## 摘要（原文）

> Autonomous Unmanned Underwater Vehicles (UUVs) enable military and civilian covert operations in coastal areas without relying on support vessels or Global Navigation Satellite Systems (GNSS). Such operations are critical when surface access is not possible and stealthy navigation is required in restricted environments such as protected zones or dangerous areas under access ban. GNSS denied navigation is then essential to maintaining concealment as surfacing could expose UUVs to detection. To ensure a precise fleet positioning a constellation of beacons deployed by aerial or surface drones establish a synthetic landmark network that will guide the fleet of UUVs along an optimized path from the continental shelf to the goal on the shore. These beacons either submerged or floating emit acoustic signals for UUV localisation and navigation. A hierarchical planner generates an adaptive route for the drones executing primitive actions while continuously monitoring and replanning as needed to maintain trajectory accuracy.

