---
layout: default
title: A Benchmark for Deep Information Synthesis
---

# A Benchmark for Deep Information Synthesis
**arXiv**：[2602.21143v1](https://arxiv.org/abs/2602.21143) · [PDF](https://arxiv.org/pdf/2602.21143.pdf)  
**作者**：Debjit Paul, Daniel Murphy, Milan Gritta, Ronald Cardenas, Victor Prokhorov, Lena Sophia Bolliger, Aysim Toker, Roy Miles, Andreea-Maria Oncescu, Jasivan Alex Sivakumar, Philipp Borchert, Ismail Elezi, Meiru Zhang, Ka Yiu Lee, Guchun Zhang, Jun Wang, Gerasimos Lampouras  

**一句话要点**：提出DEEPSYNTH基准以评估大语言模型代理在真实多源信息合成任务中的能力

**关键词**：大语言模型代理, 信息合成基准, 多源推理, 真实任务评估, 幻觉问题

## 3 点简述
- 当前基准无法充分评估大语言模型代理在真实复杂任务中的信息合成与推理能力
- DEEPSYNTH通过多阶段数据收集构建包含120个跨领域任务的基准，强调信息收集、合成与结构化推理
- 在DEEPSYNTH上评估的11个先进模型表现不佳，最高F1分数为8.97，突显基准难度与模型在幻觉和大信息空间推理方面的挑战

## 摘要（原文）

> Large language model (LLM)-based agents are increasingly used to solve complex tasks involving tool use, such as web browsing, code execution, and data analysis. However, current evaluation benchmarks do not adequately assess their ability to solve real-world tasks that require synthesizing information from multiple sources and inferring insights beyond simple fact retrieval. To address this, we introduce DEEPSYNTH, a novel benchmark designed to evaluate agents on realistic, time-consuming problems that combine information gathering, synthesis, and structured reasoning to produce insights. DEEPSYNTH contains 120 tasks collected across 7 domains and data sources covering 67 countries. DEEPSYNTH is constructed using a multi-stage data collection pipeline that requires annotators to collect official data sources, create hypotheses, perform manual analysis, and design tasks with verifiable answers. When evaluated on DEEPSYNTH, 11 state-of-the-art LLMs and deep research agents achieve a maximum F1 score of 8.97 and 17.5 on the LLM-judge metric, underscoring the difficulty of the benchmark. Our analysis reveals that current agents struggle with hallucinations and reasoning over large information spaces, highlighting DEEPSYNTH as a crucial benchmark for guiding future research.

