---
layout: default
title: B$^3$-Seg: Camera-Free, Training-Free 3DGS Segmentation via Analytic EIG and Beta-Bernoulli Bayesian Updates
---

# B$^3$-Seg: Camera-Free, Training-Free 3DGS Segmentation via Analytic EIG and Beta-Bernoulli Bayesian Updates
**arXiv**：[2602.17134v1](https://arxiv.org/abs/2602.17134) · [PDF](https://arxiv.org/pdf/2602.17134.pdf)  
**作者**：Hiromichi Kamata, Samuel Arthur Munro, Fuminori Homma  

**一句话要点**：提出B^3-Seg以解决无相机、免训练条件下3D高斯溅射的快速开放词汇分割问题

**关键词**：3D高斯溅射分割, 贝叶斯更新, 期望信息增益, 开放词汇分割, 免训练分割, 交互式3D编辑

## 3 点简述
- 现有方法依赖相机视角或重训练，不适用于低延迟交互式3D编辑场景
- 基于Beta-Bernoulli贝叶斯更新和解析期望信息增益，实现自适应单调性和次模性保证
- 实验显示在数秒内完成端到端分割，性能接近高成本监督方法

## 摘要（原文）

> Interactive 3D Gaussian Splatting (3DGS) segmentation is essential for real-time editing of pre-reconstructed assets in film and game production. However, existing methods rely on predefined camera viewpoints, ground-truth labels, or costly retraining, making them impractical for low-latency use. We propose B$^3$-Seg (Beta-Bernoulli Bayesian Segmentation for 3DGS), a fast and theoretically grounded method for open-vocabulary 3DGS segmentation under camera-free and training-free conditions. Our approach reformulates segmentation as sequential Beta-Bernoulli Bayesian updates and actively selects the next view via analytic Expected Information Gain (EIG). This Bayesian formulation guarantees the adaptive monotonicity and submodularity of EIG, which produces a greedy $(1{-}1/e)$ approximation to the optimal view sampling policy. Experiments on multiple datasets show that B$^3$-Seg achieves competitive results to high-cost supervised methods while operating end-to-end segmentation within a few seconds. The results demonstrate that B$^3$-Seg enables practical, interactive 3DGS segmentation with provable information efficiency.

