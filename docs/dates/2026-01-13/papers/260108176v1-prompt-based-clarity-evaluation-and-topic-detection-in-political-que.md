---
layout: default
title: Prompt-Based Clarity Evaluation and Topic Detection in Political Question Answering
---

# Prompt-Based Clarity Evaluation and Topic Detection in Political Question Answering
**arXiv**：[2601.08176v1](https://arxiv.org/abs/2601.08176) · [PDF](https://arxiv.org/pdf/2601.08176.pdf)  
**作者**：Lavanya Prahallad, Sai Utkarsh Choudarypally, Pragna Prahallad, Pranathi Prahallad  

**一句话要点**：研究提示设计对政治问答中清晰度评估与主题检测的影响，基于CLARITY数据集

**关键词**：政治问答, 清晰度评估, 提示设计, 思维链提示, 主题检测, 自动评估

## 3 点简述
- 核心问题：自动评估LLM政治回答时，提示设计对清晰度评估的影响未充分探索。
- 方法要点：比较GPT-3.5基线，在GPT-5.2上测试简单提示、思维链提示和带少样本的思维链提示。
- 实验或效果：思维链少样本提示将清晰度预测准确率从56%提升至63%，主题检测准确率从60%提升至74%。

## 摘要（原文）

> Automatic evaluation of large language model (LLM) responses requires not only factual correctness but also clarity, particularly in political question-answering. While recent datasets provide human annotations for clarity and evasion, the impact of prompt design on automatic clarity evaluation remains underexplored. In this paper, we study prompt-based clarity evaluation using the CLARITY dataset from the SemEval 2026 shared task. We compare a GPT-3.5 baseline provided with the dataset against GPT-5.2 evaluated under three prompting strategies: simple prompting, chain-of-thought prompting, and chain-of-thought with few-shot examples. Model predictions are evaluated against human annotations using accuracy and class-wise metrics for clarity and evasion, along with hierarchical exact match. Results show that GPT-5.2 consistently outperforms the GPT-3.5 baseline on clarity prediction, with accuracy improving from 56 percent to 63 percent under chain-of-thought with few-shot prompting. Chain-of-thought prompting yields the highest evasion accuracy at 34 percent, though improvements are less stable across fine-grained evasion categories. We further evaluate topic identification and find that reasoning-based prompting improves accuracy from 60 percent to 74 percent relative to human annotations. Overall, our findings indicate that prompt design reliably improves high-level clarity evaluation, while fine-grained evasion and topic detection remain challenging despite structured reasoning prompts.

