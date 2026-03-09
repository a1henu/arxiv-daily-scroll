---
layout: default
title: Diffusion Language Models Are Natively Length-Aware
---

# Diffusion Language Models Are Natively Length-Aware
**arXiv**：[2603.06123v1](https://arxiv.org/abs/2603.06123) · [PDF](https://arxiv.org/pdf/2603.06123.pdf)  
**作者**：Vittorio Rossi, Giacomo Cirò, Davide Beltrame, Luca Gandolfi, Paul Röttger, Dirk Hovy  

**一句话要点**：提出零样本机制以动态裁剪上下文窗口，解决扩散语言模型在短响应任务中的计算浪费问题。

**关键词**：扩散语言模型, 长度感知, 计算效率, 零样本机制, 上下文窗口裁剪, 推理任务

## 3 点简述
- 扩散语言模型生成固定长度响应，导致短响应任务计算效率低。
- 利用潜在提示表示估计输出长度，零样本动态裁剪上下文窗口。
- 在四个基准测试中实现显著计算节省，性能影响最小或有所提升。

## 摘要（原文）

> Unlike autoregressive language models, which terminate variable-length generation upon predicting an End-of-Sequence (EoS) token, Diffusion Language Models (DLMs) operate over a fixed maximum-length context window for a predetermined number of denoising steps. However, this process is independent of the required response length, resulting in computational waste for the majority of short responses common in reasoning and chat tasks. To address this problem, we conjecture that the latent prompt representation contains sufficient information to estimate the required output length. We provide empirical evidence for this phenomenon and propose a zero-shot mechanism to dynamically crop the context window before generation begins, leading to fewer diffusion steps and substantial computational savings. We evaluate our approach on four benchmarks with diverse tasks -- GSM8K (reasoning), HumanEval (code generation), IfEval (instruction following), and LongFormQA (question answering) -- revealing massive efficiency gains at minimal performance impact. We report significant reductions in FLOPs across all tasks, with no statistically significant performance degradation, and significant performance improvements in 2 out of 4 tasks.

