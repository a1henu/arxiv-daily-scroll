---
layout: default
title: UNBOX: Unveiling Black-box visual models with Natural-language
---

# UNBOX: Unveiling Black-box visual models with Natural-language
**arXiv**：[2603.08639v1](https://arxiv.org/abs/2603.08639) · [PDF](https://arxiv.org/pdf/2603.08639.pdf)  
**作者**：Simone Carnemolla, Chiara Russo, Simone Palazzo, Quentin Bouniot, Daniela Giordano, Zeynep Akata, Matteo Pennisi, Concetto Spampinato  

**一句话要点**：提出UNBOX框架，在完全黑盒约束下通过语义搜索揭示视觉模型内部概念

**关键词**：黑盒模型解释, 激活最大化, 语义搜索, 视觉识别, 可信AI, 偏见检测

## 3 点简述
- 核心问题：黑盒视觉模型缺乏透明度，阻碍可信度评估与偏见检测
- 方法要点：利用大语言模型和扩散模型，将激活最大化转化为语义搜索
- 实验或效果：在ImageNet等数据集上，性能媲美白盒解释方法

## 摘要（原文）

> Ensuring trustworthiness in open-world visual recognition requires models that are interpretable, fair, and robust to distribution shifts. Yet modern vision systems are increasingly deployed as proprietary black-box APIs, exposing only output probabilities and hiding architecture, parameters, gradients, and training data. This opacity prevents meaningful auditing, bias detection, and failure analysis. Existing explanation methods assume white- or gray-box access or knowledge of the training distribution, making them unusable in these real-world settings. We introduce UNBOX, a framework for class-wise model dissection under fully data-free, gradient-free, and backpropagation-free constraints. UNBOX leverages Large Language Models and text-to-image diffusion models to recast activation maximization as a purely semantic search driven by output probabilities. The method produces human-interpretable text descriptors that maximally activate each class, revealing the concepts a model has implicitly learned, the training distribution it reflects, and potential sources of bias. We evaluate UNBOX on ImageNet-1K, Waterbirds, and CelebA through semantic fidelity tests, visual-feature correlation analyses and slice-discovery auditing. Despite operating under the strictest black-box constraints, UNBOX performs competitively with state-of-the-art white-box interpretability methods. This demonstrates that meaningful insight into a model's internal reasoning can be recovered without any internal access, enabling more trustworthy and accountable visual recognition systems.

