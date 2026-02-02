---
layout: default
title: MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering
---

# MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering
**arXiv**：[2601.22859v1](https://arxiv.org/abs/2601.22859) · [PDF](https://arxiv.org/pdf/2601.22859.pdf)  
**作者**：Chuanzhe Guo, Jingjing Wu, Sijun He, Yang Chen, Zhaoqi Kuang, Shilong Fan, Bingjin Chen, Siqi Bao, Jing Liu, Hua Wu, Qingfu Zhu, Wanxiang Che, Haifeng Wang  

**一句话要点**：提出MEnvAgent框架以解决多语言可执行环境构建难题，支持可验证软件工程任务生成。

**关键词**：多语言环境构建, 可验证软件工程, LLM代理, Docker环境, 任务实例生成

## 3 点简述
- 核心问题：LLM软件工程代理因多语言可执行环境构建复杂，缺乏可验证数据集。
- 方法要点：采用多智能体规划-执行-验证架构，集成环境复用机制以降低计算开销。
- 实验效果：在10语言1000任务基准上，失败转成功率提升8.6%，时间成本降低43%。

## 摘要（原文）

> The evolution of Large Language Model (LLM) agents for software engineering (SWE) is constrained by the scarcity of verifiable datasets, a bottleneck stemming from the complexity of constructing executable environments across diverse languages. To address this, we introduce MEnvAgent, a Multi-language framework for automated Environment construction that facilitates scalable generation of verifiable task instances. MEnvAgent employs a multi-agent Planning-Execution-Verification architecture to autonomously resolve construction failures and integrates a novel Environment Reuse Mechanism that reduces computational overhead by incrementally patching historical environments. Evaluations on MEnvBench, a new benchmark comprising 1,000 tasks across 10 languages, demonstrate that MEnvAgent outperforms baselines, improving Fail-to-Pass (F2P) rates by 8.6% while reducing time costs by 43%. Additionally, we demonstrate the utility of MEnvAgent by constructing MEnvData-SWE, the largest open-source polyglot dataset of realistic verifiable Docker environments to date, alongside solution trajectories that enable consistent performance gains on SWE tasks across a wide range of models. Our code, benchmark, and dataset are available at https://github.com/ernie-research/MEnvAgent.

