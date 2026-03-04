---
layout: default
title: Articulation in Motion: Prior-free Part Mobility Analysis for Articulated Objects By Dynamic-Static Disentanglement
---

# Articulation in Motion: Prior-free Part Mobility Analysis for Articulated Objects By Dynamic-Static Disentanglement
**arXiv**：[2603.02910v1](https://arxiv.org/abs/2603.02910) · [PDF](https://arxiv.org/pdf/2603.02910.pdf)  
**作者**：Hao Ai, Wenjie Chang, Jianbo Jiao, Ales Leonardis, Ofek Eyal  

**一句话要点**：提出AiM框架，通过动态-静态解耦实现无先验的铰接物体部件分割与运动分析

**关键词**：铰接物体分析, 动态-静态解耦, 双高斯表示, 部件分割, 运动学估计, 无先验学习

## 3 点简述
- 核心问题：现有方法依赖先验知识（如部件数量）和清晰的双状态可见性，限制了铰接物体分析的鲁棒性和应用范围。
- 方法要点：使用双高斯场景表示从交互视频和初始扫描学习，结合运动线索分割部件并估计关节，通过顺序RANSAC自动确定部件数量并分析运动学。
- 实验或效果：在简单和复杂物体上验证了高质量部件分割和强泛化能力，无需先验知识，优于先前方法。

## 摘要（原文）

> Articulated objects are ubiquitous in daily life. Our goal is to achieve a high-quality reconstruction, segmentation of independent moving parts, and analysis of articulation. Recent methods analyse two different articulation states and perform per-point part segmentation, optimising per-part articulation using cross-state correspondences, given a priori knowledge of the number of parts. Such assumptions greatly limit their applications and performance. Their robustness is reduced when objects cannot be clearly visible in both states. To address these issues, in this paper, we present a new framework, Articulation in Motion (AiM). We infer part-level decomposition, articulation kinematics, and reconstruct an interactive 3D digital replica from a user-object interaction video and a start-state scan. We propose a dual-Gaussian scene representation that is learned from an initial 3DGS scan of the object and a video that shows the movement of separate parts. It uses motion cues to segment the object into parts and assign articulation joints. Subsequently, a robust, sequential RANSAC is employed to achieve part mobility analysis without any part-level structural priors, which clusters moving primitives into rigid parts and estimates kinematics while automatically determining the number of parts. The proposed approach separates the object into parts, each represented as a 3D Gaussian set, enabling high-quality rendering. Our approach yields higher quality part segmentation than previous methods, without prior knowledge. Extensive experimental analysis on both simple and complex objects validates the effectiveness and strong generalisation ability of our approach. Project page: https://haoai-1997.github.io/AiM/.

