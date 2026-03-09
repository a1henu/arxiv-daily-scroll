---
layout: default
title: Margin and Consistency Supervision for Calibrated and Robust Vision Models
---

# Margin and Consistency Supervision for Calibrated and Robust Vision Models
**arXiv**：[2603.05812v1](https://arxiv.org/abs/2603.05812) · [PDF](https://arxiv.org/pdf/2603.05812.pdf)  
**作者**：Salim Khazem  

**一句话要点**：提出MaCS正则化框架以提升视觉模型的校准性和鲁棒性

**关键词**：模型校准, 鲁棒性训练, 正则化方法, 视觉分类, 分布偏移

## 3 点简述
- 核心问题：深度视觉分类器校准性差且对分布偏移脆弱
- 方法要点：结合边界惩罚和一致性正则化，增强logit分离和局部稳定性
- 实验或效果：在多个基准和骨干网络上改善校准、鲁棒性，保持准确率

## 摘要（原文）

> Deep vision classifiers often achieve high accuracy while remaining poorly calibrated and fragile under small distribution shifts. We present Margin and Consistency Supervision (MaCS), a simple, architecture-agnostic regularization framework that jointly enforces logit-space separation and local prediction stability. MaCS augments cross-entropy with (i) a hinge-squared margin penalty that enforces a target logit gap between the correct class and the strongest competitor, and (ii) a consistency regularizer that minimizes the KL divergence between predictions on clean inputs and mildly perturbed views. We provide a unifying theoretical analysis showing that increasing classification margin while reducing local sensitivity formalized via a Lipschitz-type stability proxy yields improved generalization guarantees and a provable robustness radius bound scaling with the margin-to-sensitivity ratio. Across several image classification benchmarks and several backbones spanning CNNs and Vision Transformers, MaCS consistently improves calibration (lower ECE and NLL) and robustness to common corruptions while preserving or improving top-1 accuracy. Our approach requires no additional data, no architectural changes, and negligible inference overhead, making it an effective drop-in replacement for standard training objectives.

