---
layout: default
title: FGDCC: Fine-Grained Deep Cluster Categorization -- A Framework for Intra-Class Variability Problems in Plant Classification
---

# FGDCC: Fine-Grained Deep Cluster Categorization -- A Framework for Intra-Class Variability Problems in Plant Classification
**arXiv**：[2512.19960v1](https://arxiv.org/abs/2512.19960) · [PDF](https://arxiv.org/pdf/2512.19960.pdf)  
**作者**：Luciano Araujo Dourado Filho, Rodrigo Tripodi Calumby  

**一句话要点**：提出FGDCC框架，通过类内聚类和层次分类缓解细粒度视觉分类中的类内变异问题。

**关键词**：细粒度视觉分类, 类内变异, 聚类学习, 层次分类, 植物分类

## 3 点简述
- 核心问题：类内变异和样本不足阻碍深度学习模型在细粒度视觉分类中的性能提升。
- 方法要点：对每个类别单独聚类生成伪标签，用于层次分类学习更细粒度特征。
- 实验或效果：在PlantNet300k数据集上实现先进性能，但部分组件优化未知，需进一步验证。

## 摘要（原文）

> Intra-class variability is given according to the significance in the degree of dissimilarity between images within a class. In that sense, depending on its intensity, intra-class variability can hinder the learning process for DL models, specially when such classes are also underrepresented, which is a very common scenario in Fine-Grained Visual Categorization (FGVC) tasks. This paper proposes a novel method that aims at leveraging classification performance in FGVC tasks by learning fine-grained features via classification of class-wise cluster assignments. Our goal is to apply clustering over each class individually, which can allow to discover pseudo-labels that encodes a latent degree of similarity between images. In turn, those labels can be employed in a hierarchical classification process that allows to learn more fine-grained visual features and thereby mitigating intra-class variability issues. Initial experiments over the PlantNet300k enabled to shed light upon several key points in which future work will have to be developed in order to find more conclusive evidence regarding the effectiveness of our method. Our method still achieves state-of-the-art performance on the PlantNet300k dataset even though some of its components haven't been shown to be fully optimized. Our code is available at \href{https://github.com/ADAM-UEFS/FGDCC}{https://github.com/ADAM-UEFS/FGDCC}.

