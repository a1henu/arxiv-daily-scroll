---
layout: default
title: A Flexible Multi-Agent LLM-Human Framework for Fast Human Validated Tool Building
---

# A Flexible Multi-Agent LLM-Human Framework for Fast Human Validated Tool Building
**arXiv**：[2512.01434v1](https://arxiv.org/abs/2512.01434) · [PDF](https://arxiv.org/pdf/2512.01434.pdf)  
**作者**：Daull Xavier, Patrice Bellot, Emmanuel Bruno, Vincent Martin, Elisabeth Murisasco  

**一句话要点**：提出CollabToolBuilder框架，通过多智能体LLM与人在环指导快速构建工具以解决复杂迭代问题。

**关键词**：多智能体LLM框架, 人在环指导, 工具构建, 迭代问题解决, 动态提示, 人类反馈集成

## 3 点简述
- 核心问题：快速适应任务/领域并最小化人类反馈捕获，以构建符合人类意图的工具。
- 方法要点：采用四智能体架构（教练、编码员、批评者、资本化者），结合强化动态提示和系统化人类反馈集成。
- 实验或效果：初步实验展示在给定摘要下生成前沿研究论文或专利等应用，讨论其扩展性。

## 摘要（原文）

> We introduce CollabToolBuilder, a flexible multiagent LLM framework with expert-in-the-loop (HITL) guidance that iteratively learns to create tools for a target goal, aligning with human intent and process, while minimizing time for task/domain adaptation effort and human feedback capture. The architecture generates and validates tools via four specialized agents (Coach, Coder, Critic, Capitalizer) using a reinforced dynamic prompt and systematic human feedback integration to reinforce each agent's role toward goals and constraints. This work is best viewed as a system-level integration and methodology combining multi-agent in-context learning, HITL controls, and reusable tool capitalization for complex iterative problems such as scientific document generation. We illustrate it with preliminary experiments (e.g., generating state-of-the-art research papers or patents given an abstract) and discuss its applicability to other iterative problem-solving.

