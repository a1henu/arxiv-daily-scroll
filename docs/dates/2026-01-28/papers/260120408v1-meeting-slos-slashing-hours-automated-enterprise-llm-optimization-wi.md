---
layout: default
title: Meeting SLOs, Slashing Hours: Automated Enterprise LLM Optimization with OptiKIT
---

# Meeting SLOs, Slashing Hours: Automated Enterprise LLM Optimization with OptiKIT
**arXiv**：[2601.20408v1](https://arxiv.org/abs/2601.20408) · [PDF](https://arxiv.org/pdf/2601.20408.pdf)  
**作者**：Nicholas Santavas, Kareem Eissa, Patrycja Cieplicka, Piotr Florek, Matteo Nulli, Stefan Vasilev, Seyyed Hadi Hashemi, Antonios Gasteratos, Shahram Khadivi  

**一句话要点**：提出OptiKIT框架以自动化企业LLM优化，解决计算资源受限下的规模化部署挑战。

**关键词**：企业LLM优化, 模型压缩, 自动化工作流, GPU资源管理, 分布式框架, 开源系统

## 3 点简述
- 企业LLM部署面临计算预算约束和专家稀缺的规模化难题。
- OptiKIT通过自动化压缩与调优工作流，提供动态资源分配和管道执行。
- 在生产中实现GPU吞吐量提升超2倍，支持非专家团队高效部署模型。

## 摘要（原文）

> Enterprise LLM deployment faces a critical scalability challenge: organizations must optimize models systematically to scale AI initiatives within constrained compute budgets, yet the specialized expertise required for manual optimization remains a niche and scarce skillset. This challenge is particularly evident in managing GPU utilization across heterogeneous infrastructure while enabling teams with diverse workloads and limited LLM optimization experience to deploy models efficiently.
>   We present OptiKIT, a distributed LLM optimization framework that democratizes model compression and tuning by automating complex optimization workflows for non-expert teams. OptiKIT provides dynamic resource allocation, staged pipeline execution with automatic cleanup, and seamless enterprise integration.
>   In production, it delivers more than 2x GPU throughput improvement while empowering application teams to achieve consistent performance improvements without deep LLM optimization expertise. We share both the platform design and key engineering insights into resource allocation algorithms, pipeline orchestration, and integration patterns that enable large-scale, production-grade democratization of model optimization. Finally, we open-source the system to enable external contributions and broader reproducibility.

