---
layout: default
title: On Improving Deep Active Learning with Formal Verification
---

# On Improving Deep Active Learning with Formal Verification
**arXiv**：[2512.14170v1](https://arxiv.org/abs/2512.14170) · [PDF](https://arxiv.org/pdf/2512.14170.pdf)  
**作者**：Jonathan Spiegelman, Guy Amir, Guy Katz  

**一句话要点**：提出利用形式验证生成对抗样本来增强深度主动学习性能

**关键词**：深度主动学习, 形式验证, 对抗样本, 数据增强, 模型泛化

## 3 点简述
- 核心问题：深度主动学习需降低标注成本，但现有数据增强方法效率有限
- 方法要点：通过形式验证生成违反鲁棒性约束的对抗样本，优于基于梯度的攻击
- 实验或效果：应用于多种现代深度主动学习技术，显著提升模型泛化能力

## 摘要（原文）

> Deep Active Learning (DAL) aims to reduce labeling costs in neural-network training by prioritizing the most informative unlabeled samples for annotation. Beyond selecting which samples to label, several DAL approaches further enhance data efficiency by augmenting the training set with synthetic inputs that do not require additional manual labeling. In this work, we investigate how augmenting the training data with adversarial inputs that violate robustness constraints can improve DAL performance. We show that adversarial examples generated via formal verification contribute substantially more than those produced by standard, gradient-based attacks. We apply this extension to multiple modern DAL techniques, as well as to a new technique that we propose, and show that it yields significant improvements in model generalization across standard benchmarks.

