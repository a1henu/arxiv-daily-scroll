---
layout: default
title: Markerless Robot Detection and 6D Pose Estimation for Multi-Agent SLAM
---

# Markerless Robot Detection and 6D Pose Estimation for Multi-Agent SLAM
**arXiv**：[2602.16308v1](https://arxiv.org/abs/2602.16308) · [PDF](https://arxiv.org/pdf/2602.16308.pdf)  
**作者**：Markus Rueggeberg, Maximilian Ulmer, Maximilian Durner, Wout Boerdijk, Marcus Gerhard Mueller, Rudolph Triebel, Riccardo Giubilato  

**一句话要点**：提出基于深度学习的无标记6D位姿估计方法，以提升多机器人SLAM中的相对定位精度。

**关键词**：多机器人SLAM, 6D位姿估计, 无标记检测, 深度学习, 相对定位, 去中心化系统

## 3 点简述
- 核心问题：多机器人SLAM中数据关联困难，传统基于标记的方法受限于观测范围和光照条件。
- 方法要点：利用深度学习进行无标记6D位姿估计，集成到去中心化多机器人SLAM系统中。
- 实验或效果：在行星类似环境测试中验证了方法对相对定位准确性的提升。

## 摘要（原文）

> The capability of multi-robot SLAM approaches to merge localization history and maps from different observers is often challenged by the difficulty in establishing data association. Loop closure detection between perceptual inputs of different robotic agents is easily compromised in the context of perceptual aliasing, or when perspectives differ significantly. For this reason, direct mutual observation among robots is a powerful way to connect partial SLAM graphs, but often relies on the presence of calibrated arrays of fiducial markers (e.g., AprilTag arrays), which severely limits the range of observations and frequently fails under sharp lighting conditions, e.g., reflections or overexposure. In this work, we propose a novel solution to this problem leveraging recent advances in Deep-Learning-based 6D pose estimation. We feature markerless pose estimation as part of a decentralized multi-robot SLAM system and demonstrate the benefit to the relative localization accuracy among the robotic team. The solution is validated experimentally on data recorded in a test field campaign on a planetary analogous environment.

