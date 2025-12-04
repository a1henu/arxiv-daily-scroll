---
layout: default
title: RoCo: Role-Based LLMs Collaboration for Automatic Heuristic Design
---

# RoCo: Role-Based LLMs Collaboration for Automatic Heuristic Design
**arXiv**：[2512.03762v1](https://arxiv.org/abs/2512.03762) · [PDF](https://arxiv.org/pdf/2512.03762.pdf)  
**作者**：Jiawei Xu, Fengfeng Wei, Weineng Chen  

**一句话要点**：提出RoCo多智能体角色协作系统以增强自动启发式设计的多样性与质量

**关键词**：自动启发式设计, 组合优化问题, 大语言模型, 多智能体系统, 角色协作, 启发式生成

## 3 点简述
- 核心问题：现有基于LLM的自动启发式设计研究多局限于单一角色，缺乏协作机制。
- 方法要点：通过协调探索者、利用者、批评者和整合者四个角色，在结构化多轮过程中协同生成高质量启发式。
- 实验或效果：在五种组合优化问题上，RoCo在透明与黑盒场景下均优于ReEvo和HSEvo等方法。

## 摘要（原文）

> Automatic Heuristic Design (AHD) has gained traction as a promising solution for solving combinatorial optimization problems (COPs). Large Language Models (LLMs) have emerged and become a promising approach to achieving AHD, but current LLM-based AHD research often only considers a single role. This paper proposes RoCo, a novel Multi-Agent Role-Based System, to enhance the diversity and quality of AHD through multi-role collaboration. RoCo coordinates four specialized LLM-guided agents-explorer, exploiter, critic, and integrator-to collaboratively generate high-quality heuristics. The explorer promotes long-term potential through creative, diversity-driven thinking, while the exploiter focuses on short-term improvements via conservative, efficiency-oriented refinements. The critic evaluates the effectiveness of each evolution step and provides targeted feedback and reflection. The integrator synthesizes proposals from the explorer and exploiter, balancing innovation and exploitation to drive overall progress. These agents interact in a structured multi-round process involving feedback, refinement, and elite mutations guided by both short-term and accumulated long-term reflections. We evaluate RoCo on five different COPs under both white-box and black-box settings. Experimental results demonstrate that RoCo achieves superior performance, consistently generating competitive heuristics that outperform existing methods including ReEvo and HSEvo, both in white-box and black-box scenarios. This role-based collaborative paradigm establishes a new standard for robust and high-performing AHD.

