---
layout: default
title: PatientHub: A Unified Framework for Patient Simulation
---

# PatientHub: A Unified Framework for Patient Simulation
**arXiv**：[2602.11684v1](https://arxiv.org/abs/2602.11684) · [PDF](https://arxiv.org/pdf/2602.11684.pdf)  
**作者**：Sahand Sabour, TszYam NG, Minlie Huang  

**一句话要点**：提出PatientHub统一框架以标准化患者模拟，支持方法开发和评估

**关键词**：患者模拟, 统一框架, 标准化评估, 角色扮演应用, 大语言模型, 对话系统

## 3 点简述
- 核心问题：现有患者模拟方法数据格式、提示和评估指标不兼容，阻碍可复现性和公平比较。
- 方法要点：PatientHub提供模块化框架，标准化模拟患者的定义、组合和部署，支持自定义评估指标。
- 实验或效果：通过案例研究实现多种模拟方法，展示标准化跨方法评估和加速新方法开发。

## 摘要（原文）

> As Large Language Models increasingly power role-playing applications, simulating patients has become a valuable tool for training counselors and scaling therapeutic assessment. However, prior work is fragmented: existing approaches rely on incompatible, non-standardized data formats, prompts, and evaluation metrics, hindering reproducibility and fair comparison. In this paper, we introduce PatientHub, a unified and modular framework that standardizes the definition, composition, and deployment of simulated patients. To demonstrate PatientHub's utility, we implement several representative patient simulation methods as case studies, showcasing how our framework supports standardized cross-method evaluation and the seamless integration of custom evaluation metrics. We further demonstrate PatientHub's extensibility by prototyping two new simulator variants, highlighting how PatientHub accelerates method development by eliminating infrastructure overhead. By consolidating existing work into a single reproducible pipeline, PatientHub lowers the barrier to developing new simulation methods and facilitates cross-method and cross-model benchmarking. Our framework provides a practical foundation for future datasets, methods, and benchmarks in patient-centered dialogue, and the code is publicly available via https://github.com/Sahandfer/PatientHub.

