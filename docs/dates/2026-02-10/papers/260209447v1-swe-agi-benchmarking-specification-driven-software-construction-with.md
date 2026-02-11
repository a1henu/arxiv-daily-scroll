---
layout: default
title: SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in the Era of Autonomous Agents
---

# SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in the Era of Autonomous Agents
**arXiv**：[2602.09447v1](https://arxiv.org/abs/2602.09447) · [PDF](https://arxiv.org/pdf/2602.09447.pdf)  
**作者**：Zhirui Zhang, Hongbo Zhang, Haoxiang Fei, Zhiyuan Bao, Yubin Chen, Zhengyu Lei, Ziyue Liu, Yixuan Sun, Mingkun Xiao, Zihang Ye, Yu Zhang, Hongcheng Zhu, Yuxiang Wen, Heung-Yeung Shum  

**一句话要点**：提出SWE-AGI基准，用于评估基于规范驱动的大语言模型在MoonBit中构建生产级软件的能力。

**关键词**：软件工程基准, 规范驱动开发, 大语言模型评估, MoonBit编程, 自主代理, 代码生成

## 3 点简述
- 核心问题：大语言模型能否从明确规范自主构建生产规模软件仍待验证。
- 方法要点：基于MoonBit生态系统设计开源基准，任务要求实现解析器、解释器等核心逻辑。
- 实验或效果：gpt-5.3-codex表现最佳，但任务难度增加时性能显著下降，代码阅读成为瓶颈。

## 摘要（原文）

> Although large language models (LLMs) have demonstrated impressive coding capabilities, their ability to autonomously build production-scale software from explicit specifications remains an open question. We introduce SWE-AGI, an open-source benchmark for evaluating end-to-end, specification-driven construction of software systems written in MoonBit. SWE-AGI tasks require LLM-based agents to implement parsers, interpreters, binary decoders, and SAT solvers strictly from authoritative standards and RFCs under a fixed API scaffold. Each task involves implementing 1,000-10,000 lines of core logic, corresponding to weeks or months of engineering effort for an experienced human developer. By leveraging the nascent MoonBit ecosystem, SWE-AGI minimizes data leakage, forcing agents to rely on long-horizon architectural reasoning rather than code retrieval. Across frontier models, gpt-5.3-codex achieves the best overall performance (solving 19/22 tasks, 86.4%), outperforming claude-opus-4.6 (15/22, 68.2%), and kimi-2.5 exhibits the strongest performance among open-source models. Performance degrades sharply with increasing task difficulty, particularly on hard, specification-intensive systems. Behavioral analysis further reveals that as codebases scale, code reading, rather than writing, becomes the dominant bottleneck in AI-assisted development. Overall, while specification-driven autonomous software engineering is increasingly viable, substantial challenges remain before it can reliably support production-scale development.

