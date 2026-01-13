---
layout: default
title: Hidden Monotonicity: Explaining Deep Neural Networks via their DC Decomposition
---

# Hidden Monotonicity: Explaining Deep Neural Networks via their DC Decomposition
**arXiv**：[2601.07700v1](https://arxiv.org/abs/2601.07700) · [PDF](https://arxiv.org/pdf/2601.07700.pdf)  
**作者**：Jakob Paul Zimmermann, Georg Loho  

**一句话要点**：提出基于DC分解的隐藏单调性方法，以提升深度神经网络的解释性。

**关键词**：神经网络解释性, DC分解, 单调性, ReLU网络, ImageNet-S, 自解释系统

## 3 点简述
- 核心问题：单调性有助于解释性，但并非所有函数都适合单调网络近似。
- 方法要点：将ReLU网络分解为两个单调凸部分，并训练为两个单调网络之差。
- 实验或效果：SplitCAM和SplitLRP在ImageNet-S上改进量化指标，增强自解释性。

## 摘要（原文）

> It has been demonstrated in various contexts that monotonicity leads to better explainability in neural networks. However, not every function can be well approximated by a monotone neural network. We demonstrate that monotonicity can still be used in two ways to boost explainability. First, we use an adaptation of the decomposition of a trained ReLU network into two monotone and convex parts, thereby overcoming numerical obstacles from an inherent blowup of the weights in this procedure. Our proposed saliency methods -- SplitCAM and SplitLRP -- improve on state of the art results on both VGG16 and Resnet18 networks on ImageNet-S across all Quantus saliency metric categories. Second, we exhibit that training a model as the difference between two monotone neural networks results in a system with strong self-explainability properties.

