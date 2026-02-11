---
layout: default
title: Biases in the Blind Spot: Detecting What LLMs Fail to Mention
---

# Biases in the Blind Spot: Detecting What LLMs Fail to Mention
**arXiv**：[2602.10117v1](https://arxiv.org/abs/2602.10117) · [PDF](https://arxiv.org/pdf/2602.10117.pdf)  
**作者**：Iván Arcuschin, David Chanin, Adrià Garriga-Alonso, Oana-Maria Camburu  

**一句话要点**：提出自动化黑盒管道以检测LLMs在特定任务中的未言明偏见

**关键词**：未言明偏见检测, 链式思维推理, 自动化评估, 统计测试, 任务特定偏见, 黑盒方法

## 3 点简述
- 核心问题：LLMs的链式思维推理可能隐藏未言明偏见，使基于声明的监控不可靠
- 方法要点：使用LLM自动评估器生成候选偏见概念，通过统计测试和早期停止验证
- 实验或效果：在六个LLMs上评估三个决策任务，自动发现新偏见并验证已知偏见

## 摘要（原文）

> Large Language Models (LLMs) often provide chain-of-thought (CoT) reasoning traces that appear plausible, but may hide internal biases. We call these *unverbalized biases*. Monitoring models via their stated reasoning is therefore unreliable, and existing bias evaluations typically require predefined categories and hand-crafted datasets. In this work, we introduce a fully automated, black-box pipeline for detecting task-specific unverbalized biases. Given a task dataset, the pipeline uses LLM autoraters to generate candidate bias concepts. It then tests each concept on progressively larger input samples by generating positive and negative variations, and applies statistical techniques for multiple testing and early stopping. A concept is flagged as an unverbalized bias if it yields statistically significant performance differences while not being cited as justification in the model's CoTs. We evaluate our pipeline across six LLMs on three decision tasks (hiring, loan approval, and university admissions). Our technique automatically discovers previously unknown biases in these models (e.g., Spanish fluency, English proficiency, writing formality). In the same run, the pipeline also validates biases that were manually identified by prior work (gender, race, religion, ethnicity). More broadly, our proposed approach provides a practical, scalable path to automatic task-specific bias discovery.

