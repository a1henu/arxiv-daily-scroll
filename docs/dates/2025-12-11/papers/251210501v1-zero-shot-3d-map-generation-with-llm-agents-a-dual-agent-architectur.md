---
layout: default
title: Zero-shot 3D Map Generation with LLM Agents: A Dual-Agent Architecture for Procedural Content Generation
---

# Zero-shot 3D Map Generation with LLM Agents: A Dual-Agent Architecture for Procedural Content Generation
**arXiv**：[2512.10501v1](https://arxiv.org/abs/2512.10501) · [PDF](https://arxiv.org/pdf/2512.10501.pdf)  
**作者**：Lim Chien Her, Ming Yan, Yunshu Bai, Ruihao Li, Hao Zhang  

**一句话要点**：提出双智能体架构，利用LLM实现零样本3D地图生成的参数配置

**关键词**：零样本学习, 过程内容生成, 大型语言模型, 智能体架构, 3D地图生成, 参数配置

## 3 点简述
- 核心问题：PCG工具参数配置需精确控制，现成LLM难以弥合抽象指令与严格参数间的语义鸿沟
- 方法要点：采用Actor与Critic双智能体迭代工作，自主推理并优化参数以对齐人类设计偏好
- 实验或效果：在3D地图生成中验证，优于单智能体基线，从自然语言描述生成多样且结构有效的环境

## 摘要（原文）

> Procedural Content Generation (PCG) offers scalable methods for algorithmically creating complex, customizable worlds. However, controlling these pipelines requires the precise configuration of opaque technical parameters. We propose a training-free architecture that utilizes LLM agents for zero-shot PCG parameter configuration. While Large Language Models (LLMs) promise a natural language interface for PCG tools, off-the-shelf models often fail to bridge the semantic gap between abstract user instructions and strict parameter specifications. Our system pairs an Actor agent with a Critic agent, enabling an iterative workflow where the system autonomously reasons over tool parameters and refines configurations to progressively align with human design preferences. We validate this approach on the generation of various 3D maps, establishing a new benchmark for instruction-following in PCG. Experiments demonstrate that our approach outperforms single-agent baselines, producing diverse and structurally valid environments from natural language descriptions. These results demonstrate that off-the-shelf LLMs can be effectively repurposed as generalized agents for arbitrary PCG tools. By shifting the burden from model training to architectural reasoning, our method offers a scalable framework for mastering complex software without task-specific fine-tuning.

