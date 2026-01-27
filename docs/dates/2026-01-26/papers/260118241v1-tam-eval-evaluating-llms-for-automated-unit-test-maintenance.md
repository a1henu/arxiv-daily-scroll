---
layout: default
title: TAM-Eval: Evaluating LLMs for Automated Unit Test Maintenance
---

# TAM-Eval: Evaluating LLMs for Automated Unit Test Maintenance
**arXiv**：[2601.18241v1](https://arxiv.org/abs/2601.18241) · [PDF](https://arxiv.org/pdf/2601.18241.pdf)  
**作者**：Elena Bruches, Vadim Alperovich, Dari Baturova, Roman Derunets, Daniil Grebenkin, Georgy Mkrtchyan, Oleg Sedukhin, Mikhail Klementev, Ivan Bondarenko, Nikolay Bushkov, Stanislav Moiseev  

**一句话要点**：提出TAM-Eval框架以评估大语言模型在单元测试维护中的性能

**关键词**：单元测试维护, 大语言模型评估, 软件工程基准, 测试套件自动化, 代码覆盖率, 突变测试

## 3 点简述
- 核心问题：现有研究忽视测试套件维护，局限于孤立测试生成或预言预测
- 方法要点：基于测试文件级场景，支持创建、修复和更新三种维护任务的评估
- 实验或效果：实证显示先进大语言模型在真实测试维护中能力有限，效果提升微小

## 摘要（原文）

> While Large Language Models (LLMs) have shown promise in software engineering, their application to unit testing remains largely confined to isolated test generation or oracle prediction, neglecting the broader challenge of test suite maintenance. We introduce TAM-Eval (Test Automated Maintenance Evaluation), a framework and benchmark designed to evaluate model performance across three core test maintenance scenarios: creation, repair, and updating of test suites. Unlike prior work limited to function-level tasks, TAM-Eval operates at the test file level, while maintaining access to full repository context during isolated evaluation, better reflecting real-world maintenance workflows. Our benchmark comprises 1,539 automatically extracted and validated scenarios from Python, Java, and Go projects. TAM-Eval supports system-agnostic evaluation of both raw LLMs and agentic workflows, using a reference-free protocol based on test suite pass rate, code coverage, and mutation testing. Empirical results indicate that state-of-the-art LLMs have limited capabilities in realistic test maintenance processes and yield only marginal improvements in test effectiveness. We release TAM-Eval as an open-source framework to support future research in automated software testing. Our data and code are publicly available at https://github.com/trndcenter/TAM-Eval.

