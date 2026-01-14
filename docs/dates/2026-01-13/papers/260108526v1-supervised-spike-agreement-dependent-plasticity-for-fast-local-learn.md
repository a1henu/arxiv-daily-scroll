---
layout: default
title: Supervised Spike Agreement Dependent Plasticity for Fast Local Learning in Spiking Neural Networks
---

# Supervised Spike Agreement Dependent Plasticity for Fast Local Learning in Spiking Neural Networks
**arXiv**：[2601.08526v1](https://arxiv.org/abs/2601.08526) · [PDF](https://arxiv.org/pdf/2601.08526.pdf)  
**作者**：Gouri Lakshmi S, Athira Chandrasekharan, Harshit Kumar, Muhammed Sahad E, Bikas C Das, Saptarshi Bej  

**一句话要点**：提出监督式脉冲一致性依赖可塑性，以解决脉冲神经网络中快速局部学习的问题。

**关键词**：脉冲神经网络, 监督学习, 局部学习规则, 混合架构, 图像分类

## 3 点简述
- 核心问题：脉冲时序依赖可塑性依赖精确脉冲时序和成对更新，限制权重快速学习。
- 方法要点：引入监督式扩展，用群体一致性指标如Cohen's kappa替代成对比较，保持严格突触局部性和线性时间复杂度。
- 实验或效果：在混合CNN-SNN架构中验证，在多个数据集上展示竞争性性能和快速收敛。

## 摘要（原文）

> Spike-Timing-Dependent Plasticity (STDP) provides a biologically grounded learning rule for spiking neural networks (SNNs), but its reliance on precise spike timing and pairwise updates limits fast learning of weights. We introduce a supervised extension of Spike Agreement-Dependent Plasticity (SADP), which replaces pairwise spike-timing comparisons with population-level agreement metrics such as Cohen's kappa. The proposed learning rule preserves strict synaptic locality, admits linear-time complexity, and enables efficient supervised learning without backpropagation, surrogate gradients, or teacher forcing.
>   We integrate supervised SADP within hybrid CNN-SNN architectures, where convolutional encoders provide compact feature representations that are converted into Poisson spike trains for agreement-driven learning in the SNN. Extensive experiments on MNIST, Fashion-MNIST, CIFAR-10, and biomedical image classification tasks demonstrate competitive performance and fast convergence. Additional analyses show stable performance across broad hyperparameter ranges and compatibility with device-inspired synaptic update dynamics. Together, these results establish supervised SADP as a scalable, biologically grounded, and hardware-aligned learning paradigm for spiking neural networks.

