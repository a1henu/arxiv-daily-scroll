---
layout: default
title: An Information-Theoretic Framework for Robust Large Language Model Editing
---

# An Information-Theoretic Framework for Robust Large Language Model Editing
**arXiv**：[2512.16227v1](https://arxiv.org/abs/2512.16227) · [PDF](https://arxiv.org/pdf/2512.16227.pdf)  
**作者**：Qizhou Chen, Chengyu Wang, Taolin Zhang, Xiaofeng He  

**一句话要点**：提出基于信息瓶颈理论的大语言模型编辑框架，以提升知识修正的泛化性和鲁棒性。

**关键词**：大语言模型编辑, 信息瓶颈理论, 知识修正, 泛化性, 鲁棒性

## 3 点简述
- 核心问题：大语言模型知识错误或过时，现有编辑方法泛化性差，易产生副作用。
- 方法要点：利用信息瓶颈理论压缩和隔离关键信息，通过紧凑潜在表示指导梯度更新。
- 实验或效果：在多种模型和基准任务上验证，实现高精度编辑，提升泛化性和特异性。

## 摘要（原文）

> Large Language Models (LLMs) have become indispensable tools in science, technology, and society, enabling transformative advances across diverse fields. However, errors or outdated information within these models can undermine their accuracy and restrict their safe deployment. Developing efficient strategies for updating model knowledge without the expense and disruption of full retraining remains a critical challenge. Current model editing techniques frequently struggle to generalize corrections beyond narrow domains, leading to unintended consequences and limiting their practical impact. Here, we introduce a novel framework for editing LLMs, grounded in information bottleneck theory. This approach precisely compresses and isolates the essential information required for generalizable knowledge correction while minimizing disruption to unrelated model behaviors. Building upon this foundation, we present the Information Bottleneck Knowledge Editor (IBKE), which leverages compact latent representations to guide gradient-based updates, enabling robust and broadly applicable model editing. We validate IBKE's effectiveness across multiple LLM architectures and standard benchmark tasks, demonstrating state-of-the-art accuracy and improved generality and specificity of edits. These findings establish a theoretically principled and practical paradigm for open-domain knowledge editing, advancing the utility and trustworthiness of LLMs in real-world applications.

