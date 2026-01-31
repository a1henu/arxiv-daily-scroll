---
layout: default
title: Bridging the Arithmetic Gap: The Cognitive Complexity Benchmark and Financial-PoT for Robust Financial Reasoning
---

# Bridging the Arithmetic Gap: The Cognitive Complexity Benchmark and Financial-PoT for Robust Financial Reasoning
**arXiv**：[2601.21157v1](https://arxiv.org/abs/2601.21157) · [PDF](https://arxiv.org/pdf/2601.21157.pdf)  
**作者**：Boxiang Zhao, Qince Li, Zhonghao Wang, Yi Wang, Peng Cheng, Bo Lin  

**一句话要点**：提出认知复杂度基准与金融PoT框架以解决大语言模型在金融定量推理中的算术幻觉和认知崩溃问题。

**关键词**：金融定量推理, 认知复杂度基准, 神经符号架构, 算术幻觉, 迭代双相框架, Python沙箱

## 3 点简述
- 核心问题：大语言模型在金融定量推理中易出现算术幻觉和认知崩溃，导致可靠性不足。
- 方法要点：引入认知复杂度基准进行分层评估，并提出迭代双相金融PoT框架，通过神经符号架构分离语义与计算。
- 实验或效果：在Qwen3-235B模型上，平均准确率从59.7%提升至67.3%，高复杂度任务性能提升高达10倍。

## 摘要（原文）

> While Large Language Models excel at semantic tasks, they face a critical bottleneck in financial quantitative reasoning, frequently suffering from "Arithmetic Hallucinations" and a systemic failure mode we term "Cognitive Collapse". To strictly quantify this phenomenon, we introduce the Cognitive Complexity Benchmark (CCB), a robust evaluation framework grounded in a dataset constructed from 95 real-world Chinese A-share annual reports. Unlike traditional datasets, the CCB stratifies financial queries into a three-dimensional taxonomy, Data Source, Mapping Difficulty, and Result Unit, enabling the precise diagnosis of reasoning degradation in high-cognitive-load scenarios. To address these failures, we propose the Iterative Dual-Phase Financial-PoT framework. This neuro-symbolic architecture enforces a strict architectural decoupling: it first isolates semantic variable extraction and logic formulation, then offloads computation to an iterative, self-correcting Python sandbox to ensure deterministic execution. Evaluation on the CCB demonstrates that while standard Chain-of-Thought falters on complex tasks, our approach offers superior robustness, elevating the Qwen3-235B model's average accuracy from 59.7\% to 67.3\% and achieving gains of up to 10-fold in high-complexity reasoning tasks. These findings suggest that architectural decoupling is a critical enabling factor for improving reliability in financial reasoning tasks, providing a transferable architectural insight for precision-critical domains that require tight alignment between semantic understanding and quantitative computation.

