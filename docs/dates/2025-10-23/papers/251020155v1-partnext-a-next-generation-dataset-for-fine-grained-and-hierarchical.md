---
layout: default
title: PartNeXt: A Next-Generation Dataset for Fine-Grained and Hierarchical 3D Part Understanding
---

# PartNeXt: A Next-Generation Dataset for Fine-Grained and Hierarchical 3D Part Understanding
**arXiv**：[2510.20155v1](https://arxiv.org/abs/2510.20155) · [PDF](https://arxiv.org/pdf/2510.20155.pdf)  
**作者**：Penghao Wang, Yiyang He, Xin Lv, Yukai Zhou, Lan Xu, Jingyi Yu, Jiayuan Gu  

**一句话要点**：提出PartNeXt数据集以解决3D细粒度和层次化部件理解的可扩展性和可用性问题

**关键词**：3D部件理解, 细粒度分割, 层次化标注, 纹理3D模型, 多任务评估

## 3 点简述
- 现有数据集依赖无纹理几何和专家标注，限制可扩展性和可用性
- 引入包含2.3万高质量纹理3D模型的细粒度层次化部件标注数据集
- 在部件分割和3D部件问答任务中验证数据集优势，提升模型性能

## 摘要（原文）

> Understanding objects at the level of their constituent parts is fundamental
> to advancing computer vision, graphics, and robotics. While datasets like
> PartNet have driven progress in 3D part understanding, their reliance on
> untextured geometries and expert-dependent annotation limits scalability and
> usability. We introduce PartNeXt, a next-generation dataset addressing these
> gaps with over 23,000 high-quality, textured 3D models annotated with
> fine-grained, hierarchical part labels across 50 categories. We benchmark
> PartNeXt on two tasks: (1) class-agnostic part segmentation, where
> state-of-the-art methods (e.g., PartField, SAMPart3D) struggle with
> fine-grained and leaf-level parts, and (2) 3D part-centric question answering,
> a new benchmark for 3D-LLMs that reveals significant gaps in open-vocabulary
> part grounding. Additionally, training Point-SAM on PartNeXt yields substantial
> gains over PartNet, underscoring the dataset's superior quality and diversity.
> By combining scalable annotation, texture-aware labels, and multi-task
> evaluation, PartNeXt opens new avenues for research in structured 3D
> understanding.

