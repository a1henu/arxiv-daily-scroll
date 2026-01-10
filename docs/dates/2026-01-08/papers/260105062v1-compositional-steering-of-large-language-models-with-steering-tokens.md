---
layout: default
title: Compositional Steering of Large Language Models with Steering Tokens
---

# Compositional Steering of Large Language Models with Steering Tokens
**arXiv**：[2601.05062v1](https://arxiv.org/abs/2601.05062) · [PDF](https://arxiv.org/pdf/2601.05062.pdf)  
**作者**：Gorjan Radevski, Kiril Gashteovski, Giwon Hong, Carolin Lawrence, Goran Glavaš  

**一句话要点**：提出组合引导令牌以解决大语言模型多行为组合引导问题

**关键词**：组合引导, 引导令牌, 自蒸馏, 零样本泛化, 多行为控制, 大语言模型

## 3 点简述
- 核心问题：现有方法难以同时引导LLM满足多个行为需求，组合引导研究不足
- 方法要点：通过自蒸馏将自然语言指令嵌入令牌，训练组合令牌实现零样本组合泛化
- 实验或效果：在多种LLM架构上优于指令、激活引导和LoRA合并方法，与指令结合效果更佳

## 摘要（原文）

> Deploying LLMs in real-world applications requires controllable output that satisfies multiple desiderata at the same time. While existing work extensively addresses LLM steering for a single behavior, \textit{compositional steering} -- i.e., steering LLMs simultaneously towards multiple behaviors -- remains an underexplored problem. In this work, we propose \emph{compositional steering tokens} for multi-behavior steering. We first embed individual behaviors, expressed as natural language instructions, into dedicated tokens via self-distillation. Contrary to most prior work, which operates in the activation space, our behavior steers live in the space of input tokens, enabling more effective zero-shot composition. We then train a dedicated \textit{composition token} on pairs of behaviors and show that it successfully captures the notion of composition: it generalizes well to \textit{unseen} compositions, including those with unseen behaviors as well as those with an unseen \textit{number} of behaviors. Our experiments across different LLM architectures show that steering tokens lead to superior multi-behavior control compared to competing approaches (instructions, activation steering, and LoRA merging). Moreover, we show that steering tokens complement natural language instructions, with their combination resulting in further gains.

