---
layout: default
title: Accurate Calibration and Robust LiDAR-Inertial Odometry for Spinning Actuated LiDAR Systems
---

# Accurate Calibration and Robust LiDAR-Inertial Odometry for Spinning Actuated LiDAR Systems
**arXiv**：[2601.15946v1](https://arxiv.org/abs/2601.15946) · [PDF](https://arxiv.org/pdf/2601.15946.pdf)  
**作者**：Zijie Chen, Xiaowei Liu, Yong Xu, Shenghai Yuan, Jianping Li, Lihua Xie  

**一句话要点**：提出无目标LiDAR-电机标定与自适应LiDAR-惯性里程计，以提升旋转驱动LiDAR系统的标定通用性与定位鲁棒性。

**关键词**：LiDAR-电机标定, LiDAR-惯性里程计, 旋转驱动LiDAR, 无目标标定, 自适应定位, 鲁棒性增强

## 3 点简述
- 核心问题：现有方法依赖安装配置参数化，通用性差；旋转驱动LiDAR扫描无特征区域时，覆盖与鲁棒性难以平衡。
- 方法要点：基于Denavit-Hartenberg约定实现无目标标定LM-Calibr；根据空间尺度自适应选择下采样率与地图分辨率EVA-LIO。
- 实验或效果：标定方法在不同场景、安装角度和初始值下准确收敛；自适应方法使驱动器以最大速度运行，增强扫描完整性并确保鲁棒定位。

## 摘要（原文）

> Accurate calibration and robust localization are fundamental for downstream tasks in spinning actuated LiDAR applications. Existing methods, however, require parameterizing extrinsic parameters based on different mounting configurations, limiting their generalizability. Additionally, spinning actuated LiDAR inevitably scans featureless regions, which complicates the balance between scanning coverage and localization robustness. To address these challenges, this letter presents a targetless LiDAR-motor calibration (LM-Calibr) on the basis of the Denavit-Hartenberg convention and an environmental adaptive LiDAR-inertial odometry (EVA-LIO). LM-Calibr supports calibration of LiDAR-motor systems with various mounting configurations. Extensive experiments demonstrate its accuracy and convergence across different scenarios, mounting angles, and initial values. Additionally, EVA-LIO adaptively selects downsample rates and map resolutions according to spatial scale. This adaptivity enables the actuator to operate at maximum speed, thereby enhancing scanning completeness while ensuring robust localization, even when LiDAR briefly scans featureless areas. The source code and hardware design are available on GitHub: \textcolor{blue}{\href{https://github.com/zijiechenrobotics/lm_calibr}{github.com/zijiechenrobotics/lm\_calibr}}. The video is available at \textcolor{blue}{\href{https://youtu.be/cZyyrkmeoSk}{youtu.be/cZyyrkmeoSk}}

