---
layout: default
title: Towards Open-Set Myoelectric Gesture Recognition via Dual-Perspective Inconsistency Learning
---

# Towards Open-Set Myoelectric Gesture Recognition via Dual-Perspective Inconsistency Learning
**arXiv**：[2511.08344v1](https://arxiv.org/abs/2511.08344) · [PDF](https://arxiv.org/pdf/2511.08344.pdf)  
**作者**：Chen Liu, Can Han, Weishi Xu, Yaqi Wang, Dahong Qian  

**一句话要点**：提出SASG-DA数据增强方法以解决sEMG手势识别中的过拟合和泛化问题

**关键词**：表面肌电手势识别, 数据增强, 扩散模型, 语义引导, 稀疏感知采样, 泛化性能

## 3 点简述
- 核心问题：sEMG手势识别数据稀缺导致模型过拟合和泛化能力差
- 方法要点：使用扩散模型结合语义引导和稀疏感知采样生成忠实多样样本
- 实验或效果：在Ninapro数据集上显著优于现有增强方法，提升识别性能

## 摘要（原文）

> Surface electromyography (sEMG)-based gesture recognition plays a critical role in human-machine interaction (HMI), particularly for rehabilitation and prosthetic control. However, sEMG-based systems often suffer from the scarcity of informative training data, leading to overfitting and poor generalization in deep learning models. Data augmentation offers a promising approach to increasing the size and diversity of training data, where faithfulness and diversity are two critical factors to effectiveness. However, promoting untargeted diversity can result in redundant samples with limited utility. To address these challenges, we propose a novel diffusion-based data augmentation approach, Sparse-Aware Semantic-Guided Diffusion Augmentation (SASG-DA). To enhance generation faithfulness, we introduce the Semantic Representation Guidance (SRG) mechanism by leveraging fine-grained, task-aware semantic representations as generation conditions. To enable flexible and diverse sample generation, we propose a Gaussian Modeling Semantic Modeling (GMSS) strategy, which models the semantic representation distribution and allows stochastic sampling to produce both faithful and diverse samples. To enhance targeted diversity, we further introduce a Sparse-Aware Semantic Sampling strategy to explicitly explore underrepresented regions, improving distribution coverage and sample utility. Extensive experiments on benchmark sEMG datasets, Ninapro DB2, DB4, and DB7, demonstrate that SASG-DA significantly outperforms existing augmentation methods. Overall, our proposed data augmentation approach effectively mitigates overfitting and improves recognition performance and generalization by offering both faithful and diverse samples.

