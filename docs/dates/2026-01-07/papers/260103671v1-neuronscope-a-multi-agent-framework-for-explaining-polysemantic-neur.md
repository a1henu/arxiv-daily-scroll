---
layout: default
title: NeuronScope: A Multi-Agent Framework for Explaining Polysemantic Neurons in Language Models
---

# NeuronScope: A Multi-Agent Framework for Explaining Polysemantic Neurons in Language Models
**arXiv**：[2601.03671v1](https://arxiv.org/abs/2601.03671) · [PDF](https://arxiv.org/pdf/2601.03671.pdf)  
**作者**：Weiqi Liu, Yongliang Miao, Haiyan Zhao, Yanguang Liu, Mengnan Du  

**一句话要点**：提出NeuronScope多智能体框架以解决大语言模型中神经元多义性解释难题

**关键词**：神经元解释, 多义性, 多智能体框架, 激活引导, 大语言模型, 语义聚类

## 3 点简述
- 核心问题：大语言模型中神经元多义性普遍，单次解释方法难以准确捕捉多概念行为
- 方法要点：采用迭代激活引导过程，将神经元激活分解为原子语义成分并聚类为不同语义模式
- 实验或效果：实验显示NeuronScope能揭示隐藏多义性，解释的激活相关性显著高于基线方法

## 摘要（原文）

> Neuron-level interpretation in large language models (LLMs) is fundamentally challenged by widespread polysemanticity, where individual neurons respond to multiple distinct semantic concepts. Existing single-pass interpretation methods struggle to faithfully capture such multi-concept behavior. In this work, we propose NeuronScope, a multi-agent framework that reformulates neuron interpretation as an iterative, activation-guided process. NeuronScope explicitly deconstructs neuron activations into atomic semantic components, clusters them into distinct semantic modes, and iteratively refines each explanation using neuron activation feedback. Experiments demonstrate that NeuronScope uncovers hidden polysemanticity and produces explanations with significantly higher activation correlation compared to single-pass baselines.

