---
layout: default
title: ANCHOR: Integrating Adversarial Training with Hard-mined Supervised Contrastive Learning for Robust Representation Learning
---

# ANCHOR: Integrating Adversarial Training with Hard-mined Supervised Contrastive Learning for Robust Representation Learning
**arXiv**：[2510.27599v1](https://arxiv.org/abs/2510.27599) · [PDF](https://arxiv.org/pdf/2510.27599.pdf)  
**作者**：Samarup Bhattacharya, Anubhab Bhattacharya, Abir Chakraborty  

**一句话要点**：提出ANCHOR框架，结合对抗训练与硬挖掘监督对比学习以提升图像表示鲁棒性

**关键词**：对抗训练, 监督对比学习, 硬挖掘, 表示学习, 鲁棒性, 图像分类

## 3 点简述
- 核心问题：神经网络易受对抗攻击，微小扰动导致模型错误预测。
- 方法要点：集成对抗训练与硬挖掘监督对比学习，使图像及其扰动版本在嵌入空间聚类。
- 实验或效果：在CIFAR-10上，PGD-20攻击下清洁与鲁棒准确率优于标准对抗训练方法。

## 摘要（原文）

> Neural networks have changed the way machines interpret the world. At their
> core, they learn by following gradients, adjusting their parameters step by
> step until they identify the most discriminant patterns in the data. This
> process gives them their strength, yet it also opens the door to a hidden flaw.
> The very gradients that help a model learn can also be used to produce small,
> imperceptible tweaks that cause the model to completely alter its decision.
> Such tweaks are called adversarial attacks. These attacks exploit this
> vulnerability by adding tiny, imperceptible changes to images that, while
> leaving them identical to the human eye, cause the model to make wrong
> predictions. In this work, we propose Adversarially-trained Contrastive
> Hard-mining for Optimized Robustness (ANCHOR), a framework that leverages the
> power of supervised contrastive learning with explicit hard positive mining to
> enable the model to learn representations for images such that the embeddings
> for the images, their augmentations, and their perturbed versions cluster
> together in the embedding space along with those for other images of the same
> class while being separated from images of other classes. This alignment helps
> the model focus on stable, meaningful patterns rather than fragile gradient
> cues. On CIFAR-10, our approach achieves impressive results for both clean and
> robust accuracy under PGD-20 (epsilon = 0.031), outperforming standard
> adversarial training methods. Our results indicate that combining adversarial
> guidance with hard-mined contrastive supervision helps models learn more
> structured and robust representations, narrowing the gap between accuracy and
> robustness.

