---
layout: default
title: Addressing data annotation scarcity in Brain Tumor Segmentation on 3D MRI scan Using a Semi-Supervised Teacher-Student Framework
---

# Addressing data annotation scarcity in Brain Tumor Segmentation on 3D MRI scan Using a Semi-Supervised Teacher-Student Framework
**arXiv**：[2602.08797v1](https://arxiv.org/abs/2602.08797) · [PDF](https://arxiv.org/pdf/2602.08797.pdf)  
**作者**：Jiaming Liu, Cheng Ding, Daoqiang Zhang  

**一句话要点**：提出半监督师生框架，结合不确定性伪标签和渐进课程，解决脑肿瘤分割中标注稀缺问题。

**关键词**：脑肿瘤分割, 半监督学习, 不确定性估计, 伪标签, 课程学习, MRI分析

## 3 点简述
- 核心问题：脑肿瘤分割在MRI中受限于昂贵标注和数据异质性，导致模型性能受限。
- 方法要点：使用不确定性感知教师生成伪标签，学生通过置信度驱动课程和双重损失学习高置信区域并遗忘低置信区域。
- 实验或效果：在BraTS 2021上，学生模型在有限标注下显著提升分割性能，尤其在早期阶段，并超越教师模型在肿瘤子区域的表现。

## 摘要（原文）

> Accurate brain tumor segmentation from MRI is limited by expensive annotations and data heterogeneity across scanners and sites. We propose a semi-supervised teacher-student framework that combines an uncertainty-aware pseudo-labeling teacher with a progressive, confidence-based curriculum for the student. The teacher produces probabilistic masks and per-pixel uncertainty; unlabeled scans are ranked by image-level confidence and introduced in stages, while a dual-loss objective trains the student to learn from high-confidence regions and unlearn low-confidence ones. Agreement-based refinement further improves pseudo-label quality. On BraTS 2021, validation DSC increased from 0.393 (10% data) to 0.872 (100%), with the largest gains in early stages, demonstrating data efficiency. The teacher reached a validation DSC of 0.922, and the student surpassed the teacher on tumor subregions (e.g., NCR/NET 0.797 and Edema 0.980); notably, the student recovered the Enhancing class (DSC 0.620) where the teacher failed. These results show that confidence-driven curricula and selective unlearning provide robust segmentation under limited supervision and noisy pseudo-labels.

