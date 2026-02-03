---
layout: default
title: Deep Multivariate Models with Parametric Conditionals
---

# Deep Multivariate Models with Parametric Conditionals
**arXiv**：[2602.01953v1](https://arxiv.org/abs/2602.01953) · [PDF](https://arxiv.org/pdf/2602.01953.pdf)  
**作者**：Dmitrij Schlesinger, Boris Flach, Alexander Shekhovtsov  

**一句话要点**：提出基于参数化条件分布的深度多元模型，以增强计算机视觉中异构变量集合的通用性。

**关键词**：深度多元模型, 参数化条件分布, 马尔可夫链核, 异构变量, 半监督学习, 计算机视觉

## 3 点简述
- 核心问题：现有深度多元模型针对特定任务设计，限制了在其他下游任务中的适用性。
- 方法要点：通过条件概率分布表示联合分布，支持任意下游任务，并采用参数化马尔可夫链核进行学习。
- 实验或效果：未知具体实验细节，但该方法允许广泛的半监督学习场景。

## 摘要（原文）

> We consider deep multivariate models for heterogeneous collections of random variables. In the context of computer vision, such collections may e.g. consist of images, segmentations, image attributes, and latent variables. When developing such models, most existing works start from an application task and design the model components and their dependencies to meet the needs of the chosen task. This has the disadvantage of limiting the applicability of the resulting model for other downstream tasks. Here, instead, we propose to represent the joint probability distribution by means of conditional probability distributions for each group of variables conditioned on the rest. Such models can then be used for practically any possible downstream task. Their learning can be approached as training a parametrised Markov chain kernel by maximising the data likelihood of its limiting distribution. This has the additional advantage of allowing a wide range of semi-supervised learning scenarios.

