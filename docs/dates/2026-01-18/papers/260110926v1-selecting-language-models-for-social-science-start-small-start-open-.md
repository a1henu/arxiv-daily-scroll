---
layout: default
title: Selecting Language Models for Social Science: Start Small, Start Open, and Validate
---

# Selecting Language Models for Social Science: Start Small, Start Open, and Validate
**arXiv**：[2601.10926v1](https://arxiv.org/abs/2601.10926) · [PDF](https://arxiv.org/pdf/2601.10926.pdf)  
**作者**：Dustin S. Stoltz, Marshall A. Taylor, Sanuj Kumar  

**一句话要点**：提出从小型开放模型入手并构建限定基准，以提升社会科学中语言模型选择的效度与可复现性。

**关键词**：语言模型选择, 社会科学应用, 可复现性, 模型开放性, 基准测试, 计算效度

## 3 点简述
- 核心问题：社会科学中如何从数千个大型预训练语言模型中选择合适模型，基于效度、信度、可复现性和可复制性。
- 方法要点：强调模型开放性、模型规模、训练数据、架构与微调的重要性，主张优先考虑可复制性，避免过度依赖事前基准测试。
- 实验或效果：建议从小型开放模型开始，通过构建限定基准来验证整个计算流程的效度，以促进可靠的任务复现。

## 摘要（原文）

> Currently, there are thousands of large pretrained language models (LLMs) available to social scientists. How do we select among them? Using validity, reliability, reproducibility, and replicability as guides, we explore the significance of: (1) model openness, (2) model footprint, (3) training data, and (4) model architectures and fine-tuning. While ex-ante tests of validity (i.e., benchmarks) are often privileged in these discussions, we argue that social scientists cannot altogether avoid validating computational measures (ex-post). Replicability, in particular, is a more pressing guide for selecting language models. Being able to reliably replicate a particular finding that entails the use of a language model necessitates reliably reproducing a task. To this end, we propose starting with smaller, open models, and constructing delimited benchmarks to demonstrate the validity of the entire computational pipeline.

