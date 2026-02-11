---
layout: default
title: GHS-TDA: A Synergistic Reasoning Framework Integrating Global Hypothesis Space with Topological Data Analysis
---

# GHS-TDA: A Synergistic Reasoning Framework Integrating Global Hypothesis Space with Topological Data Analysis
**arXiv**：[2602.09794v1](https://arxiv.org/abs/2602.09794) · [PDF](https://arxiv.org/pdf/2602.09794.pdf)  
**作者**：Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, Xudong Wang, Zhenzhen Huang, Pengcheng Zheng, Shuai Yuan, Sheng Zheng, Qigan Sun, Jie Zou, Lik-Hang Lee, Yang Yang  

**一句话要点**：提出GHS-TDA框架，通过全局假设图与拓扑数据分析提升大语言模型推理的准确性与鲁棒性

**关键词**：思维链推理, 全局假设空间, 拓扑数据分析, 大语言模型, 推理鲁棒性

## 3 点简述
- 针对现有思维链方法易受早期错误传播且缺乏全局修正机制的问题
- 构建全局假设图协调多候选推理路径，并应用拓扑数据分析提取稳定推理骨架
- 在多个推理基准测试中，GHS-TDA在准确性和鲁棒性上优于基线方法

## 摘要（原文）

> Chain-of-Thought (CoT) has been shown to significantly improve the reasoning accuracy of large language models (LLMs) on complex tasks. However, due to the autoregressive, step-by-step generation paradigm, existing CoT methods suffer from two fundamental limitations. First, the reasoning process is highly sensitive to early decisions: once an initial error is introduced, it tends to propagate and amplify through subsequent steps, while the lack of a global coordination and revision mechanism makes such errors difficult to correct, ultimately leading to distorted reasoning chains. Second, current CoT approaches lack structured analysis techniques for filtering redundant reasoning and extracting key reasoning features, resulting in unstable reasoning processes and limited interpretability. To address these issues, we propose GHS-TDA. GHS-TDA first constructs a semantically enriched global hypothesis graph to aggregate, align, and coordinate multiple candidate reasoning paths, thereby providing alternative global correction routes when local reasoning fails. It then applies topological data analysis based on persistent homology to capture stable multi-scale structures, remove redundancy and inconsistencies, and extract a more reliable reasoning skeleton. By jointly leveraging reasoning diversity and topological stability, GHS-TDA achieves self-adaptive convergence, produces high-confidence and interpretable reasoning paths, and consistently outperforms strong baselines in terms of both accuracy and robustness across multiple reasoning benchmarks.

