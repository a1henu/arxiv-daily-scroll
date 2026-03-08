---
layout: default
title: Judge Reliability Harness: Stress Testing the Reliability of LLM Judges
---

# Judge Reliability Harness: Stress Testing the Reliability of LLM Judges
**arXiv**：[2603.05399v1](https://arxiv.org/abs/2603.05399) · [PDF](https://arxiv.org/pdf/2603.05399.pdf)  
**作者**：Sunishchal Dev, Andrew Sloan, Joshua Kavner, Nicholas Kong, Morgan Sandler  

**一句话要点**：提出Judge Reliability Harness以测试LLM法官在AI基准中的可靠性

**关键词**：LLM法官, 可靠性测试, AI基准, 开源工具, 扰动分析

## 3 点简述
- 核心问题：LLM评分在AI基准中广泛应用，但缺乏工具评估其可靠性。
- 方法要点：开源库构建验证套件，测试二元判断准确性和序数分级性能。
- 实验或效果：评估四个先进法官，发现性能因模型和扰动类型而异，无法官在所有基准中一致可靠。

## 摘要（原文）

> We present the Judge Reliability Harness, an open source library for constructing validation suites that test the reliability of LLM judges. As LLM based scoring is widely deployed in AI benchmarks, more tooling is needed to efficiently assess the reliability of these methods. Given a benchmark dataset and an LLM judge configuration, the harness generates reliability tests that evaluate both binary judgment accuracy and ordinal grading performance for free-response and agentic task formats. We evaluate four state-of-the-art judges across four benchmarks spanning safety, persuasion, misuse, and agentic behavior, and find meaningful variation in performance across models and perturbation types, highlighting opportunities to improve the robustness of LLM judges. No judge that we evaluated is uniformly reliable across benchmarks using our harness. For example, our preliminary experiments on judges revealed consistency issues as measured by accuracy in judging another LLM's ability to complete a task due to simple text formatting changes, paraphrasing, changes in verbosity, and flipping the ground truth label in LLM-produced responses. The code for this tool is available at: https://github.com/RANDCorporation/judge-reliability-harness

