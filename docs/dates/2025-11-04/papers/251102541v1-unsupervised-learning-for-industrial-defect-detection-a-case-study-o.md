---
layout: default
title: Unsupervised Learning for Industrial Defect Detection: A Case Study on Shearographic Data
---

# Unsupervised Learning for Industrial Defect Detection: A Case Study on Shearographic Data
**arXiv**：[2511.02541v1](https://arxiv.org/abs/2511.02541) · [PDF](https://arxiv.org/pdf/2511.02541.pdf)  
**作者**：Jessica Plassmann, Nicolas Schuler, Georg von Freymann, Michael Schuth  

**一句话要点**：提出无监督学习方法以解决工业剪切散斑缺陷检测中的标签依赖问题

**关键词**：无监督学习, 缺陷检测, 剪切散斑, 学生-教师模型, 自动编码器, 工业检测

## 3 点简述
- 核心问题：剪切散斑检测依赖专家解释，工业应用受限。
- 方法要点：评估三种无监督模型，仅用无缺陷数据训练。
- 实验或效果：学生-教师模型在分类和定位上表现最优。

## 摘要（原文）

> Shearography is a non-destructive testing method for detecting subsurface
> defects, offering high sensitivity and full-field inspection capabilities.
> However, its industrial adoption remains limited due to the need for expert
> interpretation. To reduce reliance on labeled data and manual evaluation, this
> study explores unsupervised learning methods for automated anomaly detection in
> shearographic images. Three architectures are evaluated: a fully connected
> autoencoder, a convolutional autoencoder, and a student-teacher feature
> matching model. All models are trained solely on defect-free data. A controlled
> dataset was developed using a custom specimen with reproducible defect
> patterns, enabling systematic acquisition of shearographic measurements under
> both ideal and realistic deformation conditions. Two training subsets were
> defined: one containing only undistorted, defect-free samples, and one
> additionally including globally deformed, yet defect-free, data. The latter
> simulates practical inspection conditions by incorporating deformation-induced
> fringe patterns that may obscure localized anomalies. The models are evaluated
> in terms of binary classification and, for the student-teacher model, spatial
> defect localization. Results show that the student-teacher approach achieves
> superior classification robustness and enables precise localization. Compared
> to the autoencoder-based models, it demonstrates improved separability of
> feature representations, as visualized through t-SNE embeddings. Additionally,
> a YOLOv8 model trained on labeled defect data serves as a reference to
> benchmark localization quality. This study underscores the potential of
> unsupervised deep learning for scalable, label-efficient shearographic
> inspection in industrial environments.

