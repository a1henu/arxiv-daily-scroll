---
layout: default
title: Neuro-Symbolic Control with Large Language Models for Language-Guided Spatial Tasks
---

# Neuro-Symbolic Control with Large Language Models for Language-Guided Spatial Tasks
**arXiv**：[2512.17321v1](https://arxiv.org/abs/2512.17321) · [PDF](https://arxiv.org/pdf/2512.17321.pdf)  
**作者**：Momina Liaqat Ali, Muhammad Abid  

**一句话要点**：提出神经符号控制框架，以解决语言引导空间任务中LLM直接控制的不稳定与低效问题。

**关键词**：神经符号控制, 大语言模型, 语言引导任务, 连续控制, 模块化框架, 平面操作

## 3 点简述
- 核心问题：LLM直接应用于连续控制时存在不稳定、收敛慢和幻觉动作等限制。
- 方法要点：采用模块化框架，分离低层运动执行与高层语义推理，LLM处理符号任务，神经控制器执行增量动作。
- 实验或效果：在平面操作任务中，相比LLM-only基线，成功率和效率显著提升，平均步骤减少超70%，速度提升达8.83倍。

## 摘要（原文）

> Although large language models (LLMs) have recently become effective tools for language-conditioned control in embodied systems, instability, slow convergence, and hallucinated actions continue to limit their direct application to continuous control. A modular neuro-symbolic control framework that clearly distinguishes between low-level motion execution and high-level semantic reasoning is proposed in this work. While a lightweight neural delta controller performs bounded, incremental actions in continuous space, a locally deployed LLM interprets symbolic tasks. We assess the suggested method in a planar manipulation setting with spatial relations between objects specified by language. Numerous tasks and local language models, such as Mistral, Phi, and LLaMA-3.2, are used in extensive experiments to compare LLM-only control, neural-only control, and the suggested LLM+DL framework. In comparison to LLM-only baselines, the results show that the neuro-symbolic integration consistently increases both success rate and efficiency, achieving average step reductions exceeding 70% and speedups of up to 8.83x while remaining robust to language model quality. The suggested framework enhances interpretability, stability, and generalization without any need of reinforcement learning or costly rollouts by controlling the LLM to symbolic outputs and allocating uninterpreted execution to a neural controller trained on artificial geometric data. These outputs show empirically that neuro-symbolic decomposition offers a scalable and principled way to integrate language understanding with ongoing control, this approach promotes the creation of dependable and effective language-guided embodied systems.

