---
layout: default
title: RadHARSimulator V2: Video to Doppler Generator
---

# RadHARSimulator V2: Video to Doppler Generator
**arXiv**：[2511.09022v1](https://arxiv.org/abs/2511.09022) · [PDF](https://arxiv.org/pdf/2511.09022.pdf)  
**作者**：Weicheng Gao  

**一句话要点**：提出RadHARSimulator V2，从视频生成多普勒谱以解决雷达人体活动识别模拟灵活性不足问题

**关键词**：雷达人体活动识别, 视频到多普勒生成, 三维姿态估计, 多普勒-时间图, 混合神经网络, 开源模拟器

## 3 点简述
- 核心问题：雷达人体活动识别缺乏灵活模拟方法，现有软件依赖模型或动捕数据。
- 方法要点：结合计算机视觉模块检测跟踪人体并估计三维姿态，雷达模块模拟回波生成多普勒-时间图。
- 实验或效果：数值实验验证模拟器和混合神经网络架构有效性，代码开源。

## 摘要（原文）

> Radar-based human activity recognition (HAR) still lacks a comprehensive simulation method. Existing software is developed based on models or motion-captured data, resulting in limited flexibility. To address this issue, a simulator that directly generates Doppler spectra from recorded video footage (RadHARSimulator V2) is presented in this paper. Both computer vision and radar modules are included in the simulator. In computer vision module, the real-time model for object detection with global nearest neighbor is first used to detect and track human targets in the video. Then, the high-resolution network is used to estimate two-dimensional poses of the detected human targets. Next, the three-dimensional poses of the detected human targets are obtained by nearest matching method. Finally, smooth temporal three-dimensional pose estimation is achieved through Kalman filtering. In radar module, pose interpolation and smoothing are first achieved through the Savitzky-Golay method. Second, the delay model and the mirror method are used to simulate echoes in both free-space and through-the-wall scenarios. Then, range-time map is generated using pulse compression, moving target indication, and DnCNN. Next, Doppler-time map (DTM) is generated using short-time Fourier transform and DnCNN again. Finally, the ridge features on the DTM are extracted using the maximum local energy method. In addition, a hybrid parallel-serial neural network architecture is proposed for radar-based HAR. Numerical experiments are conducted and analyzed to demonstrate the effectiveness of the designed simulator and the proposed network model. The open-source code of this work can be found in: https://github.com/JoeyBGOfficial/RadHARSimulatorV2-Video-to-Doppler-Generator.

