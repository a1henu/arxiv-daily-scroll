---
layout: default
title: Pipeline for Verifying LLM-Generated Mathematical Solutions
---

# Pipeline for Verifying LLM-Generated Mathematical Solutions
**arXiv**：[2602.20770v1](https://arxiv.org/abs/2602.20770) · [PDF](https://arxiv.org/pdf/2602.20770.pdf)  
**作者**：Varvara Sazonova, Dmitri Shmelkin, Stanislav Kikot, Vasily Motolygin  

**一句话要点**：提出自动与交互式验证管道，以更准确评估大语言模型数学解题能力。

**关键词**：数学解题验证, 大语言模型评估, 证明助手, 自动验证管道, 交互式验证

## 3 点简述
- 核心问题：现有基准仅检查答案，难以准确衡量大语言模型数学推理能力。
- 方法要点：通过提示获取特定形式解，便于使用证明助手和小模型进行验证。
- 实验或效果：在多个数据集上实验显示假阳性概率低，提供开源实现。

## 摘要（原文）

> With the growing popularity of Large Reasoning Models and their results in solving mathematical problems, it becomes crucial to measure their capabilities. We introduce a pipeline for both automatic and interactive verification as a more accurate alternative to only checking the answer which is currently the most popular approach for benchmarks. The pipeline can also be used as a generator of correct solutions both in formal and informal languages. 3 AI agents, which can be chosen for the benchmark accordingly, are included in the structure. The key idea is the use of prompts to obtain the solution in the specific form which allows for easier verification using proof assistants and possible use of small models ($\le 8B$). Experiments on several datasets suggest low probability of False Positives. The open-source implementation with instructions on setting up a server is available at https://github.com/LogicEnj/lean4_verification_pipeline.

