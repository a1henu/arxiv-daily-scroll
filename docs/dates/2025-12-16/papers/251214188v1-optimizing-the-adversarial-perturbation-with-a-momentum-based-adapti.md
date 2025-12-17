---
layout: default
title: Optimizing the Adversarial Perturbation with a Momentum-based Adaptive Matrix
---

# Optimizing the Adversarial Perturbation with a Momentum-based Adaptive Matrix
**arXiv**：[2512.14188v1](https://arxiv.org/abs/2512.14188) · [PDF](https://arxiv.org/pdf/2512.14188.pdf)  
**作者**：Wei Tao, Sheng Long, Xin Liu, Wei Li, Qing Tao  

**一句话要点**：提出基于动量的自适应矩阵攻击AdaMI，以优化对抗扰动并提升稳定性和可迁移性。

**关键词**：对抗攻击, 动量优化, 自适应矩阵, 对抗可迁移性, 稳定性优化

## 3 点简述
- 核心问题：现有攻击使用符号函数缩放扰动，存在优化理论问题，如非收敛性。
- 方法要点：将PGD重新表述为投影梯度法，引入基于动量的自适应矩阵来优化扰动。
- 实验或效果：AdaMI在凸问题上达到最优收敛，提升对抗可迁移性，保持稳定性和不可感知性。

## 摘要（原文）

> Generating adversarial examples (AEs) can be formulated as an optimization problem. Among various optimization-based attacks, the gradient-based PGD and the momentum-based MI-FGSM have garnered considerable interest. However, all these attacks use the sign function to scale their perturbations, which raises several theoretical concerns from the point of view of optimization. In this paper, we first reveal that PGD is actually a specific reformulation of the projected gradient method using only the current gradient to determine its step-size. Further, we show that when we utilize a conventional adaptive matrix with the accumulated gradients to scale the perturbation, PGD becomes AdaGrad. Motivated by this analysis, we present a novel momentum-based attack AdaMI, in which the perturbation is optimized with an interesting momentum-based adaptive matrix. AdaMI is proved to attain optimal convergence for convex problems, indicating that it addresses the non-convergence issue of MI-FGSM, thereby ensuring stability of the optimization process. The experiments demonstrate that the proposed momentum-based adaptive matrix can serve as a general and effective technique to boost adversarial transferability over the state-of-the-art methods across different networks while maintaining better stability and imperceptibility.

