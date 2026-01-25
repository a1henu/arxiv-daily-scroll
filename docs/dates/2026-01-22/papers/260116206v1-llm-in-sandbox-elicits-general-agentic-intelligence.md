---
layout: default
title: LLM-in-Sandbox Elicits General Agentic Intelligence
---

# LLM-in-Sandbox Elicits General Agentic Intelligence
**arXiv**：[2601.16206v1](https://arxiv.org/abs/2601.16206) · [PDF](https://arxiv.org/pdf/2601.16206.pdf)  
**作者**：Daixuan Cheng, Shaohan Huang, Yuxian Gu, Huatong Song, Guoxin Chen, Li Dong, Wayne Xin Zhao, Ji-Rong Wen, Furu Wei  

**一句话要点**：提出LLM-in-Sandbox方法，利用代码沙箱激发大语言模型在非代码领域的通用智能。

**关键词**：代码沙箱, 通用智能, 强化学习, 长上下文处理, 非代码任务, 开源工具

## 3 点简述
- 核心问题：大语言模型在非代码任务中缺乏直接执行能力，需探索如何利用代码沙箱实现通用智能。
- 方法要点：通过代码沙箱让大语言模型自主探索，如访问外部资源、处理长上下文，并引入强化学习增强代理能力。
- 实验或效果：在数学、物理、化学等多个领域实现稳健泛化，并开源为Python包便于部署。

## 摘要（原文）

> We introduce LLM-in-Sandbox, enabling LLMs to explore within a code sandbox (i.e., a virtual computer), to elicit general intelligence in non-code domains. We first demonstrate that strong LLMs, without additional training, exhibit generalization capabilities to leverage the code sandbox for non-code tasks. For example, LLMs spontaneously access external resources to acquire new knowledge, leverage the file system to handle long contexts, and execute scripts to satisfy formatting requirements. We further show that these agentic capabilities can be enhanced through LLM-in-Sandbox Reinforcement Learning (LLM-in-Sandbox-RL), which uses only non-agentic data to train models for sandbox exploration. Experiments demonstrate that LLM-in-Sandbox, in both training-free and post-trained settings, achieves robust generalization spanning mathematics, physics, chemistry, biomedicine, long-context understanding, and instruction following. Finally, we analyze LLM-in-Sandbox's efficiency from computational and system perspectives, and open-source it as a Python package to facilitate real-world deployment.

