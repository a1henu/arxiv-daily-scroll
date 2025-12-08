---
layout: default
title: Ideal Observer for Segmentation of Dead Leaves Images
---

# Ideal Observer for Segmentation of Dead Leaves Images
**arXiv**：[2512.05539v1](https://arxiv.org/abs/2512.05539) · [PDF](https://arxiv.org/pdf/2512.05539.pdf)  
**作者**：Swantje Mahncke, Malte Ott  

**一句话要点**：提出基于贝叶斯理想观测者的死叶图像分割理论方法，用于研究有限像素下的分割决策。

**关键词**：死叶图像模型, 贝叶斯理想观测者, 图像分割, 遮挡处理, 生成模型, 视觉研究

## 3 点简述
- 核心问题：人类视觉环境中物体重叠遮挡导致的分割挑战，需在死叶图像模型中处理像素分区。
- 方法要点：扩展先前工作，推导贝叶斯理想观测者，逐步计算后验概率，并分析实际应用可行性因素。
- 实验或效果：提供性能上限原则，用于比较人类和视觉算法在有限像素分割任务中的表现。

## 摘要（原文）

> The human visual environment is comprised of different surfaces that are distributed in space. The parts of a scene that are visible at any one time are governed by the occlusion of overlapping objects. In this work we consider "dead leaves" models, which replicate these occlusions when generating images by layering objects on top of each other. A dead leaves model is a generative model comprised of distributions for object position, shape, color and texture. An image is generated from a dead leaves model by sampling objects ("leaves") from these distributions until a stopping criterion is reached, usually when the image is fully covered or until a given number of leaves was sampled. Here, we describe a theoretical approach, based on previous work, to derive a Bayesian ideal observer for the partition of a given set of pixels based on independent dead leaves model distributions. Extending previous work, we provide step-by-step explanations for the computation of the posterior probability as well as describe factors that determine the feasibility of practically applying this computation. The dead leaves image model and the associated ideal observer can be applied to study segmentation decisions in a limited number of pixels, providing a principled upper-bound on performance, to which humans and vision algorithms could be compared.

