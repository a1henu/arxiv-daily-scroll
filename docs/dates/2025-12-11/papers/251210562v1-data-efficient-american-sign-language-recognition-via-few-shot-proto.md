---
layout: default
title: Data-Efficient American Sign Language Recognition via Few-Shot Prototypical Networks
---

# Data-Efficient American Sign Language Recognition via Few-Shot Prototypical Networks
**arXiv**：[2512.10562v1](https://arxiv.org/abs/2512.10562) · [PDF](https://arxiv.org/pdf/2512.10562.pdf)  
**作者**：Meher Md Saad  

**一句话要点**：提出基于骨架编码器的少样本原型网络，以解决孤立手语识别中的数据稀缺和长尾分布问题。

**关键词**：孤立手语识别, 少样本学习, 原型网络, 骨架编码, 度量学习, 零样本泛化

## 3 点简述
- 核心问题：孤立手语识别受限于数据稀缺和词汇长尾分布，传统分类方法易过拟合且泛化差。
- 方法要点：采用少样本原型网络，结合ST-GCN和多尺度时间聚合模块，学习语义度量空间进行动态分类。
- 实验或效果：在WLASL数据集上Top-1准确率43.75%，优于基线超13%，并在SignASL上实现近30%零样本泛化。

## 摘要（原文）

> Isolated Sign Language Recognition (ISLR) is critical for bridging the communication gap between the Deaf and Hard-of-Hearing (DHH) community and the hearing world. However, robust ISLR is fundamentally constrained by data scarcity and the long-tail distribution of sign vocabulary, where gathering sufficient examples for thousands of unique signs is prohibitively expensive. Standard classification approaches struggle under these conditions, often overfitting to frequent classes while failing to generalize to rare ones. To address this bottleneck, we propose a Few-Shot Prototypical Network framework adapted for a skeleton based encoder. Unlike traditional classifiers that learn fixed decision boundaries, our approach utilizes episodic training to learn a semantic metric space where signs are classified based on their proximity to dynamic class prototypes. We integrate a Spatiotemporal Graph Convolutional Network (ST-GCN) with a novel Multi-Scale Temporal Aggregation (MSTA) module to capture both rapid and fluid motion dynamics. Experimental results on the WLASL dataset demonstrate the superiority of this metric learning paradigm: our model achieves 43.75% Top-1 and 77.10% Top-5 accuracy on the test set. Crucially, this outperforms a standard classification baseline sharing the identical backbone architecture by over 13%, proving that the prototypical training strategy effectively outperforms in a data scarce situation where standard classification fails. Furthermore, the model exhibits strong zero-shot generalization, achieving nearly 30% accuracy on the unseen SignASL dataset without fine-tuning, offering a scalable pathway for recognizing extensive sign vocabularies with limited data.

