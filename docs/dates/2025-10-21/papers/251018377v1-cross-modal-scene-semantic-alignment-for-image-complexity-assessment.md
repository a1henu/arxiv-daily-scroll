---
layout: default
title: Cross-Modal Scene Semantic Alignment for Image Complexity Assessment
---

# Cross-Modal Scene Semantic Alignment for Image Complexity Assessment
**arXiv**：[2510.18377v1](https://arxiv.org/abs/2510.18377) · [PDF](https://arxiv.org/pdf/2510.18377.pdf)  
**作者**：Yuqing Luo, Yixiao Li, Jiang Liu, Jun Fu, Hadi Amirpour, Guanghui Yue, Baoquan Zhao, Padraig Corcoran, Hantao Liu, Wei Zhou  

**一句话要点**：提出跨模态场景语义对齐方法以提升图像复杂度评估性能

**关键词**：图像复杂度评估, 跨模态学习, 场景语义对齐, 计算机视觉, 感知评估

## 3 点简述
- 核心问题：现有图像复杂度评估方法依赖单模态特征，难以捕捉人类感知的复杂性。
- 方法要点：设计复杂度回归分支和场景语义对齐分支，通过跨模态学习对齐图像与文本提示。
- 实验或效果：在多个数据集上显著优于现有方法，代码已开源。

## 摘要（原文）

> Image complexity assessment (ICA) is a challenging task in perceptual
> evaluation due to the subjective nature of human perception and the inherent
> semantic diversity in real-world images. Existing ICA methods predominantly
> rely on hand-crafted or shallow convolutional neural network-based features of
> a single visual modality, which are insufficient to fully capture the perceived
> representations closely related to image complexity. Recently, cross-modal
> scene semantic information has been shown to play a crucial role in various
> computer vision tasks, particularly those involving perceptual understanding.
> However, the exploration of cross-modal scene semantic information in the
> context of ICA remains unaddressed. Therefore, in this paper, we propose a
> novel ICA method called Cross-Modal Scene Semantic Alignment (CM-SSA), which
> leverages scene semantic alignment from a cross-modal perspective to enhance
> ICA performance, enabling complexity predictions to be more consistent with
> subjective human perception. Specifically, the proposed CM-SSA consists of a
> complexity regression branch and a scene semantic alignment branch. The
> complexity regression branch estimates image complexity levels under the
> guidance of the scene semantic alignment branch, while the scene semantic
> alignment branch is used to align images with corresponding text prompts that
> convey rich scene semantic information by pair-wise learning. Extensive
> experiments on several ICA datasets demonstrate that the proposed CM-SSA
> significantly outperforms state-of-the-art approaches. Codes are available at
> https://github.com/XQ2K/First-Cross-Model-ICA.

