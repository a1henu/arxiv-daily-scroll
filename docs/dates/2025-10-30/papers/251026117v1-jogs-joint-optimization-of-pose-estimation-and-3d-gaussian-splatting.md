---
layout: default
title: JOGS: Joint Optimization of Pose Estimation and 3D Gaussian Splatting
---

# JOGS: Joint Optimization of Pose Estimation and 3D Gaussian Splatting
**arXiv**：[2510.26117v1](https://arxiv.org/abs/2510.26117) · [PDF](https://arxiv.org/pdf/2510.26117.pdf)  
**作者**：Yuxuan Li, Tao Wang, Xianben Yang  

**一句话要点**：提出联合优化相机姿态与3D高斯溅射的方法，以解决传统方法依赖外部工具的问题。

**关键词**：新视角合成, 相机姿态估计, 3D高斯溅射, 联合优化, 可微渲染

## 3 点简述
- 传统新视角合成依赖COLMAP等外部工具，导致计算瓶颈和误差传播。
- 方法通过交替优化3D高斯参数和相机姿态，结合可微渲染和3D光流算法。
- 实验显示在多个数据集上优于现有COLMAP-free方法，并超越标准基线。

## 摘要（原文）

> Traditional novel view synthesis methods heavily rely on external camera pose
> estimation tools such as COLMAP, which often introduce computational
> bottlenecks and propagate errors. To address these challenges, we propose a
> unified framework that jointly optimizes 3D Gaussian points and camera poses
> without requiring pre-calibrated inputs. Our approach iteratively refines 3D
> Gaussian parameters and updates camera poses through a novel co-optimization
> strategy, ensuring simultaneous improvements in scene reconstruction fidelity
> and pose accuracy. The key innovation lies in decoupling the joint optimization
> into two interleaved phases: first, updating 3D Gaussian parameters via
> differentiable rendering with fixed poses, and second, refining camera poses
> using a customized 3D optical flow algorithm that incorporates geometric and
> photometric constraints. This formulation progressively reduces projection
> errors, particularly in challenging scenarios with large viewpoint variations
> and sparse feature distributions, where traditional methods struggle. Extensive
> evaluations on multiple datasets demonstrate that our approach significantly
> outperforms existing COLMAP-free techniques in reconstruction quality, and also
> surpasses the standard COLMAP-based baseline in general.

