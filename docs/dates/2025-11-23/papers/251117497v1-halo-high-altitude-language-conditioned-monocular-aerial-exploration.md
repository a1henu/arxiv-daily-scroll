---
layout: default
title: HALO: High-Altitude Language-Conditioned Monocular Aerial Exploration and Navigation
---

# HALO: High-Altitude Language-Conditioned Monocular Aerial Exploration and Navigation
**arXiv**：[2511.17497v1](https://arxiv.org/abs/2511.17497) · [PDF](https://arxiv.org/pdf/2511.17497.pdf)  
**作者**：Yuezhan Tao, Dexter Ong, Fernando Cladera, Jason Hughes, Camillo J. Taylor, Pratik Chaudhari, Vijay Kumar  

**一句话要点**：提出HALO系统，实现高海拔单目视觉语言引导的空中探索与导航

**关键词**：单目视觉导航, 度量-语义映射, 语言条件控制, 无人机自主探索, 实时3D重建

## 3 点简述
- 核心问题：高海拔单目视觉实时3D重建与大规模室外环境语义探索
- 方法要点：结合GPS/IMU，实时生成度量-语义地图，支持自然语言任务规划
- 实验或效果：仿真中减少探索时间，真实世界验证在40米高覆盖2.46万平方米

## 摘要（原文）

> We demonstrate real-time high-altitude aerial metric-semantic mapping and exploration using a monocular camera paired with a global positioning system (GPS) and an inertial measurement unit (IMU). Our system, named HALO, addresses two key challenges: (i) real-time dense 3D reconstruction using vision at large distances, and (ii) mapping and exploration of large-scale outdoor environments with accurate scene geometry and semantics. We demonstrate that HALO can plan informative paths that exploit this information to complete missions with multiple tasks specified in natural language. In simulation-based evaluation across large-scale environments of size up to 78,000 sq. m., HALO consistently completes tasks with less exploration time and achieves up to 68% higher competitive ratio in terms of the distance traveled compared to the state-of-the-art semantic exploration baseline. We use real-world experiments on a custom quadrotor platform to demonstrate that (i) all modules can run onboard the robot, and that (ii) in diverse environments HALO can support effective autonomous execution of missions covering up to 24,600 sq. m. area at an altitude of 40 m. Experiment videos and more details can be found on our project page: https://tyuezhan.github.io/halo/.

