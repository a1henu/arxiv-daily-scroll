---
layout: default
title: dLLM: Simple Diffusion Language Modeling
---

# dLLM: Simple Diffusion Language Modeling
**arXiv**：[2602.22661v1](https://arxiv.org/abs/2602.22661) · [PDF](https://arxiv.org/pdf/2602.22661.pdf)  
**作者**：Zhanhui Zhou, Lingjie Chen, Hanghang Tong, Dawn Song  

**一句话要点**：提出dLLM框架以统一扩散语言模型的核心组件，支持定制化与可复现研究。

**关键词**：扩散语言模型, 开源框架, 模型复现, 可定制化, 小模型构建

## 3 点简述
- 核心问题：扩散语言模型组件分散，缺乏统一框架，导致复现与扩展困难。
- 方法要点：dLLM框架标准化训练、推理和评估，支持从零构建或转换现有模型为DLM。
- 实验或效果：提供开源大模型复现和小模型构建方案，发布检查点以促进研究。

## 摘要（原文）

> Although diffusion language models (DLMs) are evolving quickly, many recent models converge on a set of shared components. These components, however, are distributed across ad-hoc research codebases or lack transparent implementations, making them difficult to reproduce or extend. As the field accelerates, there is a clear need for a unified framework that standardizes these common components while remaining flexible enough to support new methods and architectures.
>   To address this gap, we introduce dLLM, an open-source framework that unifies the core components of diffusion language modeling -- training, inference, and evaluation -- and makes them easy to customize for new designs. With dLLM, users can reproduce, finetune, deploy, and evaluate open-source large DLMs such as LLaDA and Dream through a standardized pipeline. The framework also provides minimal, reproducible recipes for building small DLMs from scratch with accessible compute, including converting any BERT-style encoder or autoregressive LM into a DLM. We also release the checkpoints of these small DLMs to make DLMs more accessible and accelerate future research.

