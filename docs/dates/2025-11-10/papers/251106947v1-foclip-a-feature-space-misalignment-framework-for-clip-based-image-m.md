---
layout: default
title: FoCLIP: A Feature-Space Misalignment Framework for CLIP-Based Image Manipulation and Detection
---

# FoCLIP: A Feature-Space Misalignment Framework for CLIP-Based Image Manipulation and Detection
**arXiv**：[2511.06947v1](https://arxiv.org/abs/2511.06947) · [PDF](https://arxiv.org/pdf/2511.06947.pdf)  
**作者**：Yulin Chen, Zeyuan Wang, Tianyuan Yu, Yingmei Wei, Liang Bai  

**一句话要点**：提出FoCLIP框架以误导CLIP评分并实现检测防御

**关键词**：特征空间错位, CLIP评分误导, 多模态对齐, 图像质量评估, 检测防御

## 3 点简述
- 核心问题：CLIP评分易受特征空间对齐影响，导致图像质量评估脆弱。
- 方法要点：结合特征对齐、分数平衡和像素保护，优化多模态输出。
- 实验效果：在艺术和ImageNet数据集上提升CLIP评分，检测准确率达91%。

## 摘要（原文）

> The well-aligned attribute of CLIP-based models enables its effective
> application like CLIPscore as a widely adopted image quality assessment metric.
> However, such a CLIP-based metric is vulnerable for its delicate multimodal
> alignment. In this work, we propose \textbf{FoCLIP}, a feature-space
> misalignment framework for fooling CLIP-based image quality metric. Based on
> the stochastic gradient descent technique, FoCLIP integrates three key
> components to construct fooling examples: feature alignment as the core module
> to reduce image-text modality gaps, the score distribution balance module and
> pixel-guard regularization, which collectively optimize multimodal output
> equilibrium between CLIPscore performance and image quality. Such a design can
> be engineered to maximize the CLIPscore predictions across diverse input
> prompts, despite exhibiting either visual unrecognizability or semantic
> incongruence with the corresponding adversarial prompts from human perceptual
> perspectives. Experiments on ten artistic masterpiece prompts and ImageNet
> subsets demonstrate that optimized images can achieve significant improvement
> in CLIPscore while preserving high visual fidelity. In addition, we found that
> grayscale conversion induces significant feature degradation in fooling images,
> exhibiting noticeable CLIPscore reduction while preserving statistical
> consistency with original images. Inspired by this phenomenon, we propose a
> color channel sensitivity-driven tampering detection mechanism that achieves
> 91% accuracy on standard benchmarks. In conclusion, this work establishes a
> practical pathway for feature misalignment in CLIP-based multimodal systems and
> the corresponding defense method.

