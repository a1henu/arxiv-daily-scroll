---
layout: default
title: Calibratable Disambiguation Loss for Multi-Instance Partial-Label Learning
---

# Calibratable Disambiguation Loss for Multi-Instance Partial-Label Learning
**arXiv**：[2512.17788v1](https://arxiv.org/abs/2512.17788) · [PDF](https://arxiv.org/pdf/2512.17788.pdf)  
**作者**：Wei Tang, Yin-Fang Yang, Weijia Zhang, Min-Ling Zhang  

**一句话要点**：提出可校准消歧损失以提升多示例部分标签学习的分类准确性和校准性能

**关键词**：多示例部分标签学习, 弱监督学习, 校准性能, 消歧损失, 概率校准

## 3 点简述
- 现有MIPL方法校准性能差，影响分类器可靠性
- 提出两种可校准消歧损失，基于候选标签集或结合非候选标签集概率
- 实验验证CDL显著提升分类和校准性能，理论分析支持其优越性

## 摘要（原文）

> Multi-instance partial-label learning (MIPL) is a weakly supervised framework that extends the principles of multi-instance learning (MIL) and partial-label learning (PLL) to address the challenges of inexact supervision in both instance and label spaces. However, existing MIPL approaches often suffer from poor calibration, undermining classifier reliability. In this work, we propose a plug-and-play calibratable disambiguation loss (CDL) that simultaneously improves classification accuracy and calibration performance. The loss has two instantiations: the first one calibrates predictions based on probabilities from the candidate label set, while the second one integrates probabilities from both candidate and non-candidate label sets. The proposed CDL can be seamlessly incorporated into existing MIPL and PLL frameworks. We provide a theoretical analysis that establishes the lower bound and regularization properties of CDL, demonstrating its superiority over conventional disambiguation losses. Experimental results on benchmark and real-world datasets confirm that our CDL significantly enhances both classification and calibration performance.

