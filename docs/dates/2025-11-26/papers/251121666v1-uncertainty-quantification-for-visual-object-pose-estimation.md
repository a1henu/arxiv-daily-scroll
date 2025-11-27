---
layout: default
title: Uncertainty Quantification for Visual Object Pose Estimation
---

# Uncertainty Quantification for Visual Object Pose Estimation
**arXiv**：[2511.21666v1](https://arxiv.org/abs/2511.21666) · [PDF](https://arxiv.org/pdf/2511.21666.pdf)  
**作者**：Lorenzo Shaikewitz, Charis Georgiou, Luca Carlone  

**一句话要点**：提出SLUE方法以在单目视觉中估计物体位姿的不确定性边界

**关键词**：位姿估计, 不确定性量化, 凸优化, 单目视觉, SLUE方法, 无人机跟踪

## 3 点简述
- 核心问题：视觉位姿估计缺乏统计严谨的不确定性量化，需避免严格分布假设。
- 方法要点：基于像素检测噪声，SLUE通过凸优化生成高概率包含真实位姿的椭球边界。
- 实验效果：在数据集和无人机跟踪中，SLUE产生更小的平移边界和竞争性方向边界。

## 摘要（原文）

> Quantifying the uncertainty of an object's pose estimate is essential for robust control and planning. Although pose estimation is a well-studied robotics problem, attaching statistically rigorous uncertainty is not well understood without strict distributional assumptions. We develop distribution-free pose uncertainty bounds about a given pose estimate in the monocular setting. Our pose uncertainty only requires high probability noise bounds on pixel detections of 2D semantic keypoints on a known object. This noise model induces an implicit, non-convex set of pose uncertainty constraints. Our key contribution is SLUE (S-Lemma Uncertainty Estimation), a convex program to reduce this set to a single ellipsoidal uncertainty bound that is guaranteed to contain the true object pose with high probability. SLUE solves a relaxation of the minimum volume bounding ellipsoid problem inspired by the celebrated S-lemma. It requires no initial guess of the bound's shape or size and is guaranteed to contain the true object pose with high probability. For tighter uncertainty bounds at the same confidence, we extend SLUE to a sum-of-squares relaxation hierarchy which is guaranteed to converge to the minimum volume ellipsoidal uncertainty bound for a given set of keypoint constraints. We show this pose uncertainty bound can easily be projected to independent translation and axis-angle orientation bounds. We evaluate SLUE on two pose estimation datasets and a real-world drone tracking scenario. Compared to prior work, SLUE generates substantially smaller translation bounds and competitive orientation bounds. We release code at https://github.com/MIT-SPARK/PoseUncertaintySets.

