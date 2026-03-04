---
layout: default
title: Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild
---

# Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild
**arXiv**：[2603.02619v1](https://arxiv.org/abs/2603.02619) · [PDF](https://arxiv.org/pdf/2603.02619.pdf)  
**作者**：Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  

**一句话要点**：提出DrPose算法，通过直接奖励微调解决单视图3D人体重建中动态姿态不自然的问题。

**关键词**：单视图3D人体重建, 姿态奖励微调, 多视图扩散模型, 姿态一致性评估, 数据集构建

## 3 点简述
- 核心问题：现有方法在重建动态或挑战性姿态时，因3D数据集姿态多样性有限，导致重建结果不自然。
- 方法要点：引入DrPose，仅使用姿态-单视图图像对，通过直接奖励微调最大化PoseScore，提升多视图生成与真实姿态的一致性。
- 实验或效果：在DrPose15K数据集上训练，评估显示在传统基准、野外图像和新基准上均取得一致定性定量改进。

## 摘要（原文）

> Single-view 3D human reconstruction has achieved remarkable progress through the adoption of multi-view diffusion models, yet the recovered 3D humans often exhibit unnatural poses. This phenomenon becomes pronounced when reconstructing 3D humans with dynamic or challenging poses, which we attribute to the limited scale of available 3D human datasets with diverse poses. To address this limitation, we introduce DrPose, Direct Reward fine-tuning algorithm on Poses, which enables post-training of a multi-view diffusion model on diverse poses without requiring expensive 3D human assets. DrPose trains a model using only human poses paired with single-view images, employing a direct reward fine-tuning to maximize PoseScore, which is our proposed differentiable reward that quantifies consistency between a generated multi-view latent image and a ground-truth human pose. This optimization is conducted on DrPose15K, a novel dataset that was constructed from an existing human motion dataset and a pose-conditioned video generative model. Constructed from abundant human pose sequence data, DrPose15K exhibits a broader pose distribution compared to existing 3D human datasets. We validate our approach through evaluation on conventional benchmark datasets, in-the-wild images, and a newly constructed benchmark, with a particular focus on assessing performance on challenging human poses. Our results demonstrate consistent qualitative and quantitative improvements across all benchmarks. Project page: https://seunguk-do.github.io/drpose.

