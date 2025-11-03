---
layout: default
title: Rethinking Robust Adversarial Concept Erasure in Diffusion Models
---

# Rethinking Robust Adversarial Concept Erasure in Diffusion Models
**arXiv**：[2510.27285v1](https://arxiv.org/abs/2510.27285) · [PDF](https://arxiv.org/pdf/2510.27285.pdf)  
**作者**：Qinghong Yin, Yu Tian, Yue Zhang  

**一句话要点**：提出S-GRACE方法以解决扩散模型中概念擦除的鲁棒性问题

**关键词**：扩散模型, 概念擦除, 对抗训练, 语义指导, 鲁棒性优化

## 3 点简述
- 现有方法在对抗训练中忽视概念语义，导致概念空间覆盖不足或干扰其他概念
- S-GRACE利用语义指导生成对抗样本，提升概念擦除的准确性和鲁棒性
- 实验显示S-GRACE擦除性能提升26%，非目标概念保留更好，训练时间减少90%

## 摘要（原文）

> Concept erasure aims to selectively unlearning undesirable content in
> diffusion models (DMs) to reduce the risk of sensitive content generation. As a
> novel paradigm in concept erasure, most existing methods employ adversarial
> training to identify and suppress target concepts, thus reducing the likelihood
> of sensitive outputs. However, these methods often neglect the specificity of
> adversarial training in DMs, resulting in only partial mitigation. In this
> work, we investigate and quantify this specificity from the perspective of
> concept space, i.e., can adversarial samples truly fit the target concept
> space? We observe that existing methods neglect the role of conceptual
> semantics when generating adversarial samples, resulting in ineffective fitting
> of concept spaces. This oversight leads to the following issues: 1) when there
> are few adversarial samples, they fail to comprehensively cover the object
> concept; 2) conversely, they will disrupt other target concept spaces.
> Motivated by the analysis of these findings, we introduce S-GRACE
> (Semantics-Guided Robust Adversarial Concept Erasure), which grace leveraging
> semantic guidance within the concept space to generate adversarial samples and
> perform erasure training. Experiments conducted with seven state-of-the-art
> methods and three adversarial prompt generation strategies across various DM
> unlearning scenarios demonstrate that S-GRACE significantly improves erasure
> performance 26%, better preserves non-target concepts, and reduces training
> time by 90%. Our code is available at https://github.com/Qhong-522/S-GRACE.

