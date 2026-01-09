---
layout: default
title: Training a Custom CNN on Five Heterogeneous Image Datasets
---

# Training a Custom CNN on Five Heterogeneous Image Datasets
**arXiv**：[2601.04727v1](https://arxiv.org/abs/2601.04727) · [PDF](https://arxiv.org/pdf/2601.04727.pdf)  
**作者**：Anika Tabassum, Tasnuva Mahazabin Tuba, Nafisa Naznin  

**一句话要点**：提出轻量级自定义CNN，在农业与城市图像数据集上实现高效分类，并比较迁移学习与深度架构的优势。

**关键词**：卷积神经网络, 图像分类, 迁移学习, 异构数据集, 农业视觉, 城市监控

## 3 点简述
- 研究CNN在五个异构图像数据集上的有效性，涵盖芒果品种分类、道路状况评估等应用场景。
- 评估自定义CNN、ResNet-18和VGG-16，通过预处理、数据增强和迁移学习分析性能差异。
- 自定义CNN在多个领域表现竞争性，迁移学习在数据受限环境中提供显著优势。

## 摘要（原文）

> Deep learning has transformed visual data analysis, with Convolutional Neural Networks (CNNs) becoming highly effective in learning meaningful feature representations directly from images. Unlike traditional manual feature engineering methods, CNNs automatically extract hierarchical visual patterns, enabling strong performance across diverse real-world contexts. This study investigates the effectiveness of CNN-based architectures across five heterogeneous datasets spanning agricultural and urban domains: mango variety classification, paddy variety identification, road surface condition assessment, auto-rickshaw detection, and footpath encroachment monitoring. These datasets introduce varying challenges, including differences in illumination, resolution, environmental complexity, and class imbalance, necessitating adaptable and robust learning models.
>   We evaluate a lightweight, task-specific custom CNN alongside established deep architectures, including ResNet-18 and VGG-16, trained both from scratch and using transfer learning. Through systematic preprocessing, augmentation, and controlled experimentation, we analyze how architectural complexity, model depth, and pre-training influence convergence, generalization, and performance across datasets of differing scale and difficulty. The key contributions of this work are: (1) the development of an efficient custom CNN that achieves competitive performance across multiple application domains, and (2) a comprehensive comparative analysis highlighting when transfer learning and deep architectures provide substantial advantages, particularly in data-constrained environments. These findings offer practical insights for deploying deep learning models in resource-limited yet high-impact real-world visual classification tasks.

