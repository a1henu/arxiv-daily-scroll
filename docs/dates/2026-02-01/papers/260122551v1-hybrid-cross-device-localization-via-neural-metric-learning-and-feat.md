---
layout: default
title: Hybrid Cross-Device Localization via Neural Metric Learning and Feature Fusion
---

# Hybrid Cross-Device Localization via Neural Metric Learning and Feature Fusion
**arXiv**：[2601.22551v1](https://arxiv.org/abs/2601.22551) · [PDF](https://arxiv.org/pdf/2601.22551.pdf)  
**作者**：Meixia Lin, Mingkai Liu, Shuxue Peng, Dikai Fan, Shengyu Gu, Xianliang Huang, Haoyang Ye, Xiao Liu  

**一句话要点**：提出混合跨设备定位方法，通过神经度量学习和特征融合提升CroCoDL挑战中的召回率与精度。

**关键词**：跨设备定位, 神经度量学习, 特征融合, PnP几何定位, 候选剪枝, 深度条件定位

## 3 点简述
- 核心问题：解决跨设备定位中因设备差异导致的精度和召回率不足问题。
- 方法要点：结合共享检索编码器、几何分支与神经前馈分支，并采用神经引导候选剪枝和深度条件定位。
- 实验或效果：在HYDRO和SUCCU基准上显著提升性能，挑战中得分为92.62（R@0.5m, 5°）。

## 摘要（原文）

> We present a hybrid cross-device localization pipeline developed for the CroCoDL 2025 Challenge. Our approach integrates a shared retrieval encoder and two complementary localization branches: a classical geometric branch using feature fusion and PnP, and a neural feed-forward branch (MapAnything) for metric localization conditioned on geometric inputs. A neural-guided candidate pruning strategy further filters unreliable map frames based on translation consistency, while depth-conditioned localization refines metric scale and translation precision on Spot scenes. These components jointly lead to significant improvements in recall and accuracy across both HYDRO and SUCCU benchmarks. Our method achieved a final score of 92.62 (R@0.5m, 5°) during the challenge.

