---
layout: default
title: ProSona: Prompt-Guided Personalization for Multi-Expert Medical Image Segmentation
---

# ProSona: Prompt-Guided Personalization for Multi-Expert Medical Image Segmentation
**arXiv**：[2511.08046v1](https://arxiv.org/abs/2511.08046) · [PDF](https://arxiv.org/pdf/2511.08046.pdf)  
**作者**：Aya Elgebaly, Nikolaos Delopoulos, Juliane Hörner-Rieber, Carolin Rippke, Sebastian Klüter, Luca Boldrini, Lorenzo Placidi, Riccardo Dal Bello, Nicolaus Andratschke, Michael Baumgartl, Claus Belka, Christopher Kurz, Guillaume Landry, Shadi Albarqouni  

**一句话要点**：提出ProSona框架，通过自然语言提示实现多专家医学图像分割的个性化控制。

**关键词**：医学图像分割, 多专家个性化, 自然语言提示, 潜空间学习, 对比学习目标

## 3 点简述
- 医学图像分割存在高观察者间变异性，如肺结节勾画中专家意见分歧。
- 方法使用概率U-Net学习注释风格潜空间，结合提示引导投影生成个性化分割。
- 在LIDC-IDRI和前列腺MRI数据集上，比DPersona降低广义能量距离17%，提升Dice分数。

## 摘要（原文）

> Automated medical image segmentation suffers from high inter-observer variability, particularly in tasks such as lung nodule delineation, where experts often disagree. Existing approaches either collapse this variability into a consensus mask or rely on separate model branches for each annotator. We introduce ProSona, a two-stage framework that learns a continuous latent space of annotation styles, enabling controllable personalization via natural language prompts. A probabilistic U-Net backbone captures diverse expert hypotheses, while a prompt-guided projection mechanism navigates this latent space to generate personalized segmentations. A multi-level contrastive objective aligns textual and visual representations, promoting disentangled and interpretable expert styles. Across the LIDC-IDRI lung nodule and multi-institutional prostate MRI datasets, ProSona reduces the Generalized Energy Distance by 17% and improves mean Dice by more than one point compared with DPersona. These results demonstrate that natural-language prompts can provide flexible, accurate, and interpretable control over personalized medical image segmentation. Our implementation is available online 1 .

