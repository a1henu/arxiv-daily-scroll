---
layout: default
title: TempPerturb-Eval: On the Joint Effects of Internal Temperature and External Perturbations in RAG Robustness
---

# TempPerturb-Eval: On the Joint Effects of Internal Temperature and External Perturbations in RAG Robustness
**arXiv**：[2512.01183v1](https://arxiv.org/abs/2512.01183) · [PDF](https://arxiv.org/pdf/2512.01183.pdf)  
**作者**：Yongxin Zhou, Philippe Mulhem, Didier Schwab  

**一句话要点**：提出RAG扰动-温度分析框架以评估检索增强生成系统在噪声检索下的鲁棒性

**关键词**：检索增强生成, 鲁棒性评估, 温度参数, 文本扰动, 模型选择指南

## 3 点简述
- 核心问题：现有RAG评估孤立考察检索质量和温度参数，忽略其交互影响。
- 方法要点：设计框架，结合文本扰动和温度设置，分析多轮LLM运行中的交互效应。
- 实验或效果：在HotpotQA上实验显示，高温放大扰动脆弱性，某些扰动类型对温度敏感度非线性。

## 摘要（原文）

> The evaluation of Retrieval-Augmented Generation (RAG) systems typically examines retrieval quality and generation parameters like temperature in isolation, overlooking their interaction. This work presents a systematic investigation of how text perturbations (simulating noisy retrieval) interact with temperature settings across multiple LLM runs. We propose a comprehensive RAG Perturbation-Temperature Analysis Framework that subjects retrieved documents to three distinct perturbation types across varying temperature settings. Through extensive experiments on HotpotQA with both open-source and proprietary LLMs, we demonstrate that performance degradation follows distinct patterns: high-temperature settings consistently amplify vulnerability to perturbations, while certain perturbation types exhibit non-linear sensitivity across the temperature range. Our work yields three key contributions: (1) a diagnostic benchmark for assessing RAG robustness, (2) an analytical framework for quantifying perturbation-temperature interactions, and (3) practical guidelines for model selection and parameter tuning under noisy retrieval conditions.

