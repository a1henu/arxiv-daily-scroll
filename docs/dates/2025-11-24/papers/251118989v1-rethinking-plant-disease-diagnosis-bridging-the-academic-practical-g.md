---
layout: default
title: Rethinking Plant Disease Diagnosis: Bridging the Academic-Practical Gap with Vision Transformers and Zero-Shot Learning
---

# Rethinking Plant Disease Diagnosis: Bridging the Academic-Practical Gap with Vision Transformers and Zero-Shot Learning
**arXiv**：[2511.18989v1](https://arxiv.org/abs/2511.18989) · [PDF](https://arxiv.org/pdf/2511.18989.pdf)  
**作者**：Wassim Benabbas, Mohammed Brahimi, Samir Akhrouf, Bilal Fortas  

**一句话要点**：探索视觉变换器与零样本学习以弥合植物病害分类的学术-实践差距

**关键词**：植物病害分类, 视觉变换器, 零样本学习, 领域适应, CLIP模型, 泛化能力

## 3 点简述
- 核心问题：基于PlantVillage数据集的模型在真实农田图像上泛化能力差，存在学术-实践鸿沟。
- 方法要点：评估CNN、视觉变换器和基于CLIP的零样本模型，后者无需任务训练即可分类。
- 实验或效果：视觉变换器泛化更强，CLIP模型提供高适应性和可解释性，零样本学习潜力显著。

## 摘要（原文）

> Recent advances in deep learning have enabled significant progress in plant disease classification using leaf images. Much of the existing research in this field has relied on the PlantVillage dataset, which consists of well-centered plant images captured against uniform, uncluttered backgrounds. Although models trained on this dataset achieve high accuracy, they often fail to generalize to real-world field images, such as those submitted by farmers to plant diagnostic systems. This has created a significant gap between published studies and practical application requirements, highlighting the necessity of investigating and addressing this issue. In this study, we investigate whether attention-based architectures and zero-shot learning approaches can bridge the gap between curated academic datasets and real-world agricultural conditions in plant disease classification. We evaluate three model categories: Convolutional Neural Networks (CNNs), Vision Transformers, and Contrastive Language-Image Pre-training (CLIP)-based zero-shot models. While CNNs exhibit limited robustness under domain shift, Vision Transformers demonstrate stronger generalization by capturing global contextual features. Most notably, CLIP models classify diseases directly from natural language descriptions without any task-specific training, offering strong adaptability and interpretability. These findings highlight the potential of zero-shot learning as a practical and scalable domain adaptation strategy for plant health diagnosis in diverse field environments.

