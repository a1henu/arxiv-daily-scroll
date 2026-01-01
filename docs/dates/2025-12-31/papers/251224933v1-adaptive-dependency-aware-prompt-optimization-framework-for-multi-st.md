---
layout: default
title: Adaptive Dependency-aware Prompt Optimization Framework for Multi-Step LLM Pipeline
---

# Adaptive Dependency-aware Prompt Optimization Framework for Multi-Step LLM Pipeline
**arXiv**：[2512.24933v1](https://arxiv.org/abs/2512.24933) · [PDF](https://arxiv.org/pdf/2512.24933.pdf)  
**作者**：Minjun Zhao, Xinyu Zhang, Shuai Zhang, Deyang Li, Ruifeng Shi  

**一句话要点**：提出ADOPT框架以优化多步LLM管道中的提示，通过依赖建模和自适应资源分配提升性能。

**关键词**：多步LLM管道, 提示优化, 依赖建模, 自适应资源分配, 文本梯度估计

## 3 点简述
- 核心问题：多步LLM管道中提示联合优化困难，缺乏步骤级监督和依赖关系。
- 方法要点：ADOPT建模步骤间依赖，估计文本梯度，并基于Shapley值自适应分配优化资源。
- 实验或效果：在真实数据集和多样管道结构上，ADOPT有效且稳健，优于现有基线方法。

## 摘要（原文）

> Multi-step LLM pipelines invoke large language models multiple times in a structured sequence and can effectively solve complex tasks, but their performance heavily depends on the prompts used at each step. Jointly optimizing these prompts is difficult due to missing step-level supervision and inter-step dependencies. Existing end-to-end prompt optimization methods struggle under these conditions and often yield suboptimal or unstable updates. We propose ADOPT, an Adaptive Dependency-aware Prompt Optimization framework for multi-step LLM pipelines. ADOPT explicitly models the dependency between each LLM step and the final task outcome, enabling precise text-gradient estimation analogous to computing analytical derivatives. It decouples textual gradient estimation from gradient updates, reducing multi-prompt optimization to flexible single-prompt optimization steps, and employs a Shapley-based mechanism to adaptively allocate optimization resources. Experiments on real-world datasets and diverse pipeline structures show that ADOPT is effective and robust, consistently outperforming state-of-the-art prompt optimization baselines.

