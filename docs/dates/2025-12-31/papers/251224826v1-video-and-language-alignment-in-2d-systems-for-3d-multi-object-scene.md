---
layout: default
title: Video and Language Alignment in 2D Systems for 3D Multi-object Scenes with Multi-Information Derivative-Free Control
---

# Video and Language Alignment in 2D Systems for 3D Multi-object Scenes with Multi-Information Derivative-Free Control
**arXiv**：[2512.24826v1](https://arxiv.org/abs/2512.24826) · [PDF](https://arxiv.org/pdf/2512.24826.pdf)  
**作者**：Jason Armitage, Rico Sennnrich  

**一句话要点**：提出基于无导数优化的多元互信息估计方法，以提升2D跨模态系统在3D多物体场景中的在线适应能力。

**关键词**：跨模态系统, 3D场景理解, 无导数优化, 多元互信息, 相机控制, 在线适应

## 3 点简述
- 核心问题：2D跨模态系统处理3D场景时面临维度差异，需控制场景内相机以弥补差距。
- 方法要点：通过遗憾最小化和无导数优化改进多元互信息估计，辅助相机控制模块学习。
- 实验或效果：该方法使系统能在线适应物体遮挡和特征区分，提升跨模态任务性能，无需预训练或微调。

## 摘要（原文）

> Cross-modal systems trained on 2D visual inputs are presented with a dimensional shift when processing 3D scenes. An in-scene camera bridges the dimensionality gap but requires learning a control module. We introduce a new method that improves multivariate mutual information estimates by regret minimisation with derivative-free optimisation. Our algorithm enables off-the-shelf cross-modal systems trained on 2D visual inputs to adapt online to object occlusions and differentiate features. The pairing of expressive measures and value-based optimisation assists control of an in-scene camera to learn directly from the noisy outputs of vision-language models. The resulting pipeline improves performance in cross-modal tasks on multi-object 3D scenes without resorting to pretraining or finetuning.

