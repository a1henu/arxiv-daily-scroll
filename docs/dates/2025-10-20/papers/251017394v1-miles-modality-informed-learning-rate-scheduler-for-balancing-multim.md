---
layout: default
title: MILES: Modality-Informed Learning Rate Scheduler for Balancing Multimodal Learning
---

# MILES: Modality-Informed Learning Rate Scheduler for Balancing Multimodal Learning
**arXiv**：[2510.17394v1](https://arxiv.org/abs/2510.17394) · [PDF](https://arxiv.org/pdf/2510.17394.pdf)  
**作者**：Alejandro Guerra-Manzanares, Farah E. Shamout  

**一句话要点**：提出MILES学习率调度器以平衡多模态学习中的模态过拟合问题

**关键词**：多模态学习, 学习率调度, 模态平衡, 联合融合模型, 条件利用率

## 3 点简述
- 多模态网络训练常因模态过拟合导致性能不佳，依赖单一模态
- MILES利用模态条件利用率差异动态调整学习率，平衡各模态学习速度
- 在四个多模态任务中优于七种基线，提升多模态和单模态预测性能

## 摘要（原文）

> The aim of multimodal neural networks is to combine diverse data sources,
> referred to as modalities, to achieve enhanced performance compared to relying
> on a single modality. However, training of multimodal networks is typically
> hindered by modality overfitting, where the network relies excessively on one
> of the available modalities. This often yields sub-optimal performance,
> hindering the potential of multimodal learning and resulting in marginal
> improvements relative to unimodal models. In this work, we present the
> Modality-Informed Learning ratE Scheduler (MILES) for training multimodal joint
> fusion models in a balanced manner. MILES leverages the differences in
> modality-wise conditional utilization rates during training to effectively
> balance multimodal learning. The learning rate is dynamically adjusted during
> training to balance the speed of learning from each modality by the multimodal
> model, aiming for enhanced performance in both multimodal and unimodal
> predictions. We extensively evaluate MILES on four multimodal joint fusion
> tasks and compare its performance to seven state-of-the-art baselines. Our
> results show that MILES outperforms all baselines across all tasks and fusion
> methods considered in our study, effectively balancing modality usage during
> training. This results in improved multimodal performance and stronger modality
> encoders, which can be leveraged when dealing with unimodal samples or absent
> modalities. Overall, our work highlights the impact of balancing multimodal
> learning on improving model performance.

