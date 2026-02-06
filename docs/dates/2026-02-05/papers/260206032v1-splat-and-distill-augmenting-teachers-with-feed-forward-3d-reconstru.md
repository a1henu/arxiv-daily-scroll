---
layout: default
title: Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation
---

# Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation
**arXiv**：[2602.06032v1](https://arxiv.org/abs/2602.06032) · [PDF](https://arxiv.org/pdf/2602.06032.pdf)  
**作者**：David Shavin, Sagie Benaim  

**一句话要点**：提出Splat and Distill框架，通过前馈3D重建增强教师模型以提升2D视觉基础模型的3D感知能力

**关键词**：3D感知, 知识蒸馏, 前馈3D重建, 高斯表示, 视觉基础模型, 多视角对应

## 3 点简述
- 核心问题：2D视觉基础模型缺乏3D感知，影响下游任务性能
- 方法要点：使用前馈方式将2D特征提升为3D高斯表示，并投影到新视角以监督学生模型
- 实验或效果：在深度估计、表面法线估计等任务中显著优于先前方法，增强特征语义丰富性

## 摘要（原文）

> Vision Foundation Models (VFMs) have achieved remarkable success when applied to various downstream 2D tasks. Despite their effectiveness, they often exhibit a critical lack of 3D awareness. To this end, we introduce Splat and Distill, a framework that instills robust 3D awareness into 2D VFMs by augmenting the teacher model with a fast, feed-forward 3D reconstruction pipeline. Given 2D features produced by a teacher model, our method first lifts these features into an explicit 3D Gaussian representation, in a feedforward manner. These 3D features are then ``splatted" onto novel viewpoints, producing a set of novel 2D feature maps used to supervise the student model, ``distilling" geometrically grounded knowledge. By replacing slow per-scene optimization of prior work with our feed-forward lifting approach, our framework avoids feature-averaging artifacts, creating a dynamic learning process where the teacher's consistency improves alongside that of the student. We conduct a comprehensive evaluation on a suite of downstream tasks, including monocular depth estimation, surface normal estimation, multi-view correspondence, and semantic segmentation. Our method significantly outperforms prior works, not only achieving substantial gains in 3D awareness but also enhancing the underlying semantic richness of 2D features. Project page is available at https://davidshavin4.github.io/Splat-and-Distill/

