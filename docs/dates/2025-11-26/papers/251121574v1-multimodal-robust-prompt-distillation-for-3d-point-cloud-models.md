---
layout: default
title: Multimodal Robust Prompt Distillation for 3D Point Cloud Models
---

# Multimodal Robust Prompt Distillation for 3D Point Cloud Models
**arXiv**：[2511.21574v1](https://arxiv.org/abs/2511.21574) · [PDF](https://arxiv.org/pdf/2511.21574.pdf)  
**作者**：Xiang Gu, Liming Lu, Xu Zheng, Anan Du, Yongbin Zhou, Shuchao Pang  

**一句话要点**：提出多模态鲁棒提示蒸馏框架以增强3D点云模型对抗攻击的鲁棒性

**关键词**：3D点云模型, 对抗攻击防御, 多模态学习, 知识蒸馏, 鲁棒性增强, 提示学习

## 3 点简述
- 核心问题：对抗攻击威胁3D点云模型可靠性，现有防御方法计算开销高且泛化能力差
- 方法要点：使用教师-学生框架，通过多模态特征对齐和置信门控机制蒸馏鲁棒模型
- 实验或效果：在多种白盒和黑盒攻击下优于现有方法，推理时无额外计算成本

## 摘要（原文）

> Adversarial attacks pose a significant threat to learning-based 3D point cloud models, critically undermining their reliability in security-sensitive applications. Existing defense methods often suffer from (1) high computational overhead and (2) poor generalization ability across diverse attack types. To bridge these gaps, we propose a novel yet efficient teacher-student framework, namely Multimodal Robust Prompt Distillation (MRPD) for distilling robust 3D point cloud model. It learns lightweight prompts by aligning student point cloud model's features with robust embeddings from three distinct teachers: a vision model processing depth projections, a high-performance 3D model, and a text encoder. To ensure a reliable knowledge transfer, this distillation is guided by a confidence-gated mechanism which dynamically balances the contribution of all input modalities. Notably, since the distillation is all during the training stage, there is no additional computational cost at inference. Extensive experiments demonstrate that MRPD substantially outperforms state-of-the-art defense methods against a wide range of white-box and black-box attacks, while even achieving better performance on clean data. Our work presents a new, practical paradigm for building robust 3D vision systems by efficiently harnessing multimodal knowledge.

