---
layout: default
title: Equivariant Learning for Unsupervised Image Dehazing
---

# Equivariant Learning for Unsupervised Image Dehazing
**arXiv**：[2601.13986v1](https://arxiv.org/abs/2601.13986) · [PDF](https://arxiv.org/pdf/2601.13986.pdf)  
**作者**：Zhang Wen, Jiangwei Xie, Dongdong Chen  

**一句话要点**：提出EID框架，利用图像对称性实现无监督去雾，适用于科学成像和自然图像。

**关键词**：无监督去雾, 等变学习, 科学成像, 对抗学习, 图像恢复

## 3 点简述
- 核心问题：传统去雾方法依赖昂贵先验或清晰真值，在科学成像中不实用。
- 方法要点：通过强制雾霾一致性和系统等变性，结合对抗学习建模未知雾霾物理。
- 实验或效果：在科学和自然图像基准测试中显著优于现有方法，代码和数据集将发布。

## 摘要（原文）

> Image Dehazing (ID) aims to produce a clear image from an observation contaminated by haze. Current ID methods typically rely on carefully crafted priors or extensive haze-free ground truth, both of which are expensive or impractical to acquire, particularly in the context of scientific imaging. We propose a new unsupervised learning framework called Equivariant Image Dehazing (EID) that exploits the symmetry of image signals to restore clarity to hazy observations. By enforcing haze consistency and systematic equivariance, EID can recover clear patterns directly from raw, hazy images. Additionally, we propose an adversarial learning strategy to model unknown haze physics and facilitate EID learning. Experiments on two scientific image dehazing benchmarks (including cell microscopy and medical endoscopy) and on natural image dehazing have demonstrated that EID significantly outperforms state-of-the-art approaches. By unifying equivariant learning with modelling haze physics, we hope that EID will enable more versatile and effective haze removal in scientific imaging. Code and datasets will be published.

