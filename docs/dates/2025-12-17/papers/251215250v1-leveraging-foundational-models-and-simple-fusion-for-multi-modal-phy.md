---
layout: default
title: Leveraging Foundational Models and Simple Fusion for Multi-modal Physiological Signal Analysis
---

# Leveraging Foundational Models and Simple Fusion for Multi-modal Physiological Signal Analysis
**arXiv**：[2512.15250v1](https://arxiv.org/abs/2512.15250) · [PDF](https://arxiv.org/pdf/2512.15250.pdf)  
**作者**：Youssef Ghallab, Omar Iraqy, Mohamed Kandil, Mohamed Ashraf, Saadeldine Eletter, Morougue Ghazal, Ayman Khalafallah, Nagwa El-Makky  

**一句话要点**：提出基于基础模型和简单融合的多模态生理信号分析方法，以解决标签数据有限和模态差异问题。

**关键词**：多模态生理信号分析, 基础模型, 自监督预训练, 双掩码策略, 简单融合, 情感识别

## 3 点简述
- 核心问题：多模态生理信号（如ECG和EEG）集成面临标签数据有限和模态特异性差异的挑战。
- 方法要点：采用CBraMod编码器进行自监督预训练，引入双掩码策略捕获信号内和信号间依赖，并通过简单拼接融合多模态表示。
- 实验或效果：在情感识别任务中实现接近最先进的性能，验证了基础模型方法在医疗和情感计算中的潜力。

## 摘要（原文）

> Physiological signals such as electrocardiograms (ECG) and electroencephalograms (EEG) provide complementary insights into human health and cognition, yet multi-modal integration is challenging due to limited multi-modal labeled data, and modality-specific differences . In this work, we adapt the CBraMod encoder for large-scale self-supervised ECG pretraining, introducing a dual-masking strategy to capture intra- and inter-lead dependencies. To overcome the above challenges, we utilize a pre-trained CBraMod encoder for EEG and pre-train a symmetric ECG encoder, equipping each modality with a rich foundational representation. These representations are then fused via simple embedding concatenation, allowing the classification head to learn cross-modal interactions, together enabling effective downstream learning despite limited multi-modal supervision. Evaluated on emotion recognition, our approach achieves near state-of-the-art performance, demonstrating that carefully designed physiological encoders, even with straightforward fusion, substantially improve downstream performance. These results highlight the potential of foundation-model approaches to harness the holistic nature of physiological signals, enabling scalable, label-efficient, and generalizable solutions for healthcare and affective computing.

