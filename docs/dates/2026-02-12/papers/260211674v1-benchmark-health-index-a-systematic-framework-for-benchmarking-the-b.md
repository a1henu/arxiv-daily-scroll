---
layout: default
title: Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs
---

# Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs
**arXiv**：[2602.11674v1](https://arxiv.org/abs/2602.11674) · [PDF](https://arxiv.org/pdf/2602.11674.pdf)  
**作者**：Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao  

**一句话要点**：提出基准健康指数以量化大语言模型基准的可靠性，支持动态评估管理。

**关键词**：基准评估, 大语言模型, 数据驱动框架, 能力区分, 抗饱和性, 影响力量化

## 3 点简述
- 核心问题：大语言模型基准存在分数膨胀和选择性报告，导致评估结果不可信。
- 方法要点：基于数据驱动框架，从能力区分、抗饱和性和影响力三个维度审计基准。
- 实验或效果：分析2025年91个代表模型的106个基准，系统刻画评估现状。

## 摘要（原文）

> Large Language Models (LLMs) are advancing rapidly, yet the benchmarks used to measure this progress are becoming increasingly unreliable. Score inflation and selective reporting have eroded the authority of standard benchmarks, leaving the community uncertain about which evaluation results remain trustworthy. We introduce the Benchmark Health Index (BHI), a pure data-driven framework for auditing evaluation sets along three orthogonal and complementary axes: (1) Capability Discrimination, measuring how sharply a benchmark separates model performance beyond noise; (2) Anti-Saturation, estimating remaining headroom before ceiling effects erode resolution and thus the benchmark's expected longevity; and (3) Impact, quantifying influence across academic and industrial ecosystems via adoption breadth and practice-shaping power. By distilling 106 validated benchmarks from the technical reports of 91 representative models in 2025, we systematically characterize the evaluation landscape. BHI is the first framework to quantify benchmark health at a macro level, providing a principled basis for benchmark selection and enabling dynamic lifecycle management for next-generation evaluation protocols.

