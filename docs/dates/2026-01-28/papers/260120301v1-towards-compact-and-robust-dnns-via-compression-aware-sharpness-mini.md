---
layout: default
title: Towards Compact and Robust DNNs via Compression-aware Sharpness Minimization
---

# Towards Compact and Robust DNNs via Compression-aware Sharpness Minimization
**arXiv**：[2601.20301v1](https://arxiv.org/abs/2601.20301) · [PDF](https://arxiv.org/pdf/2601.20301.pdf)  
**作者**：Jialuo He, Huangxun Chen  

**一句话要点**：提出C-SAM框架，通过掩码扰动优化压缩与鲁棒性，解决SAM与模型剪枝的兼容性问题。

**关键词**：模型压缩, 锐度感知最小化, 鲁棒性优化, 剪枝算法, 深度学习框架

## 3 点简述
- 核心问题：SAM与模型剪枝结合时，参数平坦性在结构离散变化下可能损害鲁棒性。
- 方法要点：C-SAM将锐度感知学习从参数扰动转向掩码扰动，以促进结构平坦的损失景观。
- 实验或效果：在多个数据集和模型上，C-SAM提升认证鲁棒性达42%，同时保持任务精度。

## 摘要（原文）

> Sharpness-Aware Minimization (SAM) has recently emerged as an effective technique for improving DNN robustness to input variations. However, its interplay with the compactness requirements of on-device DNN deployments remains less explored. Simply pruning a SAM-trained model can undermine robustness, since flatness in the continuous parameter space does not necessarily translate to robustness under the discrete structural changes induced by pruning. Conversely, applying SAM after pruning may be fundamentally constrained by architectural limitations imposed by an early, robustness-agnostic pruning pattern. To address this gap, we propose Compression-aware ShArpness Minimization (C-SAM), a framework that shifts sharpness-aware learning from parameter perturbations to mask perturbations. By explicitly perturbing pruning masks during training, C-SAM promotes a flatter loss landscape with respect to model structure, enabling the discovery of pruning patterns that simultaneously optimize model compactness and robustness to input variations. Extensive experiments on CelebA-HQ, Flowers-102, and CIFAR-10-C across ResNet-18, GoogLeNet, and MobileNet-V2 show that C-SAM consistently achieves higher certified robustness than strong baselines, with improvements of up to 42%, while maintaining task accuracy comparable to the corresponding unpruned models.

