---
layout: default
title: MirrorBench: An Extensible Framework to Evaluate User-Proxy Agents for Human-Likeness
---

# MirrorBench: An Extensible Framework to Evaluate User-Proxy Agents for Human-Likeness
**arXiv**：[2601.08118v1](https://arxiv.org/abs/2601.08118) · [PDF](https://arxiv.org/pdf/2601.08118.pdf)  
**作者**：Ashutosh Hathidara, Julien Yu, Vaishali Senthil, Sebastian Schreiber, Anil Babu Ankisettipalli  

**一句话要点**：提出MirrorBench框架以评估用户代理的人类相似性，解耦下游任务成功。

**关键词**：用户代理评估, 人类相似性度量, 模块化基准框架, LLM模拟器, 对话系统评估

## 3 点简述
- 核心问题：LLM作为人类模拟器时，简单提示导致不真实话语，需评估用户代理的人类相似性。
- 方法要点：模块化框架支持可插拔代理、数据集和指标，提供方差感知评估和多种度量标准。
- 实验或效果：在四个开放数据集上揭示用户代理与真实用户间的系统性差距，框架开源且可扩展。

## 摘要（原文）

> Large language models (LLMs) are increasingly used as human simulators, both for evaluating conversational systems and for generating fine-tuning data. However, naive "act-as-a-user" prompting often yields verbose, unrealistic utterances, underscoring the need for principled evaluation of so-called user proxy agents. We present MIRRORBENCH, a reproducible, extensible benchmarking framework that evaluates user proxies solely on their ability to produce human-like user utterances across diverse conversational tasks, explicitly decoupled from downstream task success. MIRRORBENCH features a modular execution engine with typed interfaces, metadata-driven registries, multi-backend support, caching, and robust observability. The system supports pluggable user proxies, datasets, tasks, and metrics, enabling researchers to evaluate arbitrary simulators under a uniform, variance-aware harness. We include three lexical-diversity metrics (MATTR, YULE'S K, and HD-D) and three LLM-judge-based metrics (GTEval, Pairwise Indistinguishability, and Rubric-and-Reason). Across four open datasets, MIRRORBENCH yields variance-aware results and reveals systematic gaps between user proxies and real human users. The framework is open source and includes a simple command-line interface for running experiments, managing configurations and caching, and generating reports. The framework can be accessed at https://github.com/SAP/mirrorbench.

