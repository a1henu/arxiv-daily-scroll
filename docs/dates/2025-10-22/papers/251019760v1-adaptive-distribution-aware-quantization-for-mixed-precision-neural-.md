---
layout: default
title: Adaptive Distribution-aware Quantization for Mixed-Precision Neural Networks
---

# Adaptive Distribution-aware Quantization for Mixed-Precision Neural Networks
**arXiv**：[2510.19760v1](https://arxiv.org/abs/2510.19760) · [PDF](https://arxiv.org/pdf/2510.19760.pdf)  
**作者**：Shaohang Jia, Zhiyong Huang, Zhi Yu, Mingyang Hou, Shuai Miao, Han Yang  

**一句话要点**：提出自适应分布感知量化框架以解决混合精度神经网络量化问题

**关键词**：混合精度量化, 量化感知训练, 自适应码本, 非均匀分布, 硬件友好映射, 神经网络压缩

## 3 点简述
- 核心问题：激活分布高度非均匀和权重量化码本静态不匹配
- 方法要点：采用分位数初始化、在线码本自适应和敏感度混合精度分配
- 实验或效果：在ImageNet上ResNet-18达71.512%准确率，平均位宽2.81位

## 摘要（原文）

> Quantization-Aware Training (QAT) is a critical technique for deploying deep
> neural networks on resource-constrained devices. However, existing methods
> often face two major challenges: the highly non-uniform distribution of
> activations and the static, mismatched codebooks used in weight quantization.
> To address these challenges, we propose Adaptive Distribution-aware
> Quantization (ADQ), a mixed-precision quantization framework that employs a
> differentiated strategy. The core of ADQ is a novel adaptive weight
> quantization scheme comprising three key innovations: (1) a quantile-based
> initialization method that constructs a codebook closely aligned with the
> initial weight distribution; (2) an online codebook adaptation mechanism based
> on Exponential Moving Average (EMA) to dynamically track distributional shifts;
> and (3) a sensitivity-informed strategy for mixed-precision allocation. For
> activations, we integrate a hardware-friendly non-uniform-to-uniform mapping
> scheme. Comprehensive experiments validate the effectiveness of our method. On
> ImageNet, ADQ enables a ResNet-18 to achieve 71.512% Top-1 accuracy with an
> average bit-width of only 2.81 bits, outperforming state-of-the-art methods
> under comparable conditions. Furthermore, detailed ablation studies on CIFAR-10
> systematically demonstrate the individual contributions of each innovative
> component, validating the rationale and effectiveness of our design.

