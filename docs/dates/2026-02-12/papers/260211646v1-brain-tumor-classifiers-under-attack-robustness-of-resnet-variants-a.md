---
layout: default
title: Brain Tumor Classifiers Under Attack: Robustness of ResNet Variants Against Transferable FGSM and PGD Attacks
---

# Brain Tumor Classifiers Under Attack: Robustness of ResNet Variants Against Transferable FGSM and PGD Attacks
**arXiv**：[2602.11646v1](https://arxiv.org/abs/2602.11646) · [PDF](https://arxiv.org/pdf/2602.11646.pdf)  
**作者**：Ryan Deem, Garrett Goodman, Waqas Majeed, Md Abdullah Al Hafiz Khan, Michail S. Alexiou  

**一句话要点**：评估ResNet变体在脑肿瘤MRI分类中对FGSM和PGD攻击的鲁棒性

**关键词**：脑肿瘤分类, 对抗攻击, ResNet变体, MRI数据, 鲁棒性评估, 梯度攻击

## 3 点简述
- 核心问题：脑肿瘤分类模型的对抗鲁棒性在临床MRI应用中未充分探索
- 方法要点：基于ResNet、ResNeXt和扩张ResNet构建BrainNet、BrainNeXt和DilationNet模型
- 实验或效果：BrainNeXt对黑盒攻击最鲁棒，但数据缩减和未增强显著降低模型韧性

## 摘要（原文）

> Adversarial robustness in deep learning models for brain tumor classification remains an underexplored yet critical challenge, particularly for clinical deployment scenarios involving MRI data. In this work, we investigate the susceptibility and resilience of several ResNet-based architectures, referred to as BrainNet, BrainNeXt and DilationNet, against gradient-based adversarial attacks, namely FGSM and PGD. These models, based on ResNet, ResNeXt, and dilated ResNet variants respectively, are evaluated across three preprocessing configurations (i) full-sized augmented, (ii) shrunk augmented and (iii) shrunk non-augmented MRI datasets. Our experiments reveal that BrainNeXt models exhibit the highest robustness to black-box attacks, likely due to their increased cardinality, though they produce weaker transferable adversarial samples. In contrast, BrainNet and Dilation models are more vulnerable to attacks from each other, especially under PGD with higher iteration steps and $α$ values. Notably, shrunk and non-augmented data significantly reduce model resilience, even when the untampered test accuracy remains high, highlighting a key trade-off between input resolution and adversarial vulnerability. These results underscore the importance of jointly evaluating classification performance and adversarial robustness for reliable real-world deployment in brain MRI analysis.

