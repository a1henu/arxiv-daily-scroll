---
layout: default
title: S2AP: Score-space Sharpness Minimization for Adversarial Pruning
---

# S2AP: Score-space Sharpness Minimization for Adversarial Pruning
**arXiv**：[2510.18381v1](https://arxiv.org/abs/2510.18381) · [PDF](https://arxiv.org/pdf/2510.18381.pdf)  
**作者**：Giorgio Piras, Qi Zhao, Fabio Brau, Maura Pintor, Christian Wressnegger, Battista Biggio  

**一句话要点**：提出S2AP方法，通过分数空间锐度最小化稳定对抗剪枝中的掩码选择。

**关键词**：对抗剪枝, 分数空间优化, 锐度最小化, 掩码选择, 鲁棒性提升

## 3 点简述
- 核心问题：分数空间优化导致鲁棒损失景观的尖锐局部极小，掩码选择不稳定。
- 方法要点：在掩码搜索中扰动重要性分数并最小化鲁棒损失，以最小化分数空间锐度。
- 实验或效果：多数据集、模型和稀疏度实验显示S2AP稳定掩码选择并提升鲁棒性。

## 摘要（原文）

> Adversarial pruning methods have emerged as a powerful tool for compressing
> neural networks while preserving robustness against adversarial attacks. These
> methods typically follow a three-step pipeline: (i) pretrain a robust model,
> (ii) select a binary mask for weight pruning, and (iii) finetune the pruned
> model. To select the binary mask, these methods minimize a robust loss by
> assigning an importance score to each weight, and then keep the weights with
> the highest scores. However, this score-space optimization can lead to sharp
> local minima in the robust loss landscape and, in turn, to an unstable mask
> selection, reducing the robustness of adversarial pruning methods. To overcome
> this issue, we propose a novel plug-in method for adversarial pruning, termed
> Score-space Sharpness-aware Adversarial Pruning (S2AP). Through our method, we
> introduce the concept of score-space sharpness minimization, which operates
> during the mask search by perturbing importance scores and minimizing the
> corresponding robust loss. Extensive experiments across various datasets,
> models, and sparsity levels demonstrate that S2AP effectively minimizes
> sharpness in score space, stabilizing the mask selection, and ultimately
> improving the robustness of adversarial pruning methods.

