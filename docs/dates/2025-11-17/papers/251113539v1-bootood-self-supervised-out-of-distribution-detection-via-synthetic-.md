---
layout: default
title: BootOOD: Self-Supervised Out-of-Distribution Detection via Synthetic Sample Exposure under Neural Collapse
---

# BootOOD: Self-Supervised Out-of-Distribution Detection via Synthetic Sample Exposure under Neural Collapse
**arXiv**：[2511.13539v1](https://arxiv.org/abs/2511.13539) · [PDF](https://arxiv.org/pdf/2511.13539.pdf)  
**作者**：Yuanchao Wang, Tian Qin, Eduardo Valle, Bruno Abrahao  

**一句话要点**：提出BootOOD自监督OOD检测框架，通过合成样本暴露处理语义相似OOD样本。

**关键词**：自监督学习, 分布外检测, 神经崩溃, 特征范数分类, 图像分类

## 3 点简述
- 核心问题：现有OOD检测器在语义相似OOD样本上表现不佳。
- 方法要点：利用神经崩溃合成伪OOD特征，基于特征范数进行半径分类。
- 实验效果：在多个数据集上优于现有方法，保持或提升ID准确率。

## 摘要（原文）

> Out-of-distribution (OOD) detection is critical for deploying image classifiers in safety-sensitive environments, yet existing detectors often struggle when OOD samples are semantically similar to the in-distribution (ID) classes. We present BootOOD, a fully self-supervised OOD detection framework that bootstraps exclusively from ID data and is explicitly designed to handle semantically challenging OOD samples. BootOOD synthesizes pseudo-OOD features through simple transformations of ID representations and leverages Neural Collapse (NC), where ID features cluster tightly around class means with consistent feature norms. Unlike prior approaches that aim to constrain OOD features into subspaces orthogonal to the collapsed ID means, BootOOD introduces a lightweight auxiliary head that performs radius-based classification on feature norms. This design decouples OOD detection from the primary classifier and imposes a relaxed requirement: OOD samples are learned to have smaller feature norms than ID features, which is easier to satisfy when ID and OOD are semantically close. Experiments on CIFAR-10, CIFAR-100, and ImageNet-200 show that BootOOD outperforms prior post-hoc methods, surpasses training-based methods without outlier exposure, and is competitive with state-of-the-art outlier-exposure approaches while maintaining or improving ID accuracy.

