---
layout: default
title: MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration
---

# MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration
**arXiv**：[2511.17392v1](https://arxiv.org/abs/2511.17392) · [PDF](https://arxiv.org/pdf/2511.17392.pdf)  
**作者**：Runxun Zhang, Yizhou Liu, Li Dongrui, Bo XU, Jingwei Wei  

**一句话要点**：提出MorphSeek以解决医学图像配准中高维变形空间优化问题

**关键词**：可变形图像配准, 潜在表示优化, 强化学习, 医学图像分析, 高斯策略, 弱监督学习

## 3 点简述
- 核心问题：可变形图像配准面临高维变形空间和体素级监督稀缺的挑战
- 方法要点：在潜在特征空间使用高斯策略头进行细粒度优化，支持粗到精细化
- 实验或效果：在多个3D基准测试中Dice指标提升，标签效率高且延迟低

## 摘要（原文）

> Deformable image registration (DIR) remains a fundamental yet challenging problem in medical image analysis, largely due to the prohibitively high-dimensional deformation space of dense displacement fields and the scarcity of voxel-level supervision. Existing reinforcement learning frameworks often project this space into coarse, low-dimensional representations, limiting their ability to capture spatially variant deformations. We propose MorphSeek, a fine-grained representation-level policy optimization paradigm that reformulates DIR as a spatially continuous optimization process in the latent feature space. MorphSeek introduces a stochastic Gaussian policy head atop the encoder to model a distribution over latent features, facilitating efficient exploration and coarse-to-fine refinement. The framework integrates unsupervised warm-up with weakly supervised fine-tuning through Group Relative Policy Optimization, where multi-trajectory sampling stabilizes training and improves label efficiency. Across three 3D registration benchmarks (OASIS brain MRI, LiTS liver CT, and Abdomen MR-CT), MorphSeek achieves consistent Dice improvements over competitive baselines while maintaining high label efficiency with minimal parameter cost and low step-level latency overhead. Beyond optimizer specifics, MorphSeek advances a representation-level policy learning paradigm that achieves spatially coherent and data-efficient deformation optimization, offering a principled, backbone-agnostic, and optimizer-agnostic solution for scalable visual alignment in high-dimensional settings.

