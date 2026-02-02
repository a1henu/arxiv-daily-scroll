---
layout: default
title: Divide-and-Conquer CoT: RL for Reducing Latency via Parallel Reasoning
---

# Divide-and-Conquer CoT: RL for Reducing Latency via Parallel Reasoning
**arXiv**：[2601.23027v1](https://arxiv.org/abs/2601.23027) · [PDF](https://arxiv.org/pdf/2601.23027.pdf)  
**作者**：Arvind Mahankali, Kaiyue Wen, Tengyu Ma  

**一句话要点**：提出Divide-and-Conquer CoT方法，通过并行推理降低大语言模型长思维链的延迟。

**关键词**：长思维链推理, 并行推理, 延迟优化, 强化学习, 大语言模型

## 3 点简述
- 核心问题：长思维链推理导致大语言模型生成延迟高，影响实时应用。
- 方法要点：训练模型作为导演，识别可并行执行的子任务，并生成工作器执行，结合SFT和多阶段RL优化。
- 实验或效果：在AIME 2024等基准上，保持准确率的同时，最长路径长度减少35-40%。

## 摘要（原文）

> Long chain-of-thought reasoning (Long CoT) is now fundamental to state-of-the-art LLMs, especially in mathematical reasoning. However, LLM generation is highly sequential, and long CoTs lead to a high latency. We propose to train Divide-and-Conquer CoT (DC-CoT) to reduce the latency. With DC-CoT, the model can act as a director that identifies distinct subtasks that can be performed in parallel in its reasoning process, and then spawns workers to execute the subtasks. Our goal is to achieve high accuracy, with a low longest path length, which is a theoretical measure of the latency needed for the response. We start with a long CoT base model (DeepScaleR-1.5B-Preview), and first use SFT with a small curated demonstration set to initialize its ability to spawn workers in a certain format. Because SFT degrades the accuracy significantly, we design a multi-stage RL algorithm, with various data filtering strategies, to recover the accuracy while decreasing the longest path length. Across several benchmarks including AIME 2024 and HMMT 2025, DC-CoT achieves similar accuracy as DeepScaleR-1.5B-Preview while decreasing longest path length by 35-40%. Our code, SFT dataset and models are publicly available at https://github.com/amahankali10/DC_CoT_RL_for_Low_Latency_CoT_with_Parallel_Reasoning.

