---
layout: default
title: RePose: A Real-Time 3D Human Pose Estimation and Biomechanical Analysis Framework for Rehabilitation
---

# RePose: A Real-Time 3D Human Pose Estimation and Biomechanical Analysis Framework for Rehabilitation
**arXiv**：[2601.00625v1](https://arxiv.org/abs/2601.00625) · [PDF](https://arxiv.org/pdf/2601.00625.pdf)  
**作者**：Junxiao Xue, Pavel Smirnov, Ziao Li, Yunyun Shi, Shi Chen, Xinyi Yin, Xiaohan Yue, Lei Wang, Yiduo Wang, Feng Lin, Yijia Chen, Xiao Ma, Xiaoran Yan, Qing Zhang, Fengjian Xue, Xuecheng Wu  

**一句话要点**：提出RePose框架，用于康复训练中的实时3D人体姿态估计与生物力学分析。

**关键词**：实时3D姿态估计, 康复训练, 多摄像头系统, 快速跟踪, 姿态平滑, 生物力学分析

## 3 点简述
- 核心问题：康复训练中患者动作的实时监测与评估，需处理多人干扰和姿态误差。
- 方法要点：基于多摄像头RGB视频的端到端实时管道，结合快速跟踪和SmoothNet改进以提升精度与平滑度。
- 实验或效果：在Unity平台实现实时监控，显示肌肉应力，辅助患者正确执行康复动作。

## 摘要（原文）

> We propose a real-time 3D human pose estimation and motion analysis method termed RePose for rehabilitation training. It is capable of real-time monitoring and evaluation of patients'motion during rehabilitation, providing immediate feedback and guidance to assist patients in executing rehabilitation exercises correctly. Firstly, we introduce a unified pipeline for end-to-end real-time human pose estimation and motion analysis using RGB video input from multiple cameras which can be applied to the field of rehabilitation training. The pipeline can help to monitor and correct patients'actions, thus aiding them in regaining muscle strength and motor functions. Secondly, we propose a fast tracking method for medical rehabilitation scenarios with multiple-person interference, which requires less than 1ms for tracking for a single frame. Additionally, we modify SmoothNet for real-time posture estimation, effectively reducing pose estimation errors and restoring the patient's true motion state, making it visually smoother. Finally, we use Unity platform for real-time monitoring and evaluation of patients' motion during rehabilitation, and to display the muscle stress conditions to assist patients with their rehabilitation training.

