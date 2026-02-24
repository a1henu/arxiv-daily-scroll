---
layout: default
title: DerMAE: Improving skin lesion classification through conditioned latent diffusion and MAE distillation
---

# DerMAE: Improving skin lesion classification through conditioned latent diffusion and MAE distillation
**arXiv**：[2602.19848v1](https://arxiv.org/abs/2602.19848) · [PDF](https://arxiv.org/pdf/2602.19848.pdf)  
**作者**：Francisco Filho, Kelvin Cunha, Fábio Papais, Emanoel dos Santos, Rodrigo Mota, Thales Bezerra, Erico Medeiros, Paulo Borba, Tsang Ing Ren  

**一句话要点**：提出DerMAE方法，通过条件扩散生成与MAE蒸馏改进皮肤病变分类，适用于临床部署。

**关键词**：皮肤病变分类, 条件扩散模型, MAE预训练, 知识蒸馏, 轻量模型部署, 类别不平衡

## 3 点简述
- 皮肤病变数据集存在类别不平衡，恶性样本少导致深度学习训练偏差。
- 使用类条件扩散模型生成合成图像，结合MAE自监督预训练增强ViT特征学习。
- 通过知识蒸馏将大模型表示迁移到轻量ViT，提升分类性能并支持移动设备推理。

## 摘要（原文）

> Skin lesion classification datasets often suffer from severe class imbalance, with malignant cases significantly underrepresented, leading to biased decision boundaries during deep learning training. We address this challenge using class-conditioned diffusion models to generate synthetic dermatological images, followed by self-supervised MAE pretraining to enable huge ViT models to learn robust, domain-relevant features. To support deployment in practical clinical settings, where lightweight models are required, we apply knowledge distillation to transfer these representations to a smaller ViT student suitable for mobile devices. Our results show that MAE pretraining on synthetic data, combined with distillation, improves classification performance while enabling efficient on-device inference for practical clinical use.

