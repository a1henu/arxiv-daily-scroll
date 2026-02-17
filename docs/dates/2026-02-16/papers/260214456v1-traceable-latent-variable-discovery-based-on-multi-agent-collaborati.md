---
layout: default
title: Traceable Latent Variable Discovery Based on Multi-Agent Collaboration
---

# Traceable Latent Variable Discovery Based on Multi-Agent Collaboration
**arXiv**：[2602.14456v1](https://arxiv.org/abs/2602.14456) · [PDF](https://arxiv.org/pdf/2602.14456.pdf)  
**作者**：Huaming Du, Tao Hu, Yijie Huang, Yu Zhao, Guisong Liu, Tao Gu, Gang Kou, Carl Yang  

**一句话要点**：提出TLVD框架，结合LLM与TCDA解决因果发现中隐变量推断与语义解释难题

**关键词**：因果发现, 隐变量推断, 大语言模型, 多智能体协作, 贝叶斯纳什均衡, 可追溯性验证

## 3 点简述
- 核心问题：传统因果发现算法依赖无隐变量假设且忽视隐变量语义，数据质量不足限制应用
- 方法要点：先构建含隐变量的因果图，再通过多LLM协作建模为不完全信息博弈，求贝叶斯纳什均衡推断隐变量
- 实验或效果：在三个真实患者数据集和两个基准数据集上验证，平均Acc提升32.67%，CAcc提升62.21%

## 摘要（原文）

> Revealing the underlying causal mechanisms in the real world is crucial for scientific and technological progress. Despite notable advances in recent decades, the lack of high-quality data and the reliance of traditional causal discovery algorithms (TCDA) on the assumption of no latent confounders, as well as their tendency to overlook the precise semantics of latent variables, have long been major obstacles to the broader application of causal discovery. To address this issue, we propose a novel causal modeling framework, TLVD, which integrates the metadata-based reasoning capabilities of large language models (LLMs) with the data-driven modeling capabilities of TCDA for inferring latent variables and their semantics. Specifically, we first employ a data-driven approach to construct a causal graph that incorporates latent variables. Then, we employ multi-LLM collaboration for latent variable inference, modeling this process as a game with incomplete information and seeking its Bayesian Nash Equilibrium (BNE) to infer the possible specific latent variables. Finally, to validate the inferred latent variables across multiple real-world web-based data sources, we leverage LLMs for evidence exploration to ensure traceability. We comprehensively evaluate TLVD on three de-identified real patient datasets provided by a hospital and two benchmark datasets. Extensive experimental results confirm the effectiveness and reliability of TLVD, with average improvements of 32.67% in Acc, 62.21% in CAcc, and 26.72% in ECit across the five datasets.

