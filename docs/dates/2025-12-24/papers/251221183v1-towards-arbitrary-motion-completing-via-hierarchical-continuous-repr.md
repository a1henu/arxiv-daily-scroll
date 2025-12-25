---
layout: default
title: Towards Arbitrary Motion Completing via Hierarchical Continuous Representation
---

# Towards Arbitrary Motion Completing via Hierarchical Continuous Representation
**arXiv**：[2512.21183v1](https://arxiv.org/abs/2512.21183) · [PDF](https://arxiv.org/pdf/2512.21183.pdf)  
**作者**：Chenghao Xu, Guangtao Lyu, Qi Liu, Jiexi Yan, Muli Yang, Cheng Deng  

**一句话要点**：提出基于隐式神经表示的层次连续表示框架，实现任意帧率的人体运动序列插值与外推

**关键词**：隐式神经表示, 运动序列补全, 层次时间编码, 参数化激活函数, 傅里叶变换, 任意帧率插值

## 3 点简述
- 核心问题：探索人体运动序列的连续表示，以支持任意帧率的插值、中间帧生成和外推
- 方法要点：采用层次时间编码机制和多尺度特征提取，结合傅里叶变换驱动的参数化激活函数增强表示能力
- 实验或效果：在多个基准数据集上验证了方法的有效性和鲁棒性，提升了运动平滑性和时间一致性

## 摘要（原文）

> Physical motions are inherently continuous, and higher camera frame rates typically contribute to improved smoothness and temporal coherence. For the first time, we explore continuous representations of human motion sequences, featuring the ability to interpolate, inbetween, and even extrapolate any input motion sequences at arbitrary frame rates. To achieve this, we propose a novel parametric activation-induced hierarchical implicit representation framework, referred to as NAME, based on Implicit Neural Representations (INRs). Our method introduces a hierarchical temporal encoding mechanism that extracts features from motion sequences at multiple temporal scales, enabling effective capture of intricate temporal patterns. Additionally, we integrate a custom parametric activation function, powered by Fourier transformations, into the MLP-based decoder to enhance the expressiveness of the continuous representation. This parametric formulation significantly augments the model's ability to represent complex motion behaviors with high accuracy. Extensive evaluations across several benchmark datasets demonstrate the effectiveness and robustness of our proposed approach.

