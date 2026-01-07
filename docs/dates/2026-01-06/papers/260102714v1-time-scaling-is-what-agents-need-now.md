---
layout: default
title: Time-Scaling Is What Agents Need Now
---

# Time-Scaling Is What Agents Need Now
**arXiv**：[2601.02714v1](https://arxiv.org/abs/2601.02714) · [PDF](https://arxiv.org/pdf/2601.02714.pdf)  
**作者**：Zhi Liu, Guangzhi Wang  

**一句话要点**：提出时间缩放以增强智能体在认知约束下的深度推理与问题解决能力

**关键词**：时间缩放, 智能体推理, 认知约束, 深度推理, 问题解决

## 3 点简述
- 核心问题：早期大语言模型缺乏稳健语义推理，现有方法如思维链在搜索完整性和效率上受限
- 方法要点：时间缩放通过扩展时间路径优化智能体随时间展开推理的能力，支持深度探索和动态调整
- 实验或效果：未知，但强调时间缩放是提升推理能力的关键前沿，无需成比例增加静态参数

## 摘要（原文）

> Early artificial intelligence paradigms exhibited separated cognitive functions: Neural Networks focused on "perception-representation," Reinforcement Learning on "decision-making-behavior," and Symbolic AI on "knowledge-reasoning." With Transformer-based large models and world models, these paradigms are converging into cognitive agents with closed-loop "perception-decision-action" capabilities.
>   Humans solve complex problems under limited cognitive resources through temporalized sequential reasoning. Language relies on problem space search for deep semantic reasoning. While early large language models (LLMs) could generate fluent text, they lacked robust semantic reasoning capabilities. Prompting techniques like Chain-of-Thought (CoT) and Tree-of-Thought (ToT) extended reasoning paths by making intermediate steps explicit. Recent models like DeepSeek-R1 enhanced performance through explicit reasoning trajectories. However, these methods have limitations in search completeness and efficiency.
>   This highlights the need for "Time-Scaling"--the systematic extension and optimization of an agent's ability to unfold reasoning over time. Time-Scaling refers to architectural design utilizing extended temporal pathways, enabling deeper problem space exploration, dynamic strategy adjustment, and enhanced metacognitive control, paralleling human sequential reasoning under cognitive constraints. It represents a critical frontier for enhancing deep reasoning and problem-solving without proportional increases in static model parameters. Advancing intelligent agent capabilities requires placing Time-Scaling principles at the forefront, positioning explicit temporal reasoning management as foundational.

