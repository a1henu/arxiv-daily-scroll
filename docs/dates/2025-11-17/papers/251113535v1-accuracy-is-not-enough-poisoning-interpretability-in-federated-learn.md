---
layout: default
title: Accuracy is Not Enough: Poisoning Interpretability in Federated Learning via Color Skew
---

# Accuracy is Not Enough: Poisoning Interpretability in Federated Learning via Color Skew
**arXiv**：[2511.13535v1](https://arxiv.org/abs/2511.13535) · [PDF](https://arxiv.org/pdf/2511.13535.pdf)  
**作者**：Farhin Farhad Riya, Shahinul Hoque, Jinyuan Stella Sun, Olivera Kotevska  

**一句话要点**：提出联邦学习中通过颜色扰动毒化模型可解释性的攻击方法

**关键词**：联邦学习, 模型可解释性, 对抗攻击, 显著性图, 颜色扰动

## 3 点简述
- 核心问题：模型预测准确但可解释性被破坏，挑战了准确预测即忠实解释的假设。
- 方法要点：使用色度扰动模块，通过改变前景背景颜色对比来操纵显著性图。
- 实验或效果：攻击使Grad-CAM峰值激活重叠降低达35%，同时保持分类准确率高于96%。

## 摘要（原文）

> As machine learning models are increasingly deployed in safety-critical domains, visual explanation techniques have become essential tools for supporting transparency. In this work, we reveal a new class of attacks that compromise model interpretability without affecting accuracy. Specifically, we show that small color perturbations applied by adversarial clients in a federated learning setting can shift a model's saliency maps away from semantically meaningful regions while keeping the prediction unchanged. The proposed saliency-aware attack framework, called Chromatic Perturbation Module, systematically crafts adversarial examples by altering the color contrast between foreground and background in a way that disrupts explanation fidelity. These perturbations accumulate across training rounds, poisoning the global model's internal feature attributions in a stealthy and persistent manner. Our findings challenge a common assumption in model auditing that correct predictions imply faithful explanations and demonstrate that interpretability itself can be an attack surface. We evaluate this vulnerability across multiple datasets and show that standard training pipelines are insufficient to detect or mitigate explanation degradation, especially in the federated learning setting, where subtle color perturbations are harder to discern. Our attack reduces peak activation overlap in Grad-CAM explanations by up to 35% while preserving classification accuracy above 96% on all evaluated datasets.

