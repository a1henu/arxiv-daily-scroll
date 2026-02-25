---
layout: default
title: LST-SLAM: A Stereo Thermal SLAM System for Kilometer-Scale Dynamic Environments
---

# LST-SLAM: A Stereo Thermal SLAM System for Kilometer-Scale Dynamic Environments
**arXiv**：[2602.20925v1](https://arxiv.org/abs/2602.20925) · [PDF](https://arxiv.org/pdf/2602.20925.pdf)  
**作者**：Zeyu Jiang, Kuan Xu, Changhao Chen  

**一句话要点**：提出LST-SLAM系统以解决大规模动态环境中热成像SLAM的鲁棒性问题

**关键词**：热成像SLAM, 大规模动态环境, 自监督特征学习, 立体视觉, 闭环检测, 位姿优化

## 3 点简述
- 核心问题：热成像SLAM在动态大规模户外环境中特征提取不可靠、运动跟踪不稳定、全局位姿和地图构建不一致
- 方法要点：结合自监督热特征学习、立体双级运动跟踪、几何位姿优化和语义-几何混合约束
- 实验或效果：在千米级动态热数据集上，LST-SLAM在鲁棒性和准确性上显著优于AirSLAM和DROID-SLAM

## 摘要（原文）

> Thermal cameras offer strong potential for robot perception under challenging illumination and weather conditions. However, thermal Simultaneous Localization and Mapping (SLAM) remains difficult due to unreliable feature extraction, unstable motion tracking, and inconsistent global pose and map construction, particularly in dynamic large-scale outdoor environments. To address these challenges, we propose LST-SLAM, a novel large-scale stereo thermal SLAM system that achieves robust performance in complex, dynamic scenes. Our approach combines self-supervised thermal feature learning, stereo dual-level motion tracking, and geometric pose optimization. We also introduce a semantic-geometric hybrid constraint that suppresses potentially dynamic features lacking strong inter-frame geometric consistency. Furthermore, we develop an online incremental bag-of-words model for loop closure detection, coupled with global pose optimization to mitigate accumulated drift. Extensive experiments on kilometer-scale dynamic thermal datasets show that LST-SLAM significantly outperforms recent representative SLAM systems, including AirSLAM and DROID-SLAM, in both robustness and accuracy.

