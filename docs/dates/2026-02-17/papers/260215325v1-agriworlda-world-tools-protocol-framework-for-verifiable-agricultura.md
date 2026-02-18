---
layout: default
title: AgriWorld:A World Tools Protocol Framework for Verifiable Agricultural Reasoning with Code-Executing LLM Agents
---

# AgriWorld:A World Tools Protocol Framework for Verifiable Agricultural Reasoning with Code-Executing LLM Agents
**arXiv**：[2602.15325v1](https://arxiv.org/abs/2602.15325) · [PDF](https://arxiv.org/pdf/2602.15325.pdf)  
**作者**：Zhixing Zhang, Jesen Zhang, Hao Liu, Qinhan Lv, Jing Yang, Kaitong Cai, Keze Wang  

**一句话要点**：提出AgriWorld框架，通过代码执行LLM代理实现可验证的农业推理，以解决农业模型缺乏语言交互能力的问题。

**关键词**：农业推理框架, 代码执行LLM代理, 地理空间查询, 遥感时间序列分析, 作物生长模拟, 可验证分析

## 3 点简述
- 核心问题：农业基础模型缺乏语言推理和交互能力，限制其在真实农艺工作流中的应用。
- 方法要点：设计AgriWorld环境提供统一工具，并开发Agro-Reflective代理通过执行-观察-精炼循环进行多轮代码编写与分析。
- 实验或效果：在AgroBench基准上超越纯文本和直接工具使用基线，验证执行驱动反思对可靠农业推理的有效性。

## 摘要（原文）

> Foundation models for agriculture are increasingly trained on massive spatiotemporal data (e.g., multi-spectral remote sensing, soil grids, and field-level management logs) and achieve strong performance on forecasting and monitoring. However, these models lack language-based reasoning and interactive capabilities, limiting their usefulness in real-world agronomic workflows. Meanwhile, large language models (LLMs) excel at interpreting and generating text, but cannot directly reason over high-dimensional, heterogeneous agricultural datasets. We bridge this gap with an agentic framework for agricultural science. It provides a Python execution environment, AgriWorld, exposing unified tools for geospatial queries over field parcels, remote-sensing time-series analytics, crop growth simulation, and task-specific predictors (e.g., yield, stress, and disease risk). On top of this environment, we design a multi-turn LLM agent, Agro-Reflective, that iteratively writes code, observes execution results, and refines its analysis via an execute-observe-refine loop. We introduce AgroBench, with scalable data generation for diverse agricultural QA spanning lookups, forecasting, anomaly detection, and counterfactual "what-if" analysis. Experiments outperform text-only and direct tool-use baselines, validating execution-driven reflection for reliable agricultural reasoning.

