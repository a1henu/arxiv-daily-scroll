---
layout: default
title: MiroFlow: Towards High-Performance and Robust Open-Source Agent Framework for General Deep Research Tasks
---

# MiroFlow: Towards High-Performance and Robust Open-Source Agent Framework for General Deep Research Tasks
**arXiv**：[2602.22808v1](https://arxiv.org/abs/2602.22808) · [PDF](https://arxiv.org/pdf/2602.22808.pdf)  
**作者**：Shiqian Su, Sen Xing, Xuan Dong, Muyan Zhong, Bin Wang, Xizhou Zhu, Yuntao Chen, Wenhai Wang, Yue Deng, Pengxiang Zhu, Ziyuan Liu, Tiantong Li, Jiaheng Yu, Zhe Chen, Lidong Bing, Jifeng Dai  

**一句话要点**：提出MiroFlow开源代理框架以解决复杂任务中LLM性能瓶颈和现有框架不稳定的问题

**关键词**：代理框架, 开源工具, 深度推理, 稳健工作流, 基准测试, 外部交互

## 3 点简述
- 核心问题：独立LLM在处理需外部工具交互的复杂任务时性能受限，现有代理框架工作流简单、性能不稳定且依赖商业API
- 方法要点：引入代理图实现灵活编排，可选深度推理模式提升性能，稳健工作流执行确保稳定和可复现性
- 实验或效果：在GAIA、BrowseComp-EN/ZH、HLE、xBench-DeepSearch和FutureX等多个基准测试中达到最先进性能

## 摘要（原文）

> Despite the remarkable progress of large language models (LLMs), the capabilities of standalone LLMs have begun to plateau when tackling real-world, complex tasks that require interaction with external tools and dynamic environments. Although recent agent frameworks aim to enhance model autonomy through tool integration and external interaction, they still suffer from naive workflows, unstable performance, limited support across diverse benchmarks and tasks, and heavy reliance on costly commercial APIs. In this work, we propose a high-performance and robust open-source agent framework, termed MiroFlow, which incorporates an agent graph for flexible orchestration, an optional deep reasoning mode to enhance performance, and a robust workflow execution to ensure stable and reproducible performance. Extensive experiments demonstrate that MiroFlow consistently achieves state-of-the-art performance across multiple agent benchmarks, including GAIA, BrowseComp-EN/ZH, HLE, xBench-DeepSearch, and notably FutureX. We hope it could serve as an easily accessible, reproducible, and comparable baseline for the deep research community.

