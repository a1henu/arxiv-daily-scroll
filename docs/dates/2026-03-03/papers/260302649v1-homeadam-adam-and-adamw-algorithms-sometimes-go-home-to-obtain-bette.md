---
layout: default
title: HomeAdam: Adam and AdamW Algorithms Sometimes Go Home to Obtain Better Provable Generalization
---

# HomeAdam: Adam and AdamW Algorithms Sometimes Go Home to Obtain Better Provable Generalization
**arXiv**：[2603.02649v1](https://arxiv.org/abs/2603.02649) · [PDF](https://arxiv.org/pdf/2603.02649.pdf)  
**作者**：Feihu Huang, Guanyi Zhang, Songcan Chen  

**一句话要点**：提出HomeAdam算法，通过有时返回基于动量的SGD以改进Adam和AdamW的泛化性能。

**关键词**：自适应优化算法, 泛化误差分析, 算法稳定性, 深度学习优化, Adam变体

## 3 点简述
- 核心问题：Adam和AdamW收敛快但泛化差，理论泛化误差大于SGD。
- 方法要点：基于算法稳定性分析，证明Adam(W)-srf泛化误差，并提出HomeAdam(W)算法。
- 实验或效果：理论证明HomeAdam(W)泛化误差更小，收敛更快，数值实验验证效率。

## 摘要（原文）

> Adam and AdamW are a class of default optimizers for training deep learning models in machine learning. These adaptive algorithms converge faster but generalize worse compared to SGD. In fact, their proved generalization error $O(\frac{1}{\sqrt{N}})$ also is larger than $O(\frac{1}{N})$ of SGD, where $N$ denotes training sample size. Recently, although some variants of Adam have been proposed to improve its generalization, their improved generalizations are still unexplored in theory. To fill this gap, in the paper, we restudy generalization of Adam and AdamW via algorithmic stability, and first prove that Adam and AdamW without square-root (i.e., Adam(W)-srf) have a generalization error $O(\frac{\hatρ^{-2T}}{N})$, where $T$ denotes iteration number and $\hatρ>0$ denotes the smallest element of second-order momentum plus a small positive number. To improve generalization, we propose a class of efficient clever Adam (i.e., HomeAdam(W)) algorithms via sometimes returning momentum-based SGD. Moreover, we prove that our HomeAdam(W) have a smaller generalization error $O(\frac{1}{N})$ than $O(\frac{\hatρ^{-2T}}{N})$ of Adam(W)-srf, since $\hatρ$ is generally very small. In particular, it is also smaller than the existing $O(\frac{1}{\sqrt{N}})$ of Adam(W). Meanwhile, we prove our HomeAdam(W) have a faster convergence rate of $O(\frac{1}{T^{1/4}})$ than $O(\frac{\breveρ^{-1}}{T^{1/4}})$ of the Adam(W)-srf, where $\breveρ\leq\hatρ$ also is very small. Extensive numerical experiments demonstrate efficiency of our HomeAdam(W) algorithms.

