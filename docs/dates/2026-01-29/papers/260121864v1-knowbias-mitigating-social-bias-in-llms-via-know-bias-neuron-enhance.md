---
layout: default
title: KnowBias: Mitigating Social Bias in LLMs via Know-Bias Neuron Enhancement
---

# KnowBias: Mitigating Social Bias in LLMs via Know-Bias Neuron Enhancement
**arXiv**：[2601.21864v1](https://arxiv.org/abs/2601.21864) · [PDF](https://arxiv.org/pdf/2601.21864.pdf)  
**作者**：Jinhao Pan, Chahat Raj, Anjishnu Mukherjee, Sina Mansouri, Bowen Wei, Shloka Yada, Ziwei Zhu  

**一句话要点**：提出KnowBias框架，通过增强编码偏见的神经元来缓解LLMs中的社会偏见

**关键词**：社会偏见缓解, 神经元增强, 归因分析, 轻量级框架, 推理时干预

## 3 点简述
- 核心问题：LLMs存在社会偏见，现有去偏方法常导致能力下降或泛化性差
- 方法要点：基于归因分析识别偏见知识神经元，在推理时选择性增强而非抑制
- 实验或效果：在多个基准和LLMs上实现先进去偏性能，同时保持通用能力

## 摘要（原文）

> Large language models (LLMs) exhibit social biases that reinforce harmful stereotypes, limiting their safe deployment. Most existing debiasing methods adopt a suppressive paradigm by modifying parameters, prompts, or neurons associated with biased behavior; however, such approaches are often brittle, weakly generalizable, data-inefficient, and prone to degrading general capability. We propose \textbf{KnowBias}, a lightweight and conceptually distinct framework that mitigates bias by strengthening, rather than suppressing, neurons encoding bias-knowledge. KnowBias identifies neurons encoding bias knowledge using a small set of bias-knowledge questions via attribution-based analysis, and selectively enhances them at inference time. This design enables strong debiasing while preserving general capabilities, generalizes across bias types and demographics, and is highly data efficient, requiring only a handful of simple yes/no questions and no retraining. Experiments across multiple benchmarks and LLMs demonstrate consistent state-of-the-art debiasing performance with minimal utility degradation. Data and code are available at https://github.com/JP-25/KnowBias.

