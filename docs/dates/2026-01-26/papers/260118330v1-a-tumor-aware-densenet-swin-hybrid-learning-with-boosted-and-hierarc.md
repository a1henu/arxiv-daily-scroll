---
layout: default
title: A Tumor Aware DenseNet Swin Hybrid Learning with Boosted and Hierarchical Feature Spaces for Large-Scale Brain MRI Classification
---

# A Tumor Aware DenseNet Swin Hybrid Learning with Boosted and Hierarchical Feature Spaces for Large-Scale Brain MRI Classification
**arXiv**：[2601.18330v1](https://arxiv.org/abs/2601.18330) · [PDF](https://arxiv.org/pdf/2601.18330.pdf)  
**作者**：Muhammad Ali Shah, Muhammad Mansoor Alam, Saddam Hussain Khan  

**一句话要点**：提出EDSH框架以解决脑肿瘤MRI分类中局部纹理与全局依赖的联合建模问题。

**关键词**：脑肿瘤分类, DenseNet, Swin Transformer, 增强特征空间, 分层架构, MRI分析

## 3 点简述
- 核心问题：脑肿瘤MRI分类需同时捕捉细粒度纹理和长程上下文依赖，以应对不同肿瘤类型的诊断挑战。
- 方法要点：采用肿瘤感知设计，包括增强特征空间和分层架构，定制DenseNet和Swin Transformer分支进行互补学习。
- 实验或效果：在大规模MRI数据集上评估，准确率达98.50%，优于现有CNN、ViT及混合模型。

## 摘要（原文）

> This study proposes an efficient Densely Swin Hybrid (EDSH) framework for brain tumor MRI analysis, designed to jointly capture fine grained texture patterns and long range contextual dependencies. Two tumor aware experimental setups are introduced to address class-specific diagnostic challenges. The first setup employs a Boosted Feature Space (BFS), where independently customized DenseNet and Swint branches learn complementary local and global representations that are dimension aligned, fused, and boosted, enabling highly sensitive detection of diffuse glioma patterns by successfully learning the features of irregular shape, poorly defined mass, and heterogeneous texture. The second setup adopts a hierarchical DenseNet Swint architecture with Deep Feature Extraction have Dual Residual connections (DFE and DR), in which DenseNet serves as a stem CNN for structured local feature learning, while Swin_t models global tumor morphology, effectively suppressing false negatives in meningioma and pituitary tumor classification by learning the features of well defined mass, location (outside brain) and enlargments in tumors (dural tail or upward extension). DenseNet is customized at the input level to match MRI spatial characteristics, leveraging dense residual connectivity to preserve texture information and mitigate vanishing-gradient effects. In parallel, Swint is tailored through task aligned patch embedding and shifted-window self attention to efficiently capture hierarchical global dependencies. Extensive evaluation on a large-scale MRI dataset (stringent 40,260 images across four tumor classes) demonstrates consistent superiority over standalone CNNs, Vision Transformers, and hybrids, achieving 98.50 accuracy and recall on the test unseen dataset.

