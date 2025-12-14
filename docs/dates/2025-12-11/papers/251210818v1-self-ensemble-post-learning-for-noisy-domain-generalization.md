---
layout: default
title: Self-Ensemble Post Learning for Noisy Domain Generalization
---

# Self-Ensemble Post Learning for Noisy Domain Generalization
**arXiv**：[2512.10818v1](https://arxiv.org/abs/2512.10818) · [PDF](https://arxiv.org/pdf/2512.10818.pdf)  
**作者**：Wang Lu, Jindong Wang  

**一句话要点**：提出自集成后学习方法以解决带噪声标签的域泛化问题

**关键词**：域泛化, 噪声标签, 特征探测, 集成学习, 半监督训练, 鲁棒性增强

## 3 点简述
- 核心问题：域泛化中噪声标签加剧深层伪特征放大，导致算法性能下降
- 方法要点：利用模型中间特征训练多个探测分类器，通过集成预测提升特征多样性
- 实验或效果：实验评估显示方法增强现有方法鲁棒性，具有高灵活性的实际应用潜力

## 摘要（原文）

> While computer vision and machine learning have made great progress, their robustness is still challenged by two key issues: data distribution shift and label noise. When domain generalization (DG) encounters noise, noisy labels further exacerbate the emergence of spurious features in deep layers, i.e. spurious feature enlargement, leading to a degradation in the performance of existing algorithms. This paper, starting from domain generalization, explores how to make existing methods rework when meeting noise. We find that the latent features inside the model have certain discriminative capabilities, and different latent features focus on different parts of the image. Based on these observations, we propose the Self-Ensemble Post Learning approach (SEPL) to diversify features which can be leveraged. Specifically, SEPL consists of two parts: feature probing training and prediction ensemble inference. It leverages intermediate feature representations within the model architecture, training multiple probing classifiers to fully exploit the capabilities of pre-trained models, while the final predictions are obtained through the integration of outputs from these diverse classification heads. Considering the presence of noisy labels, we employ semi-supervised algorithms to train probing classifiers. Given that different probing classifiers focus on different areas, we integrate their predictions using a crowdsourcing inference approach. Extensive experimental evaluations demonstrate that the proposed method not only enhances the robustness of existing methods but also exhibits significant potential for real-world applications with high flexibility.

