---
layout: default
title: Credit Assignment via Neural Manifold Noise Correlation
---

# Credit Assignment via Neural Manifold Noise Correlation
**arXiv**：[2601.02636v1](https://arxiv.org/abs/2601.02636) · [PDF](https://arxiv.org/pdf/2601.02636.pdf)  
**作者**：Byungwoo Kang, Maceo Richards, Bernardo Sabatini  

**一句话要点**：提出神经流形噪声相关以解决信用分配中的噪声相关方法扩展性问题

**关键词**：信用分配, 噪声相关, 神经流形, 雅可比矩阵, 生物可塑性, 深度学习

## 3 点简述
- 核心问题：噪声相关方法在信用分配中因需大量扰动而扩展性差，且与神经活动的低维流形特性不符
- 方法要点：通过限制扰动于神经流形，利用训练网络中的雅可比行空间与流形对齐，提高信用分配效率
- 实验或效果：在CIFAR-10、ImageNet规模模型和循环网络中，相比原始噪声相关，性能与样本效率显著提升，并产生更接近灵长类视觉系统的表示

## 摘要（原文）

> Credit assignment--how changes in individual neurons and synapses affect a network's output--is central to learning in brains and machines. Noise correlation, which estimates gradients by correlating perturbations of activity with changes in output, provides a biologically plausible solution to credit assignment but scales poorly as accurately estimating the Jacobian requires that the number of perturbations scale with network size. Moreover, isotropic noise conflicts with neurobiological observations that neural activity lies on a low-dimensional manifold. To address these drawbacks, we propose neural manifold noise correlation (NMNC), which performs credit assignment using perturbations restricted to the neural manifold. We show theoretically and empirically that the Jacobian row space aligns with the neural manifold in trained networks, and that manifold dimensionality scales slowly with network size. NMNC substantially improves performance and sample efficiency over vanilla noise correlation in convolutional networks trained on CIFAR-10, ImageNet-scale models, and recurrent networks. NMNC also yields representations more similar to the primate visual system than vanilla noise correlation. These findings offer a mechanistic hypothesis for how biological circuits could support credit assignment, and suggest that biologically inspired constraints may enable, rather than limit, effective learning at scale.

