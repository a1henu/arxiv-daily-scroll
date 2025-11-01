---
layout: default
title: Sketch2PoseNet: Efficient and Generalized Sketch to 3D Human Pose Prediction
---

# Sketch2PoseNet: Efficient and Generalized Sketch to 3D Human Pose Prediction
**arXiv**：[2510.26196v1](https://arxiv.org/abs/2510.26196) · [PDF](https://arxiv.org/pdf/2510.26196.pdf)  
**作者**：Li Wang, Yiyu Zhuang, Yanwen Wang, Xun Cao, Chuan Guo, Xinxin Zuo, Hao Zhu  

**一句话要点**：提出Sketch2PoseNet以高效解决从抽象草图预测3D人体姿态的问题

**关键词**：草图到3D姿态预测, 合成数据集生成, 扩散模型, 人体姿态估计, 几何一致性损失

## 3 点简述
- 核心问题：草图抽象且不成比例，缺乏大规模标注数据，导致传统方法耗时且泛化性差
- 方法要点：采用'从合成学习'策略，生成合成数据集SKEP-120K，结合扩散模型和前馈网络进行端到端估计
- 实验或效果：在准确性和速度上显著超越先前方法，通过定性和定量评估验证

## 摘要（原文）

> 3D human pose estimation from sketches has broad applications in computer
> animation and film production. Unlike traditional human pose estimation, this
> task presents unique challenges due to the abstract and disproportionate nature
> of sketches. Previous sketch-to-pose methods, constrained by the lack of
> large-scale sketch-3D pose annotations, primarily relied on optimization with
> heuristic rules-an approach that is both time-consuming and limited in
> generalizability. To address these challenges, we propose a novel approach
> leveraging a "learn from synthesis" strategy. First, a diffusion model is
> trained to synthesize sketch images from 2D poses projected from 3D human
> poses, mimicking disproportionate human structures in sketches. This process
> enables the creation of a synthetic dataset, SKEP-120K, consisting of 120k
> accurate sketch-3D pose annotation pairs across various sketch styles. Building
> on this synthetic dataset, we introduce an end-to-end data-driven framework for
> estimating human poses and shapes from diverse sketch styles. Our framework
> combines existing 2D pose detectors and generative diffusion priors for sketch
> feature extraction with a feed-forward neural network for efficient 2D pose
> estimation. Multiple heuristic loss functions are incorporated to guarantee
> geometric coherence between the derived 3D poses and the detected 2D poses
> while preserving accurate self-contacts. Qualitative, quantitative, and
> subjective evaluations collectively show that our model substantially surpasses
> previous ones in both estimation accuracy and speed for sketch-to-pose tasks.

