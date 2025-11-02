---
layout: default
title: BRIQA: Balanced Reweighting in Image Quality Assessment of Pediatric Brain MRI
---

# BRIQA: Balanced Reweighting in Image Quality Assessment of Pediatric Brain MRI
**arXiv**：[2510.26661v1](https://arxiv.org/abs/2510.26661) · [PDF](https://arxiv.org/pdf/2510.26661.pdf)  
**作者**：Alya Almsouti, Ainur Khamitova, Darya Taratynova, Mohammad Yaqub  

**一句话要点**：提出BRIQA方法以解决儿科脑MRI图像质量评估中的类别不平衡问题

**关键词**：图像质量评估, 类别不平衡, 损失重加权, 旋转批处理, 儿科脑MRI, 伪影分类

## 3 点简述
- 核心问题：儿科脑MRI中伪影严重程度评估存在类别不平衡，影响诊断准确性。
- 方法要点：使用梯度损失重加权和旋转批处理，动态调整类别贡献，促进平衡学习。
- 实验或效果：BRIQA将平均宏F1分数从0.659提升至0.706，在多种伪影分类中表现改善。

## 摘要（原文）

> Assessing the severity of artifacts in pediatric brain Magnetic Resonance
> Imaging (MRI) is critical for diagnostic accuracy, especially in low-field
> systems where the signal-to-noise ratio is reduced. Manual quality assessment
> is time-consuming and subjective, motivating the need for robust automated
> solutions. In this work, we propose BRIQA (Balanced Reweighting in Image
> Quality Assessment), which addresses class imbalance in artifact severity
> levels. BRIQA uses gradient-based loss reweighting to dynamically adjust
> per-class contributions and employs a rotating batching scheme to ensure
> consistent exposure to underrepresented classes. Through experiments, no single
> architecture performs best across all artifact types, emphasizing the
> importance of architectural diversity. The rotating batching configuration
> improves performance across metrics by promoting balanced learning when
> combined with cross-entropy loss. BRIQA improves average macro F1 score from
> 0.659 to 0.706, with notable gains in Noise (0.430), Zipper (0.098),
> Positioning (0.097), Contrast (0.217), Motion (0.022), and Banding (0.012)
> artifact severity classification. The code is available at
> https://github.com/BioMedIA-MBZUAI/BRIQA.

