---
layout: default
title: Adversarial Evasion Attacks on Computer Vision using SHAP Values
---

# Adversarial Evasion Attacks on Computer Vision using SHAP Values
**arXiv**：[2601.10587v1](https://arxiv.org/abs/2601.10587) · [PDF](https://arxiv.org/pdf/2601.10587.pdf)  
**作者**：Frank Mollard, Marcus Becker, Florian Roehrbein  

**一句话要点**：提出基于SHAP值的白盒对抗攻击方法，以降低计算机视觉模型的输出置信度或诱导误分类。

**关键词**：对抗攻击, SHAP值, 计算机视觉, 白盒攻击, 模型鲁棒性

## 3 点简述
- 核心问题：对抗攻击可降低深度学习模型性能，且因人类视觉难以察觉而具有隐蔽性。
- 方法要点：利用SHAP值量化推理阶段输入对输出的重要性，生成对抗样本。
- 实验或效果：与FGSM方法比较，SHAP攻击在梯度隐藏场景下生成误分类更稳健。

## 摘要（原文）

> The paper introduces a white-box attack on computer vision models using SHAP values. It demonstrates how adversarial evasion attacks can compromise the performance of deep learning models by reducing output confidence or inducing misclassifications. Such attacks are particularly insidious as they can deceive the perception of an algorithm while eluding human perception due to their imperceptibility to the human eye. The proposed attack leverages SHAP values to quantify the significance of individual inputs to the output at the inference stage. A comparison is drawn between the SHAP attack and the well-known Fast Gradient Sign Method. We find evidence that SHAP attacks are more robust in generating misclassifications particularly in gradient hiding scenarios.

