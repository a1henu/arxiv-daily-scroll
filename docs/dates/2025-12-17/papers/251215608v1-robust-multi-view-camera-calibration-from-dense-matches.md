---
layout: default
title: Robust Multi-view Camera Calibration from Dense Matches
---

# Robust Multi-view Camera Calibration from Dense Matches
**arXiv**：[2512.15608v1](https://arxiv.org/abs/2512.15608) · [PDF](https://arxiv.org/pdf/2512.15608.pdf)  
**作者**：Johannes Hägerlind, Bao-Long Tran, Urs Waldmann, Per-Erik Forssén  

**一句话要点**：提出基于稠密匹配的鲁棒多视角相机标定方法，优化SfM流程以提升精度

**关键词**：多视角相机标定, 稠密匹配, 结构从运动, 径向畸变, 鲁棒性优化, 动物行为分析

## 3 点简述
- 核心问题：多视角相机标定在动物行为研究和监控分析中面临精度挑战，尤其针对强径向畸变相机
- 方法要点：研究稠密匹配对应点的子采样策略和视图增量选择准则，以改进姿态估计和标定过程
- 实验或效果：在定量评估中，方法显著提升强径向畸变相机的标定精度，并展示在全局SfM中的泛化能力

## 摘要（原文）

> Estimating camera intrinsics and extrinsics is a fundamental problem in computer vision, and while advances in structure-from-motion (SfM) have improved accuracy and robustness, open challenges remain. In this paper, we introduce a robust method for pose estimation and calibration. We consider a set of rigid cameras, each observing the scene from a different perspective, which is a typical camera setup in animal behavior studies and forensic analysis of surveillance footage. Specifically, we analyse the individual components in a structure-from-motion (SfM) pipeline, and identify design choices that improve accuracy. Our main contributions are: (1) we investigate how to best subsample the predicted correspondences from a dense matcher to leverage them in the estimation process. (2) We investigate selection criteria for how to add the views incrementally. In a rigorous quantitative evaluation, we show the effectiveness of our changes, especially for cameras with strong radial distortion (79.9% ours vs. 40.4 vanilla VGGT). Finally, we demonstrate our correspondence subsampling in a global SfM setting where we initialize the poses using VGGT. The proposed pipeline generalizes across a wide range of camera setups, and could thus become a useful tool for animal behavior and forensic analysis.

