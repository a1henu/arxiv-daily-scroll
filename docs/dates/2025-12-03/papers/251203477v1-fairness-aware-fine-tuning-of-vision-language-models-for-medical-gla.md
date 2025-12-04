---
layout: default
title: Fairness-Aware Fine-Tuning of Vision-Language Models for Medical Glaucoma Diagnosis
---

# Fairness-Aware Fine-Tuning of Vision-Language Models for Medical Glaucoma Diagnosis
**arXiv**：[2512.03477v1](https://arxiv.org/abs/2512.03477) · [PDF](https://arxiv.org/pdf/2512.03477.pdf)  
**作者**：Zijian Gu, Yuxi Liu, Zhenhao Zhang, Song Wang  

**一句话要点**：提出公平感知低秩适应方法，结合可微最大准确率差距损失，优化医学视觉语言模型在青光眼诊断中的公平性。

**关键词**：医学视觉语言模型, 公平性优化, 低秩适应, 青光眼诊断, 可微损失函数, 参数高效训练

## 3 点简述
- 医学视觉语言模型在青光眼诊断中存在跨人口群体准确率差异问题。
- 引入FR-LoRA、GR-LoRA和Hybrid-LoRA方法，通过MaxAccGap损失和梯度平衡提升公平性。
- 在10,000张眼底图像上，GR-LoRA减少69%准确率差异，整体准确率53.15%，仅需0.24%可训练参数。

## 摘要（原文）

> Vision-language models achieve expert-level performance on medical imaging tasks but exhibit significant diagnostic accuracy disparities across demographic groups. We introduce fairness-aware Low-Rank Adaptation for medical VLMs, combining parameter efficiency with explicit fairness optimization. Our key algorithmic contribution is a differentiable MaxAccGap loss that enables end-to-end optimization of accuracy parity across demographic groups. We propose three methods: FR-LoRA integrates MaxAccGap regularization into the training objective, GR-LoRA applies inverse frequency weighting to balance gradient contributions, and Hybrid-LoRA combines both mechanisms.Evaluated on 10,000 glaucoma fundus images, GR-LoRA reduces diagnostic accuracy disparities by 69% while maintaining 53.15% overall accuracy. Ablation studies reveal that strong regularization strength achieves optimal fairness with minimal accuracy trade-off, and race-specific optimization yields 60% disparity reduction. Our approach requires only 0.24% trainable parameters, enabling practical deployment of fair medical AI in resource-constrained healthcare settings.

