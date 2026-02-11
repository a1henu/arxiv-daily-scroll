---
layout: default
title: Equilibrium contrastive learning for imbalanced image classification
---

# Equilibrium contrastive learning for imbalanced image classification
**arXiv**：[2602.09506v1](https://arxiv.org/abs/2602.09506) · [PDF](https://arxiv.org/pdf/2602.09506.pdf)  
**作者**：Sumin Roh, Harim Kim, Ho Yun Lee, Il Yong Chun  

**一句话要点**：提出均衡对比学习框架，以解决不平衡图像分类中几何失衡问题

**关键词**：不平衡图像分类, 监督对比学习, 几何均衡, 类原型, 长尾数据集, 医学图像分析

## 3 点简述
- 现有监督对比学习方法在不平衡数据集上存在类均值/原型与分类器未对齐、原型贡献不平衡两个主要局限
- ECL框架通过促进表示几何均衡和分类器-类中心几何均衡来协调类特征、均值和分类器
- 在CIFAR-10-LT、ImageNet-LT等长尾数据集和医学数据集上优于现有最先进方法

## 摘要（原文）

> Contrastive learning (CL) is a predominant technique in image classification, but they showed limited performance with an imbalanced dataset. Recently, several supervised CL methods have been proposed to promote an ideal regular simplex geometric configuration in the representation space-characterized by intra-class feature collapse and uniform inter-class mean spacing, especially for imbalanced datasets. In particular, existing prototype-based methods include class prototypes, as additional samples to consider all classes. However, the existing CL methods suffer from two limitations. First, they do not consider the alignment between the class means/prototypes and classifiers, which could lead to poor generalization. Second, existing prototype-based methods treat prototypes as only one additional sample per class, making their influence depend on the number of class instances in a batch and causing unbalanced contributions across classes. To address these limitations, we propose Equilibrium Contrastive Learning (ECL), a supervised CL framework designed to promote geometric equilibrium, where class features, means, and classifiers are harmoniously balanced under data imbalance. The proposed ECL framework uses two main components. First, ECL promotes the representation geometric equilibrium (i.e., a regular simplex geometry characterized by collapsed class samples and uniformly distributed class means), while balancing the contributions of class-average features and class prototypes. Second, ECL establishes a classifier-class center geometric equilibrium by aligning classifier weights and class prototypes. We ran experiments with three long-tailed datasets, the CIFAR-10(0)-LT, ImageNet-LT, and the two imbalanced medical datasets, the ISIC 2019 and our constructed LCCT dataset. Results show that ECL outperforms existing SOTA supervised CL methods designed for imbalanced classification.

