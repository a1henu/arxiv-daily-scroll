---
layout: default
title: Towards Green AI: Decoding the Energy of LLM Inference in Software Development
---

# Towards Green AI: Decoding the Energy of LLM Inference in Software Development
**arXiv**：[2602.05712v1](https://arxiv.org/abs/2602.05712) · [PDF](https://arxiv.org/pdf/2602.05712.pdf)  
**作者**：Lola Solovyeva, Fernando Castor  

**一句话要点**：分析LLM推理能耗阶段并提出抑制冗余输出以降低软件开发中AI工具能耗

**关键词**：LLM推理能耗, 绿色AI, 代码生成, 能耗分析, 冗余输出抑制

## 3 点简述
- 核心问题：LLM推理在软件开发中能耗高，需可持续解决方案
- 方法要点：区分预填充和解码阶段，分析能耗模式及冗余输出影响
- 实验或效果：在代码基准测试中，抑制冗余输出可节省44%至89%能耗

## 摘要（原文）

> Context: AI-assisted tools are increasingly integrated into software development workflows, but their reliance on large language models (LLMs) introduces substantial computational and energy costs. Understanding and reducing the energy footprint of LLM inference is therefore essential for sustainable software development. Objective: In this study, we conduct a phase-level analysis of LLM inference energy consumption, distinguishing between the (1) prefill, where the model processes the input and builds internal representations, and (2) decoding, where output tokens are generated using the stored state. Method: We investigate six 6B-7B and four 3B-4B transformer-based models, evaluating them on code-centric benchmarks HumanEval for code generation and LongBench for code understanding. Results: Our findings show that, within both parameter groups, models exhibit distinct energy patterns across phases. Furthermore, we observed that increases in prefill cost amplify the energy cost per token during decoding, with amplifications ranging from 1.3% to 51.8% depending on the model. Lastly, three out of ten models demonstrate babbling behavior, adding excessive content to the output that unnecessarily inflates energy consumption. We implemented babbling suppression for code generation, achieving energy savings ranging from 44% to 89% without affecting generation accuracy. Conclusion: These findings show that prefill costs influence decoding, which dominates energy consumption, and that babbling suppression can yield up to 89% energy savings. Reducing inference energy therefore requires both mitigating babbling behavior and limiting impact of prefill on decoding.

