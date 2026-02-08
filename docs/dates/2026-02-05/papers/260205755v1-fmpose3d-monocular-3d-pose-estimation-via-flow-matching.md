---
layout: default
title: FMPose3D: monocular 3D pose estimation via flow matching
---

# FMPose3D: monocular 3D pose estimation via flow matching
**arXiv**：[2602.05755v1](https://arxiv.org/abs/2602.05755) · [PDF](https://arxiv.org/pdf/2602.05755.pdf)  
**作者**：Ti Wang, Xiaohang Yu, Mackenzie Weygandt Mathis  

**一句话要点**：提出FMPose3D，基于流匹配的单目3D姿态估计方法，以高效生成多假设姿态。

**关键词**：单目3D姿态估计, 流匹配, 概率生成模型, ODE轨迹, 多假设生成, 后验期望聚合

## 3 点简述
- 单目3D姿态估计因深度模糊和遮挡而病态，需概率方法生成多假设。
- 利用流匹配学习ODE定义的流场，通过少量积分步高效生成3D姿态样本。
- 在Human3.6M、MPI-INF-3DHP、Animal3D和CtrlAni3D数据集上达到先进性能。

## 摘要（原文）

> Monocular 3D pose estimation is fundamentally ill-posed due to depth ambiguity and occlusions, thereby motivating probabilistic methods that generate multiple plausible 3D pose hypotheses. In particular, diffusion-based models have recently demonstrated strong performance, but their iterative denoising process typically requires many timesteps for each prediction, making inference computationally expensive. In contrast, we leverage Flow Matching (FM) to learn a velocity field defined by an Ordinary Differential Equation (ODE), enabling efficient generation of 3D pose samples with only a few integration steps. We propose a novel generative pose estimation framework, FMPose3D, that formulates 3D pose estimation as a conditional distribution transport problem. It continuously transports samples from a standard Gaussian prior to the distribution of plausible 3D poses conditioned only on 2D inputs. Although ODE trajectories are deterministic, FMPose3D naturally generates various pose hypotheses by sampling different noise seeds. To obtain a single accurate prediction from those hypotheses, we further introduce a Reprojection-based Posterior Expectation Aggregation (RPEA) module, which approximates the Bayesian posterior expectation over 3D hypotheses. FMPose3D surpasses existing methods on the widely used human pose estimation benchmarks Human3.6M and MPI-INF-3DHP, and further achieves state-of-the-art performance on the 3D animal pose datasets Animal3D and CtrlAni3D, demonstrating strong performance across both 3D pose domains. The code is available at https://github.com/AdaptiveMotorControlLab/FMPose3D.

