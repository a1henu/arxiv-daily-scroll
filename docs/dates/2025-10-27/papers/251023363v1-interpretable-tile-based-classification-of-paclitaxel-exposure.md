---
layout: default
title: Interpretable Tile-Based Classification of Paclitaxel Exposure
---

# Interpretable Tile-Based Classification of Paclitaxel Exposure
**arXiv**：[2510.23363v1](https://arxiv.org/abs/2510.23363) · [PDF](https://arxiv.org/pdf/2510.23363.pdf)  
**作者**：Sean Fletcher, Gabby Scott, Douglas Currie, Xin Zhang, Yuqi Song, Bruce MacLeod  

**一句话要点**：提出基于分块与聚合的管道，用于紫杉醇暴露分类，提升准确性与可解释性。

**关键词**：医学图像分析, 分块分类, 紫杉醇暴露, 模型可解释性, Grad-CAM, Score-CAM

## 3 点简述
- 核心问题：从C6胶质瘤细胞相位对比显微镜图像中分类紫杉醇暴露，剂量差异细微，挑战全图像模型。
- 方法要点：采用简单分块与聚合流程，处理局部图像块并整合输出，实现图像级分类。
- 实验或效果：在基准数据集上达到最先进准确率，比基线提升约20个百分点，并通过交叉验证确认趋势。

## 摘要（原文）

> Medical image analysis is central to drug discovery and preclinical
> evaluation, where scalable, objective readouts can accelerate decision-making.
> We address classification of paclitaxel (Taxol) exposure from phase-contrast
> microscopy of C6 glioma cells -- a task with subtle dose differences that
> challenges full-image models. We propose a simple tiling-and-aggregation
> pipeline that operates on local patches and combines tile outputs into an image
> label, achieving state-of-the-art accuracy on the benchmark dataset and
> improving over the published baseline by around 20 percentage points, with
> trends confirmed by cross-validation. To understand why tiling is effective, we
> further apply Grad-CAM and Score-CAM and attention analyses, which enhance
> model interpretability and point toward robustness-oriented directions for
> future medical image research. Code is released to facilitate reproduction and
> extension.

