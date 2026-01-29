---
layout: default
title: MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents
---

# MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents
**arXiv**：[2601.20831v1](https://arxiv.org/abs/2601.20831) · [PDF](https://arxiv.org/pdf/2601.20831.pdf)  
**作者**：Vishnu Sashank Dorbala, Dinesh Manocha  

**一句话要点**：提出MemCtrl框架，使用MLLMs作为具身代理的在线内存控制器以优化决策。

**关键词**：具身代理, 多模态大语言模型, 在线内存控制, 内存剪枝, 强化学习, 基准评估

## 3 点简述
- 核心问题：具身代理在严格内存和计算约束下，现有内存系统如RAG不适合在线操作。
- 方法要点：通过可训练内存头μ，让MLLMs在线剪枝内存，决定保留、更新或丢弃观察。
- 实验或效果：在EmbodiedBench基准上，μ增强的MLLMs平均提升约16%，特定指令子集超20%。

## 摘要（原文）

> Foundation models rely on in-context learning for personalized decision making. The limited size of this context window necessitates memory compression and retrieval systems like RAG. These systems however often treat memory as large offline storage spaces, which is unfavorable for embodied agents that are expected to operate under strict memory and compute constraints, online. In this work, we propose MemCtrl, a novel framework that uses Multimodal Large Language Models (MLLMs) for pruning memory online. MemCtrl augments MLLMs with a trainable memory head μthat acts as a gate to determine which observations or reflections to retain, update, or discard during exploration. We evaluate with training two types of μ, 1) via an offline expert, and 2) via online RL, and observe significant improvement in overall embodied task completion ability on μ-augmented MLLMs. In particular, on augmenting two low performing MLLMs with MemCtrl on multiple subsets of the EmbodiedBench benchmark, we observe that μ-augmented MLLMs show an improvement of around 16% on average, with over 20% on specific instruction subsets. Finally, we present a qualitative analysis on the memory fragments collected by μ, noting the superior performance of μaugmented MLLMs on long and complex instruction types.

