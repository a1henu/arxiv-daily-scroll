---
layout: default
title: Evaluating Chain-of-Thought Reasoning through Reusability and Verifiability
---

# Evaluating Chain-of-Thought Reasoning through Reusability and Verifiability
**arXiv**：[2602.17544v1](https://arxiv.org/abs/2602.17544) · [PDF](https://arxiv.org/pdf/2602.17544.pdf)  
**作者**：Shashank Aggarwal, Ram Vikas Mishra, Amit Awekar  

**一句话要点**：提出可重用性与可验证性以评估多智能体IR管道中的思维链推理质量

**关键词**：思维链评估, 可重用性, 可验证性, 多智能体系统, 信息检索管道

## 3 点简述
- 当前思维链评估仅关注任务准确性，忽略推理过程本身的质量。
- 引入可重用性与可验证性度量，采用Thinker-Executor框架解耦生成与执行。
- 实验显示新度量与标准准确性不相关，揭示推理能力评估盲点。

## 摘要（原文）

> In multi-agent IR pipelines for tasks such as search and ranking, LLM-based agents exchange intermediate reasoning in terms of Chain-of-Thought (CoT) with each other. Current CoT evaluation narrowly focuses on target task accuracy. However, this metric fails to assess the quality or utility of the reasoning process itself. To address this limitation, we introduce two novel measures: reusability and verifiability. We decouple CoT generation from execution using a Thinker-Executor framework. Reusability measures how easily an Executor can reuse the Thinker's CoT. Verifiability measures how frequently an Executor can match the Thinker's answer using the CoT. We evaluated four Thinker models against a committee of ten Executor models across five benchmarks. Our results reveal that reusability and verifiability do not correlate with standard accuracy, exposing a blind spot in current accuracy-based leaderboards for reasoning capability. Surprisingly, we find that CoTs from specialized reasoning models are not consistently more reusable or verifiable than those from general-purpose LLMs like Llama and Gemma.

