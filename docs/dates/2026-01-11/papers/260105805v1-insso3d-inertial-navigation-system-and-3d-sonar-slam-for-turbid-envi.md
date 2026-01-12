---
layout: default
title: InsSo3D: Inertial Navigation System and 3D Sonar SLAM for turbid environment inspection
---

# InsSo3D: Inertial Navigation System and 3D Sonar SLAM for turbid environment inspection
**arXiv**：[2601.05805v1](https://arxiv.org/abs/2601.05805) · [PDF](https://arxiv.org/pdf/2601.05805.pdf)  
**作者**：Simon Archieri, Ahmet Cinar, Shu Pan, Jonatan Scharff Willners, Michele Grimald, Ignacio Carlucho, Yvan Petillot  

**一句话要点**：提出InsSo3D方法，结合3D声纳与惯性导航系统，实现浑浊水下环境的大规模3D SLAM。

**关键词**：3D SLAM, 水下导航, 声纳点云, 惯性导航系统, 浑浊环境检测

## 3 点简述
- 核心问题：传统2D声纳缺乏高程信息，导致SLAM在浑浊水下环境存在高程模糊问题。
- 方法要点：利用3D声纳点云消除高程模糊，结合INS先验，构建鲁棒SLAM框架，包括闭环检测与位姿图优化。
- 实验或效果：在测试池与室外淹没采石场验证，平均轨迹误差低于21cm，重建误差9cm，有效校正里程计漂移。

## 摘要（原文）

> This paper presents InsSo3D, an accurate and efficient method for large-scale 3D Simultaneous Localisation and Mapping (SLAM) using a 3D Sonar and an Inertial Navigation System (INS). Unlike traditional sonar, which produces 2D images containing range and azimuth information but lacks elevation information, 3D Sonar produces a 3D point cloud, which therefore does not suffer from elevation ambiguity. We introduce a robust and modern SLAM framework adapted to the 3D Sonar data using INS as prior, detecting loop closure and performing pose graph optimisation. We evaluated InsSo3D performance inside a test tank with access to ground truth data and in an outdoor flooded quarry. Comparisons to reference trajectories and maps obtained from an underwater motion tracking system and visual Structure From Motion (SFM) demonstrate that InsSo3D efficiently corrects odometry drift. The average trajectory error is below 21cm during a 50-minute-long mission, producing a map of 10m by 20m with a 9cm average reconstruction error, enabling safe inspection of natural or artificial underwater structures even in murky water conditions.

