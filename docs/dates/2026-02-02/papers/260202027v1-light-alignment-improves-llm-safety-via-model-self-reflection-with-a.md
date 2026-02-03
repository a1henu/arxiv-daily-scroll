---
layout: default
title: Light Alignment Improves LLM Safety via Model Self-Reflection with a Single Neuron
---

# Light Alignment Improves LLM Safety via Model Self-Reflection with a Single Neuron
**arXiv**：[2602.02027v1](https://arxiv.org/abs/2602.02027) · [PDF](https://arxiv.org/pdf/2602.02027.pdf)  
**作者**：Sicheng Shen, Mingyang Lv, Han Shen, Jialin Wu, Binghao Wang, Zhou Yang, Guobin Shen, Dongcheng Zhao, Feifei Zhao, Yi Zeng  

**一句话要点**：提出基于单神经元门控的轻量对齐方法，以提升大语言模型安全性与实用性。

**关键词**：大语言模型安全, 轻量对齐, 单神经元门控, 安全解码, 模型泛化, 实用部署

## 3 点简述
- 核心问题：现有安全对齐方法计算成本高、泛化能力差，轻量方法依赖外部注入或模型能力，导致效率与实用性受限。
- 方法要点：通过低成本训练专家模型，利用单神经元门控机制平衡模型内在能力与外部指导，实现安全解码。
- 实验或效果：在训练开销和跨模型规模泛化方面表现优势，为轻量对齐提供新视角，代码已开源。

## 摘要（原文）

> The safety of large language models (LLMs) has increasingly emerged as a fundamental aspect of their development. Existing safety alignment for LLMs is predominantly achieved through post-training methods, which are computationally expensive and often fail to generalize well across different models. A small number of lightweight alignment approaches either rely heavily on prior-computed safety injections or depend excessively on the model's own capabilities, resulting in limited generalization and degraded efficiency and usability during generation. In this work, we propose a safety-aware decoding method that requires only low-cost training of an expert model and employs a single neuron as a gating mechanism. By effectively balancing the model's intrinsic capabilities with external guidance, our approach simultaneously preserves utility and enhances output safety. It demonstrates clear advantages in training overhead and generalization across model scales, offering a new perspective on lightweight alignment for the safe and practical deployment of large language models. Code: https://github.com/Beijing-AISI/NGSD.

