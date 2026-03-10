---
layout: default
title: Viewpoint-Agnostic Grasp Pipeline using VLM and Partial Observations
---

# Viewpoint-Agnostic Grasp Pipeline using VLM and Partial Observations
**arXiv**：[2603.07866v1](https://arxiv.org/abs/2603.07866) · [PDF](https://arxiv.org/pdf/2603.07866.pdf)  
**作者**：Dilermando Almeida, Juliano Negri, Guilherme Lazzarini, Thiago H. Segreto, Ranulfo Bezerra, Ricardo V. Godoy, Marcelo Becker  

**一句话要点**：提出基于视觉语言模型和部分观测的视点无关抓取管道，以解决杂乱环境中移动腿式机械臂的抓取挑战。

**关键词**：视觉语言模型, 部分观测抓取, 点云补全, 6自由度抓取, 移动腿式机械臂, 杂乱环境

## 3 点简述
- 核心问题：杂乱无结构环境中，遮挡导致部分观测、深度估计不可靠，需安全可行的抓取方法。
- 方法要点：使用语言引导，通过开放词汇检测和点云补全，生成并筛选6自由度抓取候选。
- 实验或效果：在四足机器人上测试，成功率90%，相比基线30%显著提升，增强对遮挡的鲁棒性。

## 摘要（原文）

> Robust grasping in cluttered, unstructured environments remains challenging for mobile legged manipulators due to occlusions that lead to partial observations, unreliable depth estimates, and the need for collision-free, execution-feasible approaches. In this paper we present an end-to-end pipeline for language-guided grasping that bridges open-vocabulary target selection to safe grasp execution on a real robot. Given a natural-language command, the system grounds the target in RGB using open-vocabulary detection and promptable instance segmentation, extracts an object-centric point cloud from RGB-D, and improves geometric reliability under occlusion via back-projected depth compensation and two-stage point cloud completion. We then generate and collision-filter 6-DoF grasp candidates and select an executable grasp using safety-oriented heuristics that account for reachability, approach feasibility, and clearance. We evaluate the method on a quadruped robot with an arm in two cluttered tabletop scenarios, using paired trials against a view-dependent baseline. The proposed approach achieves a 90% overall success rate (9/10) against 30% (3/10) for the baseline, demonstrating substantially improved robustness to occlusions and partial observations in clutter.

