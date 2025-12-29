---
layout: default
title: Scaling Adversarial Training via Data Selection
---

# Scaling Adversarial Training via Data Selection
**arXiv**：[2512.22069v1](https://arxiv.org/abs/2512.22069) · [PDF](https://arxiv.org/pdf/2512.22069.pdf)  
**作者**：Youran Ye, Dejin Wang, Ajinkya Bhandare  

**一句话要点**：提出选择性对抗训练，通过关键样本子集扰动，在减少计算成本的同时保持对抗鲁棒性。

**关键词**：对抗训练, 样本选择, 计算效率, PGD攻击, 鲁棒性优化

## 3 点简述
- 核心问题：PGD对抗训练计算成本高，所有样本均等处理导致效率低下。
- 方法要点：引入基于边界和梯度匹配的样本选择准则，仅扰动关键样本子集。
- 实验或效果：在MNIST和CIFAR-10上实现与全PGD相当的鲁棒性，计算成本降低达50%。

## 摘要（原文）

> Projected Gradient Descent (PGD) is a strong and widely used first-order adversarial attack, yet its computational cost scales poorly, as all training samples undergo identical iterative inner-loop optimization despite contributing unequally to robustness. Motivated by this inefficiency, we propose \emph{Selective Adversarial Training}, which perturbs only a subset of critical samples in each minibatch. Specifically, we introduce two principled selection criteria: (1) margin-based sampling, which prioritizes samples near the decision boundary, and (2) gradient-matching sampling, which selects samples whose gradients align with the dominant batch optimization direction. Adversarial examples are generated only for the selected subset, while the remaining samples are trained cleanly using a mixed objective. Experiments on MNIST and CIFAR-10 show that the proposed methods achieve robustness comparable to, or even exceeding, full PGD adversarial training, while reducing adversarial computation by up to $50\%$, demonstrating that informed sample selection is sufficient for scalable adversarial robustness.

