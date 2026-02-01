---
layout: default
title: SWE-Spot: Building Small Repo-Experts with Repository-Centric Learning
---

# SWE-Spot: Building Small Repo-Experts with Repository-Centric Learning
**arXiv**：[2601.21649v1](https://arxiv.org/abs/2601.21649) · [PDF](https://arxiv.org/pdf/2601.21649.pdf)  
**作者**：Jinjun Peng, Magnus Saebo, Tianjun Zhong, Yi-Jie Cheng, Junfeng Yang, Baishakhi Ray, Simin Chen, Yangruibo Ding  

**一句话要点**：提出Repository-Centric Learning以训练小型代码专家模型，解决隐私敏感和资源受限环境中的代码库适应问题。

**关键词**：小型语言模型, 代码库学习, 软件工程任务, 参数化知识获取, 推理效率

## 3 点简述
- 核心问题：小型语言模型在复杂陌生代码库上缺乏推理时强泛化能力，传统Task-Centric Learning范式不足。
- 方法要点：设计Repository-Centric Learning范式，通过Repository-Centric Experience将静态代码库转化为交互学习信号，训练repo-specialized专家模型。
- 实验或效果：SWE-Spot-4B模型在多个软件工程任务上超越更大开源模型，匹配或超越高效商业模型，训练样本效率和推理成本更低。

## 摘要（原文）

> The deployment of coding agents in privacy-sensitive and resource-constrained environments drives the demand for capable open-weight Small Language Models (SLMs). However, they suffer from a fundamental capability gap: unlike frontier large models, they lack the inference-time strong generalization to work with complicated, unfamiliar codebases. We identify that the prevailing Task-Centric Learning (TCL) paradigm, which scales exposure across disparate repositories, fails to address this limitation. In response, we propose Repository-Centric Learning (RCL), a paradigm shift that prioritizes vertical repository depth over horizontal task breadth, suggesting SLMs must internalize the "physics" of a target software environment through parametric knowledge acquisition, rather than attempting to recover it via costly inference-time search. Following this new paradigm, we design a four-unit Repository-Centric Experience, transforming static codebases into interactive learning signals, to train SWE-Spot-4B, a family of highly compact models built as repo-specialized experts that breaks established scaling trends, outperforming open-weight models up to larger (e.g., CWM by Meta, Qwen3-Coder-30B) and surpassing/matching efficiency-focused commercial models (e.g., GPT-4.1-mini, GPT-5-nano) across multiple SWE tasks. Further analysis reveals that RCL yields higher training sample efficiency and lower inference costs, emphasizing that for building efficient intelligence, repository mastery is a distinct and necessary dimension that complements general coding capability.

