---
layout: default
title: Funny or Persuasive, but Not Both: Evaluating Fine-Grained Multi-Concept Control in LLMs
---

# Funny or Persuasive, but Not Both: Evaluating Fine-Grained Multi-Concept Control in LLMs
**arXiv**：[2601.18483v1](https://arxiv.org/abs/2601.18483) · [PDF](https://arxiv.org/pdf/2601.18483.pdf)  
**作者**：Arya Labroo, Ivaxi Sheth, Vyas Raina, Amaani Ahmed, Mario Fritz  

**一句话要点**：提出细粒度多概念控制评估框架，揭示大语言模型在双概念场景下的性能下降问题。

**关键词**：大语言模型, 细粒度控制, 多概念评估, 组合性局限, 提示工程

## 3 点简述
- 核心问题：大语言模型在细粒度多概念控制（如幽默与说服力）上缺乏系统评估，现有方法难以实现有效组合。
- 方法要点：引入评估框架，针对单概念和双概念场景，关注语言上独立的概念对，进行系统测量。
- 实验或效果：发现多模型和任务中双概念控制性能下降，表明基于提示的朴素控制存在组合性局限。

## 摘要（原文）

> Large Language Models (LLMs) offer strong generative capabilities, but many applications require explicit and \textit{fine-grained} control over specific textual concepts, such as humor, persuasiveness, or formality. Prior approaches in prompting and representation engineering can provide coarse or single-attribute control, but systematic evaluation of multi-attribute settings remains limited. We introduce an evaluation framework for fine-grained controllability for both single- and dual-concept scenarios, focusing on linguistically distinct concept pairs (e.g., persuasiveness vs.~humor). Surprisingly, across multiple LLMs and generative tasks, we find that performance often drops in the dual-concept setting, even though the chosen concepts should in principle be separable. This reveals a fundamental limitation of naive prompting-based control: models struggle with compositionality even when concepts are intuitively independent. Our framework provides systematic evidence of this gap and offers a principled approach for measuring the ability of future methods for multi-concept control.

