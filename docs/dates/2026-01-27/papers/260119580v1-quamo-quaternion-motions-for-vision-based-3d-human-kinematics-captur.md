---
layout: default
title: QuaMo: Quaternion Motions for Vision-based 3D Human Kinematics Capture
---

# QuaMo: Quaternion Motions for Vision-based 3D Human Kinematics Capture
**arXiv**：[2601.19580v1](https://arxiv.org/abs/2601.19580) · [PDF](https://arxiv.org/pdf/2601.19580.pdf)  
**作者**：Cuong Le, Pavlo Melnyk, Urs Waldmann, Mårten Wadenbäck, Bastian Wandt  

**一句话要点**：提出QuaMo方法，利用四元数微分方程解决基于视觉的3D人体运动捕捉中的不连续性问题。

**关键词**：3D人体运动捕捉, 四元数微分方程, 运动学估计, 时间一致性, 状态空间模型, 加速度增强

## 3 点简述
- 核心问题：传统3D姿态估计忽略时间一致性，导致运动不连续和抖动；基于运动学的方法依赖欧拉角，存在不连续性。
- 方法要点：使用四元数状态空间模型和四元数微分方程，结合元PD控制器增强加速度，在单位球约束下求解，确保连续运动。
- 实验或效果：在Human3.6M等数据集上优于现有方法，实现无间断、最小不合理性的3D人体运动捕捉。

## 摘要（原文）

> Vision-based 3D human motion capture from videos remains a challenge in computer vision. Traditional 3D pose estimation approaches often ignore the temporal consistency between frames, causing implausible and jittery motion. The emerging field of kinematics-based 3D motion capture addresses these issues by estimating the temporal transitioning between poses instead. A major drawback in current kinematics approaches is their reliance on Euler angles. Despite their simplicity, Euler angles suffer from discontinuity that leads to unstable motion reconstructions, especially in online settings where trajectory refinement is unavailable. Contrarily, quaternions have no discontinuity and can produce continuous transitions between poses. In this paper, we propose QuaMo, a novel Quaternion Motions method using quaternion differential equations (QDE) for human kinematics capture. We utilize the state-space model, an effective system for describing real-time kinematics estimations, with quaternion state and the QDE describing quaternion velocity. The corresponding angular acceleration is computed from a meta-PD controller with a novel acceleration enhancement that adaptively regulates the control signals as the human quickly changes to a new pose. Unlike previous work, our QDE is solved under the quaternion unit-sphere constraint that results in more accurate estimations. Experimental results show that our novel formulation of the QDE with acceleration enhancement accurately estimates 3D human kinematics with no discontinuity and minimal implausibilities. QuaMo outperforms comparable state-of-the-art methods on multiple datasets, namely Human3.6M, Fit3D, SportsPose and AIST. The code is available at https://github.com/cuongle1206/QuaMo

