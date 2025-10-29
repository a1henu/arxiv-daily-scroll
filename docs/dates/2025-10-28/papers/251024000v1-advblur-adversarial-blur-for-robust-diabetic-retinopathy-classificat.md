---
layout: default
title: AdvBlur: Adversarial Blur for Robust Diabetic Retinopathy Classification and Cross-Domain Generalization
---

# AdvBlur: Adversarial Blur for Robust Diabetic Retinopathy Classification and Cross-Domain Generalization
**arXiv**：[2510.24000v1](https://arxiv.org/abs/2510.24000) · [PDF](https://arxiv.org/pdf/2510.24000.pdf)  
**作者**：Heethanjan Kanagalingam, Thenukan Pathmanathan, Mokeeshan Vathanakumar, Tharmakulasingam Mukunthan  

**一句话要点**：提出AdvBlur方法，通过对抗模糊图像增强糖尿病视网膜病变分类的鲁棒性和跨域泛化能力。

**关键词**：糖尿病视网膜病变分类, 对抗模糊, 域泛化, 双损失函数, 鲁棒性增强

## 3 点简述
- 糖尿病视网膜病变分类模型面临分布变化导致的鲁棒性挑战。
- 方法集成对抗模糊图像，采用双损失函数框架提升泛化性能。
- 实验验证在多个数据集上有效，性能与先进域泛化模型相当。

## 摘要（原文）

> Diabetic retinopathy (DR) is a leading cause of vision loss worldwide, yet
> early and accurate detection can significantly improve treatment outcomes.
> While numerous Deep learning (DL) models have been developed to predict DR from
> fundus images, many face challenges in maintaining robustness due to
> distributional variations caused by differences in acquisition devices,
> demographic disparities, and imaging conditions. This paper addresses this
> critical limitation by proposing a novel DR classification approach, a method
> called AdvBlur. Our method integrates adversarial blurred images into the
> dataset and employs a dual-loss function framework to address domain
> generalization. This approach effectively mitigates the impact of unseen
> distributional variations, as evidenced by comprehensive evaluations across
> multiple datasets. Additionally, we conduct extensive experiments to explore
> the effects of factors such as camera type, low-quality images, and dataset
> size. Furthermore, we perform ablation studies on blurred images and the loss
> function to ensure the validity of our choices. The experimental results
> demonstrate the effectiveness of our proposed method, achieving competitive
> performance compared to state-of-the-art domain generalization DR models on
> unseen external datasets.

