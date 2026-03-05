---
layout: default
title: Machine Pareidolia: Protecting Facial Image with Emotional Editing
---

# Machine Pareidolia: Protecting Facial Image with Emotional Editing
**arXiv**：[2603.03665v1](https://arxiv.org/abs/2603.03665) · [PDF](https://arxiv.org/pdf/2603.03665.pdf)  
**作者**：Binh M. Le, Simon S. Woo  

**一句话要点**：提出MAP方法，通过情感编辑保护人脸图像隐私，以应对黑盒场景下的面部识别威胁。

**关键词**：人脸隐私保护, 情感编辑, 分数网络, 黑盒攻击, 梯度投影, 图像质量优化

## 3 点简述
- 核心问题：传统人脸隐私保护方法在黑盒设置下迁移性低，且对男性、深肤色等群体适用性有限。
- 方法要点：利用情感修改伪装身份，通过分数网络微调学习目标身份和表情，结合梯度投影优化。
- 实验或效果：在质量和定量指标上超越基线方法，有效对抗在线FR API，并在罕见摄影场景中展现适应性。

## 摘要（原文）

> The proliferation of facial recognition (FR) systems has raised privacy concerns in the digital realm, as malicious uses of FR models pose a significant threat. Traditional countermeasures, such as makeup style transfer, have suffered from low transferability in black-box settings and limited applicability across various demographic groups, including males and individuals with darker skin tones. To address these challenges, we introduce a novel facial privacy protection method, dubbed \textbf{MAP}, a pioneering approach that employs human emotion modifications to disguise original identities as target identities in facial images. Our method uniquely fine-tunes a score network to learn dual objectives, target identity and human expression, which are jointly optimized through gradient projection to ensure convergence at a shared local optimum. Additionally, we enhance the perceptual quality of protected images by applying local smoothness regularization and optimizing the score matching loss within our network. Empirical experiments demonstrate that our innovative approach surpasses previous baselines, including noise-based, makeup-based, and freeform attribute methods, in both qualitative fidelity and quantitative metrics. Furthermore, MAP proves its effectiveness against an online FR API and shows advanced adaptability in uncommon photographic scenarios.

