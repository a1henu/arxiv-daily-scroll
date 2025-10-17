---
layout: default
title: Hierarchical Re-Classification: Combining Animal Classification Models with Vision Transformers
---

# Hierarchical Re-Classification: Combining Animal Classification Models with Vision Transformers
**arXiv**：[2510.14594v1](https://arxiv.org/abs/2510.14594) · [PDF](https://arxiv.org/pdf/2510.14594.pdf)  
**作者**：Hugo Markoff, Jevgenijs Galaktionovs  

**一句话要点**：提出分层重分类系统以提升动物检测平台物种级识别精度

**关键词**：动物分类, 分层重分类, Vision Transformer, 度量学习, 物种识别, CLIP嵌入

## 3 点简述
- 现有动物分类模型预测保守，常标记为高级分类而非物种级
- 结合SpeciesNet预测、CLIP嵌入和度量学习，构建五阶段重分类流程
- 在LILA BC数据集上验证，重分类准确率96.5%，物种级识别达64.9%

## 摘要（原文）

> State-of-the-art animal classification models like SpeciesNet provide
> predictions across thousands of species but use conservative rollup strategies,
> resulting in many animals labeled at high taxonomic levels rather than species.
> We present a hierarchical re-classification system for the Animal Detect
> platform that combines SpeciesNet EfficientNetV2-M predictions with CLIP
> embeddings and metric learning to refine high-level taxonomic labels toward
> species-level identification. Our five-stage pipeline (high-confidence
> acceptance, bird override, centroid building, triplet-loss metric learning, and
> adaptive cosine-distance scoring) is evaluated on a segment of the LILA BC
> Desert Lion Conservation dataset (4,018 images, 15,031 detections). After
> recovering 761 bird detections from "blank" and "animal" labels, we re-classify
> 456 detections labeled animal, mammal, or blank with 96.5% accuracy, achieving
> species-level identification for 64.9 percent

