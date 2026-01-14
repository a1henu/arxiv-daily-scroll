---
layout: default
title: Closed-Loop LLM Discovery of Non-Standard Channel Priors in Vision Models
---

# Closed-Loop LLM Discovery of Non-Standard Channel Priors in Vision Models
**arXiv**：[2601.08517v1](https://arxiv.org/abs/2601.08517) · [PDF](https://arxiv.org/pdf/2601.08517.pdf)  
**作者**：Tolgay Atinc Uzun, Dmitry Ignatov, Radu Timofte  

**一句话要点**：提出基于LLM的闭环NAS框架以优化视觉模型中的通道配置搜索

**关键词**：神经架构搜索, 通道配置优化, 大语言模型应用, 视觉模型设计, 代码生成

## 3 点简述
- 核心问题：通道配置搜索是受张量形状和计算预算约束的组合优化难题。
- 方法要点：利用LLM通过代码生成和AST突变生成大量有效架构，学习配置与性能关系。
- 实验或效果：在CIFAR-100上验证，模型准确率有统计显著提升，优于随机搜索。

## 摘要（原文）

> Channel configuration search the optimization of layer specifications such as layer widths in deep neural networks presents a complex combinatorial challenge constrained by tensor shape compatibility and computational budgets. We posit that Large Language Models (LLMs) offer a transformative approach to Neural Architecture Search (NAS), capable of reasoning about architectural code structure in ways that traditional heuristics cannot. In this paper, we investigate the application of an LLM-driven NAS framework to the problem of channel configuration. We formulate the search as a sequence of conditional code generation tasks, where an LLM refines architectural specifications based on performance telemetry. Crucially, we address the data scarcity problem by generating a vast corpus of valid, shape-consistent architectures via Abstract Syntax Tree (AST) mutations. While these mutated networks are not necessarily high-performing, they provide the critical volume of structural data required for the LLM to learn the latent relationship between channel configurations and model performance. This allows the LLM to internalize complex design patterns and apply them to optimize feature extraction strategies. Experimental results on CIFAR-100 validate the efficacy of this approach, demonstrating that the model yields statistically significant improvements in accuracy. Our analysis confirms that the LLM successfully acquires domain-specific architectural priors, distinguishing this method from random search and highlighting the immense potential of language-driven design in deep learning.

