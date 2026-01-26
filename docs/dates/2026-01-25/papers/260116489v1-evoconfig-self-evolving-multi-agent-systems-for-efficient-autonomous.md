---
layout: default
title: EvoConfig: Self-Evolving Multi-Agent Systems for Efficient Autonomous Environment Configuration
---

# EvoConfig: Self-Evolving Multi-Agent Systems for Efficient Autonomous Environment Configuration
**arXiv**：[2601.16489v1](https://arxiv.org/abs/2601.16489) · [PDF](https://arxiv.org/pdf/2601.16489.pdf)  
**作者**：Xinshuai Guo, Jiayi Kuang, Linyue Pan, Yinghui Li, Yangning Li, Hai-Tao Zheng, Ying Shen, Di Yin, Xing Sun  

**一句话要点**：提出EvoConfig框架以优化多智能体协作，高效构建可靠软件环境配置。

**关键词**：环境配置, 多智能体系统, 自进化机制, 错误诊断, 软件工程任务

## 3 点简述
- 核心问题：现有方法忽视智能体动作细粒度分析，难以处理复杂错误导致配置失败。
- 方法要点：引入专家诊断模块进行细粒度后执行分析，并采用自进化机制实时调整错误修复优先级。
- 实验或效果：在Envbench上达到78.1%成功率，比Repo2Run提升7.1%，并展示更强的调试能力。

## 摘要（原文）

> A reliable executable environment is the foundation for ensuring that large language models solve software engineering tasks. Due to the complex and tedious construction process, large-scale configuration is relatively inefficient. However, most methods always overlook fine-grained analysis of the actions performed by the agent, making it difficult to handle complex errors and resulting in configuration failures. To address this bottleneck, we propose EvoConfig, an efficient environment configuration framework that optimizes multi-agent collaboration to build correct runtime environments. EvoConfig features an expert diagnosis module for fine-grained post-execution analysis, and a self-evolving mechanism that lets expert agents self-feedback and dynamically adjust error-fixing priorities in real time. Empirically, EvoConfig matches the previous state-of-the-art Repo2Run on Repo2Run's 420 repositories, while delivering clear gains on harder cases: on the more challenging Envbench, EvoConfig achieves a 78.1% success rate, outperforming Repo2Run by 7.1%. Beyond end-to-end success, EvoConfig also demonstrates stronger debugging competence, achieving higher accuracy in error identification and producing more effective repair recommendations than existing methods.

