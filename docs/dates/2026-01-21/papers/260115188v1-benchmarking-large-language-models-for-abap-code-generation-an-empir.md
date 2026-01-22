---
layout: default
title: Benchmarking Large Language Models for ABAP Code Generation: An Empirical Study on Iterative Improvement by Compiler Feedback
---

# Benchmarking Large Language Models for ABAP Code Generation: An Empirical Study on Iterative Improvement by Compiler Feedback
**arXiv**：[2601.15188v1](https://arxiv.org/abs/2601.15188) · [PDF](https://arxiv.org/pdf/2601.15188.pdf)  
**作者**：Stephan Wallraven, Tim Köhne, Hartmut Westenberger, Andreas Moser  

**一句话要点**：评估大语言模型在ABAP代码生成中的性能，基于编译器反馈的迭代改进实证研究

**关键词**：ABAP代码生成, 大语言模型评估, 编译器反馈, 迭代改进, 实证研究, SAP场景

## 3 点简述
- 核心问题：大语言模型在ABAP代码生成中的性能未知，缺乏系统分析。
- 方法要点：通过180个任务基准测试，结合HumanEval任务和SAP场景，评估模型生成语法正确和功能代码的能力。
- 实验或效果：强大模型在多次迭代后成功率约75%，编译器反馈显著提升性能，小模型表现较弱。

## 摘要（原文）

> This work investigates the performance of Large Language Models (LLMs) in generating ABAP code. Despite successful applications of generative AI in many programming languages, there are hardly any systematic analyses of ABAP code generation to date. The aim of the study is to empirically analyze to what extent various LLMs can generate syntactically correct and functional ABAP code, how effectively they use compiler feedback for iterative improvement, and which task types pose special challenges. For this purpose, a benchmark with 180 tasks is conducted, consisting of adapted HumanEval tasks and practical SAP scenarios. The results show significant performance differences between the models: more powerful LLMs achieve success rates of around 75% after several iterations and benefit greatly from compiler feedback, while smaller models perform significantly weaker. Overall, the study highlights the high potential of powerful LLMs for ABAP development processes, especially in iterative error correction.

