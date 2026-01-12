---
layout: default
title: Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection
---

# Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection
**arXiv**：[2601.05501v1](https://arxiv.org/abs/2601.05501) · [PDF](https://arxiv.org/pdf/2601.05501.pdf)  
**作者**：Feihu Jin, Ying Tan  

**一句话要点**：提出Hi-ZFO分层混合优化框架，结合零阶和一阶方法以提升大语言模型微调性能。

**关键词**：大语言模型微调, 分层优化, 零阶优化, 一阶优化, 重要性分析, 生成任务

## 3 点简述
- 标准一阶优化易陷于尖锐最小值，零阶方法探索性强但收敛慢且方差大。
- Hi-ZFO通过层重要性分析自适应分区，关键层用一阶更新，非关键层用零阶优化引入有益随机性。
- 在生成、数学和代码推理任务中验证，Hi-ZFO性能优越且显著减少训练时间。

## 摘要（原文）

> Fine-tuning large language models (LLMs) using standard first-order (FO) optimization often drives training toward sharp, poorly generalizing minima. Conversely, zeroth-order (ZO) methods offer stronger exploratory behavior without relying on explicit gradients, yet suffer from slow convergence. More critically, our analysis reveals that in generative tasks, the vast output and search space significantly amplify estimation variance, rendering ZO methods both noisy and inefficient. To address these challenges, we propose \textbf{Hi-ZFO} (\textbf{Hi}erarchical \textbf{Z}eroth- and \textbf{F}irst-\textbf{O}rder optimization), a hybrid framework designed to synergize the precision of FO gradients with the exploratory capability of ZO estimation. Hi-ZFO adaptively partitions the model through layer-wise importance profiling, applying precise FO updates to critical layers while leveraging ZO optimization for less sensitive ones. Notably, ZO in Hi-ZFO is not merely a memory-saving surrogate; it is intentionally introduced as a source of "beneficial stochasticity" to help the model escape the local minima where pure FO optimization tends to stagnate. Validated across diverse generative, mathematical, and code reasoning tasks, Hi-ZFO consistently achieves superior performance while significantly reducing the training time. These results demonstrate the effectiveness of hierarchical hybrid optimization for LLM fine-tuning.

