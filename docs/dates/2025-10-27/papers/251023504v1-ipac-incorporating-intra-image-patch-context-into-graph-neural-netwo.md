---
layout: default
title: iPac: Incorporating Intra-image Patch Context into Graph Neural Networks for Medical Image Classification
---

# iPac: Incorporating Intra-image Patch Context into Graph Neural Networks for Medical Image Classification
**arXiv**：[2510.23504v1](https://arxiv.org/abs/2510.23504) · [PDF](https://arxiv.org/pdf/2510.23504.pdf)  
**作者**：Usama Zidan, Mohamed Gaber, Mohammed M. Abdelsamea  

**一句话要点**：提出iPac方法，通过整合图像内补丁上下文增强图神经网络，以改进医学图像分类。

**关键词**：图神经网络, 医学图像分类, 图像补丁上下文, 图表示学习, 特征聚类

## 3 点简述
- 核心问题：图神经网络在图像分类中忽视视觉实体间结构和关系，限制性能。
- 方法要点：结合补丁划分、特征提取、聚类、图构建和学习，构建语义图表示。
- 实验或效果：在多个医学图像数据集上，平均准确率提升最高达5%。

## 摘要（原文）

> Graph neural networks have emerged as a promising paradigm for image
> processing, yet their performance in image classification tasks is hindered by
> a limited consideration of the underlying structure and relationships among
> visual entities. This work presents iPac, a novel approach to introduce a new
> graph representation of images to enhance graph neural network image
> classification by recognizing the importance of underlying structure and
> relationships in medical image classification. iPac integrates various stages,
> including patch partitioning, feature extraction, clustering, graph
> construction, and graph-based learning, into a unified network to advance graph
> neural network image classification. By capturing relevant features and
> organising them into clusters, we construct a meaningful graph representation
> that effectively encapsulates the semantics of the image. Experimental
> evaluation on diverse medical image datasets demonstrates the efficacy of iPac,
> exhibiting an average accuracy improvement of up to 5% over baseline methods.
> Our approach offers a versatile and generic solution for image classification,
> particularly in the realm of medical images, by leveraging the graph
> representation and accounting for the inherent structure and relationships
> among visual entities.

