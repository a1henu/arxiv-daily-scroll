---
layout: default
title: Anatomical Region-Guided Contrastive Decoding: A Plug-and-Play Strategy for Mitigating Hallucinations in Medical VLMs
---

# Anatomical Region-Guided Contrastive Decoding: A Plug-and-Play Strategy for Mitigating Hallucinations in Medical VLMs
**arXiv**：[2512.17189v1](https://arxiv.org/abs/2512.17189) · [PDF](https://arxiv.org/pdf/2512.17189.pdf)  
**作者**：Xiao Liang, Chenxi Liu, Zhi Ma, Di Wang, Bin Jing, Quan Wang, Yuanyuan Shi  

**一句话要点**：提出解剖区域引导对比解码策略，以缓解医学视觉语言模型中的幻觉问题。

**关键词**：医学视觉语言模型, 幻觉缓解, 对比解码, 解剖区域引导, 训练免费策略

## 3 点简述
- 核心问题：医学视觉语言模型存在幻觉，依赖文本先验而非视觉证据，影响可靠性。
- 方法要点：引入解剖区域引导对比解码，通过解剖掩码动态重加权，实现区域特异性指导。
- 实验或效果：在多种医学影像数据集上验证，提升区域理解、减少幻觉并增强诊断准确性。

## 摘要（原文）

> Medical Vision-Language Models (MedVLMs) show immense promise in clinical applicability. However, their reliability is hindered by hallucinations, where models often fail to derive answers from visual evidence, instead relying on learned textual priors. Existing mitigation strategies for MedVLMs have distinct limitations: training-based methods rely on costly expert annotations, limiting scalability, while training-free interventions like contrastive decoding, though data-efficient, apply a global, untargeted correction whose effects in complex real-world clinical settings can be unreliable. To address these challenges, we introduce Anatomical Region-Guided Contrastive Decoding (ARCD), a plug-and-play strategy that mitigates hallucinations by providing targeted, region-specific guidance. Our module leverages an anatomical mask to direct a three-tiered contrastive decoding process. By dynamically re-weighting at the token, attention, and logits levels, it verifiably steers the model's focus onto specified regions, reinforcing anatomical understanding and suppressing factually incorrect outputs. Extensive experiments across diverse datasets, including chest X-ray, CT, brain MRI, and ocular ultrasound, demonstrate our method's effectiveness in improving regional understanding, reducing hallucinations, and enhancing overall diagnostic accuracy.

