---
layout: default
title: Evaluating LLMs for One-Shot Patching of Real and Artificial Vulnerabilities
---

# Evaluating LLMs for One-Shot Patching of Real and Artificial Vulnerabilities
**arXiv**：[2511.23408v1](https://arxiv.org/abs/2511.23408) · [PDF](https://arxiv.org/pdf/2511.23408.pdf)  
**作者**：Aayush Garg, Zanis Ali Khan, Renzo Degiovanni, Qiang Tang  

**一句话要点**：评估大语言模型在真实与人工漏洞单次补丁生成中的效果与互补性

**关键词**：漏洞自动补丁, 大语言模型评估, PoV测试执行, 模型互补性, 软件安全

## 3 点简述
- 核心问题：现有研究主要基于公开漏洞评估LLMs，对人工漏洞的补丁效果未知
- 方法要点：使用PoV测试执行评估GPT、LLaMA等模型在真实与人工漏洞上的补丁成功率
- 实验或效果：LLMs对真实漏洞补丁更有效，不同模型在重叠与互补性上差异显著

## 摘要（原文）

> Automated vulnerability patching is crucial for software security, and recent advancements in Large Language Models (LLMs) present promising capabilities for automating this task. However, existing research has primarily assessed LLMs using publicly disclosed vulnerabilities, leaving their effectiveness on related artificial vulnerabilities largely unexplored. In this study, we empirically evaluate the patching effectiveness and complementarity of several prominent LLMs, such as OpenAI's GPT variants, LLaMA, DeepSeek, and Mistral models, using both real and artificial vulnerabilities. Our evaluation employs Proof-of-Vulnerability (PoV) test execution to concretely assess whether LLM-generated source code successfully patches vulnerabilities. Our results reveal that LLMs patch real vulnerabilities more effectively compared to artificial ones. Additionally, our analysis reveals significant variability across LLMs in terms of overlapping (multiple LLMs patching the same vulnerabilities) and complementarity (vulnerabilities patched exclusively by a single LLM), emphasizing the importance of selecting appropriate LLMs for effective vulnerability patching.

