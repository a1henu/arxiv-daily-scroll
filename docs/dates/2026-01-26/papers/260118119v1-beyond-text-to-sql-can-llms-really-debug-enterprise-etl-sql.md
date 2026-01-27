---
layout: default
title: Beyond Text-to-SQL: Can LLMs Really Debug Enterprise ETL SQL?
---

# Beyond Text-to-SQL: Can LLMs Really Debug Enterprise ETL SQL?
**arXiv**：[2601.18119v1](https://arxiv.org/abs/2601.18119) · [PDF](https://arxiv.org/pdf/2601.18119.pdf)  
**作者**：Jing Ye, Yiwen Duan, Yonghong Yu, Victor Ma, Yang Gao, Xing Chen  

**一句话要点**：提出OurBench基准以评估企业级SQL调试能力，揭示LLMs性能差距。

**关键词**：SQL调试, 企业数据工程, LLMs评估, 基准构建, 语义错误, 语法错误

## 3 点简述
- 核心问题：企业SQL代码生成常需多次调试，现有LLMs难以一次生成完全正确代码。
- 方法要点：通过逆向工程自动注入真实错误，构建大规模、多样化的SQL调试基准。
- 实验或效果：评估近30个LLMs，最佳模型准确率仅约36%，多数低于20%。

## 摘要（原文）

> SQL is central to enterprise data engineering, yet generating fully correct SQL code in a single attempt remains difficult, even for experienced developers and advanced text-to-SQL LLMs, often requiring multiple debugging iterations. We introduce OurBench, the first benchmark for enterprise-level SQL reasoning and debugging. Our benchmark is built on two key innovations: (1) an automated construction workflow that uses reverse engineering to systematically inject realistic bugs into large-scale SQL code, enabling scalable and diverse benchmark generation; and (2) an execution-free evaluation framework tailored to enterprise settings, providing fast, accurate, and resource-efficient assessment.
>   OurBench comprises 469 OurBenchSyn queries featuring syntax errors with explicit error messages, and 516 OurBenchSem queries targeting semantic errors in which the code fails to meet user intent. The queries are highly complex, averaging over 140 lines and featuring deep and wide abstract syntax trees.
>   Evaluation of nearly 30 LLMs reveals a substantial performance gap: the best-performing model, Claude-4-Sonnet, achieves only 36.46 percent accuracy on OurBenchSyn and 32.17 percent on OurBenchSem, while most models score below 20 percent. We further explore four solution strategies, identify key challenges, and outline promising directions for enterprise SQL debugging with LLMs.

