---
layout: default
title: AutoAdapt: An Automated Domain Adaptation Framework for LLMs
---

# AutoAdapt: An Automated Domain Adaptation Framework for LLMs
**arXiv**：[2603.08181v1](https://arxiv.org/abs/2603.08181) · [PDF](https://arxiv.org/pdf/2603.08181.pdf)  
**作者**：Sidharth Sinha, Anson Bastos, Xuchao Zhang, Akshay Nambi, Chetan Bansal, Saravan Rajmohan  

**一句话要点**：提出AutoAdapt自动化框架以解决大语言模型在专业领域适应中的高成本与不确定性

**关键词**：大语言模型, 领域适应, 自动化框架, 超参数优化, 多代理系统, 知识库集成

## 3 点简述
- 核心问题：大语言模型在数据有限、知识演化的专业领域适应依赖手动试错，超参数复杂且效果不确定
- 方法要点：利用知识库减少专家干预，设计多代理辩论系统对齐用户意图，并基于LLM代理优化超参数
- 实验或效果：在10个任务上，相比自动化机器学习基线，平均相对准确率提升25%，开销最小

## 摘要（原文）

> Large language models (LLMs) excel in open domains but struggle in specialized settings with limited data and evolving knowledge. Existing domain adaptation practices rely heavily on manual trial-and-error processes, incur significant hyperparameter complexity, and are highly sensitive to data and user preferences, all under the high cost of LLM training. Moreover, the interactions and transferability of hyperparameter choices across models/domains remain poorly understood, making adaptation gains uncertain even with substantial effort. To solve these challenges, we present AutoAdapt, a novel end-to-end automated framework for efficient and reliable LLM domain adaptation. AutoAdapt leverages curated knowledge bases from literature and open-source resources to reduce expert intervention. To narrow the search space, we design a novel multi-agent debating system in which proposal and critic agents iteratively interact to align user intent and incorporate data signals and best practices into the planning process. To optimize hyperparameters under tight budgets, we propose AutoRefine, a novel LLM-based surrogate that replaces costly black-box search. Across 10 tasks, AutoAdapt achieves a 25% average relative accuracy improvement over state-of-the-art Automated Machine Learning baselines with minimal overhead.

