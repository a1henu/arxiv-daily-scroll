---
layout: default
title: Flow Matching for Probabilistic Monocular 3D Human Pose Estimation
---

# Flow Matching for Probabilistic Monocular 3D Human Pose Estimation
**arXiv**：[2601.16763v1](https://arxiv.org/abs/2601.16763) · [PDF](https://arxiv.org/pdf/2601.16763.pdf)  
**作者**：Cuong Le, Pavló Melnyk, Bastian Wandt, Mårten Wadenbäck  

**一句话要点**：提出FMPose基于流匹配生成方法，用于概率性单目3D人体姿态估计，以解决深度模糊问题。

**关键词**：概率性3D姿态估计, 流匹配生成, 图卷积网络, 最优传输, 单目视觉, 深度模糊

## 3 点简述
- 核心问题：单目3D人体姿态估计因深度模糊而高度不适定，现有方法常产生错误但过度自信的估计。
- 方法要点：采用流匹配生成方法，通过连续归一化流学习从简单源分布到3D姿态分布的最优传输，并利用图卷积网络建模2D线索条件。
- 实验或效果：在Human3.6M、MPI-INF-3DHP和3DPW基准上优于当前最先进方法，相比扩散方法更快更准确。

## 摘要（原文）

> Recovering 3D human poses from a monocular camera view is a highly ill-posed problem due to the depth ambiguity. Earlier studies on 3D human pose lifting from 2D often contain incorrect-yet-overconfident 3D estimations. To mitigate the problem, emerging probabilistic approaches treat the 3D estimations as a distribution, taking into account the uncertainty measurement of the poses. Falling in a similar category, we proposed FMPose, a probabilistic 3D human pose estimation method based on the flow matching generative approach. Conditioned on the 2D cues, the flow matching scheme learns the optimal transport from a simple source distribution to the plausible 3D human pose distribution via continuous normalizing flows. The 2D lifting condition is modeled via graph convolutional networks, leveraging the learnable connections between human body joints as the graph structure for feature aggregation. Compared to diffusion-based methods, the FMPose with optimal transport produces faster and more accurate 3D pose generations. Experimental results show major improvements of our FMPose over current state-of-the-art methods on three common benchmarks for 3D human pose estimation, namely Human3.6M, MPI-INF-3DHP and 3DPW.

