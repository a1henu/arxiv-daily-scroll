---
layout: default
title: MHRC-Bench: A Multilingual Hardware Repository-Level Code Completion benchmark
---

# MHRC-Bench: A Multilingual Hardware Repository-Level Code Completion benchmark
**arXiv**：[2601.03708v1](https://arxiv.org/abs/2601.03708) · [PDF](https://arxiv.org/pdf/2601.03708.pdf)  
**作者**：Qingyun Zou, Jiahao Cui, Nuo Chen, Bingsheng He, Weng-Fai Wong  

**一句话要点**：提出MHRC-Bench以评估多语言硬件仓库级代码补全性能

**关键词**：硬件代码补全, 仓库级基准, 多语言评估, 硬件描述语言, 代码结构分析

## 3 点简述
- 现有基准主要关注软件代码，缺乏硬件描述语言的仓库级补全评估
- MHRC-Bench包含训练和评估集，覆盖三种硬件设计编码风格，并标注代码结构和语义标签
- 通过综合评估验证了基准的有效性，但具体模型性能未知

## 摘要（原文）

> Large language models (LLMs) have achieved strong performance on code completion tasks in general-purpose programming languages. However, existing repository-level code completion benchmarks focus almost exclusively on software code and largely overlook hardware description languages. In this work, we present \textbf{MHRC-Bench}, consisting of \textbf{MHRC-Bench-Train} and \textbf{MHRC-Bench-Eval}, the first benchmark designed for multilingual hardware code completion at the repository level. Our benchmark targets completion tasks and covers three major hardware design coding styles. Each completion target is annotated with code-structure-level and hardware-oriented semantic labels derived from concrete syntax tree analysis. We conduct a comprehensive evaluation of models on MHRC-Bench-Eval. Comprehensive evaluation results and analysis demonstrate the effectiveness of MHRC-Bench.

