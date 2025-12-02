---
layout: default
title: Fantastic Features and Where to Find Them: A Probing Method to combine Features from Multiple Foundation Models
---

# Fantastic Features and Where to Find Them: A Probing Method to combine Features from Multiple Foundation Models
**arXiv**：[2512.01405v1](https://arxiv.org/abs/2512.01405) · [PDF](https://arxiv.org/pdf/2512.01405.pdf)  
**作者**：Benjamin Ramtoula, Pierre-Yves Lajoie, Paul Newman, Daniele De Martini  

**一句话要点**：提出ComBo方法以结合多基础模型特征，提升下游任务性能

**关键词**：基础模型, 特征融合, 探测方法, 轻量适配器, 多模型集成, 下游任务

## 3 点简述
- 现有方法未有效利用多基础模型的互补优势，且可扩展性差
- ComBo通过压缩激活和轻量Transformer整合特征，无需数据集调优
- 在VTAB-1k基准上优于先前探测方法，匹配或超越昂贵替代方案

## 摘要（原文）

> Foundation models (FMs) trained with different objectives and data learn diverse representations, making some more effective than others for specific downstream tasks. Existing adaptation strategies, such as parameter-efficient fine-tuning, focus on individual models and do not exploit the complementary strengths across models. Probing methods offer a promising alternative by extracting information from frozen models, but current techniques do not scale well with large feature sets and often rely on dataset-specific hyperparameter tuning. We propose Combined backBones (ComBo), a simple and scalable probing-based adapter that effectively integrates features from multiple models and layers. ComBo compresses activations from layers of one or more FMs into compact token-wise representations and processes them with a lightweight transformer for task-specific prediction. Crucially, ComBo does not require dataset-specific tuning or backpropagation through the backbone models. However, not all models are equally relevant for all tasks. To address this, we introduce a mechanism that leverages ComBo's joint multi-backbone probing to efficiently evaluate each backbone's task-relevance, enabling both practical model comparison and improved performance through selective adaptation. On the 19 tasks of the VTAB-1k benchmark, ComBo outperforms previous probing methods, matches or surpasses more expensive alternatives, such as distillation-based model merging, and enables efficient probing of tuned models. Our results demonstrate that ComBo offers a practical and general-purpose framework for combining diverse representations from multiple FMs.

