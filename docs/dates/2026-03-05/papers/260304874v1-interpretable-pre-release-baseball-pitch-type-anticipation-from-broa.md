---
layout: default
title: Interpretable Pre-Release Baseball Pitch Type Anticipation from Broadcast 3D Kinematics
---

# Interpretable Pre-Release Baseball Pitch Type Anticipation from Broadcast 3D Kinematics
**arXiv**：[2603.04874v1](https://arxiv.org/abs/2603.04874) · [PDF](https://arxiv.org/pdf/2603.04874.pdf)  
**作者**：Jerrin Bright, Michelle Lu, John Zelek  

**一句话要点**：提出基于单目3D姿态序列的棒球投球类型预测方法，仅使用身体运动学实现80.4%准确率。

**关键词**：3D姿态估计, 运动学分析, 棒球投球预测, 生物力学特征, 梯度提升分类

## 3 点简述
- 研究问题：仅通过投手身体运动学预测投球类型，不依赖球飞行数据。
- 方法要点：结合扩散模型3D姿态估计、自动事件检测、生物力学特征提取和梯度提升分类。
- 实验效果：在119,561次投球数据上验证，分析上下半身贡献度，确定运动学信息上限。

## 摘要（原文）

> How much can a pitcher's body reveal about the upcoming pitch? We study this question at scale by classifying eight pitch types from monocular 3D pose sequences, without access to ball-flight data. Our pipeline chains a diffusion-based 3D pose backbone with automatic pitching-event detection, groundtruth-validated biomechanical feature extraction, and gradient-boosted classification over 229 kinematic features. Evaluated on 119,561 professional pitches, the largest such benchmark to date, we achieve 80.4\% accuracy using body kinematics alone. A systematic importance analysis reveals that upper-body mechanics contribute 64.9\% of the predictive signal versus 35.1\% for the lower body, with wrist position (14.8\%) and trunk lateral tilt emerging as the most informative joint group and biomechanical feature, respectively. We further show that grip-defined variants (four-seam vs.\ two-seam fastball) are not separable from pose, establishing an empirical ceiling near 80\% and delineating where kinematic information ends and ball-flight information begins.

