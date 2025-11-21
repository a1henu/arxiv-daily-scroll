---
layout: default
title: SpectralTrain: A Universal Framework for Hyperspectral Image Classification
---

# SpectralTrain: A Universal Framework for Hyperspectral Image Classification
**arXiv**：[2511.16084v1](https://arxiv.org/abs/2511.16084) · [PDF](https://arxiv.org/pdf/2511.16084.pdf)  
**作者**：Meihua Zhou, Liping Yu, Jiawei Cai, Wai Kin Fung, Ruiguo Hu, Jiarui Zhao, Wenzhuo Liu, Nan Wan  

**一句话要点**：提出SpectralTrain框架以解决高光谱图像分类中计算成本高的问题

**关键词**：高光谱图像分类, 课程学习, PCA降维, 训练效率优化, 遥感应用

## 3 点简述
- 高光谱图像分类面临大规模数据和计算密集型训练挑战，限制实际部署
- 集成课程学习与PCA降维，逐步引入光谱复杂性，降低计算成本
- 在多个数据集上验证，训练速度提升2-7倍，精度损失小，泛化性强

## 摘要（原文）

> Hyperspectral image (HSI) classification typically involves large-scale data and computationally intensive training, which limits the practical deployment of deep learning models in real-world remote sensing tasks. This study introduces SpectralTrain, a universal, architecture-agnostic training framework that enhances learning efficiency by integrating curriculum learning (CL) with principal component analysis (PCA)-based spectral downsampling. By gradually introducing spectral complexity while preserving essential information, SpectralTrain enables efficient learning of spectral -- spatial patterns at significantly reduced computational costs. The framework is independent of specific architectures, optimizers, or loss functions and is compatible with both classical and state-of-the-art (SOTA) models. Extensive experiments on three benchmark datasets -- Indian Pines, Salinas-A, and the newly introduced CloudPatch-7 -- demonstrate strong generalization across spatial scales, spectral characteristics, and application domains. The results indicate consistent reductions in training time by 2-7x speedups with small-to-moderate accuracy deltas depending on backbone. Its application to cloud classification further reveals potential in climate-related remote sensing, emphasizing training strategy optimization as an effective complement to architectural design in HSI models. Code is available at https://github.com/mh-zhou/SpectralTrain.

