---
layout: default
title: Stereo-Inertial Poser: Towards Metric-Accurate Shape-Aware Motion Capture Using Sparse IMUs and a Single Stereo Camera
---

# Stereo-Inertial Poser: Towards Metric-Accurate Shape-Aware Motion Capture Using Sparse IMUs and a Single Stereo Camera
**arXiv**：[2603.02130v1](https://arxiv.org/abs/2603.02130) · [PDF](https://arxiv.org/pdf/2603.02130.pdf)  
**作者**：Tutian Tang, Xingyu Ji, Yutong Li, MingHao Liu, Wenqiang Xu, Cewu Lu  

**一句话要点**：提出Stereo-Inertial Poser，利用单立体相机和稀疏IMU实现度量准确、形状感知的实时运动捕捉

**关键词**：立体视觉, 惯性测量单元, 运动捕捉, 度量准确, 形状感知, 实时系统

## 3 点简述
- 核心问题：现有视觉-惯性系统存在单目深度模糊导致的度量不准确和忽略人体形状变化的问题
- 方法要点：通过立体视觉解决深度模糊，结合IMU数据预测无漂移关节位置，并引入形状感知融合模块
- 实验或效果：在多个数据集上达到先进性能，实时运行超过200 FPS，减少脚滑效应

## 摘要（原文）

> Recent advancements in visual-inertial motion capture systems have demonstrated the potential of combining monocular cameras with sparse inertial measurement units (IMUs) as cost-effective solutions, which effectively mitigate occlusion and drift issues inherent in single-modality systems. However, they are still limited by metric inaccuracies in global translations stemming from monocular depth ambiguity, and shape-agnostic local motion estimations that ignore anthropometric variations. We present Stereo-Inertial Poser, a real-time motion capture system that leverages a single stereo camera and six IMUs to estimate metric-accurate and shape-aware 3D human motion. By replacing the monocular RGB with stereo vision, our system resolves depth ambiguity through calibrated baseline geometry, enabling direct 3D keypoint extraction and body shape parameter estimation. IMU data and visual cues are fused for predicting drift-compensated joint positions and root movements, while a novel shape-aware fusion module dynamically harmonizes anthropometry variations with global translations. Our end-to-end pipeline achieves over 200 FPS without optimization-based post-processing, enabling real-time deployment. Quantitative evaluations across various datasets demonstrate state-of-the-art performance. Qualitative results show our method produces drift-free global translation under a long recording time and reduces foot-skating effects.

