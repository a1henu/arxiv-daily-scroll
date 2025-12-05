---
layout: default
title: Rethinking Decoupled Knowledge Distillation: A Predictive Distribution Perspective
---

# Rethinking Decoupled Knowledge Distillation: A Predictive Distribution Perspective
**arXiv**：[2512.04625v1](https://arxiv.org/abs/2512.04625) · [PDF](https://arxiv.org/pdf/2512.04625.pdf)  
**作者**：Bowen Zheng, Ran Cheng  

**一句话要点**：提出广义解耦知识蒸馏以优化预测分布视角下的知识蒸馏性能

**关键词**：知识蒸馏, 预测分布, 解耦策略, 梯度分析, 模型优化, 计算机视觉

## 3 点简述
- 从预测分布视角重新审视解耦知识蒸馏，揭示教师模型预测分布对梯度的影响
- 引入广义解耦知识蒸馏损失，提供更通用的logit解耦方法，并设计高效分区策略
- 在多个基准数据集上验证，GDKD优于原始DKD及其他主流知识蒸馏方法

## 摘要（原文）

> In the history of knowledge distillation, the focus has once shifted over time from logit-based to feature-based approaches. However, this transition has been revisited with the advent of Decoupled Knowledge Distillation (DKD), which re-emphasizes the importance of logit knowledge through advanced decoupling and weighting strategies. While DKD marks a significant advancement, its underlying mechanisms merit deeper exploration. As a response, we rethink DKD from a predictive distribution perspective. First, we introduce an enhanced version, the Generalized Decoupled Knowledge Distillation (GDKD) loss, which offers a more versatile method for decoupling logits. Then we pay particular attention to the teacher model's predictive distribution and its impact on the gradients of GDKD loss, uncovering two critical insights often overlooked: (1) the partitioning by the top logit considerably improves the interrelationship of non-top logits, and (2) amplifying the focus on the distillation loss of non-top logits enhances the knowledge extraction among them. Utilizing these insights, we further propose a streamlined GDKD algorithm with an efficient partition strategy to handle the multimodality of teacher models' predictive distribution. Our comprehensive experiments conducted on a variety of benchmarks, including CIFAR-100, ImageNet, Tiny-ImageNet, CUB-200-2011, and Cityscapes, demonstrate GDKD's superior performance over both the original DKD and other leading knowledge distillation methods. The code is available at https://github.com/ZaberKo/GDKD.

