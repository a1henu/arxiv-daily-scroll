---
layout: default
title: mmJoints: Expanding Joint Representations Beyond (x,y,z) in mmWave-Based 3D Pose Estimation
---

# mmJoints: Expanding Joint Representations Beyond (x,y,z) in mmWave-Based 3D Pose Estimation
**arXiv**：[2510.08970v1](https://arxiv.org/abs/2510.08970) · [PDF](https://arxiv.org/pdf/2510.08970.pdf)  
**作者**：Zhenyu Wang, Mahathir Monjur, Shahriar Nirjon  
**一句话要点**：提出mmJoints框架，通过增强关节描述符提升毫米波3D姿态估计的可靠性和下游任务性能
**关键词**：毫米波3D姿态估计, 关节描述符, 可解释性增强, 活动识别, 可靠性估计

## 3 点简述
- 毫米波姿态估计中，稀疏信号和弱反射导致模型过度依赖统计先验，影响下游任务性能
- mmJoints框架估计关节被感知的可能性和位置可靠性，增强输出可解释性
- 实验显示，mmJoints降低描述符误差至4.2%以下，提升姿态和活动识别准确率

## 摘要（原文）

> In mmWave-based pose estimation, sparse signals and weak reflections often
> cause models to infer body joints from statistical priors rather than sensor
> data. While prior knowledge helps in learning meaningful representations,
> over-reliance on it degrades performance in downstream tasks like gesture and
> activity recognition. In this paper, we introduce mmJoints, a framework that
> augments a pre-trained, black-box mmWave-based 3D pose estimator's output with
> additional joint descriptors. Rather than mitigating bias, mmJoints makes it
> explicit by estimating the likelihood of a joint being sensed and the
> reliability of its predicted location. These descriptors enhance
> interpretability and improve downstream task accuracy. Through extensive
> evaluations using over 115,000 signal frames across 13 pose estimation
> settings, we show that mmJoints estimates descriptors with an error rate below
> 4.2%. mmJoints also improves joint position accuracy by up to 12.5% and boosts
> activity recognition by up to 16% over state-of-the-art methods.

