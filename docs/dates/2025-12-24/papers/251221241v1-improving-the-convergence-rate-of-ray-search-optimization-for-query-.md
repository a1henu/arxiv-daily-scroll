---
layout: default
title: Improving the Convergence Rate of Ray Search Optimization for Query-Efficient Hard-Label Attacks
---

# Improving the Convergence Rate of Ray Search Optimization for Query-Efficient Hard-Label Attacks
**arXiv**：[2512.21241v1](https://arxiv.org/abs/2512.21241) · [PDF](https://arxiv.org/pdf/2512.21241.pdf)  
**作者**：Xinjie Xu, Shuyu Cheng, Dongwei Xu, Qi Xuan, Chen Ma  

**一句话要点**：提出基于动量的射线搜索优化算法以提升硬标签黑盒攻击的查询效率

**关键词**：硬标签黑盒攻击, 射线搜索优化, 动量算法, 查询效率, 对抗样本

## 3 点简述
- 针对硬标签黑盒攻击中查询复杂度高的问题，优化射线搜索类方法
- 引入Nesterov加速梯度思想，设计动量算法ARS-OPT，通过预估未来射线方向梯度提升收敛
- 在ImageNet和CIFAR-10上实验，超越13种先进方法，验证查询效率优势

## 摘要（原文）

> In hard-label black-box adversarial attacks, where only the top-1 predicted label is accessible, the prohibitive query complexity poses a major obstacle to practical deployment. In this paper, we focus on optimizing a representative class of attacks that search for the optimal ray direction yielding the minimum $\ell_2$-norm perturbation required to move a benign image into the adversarial region. Inspired by Nesterov's Accelerated Gradient (NAG), we propose a momentum-based algorithm, ARS-OPT, which proactively estimates the gradient with respect to a future ray direction inferred from accumulated momentum. We provide a theoretical analysis of its convergence behavior, showing that ARS-OPT enables more accurate directional updates and achieves faster, more stable optimization. To further accelerate convergence, we incorporate surrogate-model priors into ARS-OPT's gradient estimation, resulting in PARS-OPT with enhanced performance. The superiority of our approach is supported by theoretical guarantees under standard assumptions. Extensive experiments on ImageNet and CIFAR-10 demonstrate that our method surpasses 13 state-of-the-art approaches in query efficiency.

