---
layout: default
title: One Tool Is Enough: Reinforcement Learning for Repository-Level LLM Agents
---

# One Tool Is Enough: Reinforcement Learning for Repository-Level LLM Agents
**arXiv**：[2512.20957v1](https://arxiv.org/abs/2512.20957) · [PDF](https://arxiv.org/pdf/2512.20957.pdf)  
**作者**：Zhaoxi Zhang, Yitong Duan, Yanzhi Zhang, Yiming Xu, Jiyan He, Yunfang Wu  

**一句话要点**：提出RepoNavigator，通过强化学习训练单工具LLM代理以解决大型开源软件仓库问题定位挑战。

**关键词**：仓库级问题定位, LLM代理, 强化学习训练, 单工具设计, 代码执行感知, 开源软件分析

## 3 点简述
- 核心问题：大型开源软件仓库中定位需修改的文件和函数困难，现有方法依赖多工具且忽略代码执行逻辑。
- 方法要点：设计单执行感知工具（跳转到符号定义），通过强化学习端到端训练LLM代理，简化工具操作并反映代码执行流。
- 实验或效果：RL训练的RepoNavigator在7B、14B、32B模型上均超越基线，甚至超过闭源模型如Claude-3.7，实现高效可扩展的仓库级问题定位。

## 摘要（原文）

> Locating the files and functions requiring modification in large open-source software (OSS) repositories is challenging due to their scale and structural complexity. Existing large language model (LLM)-based methods typically treat this as a repository-level retrieval task and rely on multiple auxiliary tools, which overlook code execution logic and complicate model control. We propose RepoNavigator, an LLM agent equipped with a single execution-aware tool-jumping to the definition of an invoked symbol. This unified design reflects the actual flow of code execution while simplifying tool manipulation. RepoNavigator is trained end-to-end via Reinforcement Learning (RL) directly from a pretrained model, without any closed-source distillation. Experiments demonstrate that RL-trained RepoNavigator achieves state-of-the-art performance, with the 7B model outperforming 14B baselines, the 14B model surpassing 32B competitors, and even the 32B model exceeding closed-source models such as Claude-3.7. These results confirm that integrating a single, structurally grounded tool with RL training provides an efficient and scalable solution for repository-level issue localization.

