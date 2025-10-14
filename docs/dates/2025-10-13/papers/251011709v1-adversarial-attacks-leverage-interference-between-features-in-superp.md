---
layout: default
title: Adversarial Attacks Leverage Interference Between Features in Superposition
---

# Adversarial Attacks Leverage Interference Between Features in Superposition
**arXiv**：[2510.11709v1](https://arxiv.org/abs/2510.11709) · [PDF](https://arxiv.org/pdf/2510.11709.pdf)  
**作者**：Edward Stevinson, Lucas Prieto, Melih Barsbey, Tolga Birdal  

**一句话要点**：提出利用特征叠加干扰解释对抗性攻击，揭示网络压缩导致漏洞

**关键词**：对抗性攻击, 特征叠加, 神经网络压缩, 攻击可转移性, ViT模型

## 3 点简述
- 核心问题：对抗性漏洞源于神经网络高效信息编码中的特征叠加干扰
- 方法要点：通过特征叠加机制预测攻击模式，解释模型间攻击可转移性
- 实验或效果：在合成和ViT-CIFAR-10实验中验证叠加足以引发对抗性漏洞

## 摘要（原文）

> Fundamental questions remain about when and why adversarial examples arise in
> neural networks, with competing views characterising them either as artifacts
> of the irregularities in the decision landscape or as products of sensitivity
> to non-robust input features. In this paper, we instead argue that adversarial
> vulnerability can stem from efficient information encoding in neural networks.
> Specifically, we show how superposition - where networks represent more
> features than they have dimensions - creates arrangements of latent
> representations that adversaries can exploit. We demonstrate that adversarial
> perturbations leverage interference between superposed features, making attack
> patterns predictable from feature arrangements. Our framework provides a
> mechanistic explanation for two known phenomena: adversarial attack
> transferability between models with similar training regimes and class-specific
> vulnerability patterns. In synthetic settings with precisely controlled
> superposition, we establish that superposition suffices to create adversarial
> vulnerability. We then demonstrate that these findings persist in a ViT trained
> on CIFAR-10. These findings reveal adversarial vulnerability can be a byproduct
> of networks' representational compression, rather than flaws in the learning
> process or non-robust inputs.

