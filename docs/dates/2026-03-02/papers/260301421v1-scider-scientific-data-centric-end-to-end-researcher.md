---
layout: default
title: SciDER: Scientific Data-centric End-to-end Researcher
---

# SciDER: Scientific Data-centric End-to-end Researcher
**arXiv**：[2603.01421v1](https://arxiv.org/abs/2603.01421) · [PDF](https://arxiv.org/pdf/2603.01421.pdf)  
**作者**：Ke Lin, Yilin Lu, Shreyas Bhat, Xuehang Guo, Junier Oliva, Qingyun Wang  

**一句话要点**：提出SciDER系统以自动化处理原始科学数据的研究生命周期

**关键词**：科学数据自动化, 端到端研究系统, 自主科学发现, 数据驱动代理, 模块化Python包

## 3 点简述
- 核心问题：现有AI代理难以自主处理科学实验收集的原始数据
- 方法要点：通过专门代理协作解析数据、生成假设与实验设计，并执行代码
- 实验或效果：在三个基准测试中优于通用代理和先进模型，支持自进化记忆和反馈循环

## 摘要（原文）

> Automated scientific discovery with large language models is transforming the research lifecycle from ideation to experimentation, yet existing agents struggle to autonomously process raw data collected from scientific experiments. We introduce SciDER, a data-centric end-to-end system that automates the research lifecycle. Unlike traditional frameworks, our specialized agents collaboratively parse and analyze raw scientific data, generate hypotheses and experimental designs grounded in specific data characteristics, and write and execute corresponding code. Evaluation on three benchmarks shows SciDER excels in specialized data-driven scientific discovery and outperforms general-purpose agents and state-of-the-art models through its self-evolving memory and critic-led feedback loop. Distributed as a modular Python package, we also provide easy-to-use PyPI packages with a lightweight web interface to accelerate autonomous, data-driven research and aim to be accessible to all researchers and developers.

