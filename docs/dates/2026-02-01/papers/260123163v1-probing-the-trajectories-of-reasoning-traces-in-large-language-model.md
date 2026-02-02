---
layout: default
title: Probing the Trajectories of Reasoning Traces in Large Language Models
---

# Probing the Trajectories of Reasoning Traces in Large Language Models
**arXiv**：[2601.23163v1](https://arxiv.org/abs/2601.23163) · [PDF](https://arxiv.org/pdf/2601.23163.pdf)  
**作者**：Marthe Ballon, Brecht Verbeken, Vincent Ginis, Andres Algaba  

**一句话要点**：提出轨迹探测协议以分析大语言模型推理轨迹的准确性与决策演化

**关键词**：推理轨迹分析, 大语言模型评估, 轨迹探测协议, 决策演化, 模型可靠性

## 3 点简述
- 核心问题：大语言模型推理轨迹中准确性与决策承诺如何演化，中间段是否提供答案相关信息
- 方法要点：通过生成、截断和注入部分推理轨迹，测量模型对答案选择的概率分布
- 实验或效果：在GPQA Diamond和MMLU-Pro基准上应用，发现准确性与决策承诺随推理令牌百分比增加而提升

## 摘要（原文）

> Large language models (LLMs) increasingly solve difficult problems by producing "reasoning traces" before emitting a final response. However, it remains unclear how accuracy and decision commitment evolve along a reasoning trajectory, and whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects. Here, we propose a protocol to systematically probe the trajectories of reasoning traces in LLMs by 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities. We apply this protocol to the open-source Qwen3-4B/-8B/-14B and gpt-oss-20b/-120b models across the multiple-choice GPQA Diamond and MMLU-Pro benchmarks. We find that accuracy and decision commitment consistently increase as the percentage of provided reasoning tokens grows. These gains are primarily driven by relevant content in the model generation rather than context length or generic "reasoning style" effects. Stronger models often backtrack successfully from incorrect partial traces, but immediate answers often remain anchored in the weaker model's incorrect response. More broadly, we show that trajectory probing provides diagnostics for efficient and safer deployment of reasoning models as the measurements can inform practical trace-handling and monitoring policies that improve reliability without assuming intermediate tokens are inherently faithful explanations.

