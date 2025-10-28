---
layout: default
title: CURVETE: Curriculum Learning and Progressive Self-supervised Training for Medical Image Classification
---

# CURVETE: Curriculum Learning and Progressive Self-supervised Training for Medical Image Classification
**arXiv**：[2510.23442v1](https://arxiv.org/abs/2510.23442) · [PDF](https://arxiv.org/pdf/2510.23442.pdf)  
**作者**：Asmaa Abbas, Mohamed Gaber, Mohammed M. Abdelsamea  

**一句话要点**：提出CURVETE方法，通过课程学习和自监督训练解决医学图像分类中的样本不足和类别分布不均问题。

**关键词**：医学图像分类, 课程学习, 自监督训练, 样本分解, 类别分布不均, 深度学习

## 3 点简述
- 核心问题：医学图像分析中样本标注困难且类别分布不均，影响模型性能。
- 方法要点：结合课程学习和自监督训练，使用样本分解策略提升泛化能力。
- 实验效果：在脑肿瘤、膝关节X光和Mini-DDSM数据集上，准确率最高达96.60%，优于基线方法。

## 摘要（原文）

> Identifying high-quality and easily accessible annotated samples poses a
> notable challenge in medical image analysis. Transfer learning techniques,
> leveraging pre-training data, offer a flexible solution to this issue. However,
> the impact of fine-tuning diminishes when the dataset exhibits an irregular
> distribution between classes. This paper introduces a novel deep convolutional
> neural network, named Curriculum Learning and Progressive Self-supervised
> Training (CURVETE). CURVETE addresses challenges related to limited samples,
> enhances model generalisability, and improves overall classification
> performance. It achieves this by employing a curriculum learning strategy based
> on the granularity of sample decomposition during the training of generic
> unlabelled samples. Moreover, CURVETE address the challenge of irregular class
> distribution by incorporating a class decomposition approach in the downstream
> task. The proposed method undergoes evaluation on three distinct medical image
> datasets: brain tumour, digital knee x-ray, and Mini-DDSM datasets. We
> investigate the classification performance using a generic self-supervised
> sample decomposition approach with and without the curriculum learning
> component in training the pretext task. Experimental results demonstrate that
> the CURVETE model achieves superior performance on test sets with an accuracy
> of 96.60% on the brain tumour dataset, 75.60% on the digital knee x-ray
> dataset, and 93.35% on the Mini-DDSM dataset using the baseline ResNet-50.
> Furthermore, with the baseline DenseNet-121, it achieved accuracies of 95.77%,
> 80.36%, and 93.22% on the brain tumour, digital knee x-ray, and Mini-DDSM
> datasets, respectively, outperforming other training strategies.

