---
layout: default
title: Defense That Attacks: How Robust Models Become Better Attackers
---

# Defense That Attacks: How Robust Models Become Better Attackers
**arXiv**：[2512.02830v1](https://arxiv.org/abs/2512.02830) · [PDF](https://arxiv.org/pdf/2512.02830.pdf)  
**作者**：Mohamed Awad, Mahmoud Akrm, Walid Gomaa  

**一句话要点**：揭示对抗训练意外增强对抗样本可迁移性，提出新风险评估框架

**关键词**：对抗训练, 对抗样本可迁移性, 模型鲁棒性评估, 计算机视觉安全, 深度学习漏洞

## 3 点简述
- 核心问题：对抗训练对对抗样本可迁移性的影响未知，可能引入新风险
- 方法要点：训练36个多样化模型，包括CNN和ViT，进行综合可迁移性实验
- 实验或效果：发现对抗训练模型产生的扰动更易迁移，形成悖论，并发布代码促进研究

## 摘要（原文）

> Deep learning has achieved great success in computer vision, but remains vulnerable to adversarial attacks. Adversarial training is the leading defense designed to improve model robustness. However, its effect on the transferability of attacks is underexplored. In this work, we ask whether adversarial training unintentionally increases the transferability of adversarial examples. To answer this, we trained a diverse zoo of 36 models, including CNNs and ViTs, and conducted comprehensive transferability experiments. Our results reveal a clear paradox: adversarially trained (AT) models produce perturbations that transfer more effectively than those from standard models, which introduce a new ecosystem risk. To enable reproducibility and further study, we release all models, code, and experimental scripts. Furthermore, we argue that robustness evaluations should assess not only the resistance of a model to transferred attacks but also its propensity to produce transferable adversarial examples.

