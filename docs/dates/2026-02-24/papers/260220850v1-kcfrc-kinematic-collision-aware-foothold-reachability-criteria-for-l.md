---
layout: default
title: KCFRC: Kinematic Collision-Aware Foothold Reachability Criteria for Legged Locomotion
---

# KCFRC: Kinematic Collision-Aware Foothold Reachability Criteria for Legged Locomotion
**arXiv**：[2602.20850v1](https://arxiv.org/abs/2602.20850) · [PDF](https://arxiv.org/pdf/2602.20850.pdf)  
**作者**：Lei Ye, Haibo Gao, Huaiguang Yang, Peng Xu, Haoyu Wang, Tie Liu, Junqi Shan, Zongquan Deng, Liang Ding  

**一句话要点**：提出KCFRC算法以解决足式机器人在复杂环境中实时验证无碰撞摆动轨迹的足部可达性问题。

**关键词**：足式机器人, 足部可达性, 无碰撞轨迹, 实时验证, 接触规划, 轨迹优化

## 3 点简述
- 核心问题：现有方法在足部选择时难以高效验证无碰撞摆动轨迹的存在性。
- 方法要点：基于足部可达性的充分条件，开发KCFRC算法实现实时验证。
- 实验或效果：KCFRC在900个潜在足部位置检查中平均耗时2毫秒，提升轨迹优化和受限空间接触规划。

## 摘要（原文）

> Legged robots face significant challenges in navigating complex environments, as they require precise real-time decisions for foothold selection and contact planning. While existing research has explored methods to select footholds based on terrain geometry or kinematics, a critical gap remains: few existing methods efficiently validate the existence of a non-collision swing trajectory. This paper addresses this gap by introducing KCFRC, a novel approach for efficient foothold reachability analysis. We first formally define the foothold reachability problem and establish a sufficient condition for foothold reachability. Based on this condition, we develop the KCFRC algorithm, which enables robots to validate foothold reachability in real time. Our experimental results demonstrate that KCFRC achieves remarkable time efficiency, completing foothold reachability checks for a single leg across 900 potential footholds in an average of 2 ms. Furthermore, we show that KCFRC can accelerate trajectory optimization and is particularly beneficial for contact planning in confined spaces, enhancing the adaptability and robustness of legged robots in challenging environments.

