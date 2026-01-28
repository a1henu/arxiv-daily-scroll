---
layout: default
title: Tri-Reader: An Open-Access, Multi-Stage AI Pipeline for First-Pass Lung Nodule Annotation in Screening CT
---

# Tri-Reader: An Open-Access, Multi-Stage AI Pipeline for First-Pass Lung Nodule Annotation in Screening CT
**arXiv**：[2601.19380v1](https://arxiv.org/abs/2601.19380) · [PDF](https://arxiv.org/pdf/2601.19380.pdf)  
**作者**：Fakrul Islam Tushar, Joseph Y. Lo  

**一句话要点**：提出Tri-Reader多阶段AI管道，用于筛查CT中肺结节的首次标注，以提升敏感度并减轻标注负担。

**关键词**：肺结节检测, CT筛查, 多阶段AI管道, 开源模型, 标注辅助

## 3 点简述
- 核心问题：在筛查CT中实现肺结节的自动首次标注，需平衡高敏感度与低候选负担。
- 方法要点：集成肺分割、结节检测和恶性分类三阶段，基于公开数据集训练的开源模型构建。
- 实验或效果：在多个内外数据集上评估，与专家标注和参考标准比较，验证准确性和泛化性。

## 摘要（原文）

> Using multiple open-access models trained on public datasets, we developed Tri-Reader, a comprehensive, freely available pipeline that integrates lung segmentation, nodule detection, and malignancy classification into a unified tri-stage workflow. The pipeline is designed to prioritize sensitivity while reducing the candidate burden for annotators. To ensure accuracy and generalizability across diverse practices, we evaluated Tri-Reader on multiple internal and external datasets as compared with expert annotations and dataset-provided reference standards.

