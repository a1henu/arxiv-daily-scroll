---
layout: default
title: PILOT-Bench: A Benchmark for Legal Reasoning in the Patent Domain with IRAC-Aligned Classification Tasks
---

# PILOT-Bench: A Benchmark for Legal Reasoning in the Patent Domain with IRAC-Aligned Classification Tasks
**arXiv**：[2601.04758v1](https://arxiv.org/abs/2601.04758) · [PDF](https://arxiv.org/pdf/2601.04758.pdf)  
**作者**：Yehoon Jang, Chaewon Lee, Hyun-seok Min, Sungchul Choi  

**一句话要点**：提出PILOT-Bench基准以系统评估专利领域法律推理能力，基于PTAB决策与IRAC对齐任务。

**关键词**：专利法律推理, 基准评估, IRAC分类, 大语言模型, PTAB决策

## 3 点简述
- 核心问题：缺乏系统评估LLMs在专利领域结构化法律推理能力的基准。
- 方法要点：构建首个PTAB中心基准，对齐案例级数据并定义IRAC分类任务。
- 实验或效果：评估闭源与开源模型，闭源模型在Issue Type任务上表现优异，开源模型存在差距。

## 摘要（原文）

> The Patent Trial and Appeal Board (PTAB) of the USPTO adjudicates thousands of ex parte appeals each year, requiring the integration of technical understanding and legal reasoning. While large language models (LLMs) are increasingly applied in patent and legal practice, their use has remained limited to lightweight tasks, with no established means of systematically evaluating their capacity for structured legal reasoning in the patent domain. In this work, we introduce PILOT-Bench, the first PTAB-centric benchmark that aligns PTAB decisions with USPTO patent data at the case-level and formalizes three IRAC-aligned classification tasks: Issue Type, Board Authorities, and Subdecision. We evaluate a diverse set of closed-source (commercial) and open-source LLMs and conduct analyses across multiple perspectives, including input-variation settings, model families, and error tendencies. Notably, on the Issue Type task, closed-source models consistently exceed 0.75 in Micro-F1 score, whereas the strongest open-source model (Qwen-8B) achieves performance around 0.56, highlighting a substantial gap in reasoning capabilities. PILOT-Bench establishes a foundation for the systematic evaluation of patent-domain legal reasoning and points toward future directions for improving LLMs through dataset design and model alignment. All data, code, and benchmark resources are available at https://github.com/TeamLab/pilot-bench.

