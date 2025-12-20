---
layout: default
title: In-Context Multi-Operator Learning with DeepOSets
---

# In-Context Multi-Operator Learning with DeepOSets
**arXiv**：[2512.16074v1](https://arxiv.org/abs/2512.16074) · [PDF](https://arxiv.org/pdf/2512.16074.pdf)  
**作者**：Shao-Ting Chiu, Aditya Nambiar, Ali Syed, Jonathan W. Siegel, Ulisses Braga-Neto  

**一句话要点**：提出DeepOSets架构实现多算子上下文学习，用于未见训练PDE的求解算子恢复。

**关键词**：上下文学习, 算子学习, 偏微分方程求解, DeepOSets架构, 科学机器学习

## 3 点简述
- 核心问题：探索非自回归、非注意力架构在上下文学习中的能力，特别是针对PDE求解算子的泛化。
- 方法要点：结合DeepSets和DeepONets，通过修改DeepOSets实现多算子上下文学习，无需权重更新。
- 实验或效果：在Poisson和反应-扩散正反边值问题上验证，能准确预测未见PDE的参数对应解。

## 摘要（原文）

> In-context Learning (ICL) is the remarkable capability displayed by some machine learning models to learn from examples in a prompt, without any further weight updates. ICL had originally been thought to emerge from the self-attention mechanism in autoregressive transformer architectures. DeepOSets is a non-autoregressive, non-attention based neural architecture that combines set learning via the DeepSets architecture with operator learning via Deep Operator Networks (DeepONets). In a previous study, DeepOSets was shown to display ICL capabilities in supervised learning problems. In this paper, we show that the DeepOSets architecture, with the appropriate modifications, is a multi-operator in-context learner that can recover the solution operator of a new PDE, not seen during training, from example pairs of parameter and solution placed in a user prompt, without any weight updates. Furthermore, we show that DeepOSets is a universal uniform approximator over a class of continuous operators, which we believe is the first result of its kind in the literature of scientific machine learning. This means that a single DeepOSets architecture exists that approximates in-context any continuous operator in the class to any fixed desired degree accuracy, given an appropriate number of examples in the prompt. Experiments with Poisson and reaction-diffusion forward and inverse boundary-value problems demonstrate the ability of the proposed model to use in-context examples to predict accurately the solutions corresponding to parameter queries for PDEs not seen during training.

