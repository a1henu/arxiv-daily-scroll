---
layout: default
title: VideoGPA: Distilling Geometry Priors for 3D-Consistent Video Generation
---

# VideoGPA: Distilling Geometry Priors for 3D-Consistent Video Generation
**arXiv**：[2601.23286v1](https://arxiv.org/abs/2601.23286) · [PDF](https://arxiv.org/pdf/2601.23286.pdf)  
**作者**：Hongyang Du, Junjie Ye, Xiaoyan Cong, Runhao Li, Jingcheng Ni, Aman Agarwal, Zeqi Zhou, Zekun Li, Randall Balestriero, Yue Wang  

**一句话要点**：提出VideoGPA框架，通过几何先验蒸馏解决视频生成中的3D结构不一致问题

**关键词**：视频生成, 3D一致性, 几何先验, 偏好对齐, 自监督学习, 扩散模型

## 3 点简述
- 核心问题：视频扩散模型缺乏几何一致性，导致物体变形或空间漂移
- 方法要点：利用几何基础模型自动生成密集偏好信号，通过DPO引导模型学习3D一致性
- 实验或效果：在少量偏好对下显著提升时间稳定性、物理合理性和运动连贯性，优于现有基线

## 摘要（原文）

> While recent video diffusion models (VDMs) produce visually impressive results, they fundamentally struggle to maintain 3D structural consistency, often resulting in object deformation or spatial drift. We hypothesize that these failures arise because standard denoising objectives lack explicit incentives for geometric coherence. To address this, we introduce VideoGPA (Video Geometric Preference Alignment), a data-efficient self-supervised framework that leverages a geometry foundation model to automatically derive dense preference signals that guide VDMs via Direct Preference Optimization (DPO). This approach effectively steers the generative distribution toward inherent 3D consistency without requiring human annotations. VideoGPA significantly enhances temporal stability, physical plausibility, and motion coherence using minimal preference pairs, consistently outperforming state-of-the-art baselines in extensive experiments.

