---
layout: default
title: GLUScope: A Tool for Analyzing GLU Neurons in Transformer Language Models
---

# GLUScope: A Tool for Analyzing GLU Neurons in Transformer Language Models
**arXiv**：[2602.23826v1](https://arxiv.org/abs/2602.23826) · [PDF](https://arxiv.org/pdf/2602.23826.pdf)  
**作者**：Sebastian Gerstner, Hinrich Schütze  

**一句话要点**：提出GLUScope工具以分析Transformer语言模型中的GLU神经元，支持门控激活函数分析。

**关键词**：Transformer语言模型, 神经元分析, 门控激活函数, 可解释性研究, 开源工具

## 3 点简述
- 核心问题：传统工具难以分析门控激活函数（如SwiGLU）的神经元，需考虑正负激活组合。
- 方法要点：工具展示四种符号组合的文本示例，并统计各组合频率，帮助理解神经元功能。
- 实验或效果：通过示例展示工具能带来新见解，提供开源工具和在线演示。

## 摘要（原文）

> We present GLUScope, an open-source tool for analyzing neurons in Transformer-based language models, intended for interpretability researchers. We focus on more recent models than previous tools do; specifically we consider gated activation functions such as SwiGLU. This introduces a new challenge: understanding positive activations is not enough. Instead, both the gate and the in activation of a neuron can be positive or negative, leading to four different possible sign combinations that in some cases have quite different functionalities. Accordingly, for any neuron, our tool shows text examples for each of the four sign combinations, and indicates how often each combination occurs. We describe examples of how our tool can lead to novel insights. A demo is available at https: //sjgerstner.github.io/gluscope.

