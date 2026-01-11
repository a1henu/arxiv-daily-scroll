---
layout: default
title: Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human-Agent Interaction
---

# Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human-Agent Interaction
**arXiv**：[2601.05107v1](https://arxiv.org/abs/2601.05107) · [PDF](https://arxiv.org/pdf/2601.05107.pdf)  
**作者**：Muzhao Tian, Zisu Huang, Xiaohua Wang, Jingwen Xu, Zhengkang Guo, Qi Qian, Yuanzhe Shen, Kaitao Song, Jiakang Yuan, Changze Lv, Xiaoqing Zheng  

**一句话要点**：提出SteeM框架以解决长程人机交互中记忆依赖的平衡问题

**关键词**：长程人机交互, 记忆管理, 个性化代理, 可控记忆, 交互历史, 记忆锚定

## 3 点简述
- 核心问题：现有系统在长程交互中采用全有或全无的记忆策略，导致记忆锚定或历史利用不足。
- 方法要点：引入可量化的记忆依赖度量，并设计用户可动态调控记忆依赖的SteeM框架。
- 实验或效果：在多种场景下优于传统提示和固定记忆掩码策略，实现更精细的个性化控制。

## 摘要（原文）

> As LLM-based agents are increasingly used in long-term interactions, cumulative memory is critical for enabling personalization and maintaining stylistic consistency. However, most existing systems adopt an ``all-or-nothing'' approach to memory usage: incorporating all relevant past information can lead to \textit{Memory Anchoring}, where the agent is trapped by past interactions, while excluding memory entirely results in under-utilization and the loss of important interaction history. We show that an agent's reliance on memory can be modeled as an explicit and user-controllable dimension. We first introduce a behavioral metric of memory dependence to quantify the influence of past interactions on current outputs. We then propose \textbf{Stee}rable \textbf{M}emory Agent, \texttt{SteeM}, a framework that allows users to dynamically regulate memory reliance, ranging from a fresh-start mode that promotes innovation to a high-fidelity mode that closely follows interaction history. Experiments across different scenarios demonstrate that our approach consistently outperforms conventional prompting and rigid memory masking strategies, yielding a more nuanced and effective control for personalized human-agent collaboration.

