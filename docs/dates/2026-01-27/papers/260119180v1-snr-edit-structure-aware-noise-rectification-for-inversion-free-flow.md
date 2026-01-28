---
layout: default
title: SNR-Edit: Structure-Aware Noise Rectification for Inversion-Free Flow-Based Editing
---

# SNR-Edit: Structure-Aware Noise Rectification for Inversion-Free Flow-Based Editing
**arXiv**：[2601.19180v1](https://arxiv.org/abs/2601.19180) · [PDF](https://arxiv.org/pdf/2601.19180.pdf)  
**作者**：Lifan Jiang, Boxi Wu, Yuhang Pei, Tianrun Wu, Yongyuan Chen, Yan Zhao, Shiyu Yu, Deng Cai  

**一句话要点**：提出SNR-Edit框架，通过结构感知噪声校正实现免反演的流模型图像编辑

**关键词**：图像编辑, 流生成模型, 噪声校正, 结构保持, 免反演编辑, 轨迹优化

## 3 点简述
- 核心问题：现有免反演流模型编辑方法使用固定高斯噪声，导致轨迹偏差和结构退化
- 方法要点：采用结构感知噪声校正，将分割约束注入初始噪声，减少轨迹漂移
- 实验或效果：在SD3和FLUX上评估，SNR-Edit提升像素级指标和VLM评分，仅增加约1秒开销

## 摘要（原文）

> Inversion-free image editing using flow-based generative models challenges the prevailing inversion-based pipelines. However, existing approaches rely on fixed Gaussian noise to construct the source trajectory, leading to biased trajectory dynamics and causing structural degradation or quality loss. To address this, we introduce SNR-Edit, a training-free framework achieving faithful Latent Trajectory Correction via adaptive noise control. Mechanistically, SNR-Edit uses structure-aware noise rectification to inject segmentation constraints into the initial noise, anchoring the stochastic component of the source trajectory to the real image's implicit inversion position and reducing trajectory drift during source--target transport. This lightweight modification yields smoother latent trajectories and ensures high-fidelity structural preservation without requiring model tuning or inversion. Across SD3 and FLUX, evaluations on PIE-Bench and SNR-Bench show that SNR-Edit delivers performance on pixel-level metrics and VLM-based scoring, while adding only about 1s overhead per image.

