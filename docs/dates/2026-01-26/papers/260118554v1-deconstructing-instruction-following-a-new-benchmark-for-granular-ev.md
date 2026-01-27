---
layout: default
title: Deconstructing Instruction-Following: A New Benchmark for Granular Evaluation of Large Language Model Instruction Compliance Abilities
---

# Deconstructing Instruction-Following: A New Benchmark for Granular Evaluation of Large Language Model Instruction Compliance Abilities
**arXiv**：[2601.18554v1](https://arxiv.org/abs/2601.18554) · [PDF](https://arxiv.org/pdf/2601.18554.pdf)  
**作者**：Alberto Purpura, Li Wang, Sahil Badyal, Eugenio Beaufrand, Adam Faulkner  

**一句话要点**：提出MOSAIC框架以细粒度评估大语言模型指令遵循能力

**关键词**：指令遵循评估, 大语言模型基准, 细粒度分析, 约束交互, 模型诊断

## 3 点简述
- 现有基准难以独立评估指令遵循，常与任务成功混淆
- MOSAIC使用动态生成数据集，支持多达20个应用导向约束
- 评估揭示模型遵循能力随约束类型、数量和位置显著变化

## 摘要（原文）

> Reliably ensuring Large Language Models (LLMs) follow complex instructions is a critical challenge, as existing benchmarks often fail to reflect real-world use or isolate compliance from task success. We introduce MOSAIC (MOdular Synthetic Assessment of Instruction Compliance), a modular framework that uses a dynamically generated dataset with up to 20 application-oriented generation constraints to enable a granular and independent analysis of this capability. Our evaluation of five LLMs from different families based on this new benchmark demonstrates that compliance is not a monolithic capability but varies significantly with constraint type, quantity, and position. The analysis reveals model-specific weaknesses, uncovers synergistic and conflicting interactions between instructions, and identifies distinct positional biases such as primacy and recency effects. These granular insights are critical for diagnosing model failures and developing more reliable LLMs for systems that demand strict adherence to complex instructions.

