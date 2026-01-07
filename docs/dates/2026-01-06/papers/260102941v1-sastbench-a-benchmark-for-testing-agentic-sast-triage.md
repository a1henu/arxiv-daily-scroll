---
layout: default
title: SastBench: A Benchmark for Testing Agentic SAST Triage
---

# SastBench: A Benchmark for Testing Agentic SAST Triage
**arXiv**：[2601.02941v1](https://arxiv.org/abs/2601.02941) · [PDF](https://arxiv.org/pdf/2601.02941.pdf)  
**作者**：Jake Feiglin, Guy Dar  

**一句话要点**：提出SastBench基准以评估SAST分类代理在真实分布下的性能

**关键词**：静态应用安全测试, 基准测试, 误报分类, 大语言模型代理, 网络安全自动化, 数据集分析

## 3 点简述
- 核心问题：SAST工具产生大量误报，现有基准无法模拟真实SAST发现分布
- 方法要点：结合真实CVE作为真阳性和过滤SAST发现作为近似误报，设计代理无关基准
- 实验或效果：评估不同代理性能，提供数据集分析和未来开发启示

## 摘要（原文）

> SAST (Static Application Security Testing) tools are among the most widely used techniques in defensive cybersecurity, employed by commercial and non-commercial organizations to identify potential vulnerabilities in software. Despite their great utility, they generate numerous false positives, requiring costly manual filtering (aka triage). While LLM-powered agents show promise for automating cybersecurity tasks, existing benchmarks fail to emulate real-world SAST finding distributions. We introduce SastBench, a benchmark for evaluating SAST triage agents that combines real CVEs as true positives with filtered SAST tool findings as approximate false positives. SastBench features an agent-agnostic design. We evaluate different agents on the benchmark and present a comparative analysis of their performance, provide a detailed analysis of the dataset, and discuss the implications for future development.

