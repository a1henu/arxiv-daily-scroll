---
layout: default
title: ATATA: One Algorithm to Align Them All
---

# ATATA: One Algorithm to Align Them All
**arXiv**：[2601.11194v1](https://arxiv.org/abs/2601.11194) · [PDF](https://arxiv.org/pdf/2601.11194.pdf)  
**作者**：Boyi Pang, Savva Ignatyev, Vladimir Ippolitov, Ramil Khafizov, Yurii Melnik, Oleg Voynov, Maksim Nakhodnov, Aibek Alanov, Xiaopeng Fan, Peter Wonka, Evgeny Burnaev  

**一句话要点**：提出ATATA算法，基于Rectified Flow模型实现多模态样本的结构对齐联合生成。

**关键词**：多模态生成, 结构对齐, Rectified Flow, 联合推理, 3D形状生成, 快速推理

## 3 点简述
- 核心问题：现有方法在联合生成时未从结构对齐角度处理，或依赖耗时且易模式崩溃的Score Distillation Sampling。
- 方法要点：利用样本空间中的联合传输，在结构化潜在空间上构建，实现快速推理。
- 实验或效果：在图像、视频和3D形状生成中展示高结构对齐度和视觉质量，提升图像和视频生成性能，3D生成速度显著加快。

## 摘要（原文）

> We suggest a new multi-modal algorithm for joint inference of paired structurally aligned samples with Rectified Flow models. While some existing methods propose a codependent generation process, they do not view the problem of joint generation from a structural alignment perspective. Recent work uses Score Distillation Sampling to generate aligned 3D models, but SDS is known to be time-consuming, prone to mode collapse, and often provides cartoonish results. By contrast, our suggested approach relies on the joint transport of a segment in the sample space, yielding faster computation at inference time. Our approach can be built on top of an arbitrary Rectified Flow model operating on the structured latent space. We show the applicability of our method to the domains of image, video, and 3D shape generation using state-of-the-art baselines and evaluate it against both editing-based and joint inference-based competing approaches. We demonstrate a high degree of structural alignment for the sample pairs obtained with our method and a high visual quality of the samples. Our method improves the state-of-the-art for image and video generation pipelines. For 3D generation, it is able to show comparable quality while working orders of magnitude faster.

