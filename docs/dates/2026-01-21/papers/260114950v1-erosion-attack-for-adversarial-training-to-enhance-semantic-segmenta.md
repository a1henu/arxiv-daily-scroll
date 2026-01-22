---
layout: default
title: Erosion Attack for Adversarial Training to Enhance Semantic Segmentation Robustness
---

# Erosion Attack for Adversarial Training to Enhance Semantic Segmentation Robustness
**arXiv**：[2601.14950v1](https://arxiv.org/abs/2601.14950) · [PDF](https://arxiv.org/pdf/2601.14950.pdf)  
**作者**：Yufei Song, Ziqi Zhou, Menghao Deng, Yifan Hu, Shengshan Hu, Minghui Li, Leo Yu Zhang  

**一句话要点**：提出EroSeg-AT框架，利用EroSeg生成对抗样本来增强语义分割模型的鲁棒性。

**关键词**：语义分割, 对抗训练, 对抗攻击, 鲁棒性增强, 像素级扰动

## 3 点简述
- 现有分割模型易受对抗攻击，现有攻击方法忽略上下文语义关系，限制对抗训练效果。
- EroSeg-AT基于像素级置信度选择敏感像素，逐步传播扰动以破坏样本语义一致性。
- 实验表明，该方法显著提升攻击效果，并在对抗训练下增强模型鲁棒性。

## 摘要（原文）

> Existing segmentation models exhibit significant vulnerability to adversarial attacks.To improve robustness, adversarial training incorporates adversarial examples into model training. However, existing attack methods consider only global semantic information and ignore contextual semantic relationships within the samples, limiting the effectiveness of adversarial training. To address this issue, we propose EroSeg-AT, a vulnerability-aware adversarial training framework that leverages EroSeg to generate adversarial examples. EroSeg first selects sensitive pixels based on pixel-level confidence and then progressively propagates perturbations to higher-confidence pixels, effectively disrupting the semantic consistency of the samples. Experimental results show that, compared to existing methods, our approach significantly improves attack effectiveness and enhances model robustness under adversarial training.

