---
layout: default
title: FusionNet: Physics-Aware Representation Learning for Multi-Spectral and Thermal Data via Trainable Signal-Processing Priors
---

# FusionNet: Physics-Aware Representation Learning for Multi-Spectral and Thermal Data via Trainable Signal-Processing Priors
**arXiv**：[2512.19504v1](https://arxiv.org/abs/2512.19504) · [PDF](https://arxiv.org/pdf/2512.19504.pdf)  
**作者**：Georgios Voulgaris  

**一句话要点**：提出FusionNet，通过可训练信号处理先验增强多光谱与热红外数据的物理感知表示学习。

**关键词**：多光谱学习, 热红外数据, 物理感知表示学习, 可训练信号处理先验, 跨光谱鲁棒性

## 3 点简述
- 核心问题：现有深度学习模型在多模态视觉信号中，归纳偏置与信号形成的物理过程不匹配，导致跨光谱和真实场景性能脆弱。
- 方法要点：集成地质短波红外比率与热红外数据，采用中间融合架构，嵌入可训练微分信号处理先验于卷积层，结合混合池化策略和宽感受野。
- 实验或效果：在五种光谱配置上超越基线，FusionNet准确率达90.6%，真实数据评估显示物理感知特征选择与深度学习架构结合提升鲁棒性和泛化性。

## 摘要（原文）

> Modern deep learning models operating on multi-modal visual signals often rely on inductive biases that are poorly aligned with the physical processes governing signal formation, leading to brittle performance under cross-spectral and real-world conditions. In particular, approaches that prioritise direct thermal cues struggle to capture indirect yet persistent environmental alterations induced by sustained heat emissions.
>   This work introduces a physics-aware representation learning framework that leverages multi-spectral information to model stable signatures of long-term physical processes. Specifically, a geological Short Wave Infrared (SWIR) ratio sensitive to soil property changes is integrated with Thermal Infrared (TIR) data through an intermediate fusion architecture, instantiated as FusionNet. The proposed backbone embeds trainable differential signal-processing priors within convolutional layers, combines mixed pooling strategies, and employs wider receptive fields to enhance robustness across spectral modalities.
>   Systematic ablations show that each architectural component contributes to performance gains, with DGCNN achieving 88.7% accuracy on the SWIR ratio and FusionNet reaching 90.6%, outperforming state-of-the-art baselines across five spectral configurations. Transfer learning experiments further show that ImageNet pretraining degrades TIR performance, highlighting the importance of modality-aware training for cross-spectral learning.
>   Evaluated on real-world data, the results demonstrate that combining physics-aware feature selection with principled deep learning architectures yields robust and generalisable representations, illustrating how first-principles signal modelling can improve multi-spectral learning under challenging conditions.

