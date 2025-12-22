---
layout: default
title: AnyCXR: Human Anatomy Segmentation of Chest X-ray at Any Acquisition Position using Multi-stage Domain Randomized Synthetic Data with Imperfect Annotations and Conditional Joint Annotation Regularization Learning
---

# AnyCXR: Human Anatomy Segmentation of Chest X-ray at Any Acquisition Position using Multi-stage Domain Randomized Synthetic Data with Imperfect Annotations and Conditional Joint Annotation Regularization Learning
**arXiv**：[2512.17263v1](https://arxiv.org/abs/2512.17263) · [PDF](https://arxiv.org/pdf/2512.17263.pdf)  
**作者**：Dong Zifei, Wu Wenjie, Hao Jinkui, Chen Tianqi, Weng Ziqiao, Zhou Bo  

**一句话要点**：提出AnyCXR框架，利用多阶段域随机化合成数据和条件联合标注正则化学习，实现任意投照角度胸部X光的多器官分割。

**关键词**：胸部X光分割, 合成数据生成, 域随机化, 标注正则化, 零样本泛化, 临床任务支持

## 3 点简述
- 核心问题：胸部X光分割因标注稀缺和真实采集条件多变而具挑战性。
- 方法要点：结合多阶段域随机化生成合成数据，并通过条件联合标注正则化利用不完美标注。
- 实验或效果：在合成数据上训练，零样本泛化至真实数据集，支持下游临床任务。

## 摘要（原文）

> Robust anatomical segmentation of chest X-rays (CXRs) remains challenging due to the scarcity of comprehensive annotations and the substantial variability of real-world acquisition conditions. We propose AnyCXR, a unified framework that enables generalizable multi-organ segmentation across arbitrary CXR projection angles using only synthetic supervision. The method combines a Multi-stage Domain Randomization (MSDR) engine, which generates over 100,000 anatomically faithful and highly diverse synthetic radiographs from 3D CT volumes, with a Conditional Joint Annotation Regularization (CAR) learning strategy that leverages partial and imperfect labels by enforcing anatomical consistency in a latent space. Trained entirely on synthetic data, AnyCXR achieves strong zero-shot generalization on multiple real-world datasets, providing accurate delineation of 54 anatomical structures in PA, lateral, and oblique views. The resulting segmentation maps support downstream clinical tasks, including automated cardiothoracic ratio estimation, spine curvature assessment, and disease classification, where the incorporation of anatomical priors improves diagnostic performance. These results demonstrate that AnyCXR establishes a scalable and reliable foundation for anatomy-aware CXR analysis and offers a practical pathway toward reducing annotation burdens while improving robustness across diverse imaging conditions.

