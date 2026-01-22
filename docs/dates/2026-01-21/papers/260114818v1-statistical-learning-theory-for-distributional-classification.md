---
layout: default
title: Statistical Learning Theory for Distributional Classification
---

# Statistical Learning Theory for Distributional Classification
**arXiv**：[2601.14818v1](https://arxiv.org/abs/2601.14818) · [PDF](https://arxiv.org/pdf/2601.14818.pdf)  
**作者**：Christian Fiedler  

**一句话要点**：提出基于核方法的分布分类理论分析，聚焦SVM在分布输入下的学习率与一致性

**关键词**：分布分类, 核均值嵌入, 支持向量机, 学习理论, 两阶段采样, 高斯核

## 3 点简述
- 核心问题：在分布输入的两阶段采样设置中，学习阶段仅能访问分布的样本而非分布本身，适用于医疗筛查等应用
- 方法要点：使用核均值嵌入将分布或样本映射到希尔伯特空间，应用SVM等标准核方法，建立新的oracle不等式
- 实验或效果：推导一致性和学习率结果，针对高斯核和铰链损失提出噪声假设变体，技术工具如新特征空间具有独立价值

## 摘要（原文）

> In supervised learning with distributional inputs in the two-stage sampling setup, relevant to applications like learning-based medical screening or causal learning, the inputs (which are probability distributions) are not accessible in the learning phase, but only samples thereof. This problem is particularly amenable to kernel-based learning methods, where the distributions or samples are first embedded into a Hilbert space, often using kernel mean embeddings (KMEs), and then a standard kernel method like Support Vector Machines (SVMs) is applied, using a kernel defined on the embedding Hilbert space. In this work, we contribute to the theoretical analysis of this latter approach, with a particular focus on classification with distributional inputs using SVMs. We establish a new oracle inequality and derive consistency and learning rate results. Furthermore, for SVMs using the hinge loss and Gaussian kernels, we formulate a novel variant of an established noise assumption from the binary classification literature, under which we can establish learning rates. Finally, some of our technical tools like a new feature space for Gaussian kernels on Hilbert spaces are of independent interest.

