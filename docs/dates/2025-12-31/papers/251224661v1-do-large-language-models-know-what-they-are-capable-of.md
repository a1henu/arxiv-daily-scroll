---
layout: default
title: Do Large Language Models Know What They Are Capable Of?
---

# Do Large Language Models Know What They Are Capable Of?
**arXiv**：[2512.24661v1](https://arxiv.org/abs/2512.24661) · [PDF](https://arxiv.org/pdf/2512.24661.pdf)  
**作者**：Casey O. Barkan, Sid Black, Oliver Sourbut  

**一句话要点**：探究大语言模型能否预测自身任务成功率及其决策理性

**关键词**：大语言模型, 能力预测, 过度自信, 决策理性, 多步任务, 上下文学习

## 3 点简述
- 核心问题：大语言模型是否具备预测自身任务成功的能力，以及其预测在多步任务中的变化。
- 方法要点：通过实验测试LLMs的预测准确性，分析其过度自信现象及在失败经验后的决策改进。
- 实验或效果：发现多数LLMs预测优于随机但过度自信，部分模型能从失败中学习，但整体决策因乐观估计而受限。

## 摘要（原文）

> We investigate whether large language models (LLMs) can predict whether they will succeed on a given task and whether their predictions improve as they progress through multi-step tasks. We also investigate whether LLMs can learn from in-context experiences to make better decisions about whether to pursue a task in scenarios where failure is costly. All LLMs we tested are overconfident, but most predict their success with better-than-random discriminatory power. We find that newer and larger LLMs generally do not have greater discriminatory power, though Claude models do show such a trend. On multi-step agentic tasks, the overconfidence of several frontier LLMs worsens as they progress through the tasks, and reasoning LLMs perform comparably to or worse than non-reasoning LLMs. With in-context experiences of failure, some but not all LLMs reduce their overconfidence leading to significantly improved decision making, while others do not. Interestingly, all LLMs' decisions are approximately rational given their estimated probabilities of success, yet their overly-optimistic estimates result in poor decision making. These results suggest that current LLM agents are hindered by their lack of awareness of their own capabilities. We discuss the implications of LLMs' awareness of their capabilities for AI misuse and misalignment risks.

