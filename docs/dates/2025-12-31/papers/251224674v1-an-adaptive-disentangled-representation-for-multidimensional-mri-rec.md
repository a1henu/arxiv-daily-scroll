---
layout: default
title: An Adaptive, Disentangled Representation for Multidimensional MRI Reconstruction
---

# An Adaptive, Disentangled Representation for Multidimensional MRI Reconstruction
**arXiv**：[2512.24674v1](https://arxiv.org/abs/2512.24674) · [PDF](https://arxiv.org/pdf/2512.24674.pdf)  
**作者**：Ruiyang Zhao, Fan Lam  

**一句话要点**：提出自适应解耦表示方法，用于多维MRI重建，无需任务特定训练。

**关键词**：多维MRI重建, 解耦表示, 潜在扩散模型, 零样本自监督学习, 特征相关性利用

## 3 点简述
- 核心问题：多维MRI数据重建中，特征相关性利用不足，且数据有限。
- 方法要点：通过编码器-解码器网络解耦几何与对比度特征，结合潜在扩散模型增强约束。
- 实验或效果：在加速T1和T2参数映射中，性能优于现有方法，无需监督训练。

## 摘要（原文）

> We present a new approach for representing and reconstructing multidimensional magnetic resonance imaging (MRI) data. Our method builds on a novel, learned feature-based image representation that disentangles different types of features, such as geometry and contrast, into distinct low-dimensional latent spaces, enabling better exploitation of feature correlations in multidimensional images and incorporation of pre-learned priors specific to different feature types for reconstruction. More specifically, the disentanglement was achieved via an encoderdecoder network and image transfer training using large public data, enhanced by a style-based decoder design. A latent diffusion model was introduced to impose stronger constraints on distinct feature spaces. New reconstruction formulations and algorithms were developed to integrate the learned representation with a zero-shot selfsupervised learning adaptation and subspace modeling. The proposed method has been evaluated on accelerated T1 and T2 parameter mapping, achieving improved performance over state-of-the-art reconstruction methods, without task-specific supervised training or fine-tuning. This work offers a new strategy for learning-based multidimensional image reconstruction where only limited data are available for problem-specific or task-specific training.

