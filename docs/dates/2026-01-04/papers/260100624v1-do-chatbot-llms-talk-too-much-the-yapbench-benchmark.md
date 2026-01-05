---
layout: default
title: Do Chatbot LLMs Talk Too Much? The YapBench Benchmark
---

# Do Chatbot LLMs Talk Too Much? The YapBench Benchmark
**arXiv**：[2601.00624v1](https://arxiv.org/abs/2601.00624) · [PDF](https://arxiv.org/pdf/2601.00624.pdf)  
**作者**：Vadim Borisov, Michael Gröger, Mina Mikhael, Richard H. Schreiber  

**一句话要点**：提出YapBench基准以量化LLM在简洁理想提示下的过度生成问题

**关键词**：LLM过度生成, 简洁性基准, YapBench, 字符长度指标, 用户可见冗余, 基准评估

## 3 点简述
- 核心问题：LLM在简单请求上常生成冗余内容，增加认知负担和推理成本
- 方法要点：基于字符长度设计YapScore指标，构建包含三类简洁理想提示的基准
- 实验或效果：评估76个LLM，发现中位过度长度差异达数量级，揭示类别特定失败模式

## 摘要（原文）

> Large Language Models (LLMs) such as ChatGPT, Claude, and Gemini increasingly act as general-purpose copilots, yet they often respond with unnecessary length on simple requests, adding redundant explanations, hedging, or boilerplate that increases cognitive load and inflates token-based inference cost. Prior work suggests that preference-based post-training and LLM-judged evaluations can induce systematic length bias, where longer answers are rewarded even at comparable quality.
>   We introduce YapBench, a lightweight benchmark for quantifying user-visible over-generation on brevity-ideal prompts. Each item consists of a single-turn prompt, a curated minimal-sufficient baseline answer, and a category label. Our primary metric, YapScore, measures excess response length beyond the baseline in characters, enabling comparisons across models without relying on any specific tokenizer. We summarize model performance via the YapIndex, a uniformly weighted average of category-level median YapScores.
>   YapBench contains over three hundred English prompts spanning three common brevity-ideal settings: (A) minimal or ambiguous inputs where the ideal behavior is a short clarification, (B) closed-form factual questions with short stable answers, and (C) one-line coding tasks where a single command or snippet suffices. Evaluating 76 assistant LLMs, we observe an order-of-magnitude spread in median excess length and distinct category-specific failure modes, including vacuum-filling on ambiguous inputs and explanation or formatting overhead on one-line technical requests. We release the benchmark and maintain a live leaderboard for tracking verbosity behavior over time.

