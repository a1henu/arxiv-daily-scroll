---
layout: default
title: Accurate Calibration and Robust LiDAR-Inertial Odometry for Spinning Actuated LiDAR Systems
---

# Accurate Calibration and Robust LiDAR-Inertial Odometry for Spinning Actuated LiDAR Systems
**arXiv**：[2601.15946v1](https://arxiv.org/abs/2601.15946) · [PDF](https://arxiv.org/pdf/2601.15946.pdf)  
**作者**：Zijie Chen, Xiaowei Liu, Yong Xu, Shenghai Yuan, Jianping Li, Lihua Xie  

**一句话要点**：提出无目标标定与自适应里程计以解决旋转驱动LiDAR系统的标定泛化与鲁棒定位问题

**关键词**：LiDAR-惯性里程计, 无目标标定, 自适应定位, 旋转驱动LiDAR, DH约定, 环境适应性

## 3 点简述
- 核心问题：现有方法依赖安装配置参数化，限制泛化性；旋转扫描特征缺失区域影响定位鲁棒性。
- 方法要点：基于DH约定实现无目标LiDAR-电机标定；根据空间尺度自适应选择下采样率与地图分辨率。
- 实验或效果：标定方法在不同场景、安装角度和初始值下准确收敛；自适应里程计提升扫描完整性与定位鲁棒性。

## 摘要（原文）

> Accurate calibration and robust localization are fundamental for downstream tasks in spinning actuated LiDAR applications. Existing methods, however, require parameterizing extrinsic parameters based on different mounting configurations, limiting their generalizability. Additionally, spinning actuated LiDAR inevitably scans featureless regions, which complicates the balance between scanning coverage and localization robustness. To address these challenges, this letter presents a targetless LiDAR-motor calibration (LM-Calibr) on the basis of the Denavit-Hartenberg convention and an environmental adaptive LiDAR-inertial odometry (EVA-LIO). LM-Calibr supports calibration of LiDAR-motor systems with various mounting configurations. Extensive experiments demonstrate its accuracy and convergence across different scenarios, mounting angles, and initial values. Additionally, EVA-LIO adaptively selects downsample rates and map resolutions according to spatial scale. This adaptivity enables the actuator to operate at maximum speed, thereby enhancing scanning completeness while ensuring robust localization, even when LiDAR briefly scans featureless areas. The source code and hardware design are available on GitHub: \textcolor{blue}{\href{https://github.com/zijiechenrobotics/lm_calibr}{github.com/zijiechenrobotics/lm\_calibr}}. The video is available at \textcolor{blue}{\href{https://youtu.be/cZyyrkmeoSk}{youtu.be/cZyyrkmeoSk}}

