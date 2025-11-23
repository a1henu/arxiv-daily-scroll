---
layout: default
title: Erase to Retain: Low Rank Adaptation Guided Selective Unlearning in Medical Segmentation Networks
---

# Erase to Retain: Low Rank Adaptation Guided Selective Unlearning in Medical Segmentation Networks
**arXiv**：[2511.16574v1](https://arxiv.org/abs/2511.16574) · [PDF](https://arxiv.org/pdf/2511.16574.pdf)  
**作者**：Nirjhor Datta, Md. Golam Rabiul Alam  

**一句话要点**：提出Erase to Retain框架，用于医学分割网络的选择性遗忘以实现隐私合规。

**关键词**：医学图像分割, 选择性遗忘, 低秩适应, 蒸馏训练, 隐私合规, 子空间更新

## 3 点简述
- 核心问题：医学分割网络需选择性移除知识以符合隐私和伦理要求。
- 方法要点：使用教师-学生蒸馏与LoRA约束子空间更新，实现可控遗忘。
- 实验效果：在ISIC和CHASE数据集上，有效降低遗忘集性能，同时保持保留集性能。

## 摘要（原文）

> The ability to selectively remove knowledge from medical segmentation networks is increasingly important for privacy compliance, ethical deployment, and continual dataset revision. We introduce Erase to Retain, a controllable unlearning framework for medical image segmentation that achieves targeted forgetting without full retraining. Our method uses a teacher-student distillation paradigm with Low-Rank Adaptation (LoRA) constrained subspace updates, enabling the student network to erase lesion-specific or class-specific representations in low-rank decoder spaces while preserving global anatomical understanding. During the strong unlearning phase, LoRA modules are adversarially optimized to contradict the teacher's confident predictions on a designated forget subset, enforcing semantic removal. This is followed by a gentle restoration phase that recovers generalization on retained data through head-only supervised refinement.
>   For ISIC segmentation, the student reduces forget-set IoU from 0.875 to 0.509 while maintaining competitive performance on the retain and validation splits (0.647 to 0.677 IoU). On the cross-domain CHASE dataset, Erase to Retain consistently lowers forget-set IoU while preserving utility on retain and validation sets. For ISIC classification, our method decreases accuracy on the forget subset from 87.0 percent to 64.1 percent while improving retain accuracy from 83.9 percent to 90.6 percent.
>   These results demonstrate that LoRA-based subspace unlearning provides a practical pathway toward responsible, controllable, and reversible unlearning in medical image analysis, enabling models to forget sensitive samples or structures while preserving performance where it matters most.

