---
layout: default
title: Bayesian Adversarial Privacy
---

# Bayesian Adversarial Privacy
**arXiv**：[2603.04199v1](https://arxiv.org/abs/2603.04199) · [PDF](https://arxiv.org/pdf/2603.04199.pdf)  
**作者**：Cameron Bell, Timothy Johnston, Antoine Luciano, Christian P Robert  

**一句话要点**：提出贝叶斯对抗隐私以提供更优的隐私量化定义，超越差分隐私和统计披露理论。

**关键词**：隐私量化, 贝叶斯决策理论, 对抗隐私, 统计披露, 上下文隐私, 先验视角

## 3 点简述
- 核心问题：现有隐私框架如差分隐私和统计披露理论在上下文特定性和严谨性方面存在不足。
- 方法要点：基于标准贝叶斯决策理论，但强调从先验视角而非数据条件进行披露决策。
- 实验或效果：通过详细玩具示例和计算方法阐明方法的特异性，未知实际应用效果。

## 摘要（原文）

> Theoretical and applied research into privacy encompasses an incredibly broad swathe of differing approaches, emphasis and aims. This work introduces a new quantitative notion of privacy that is both contextual and specific. We argue that it provides a more meaningful notion of privacy than the widely utilised framework of differential privacy and a more explicit and rigorous formulation than what is commonly used in statistical disclosure theory. Our definition relies on concepts inherent to standard Bayesian decision theory, while departing from it in several important respects. In particular, the party controlling the release of sensitive information should make disclosure decisions from the prior viewpoint, rather than conditional on the data, even when the data is itself observed. Illuminating toy examples and computational methods are discussed in high detail in order to highlight the specificities of the method.

