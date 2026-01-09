---
layout: default
title: MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
---

# MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
**arXiv**：[2601.05215v1](https://arxiv.org/abs/2601.05215) · [PDF](https://arxiv.org/pdf/2601.05215.pdf)  
**作者**：Tamil Sudaravan Mohan Doss, Michael Xu, Sudha Rao, Andrew D. Wilson, Balasaravanan Thoravi Kumaravel  

**一句话要点**：提出MineNPC-Task基准套件，用于评估开放世界Minecraft中记忆感知混合主动LLM代理。

**关键词**：记忆感知代理, 开放世界基准, 混合主动交互, Minecraft评估, 任务模板

## 3 点简述
- 核心问题：现有基准依赖合成提示，缺乏真实玩家交互和记忆感知评估。
- 方法要点：基于专家玩家共玩设计参数化任务模板，配备机器可检查验证器和有界知识策略。
- 实验或效果：使用GPT-4o评估216个子任务，识别执行、导航等故障模式，玩家反馈交互质量良好。

## 摘要（原文）

> We present \textsc{MineNPC-Task}, a user-authored benchmark and evaluation harness for testing memory-aware, mixed-initiative LLM agents in open-world \emph{Minecraft}. Rather than relying on synthetic prompts, tasks are elicited from formative and summative co-play with expert players, normalized into parametric templates with explicit preconditions and dependency structure, and paired with machine-checkable validators under a bounded-knowledge policy that forbids out-of-world shortcuts. The harness captures plan/act/memory events-including plan previews, targeted clarifications, memory reads and writes, precondition checks, and repair attempts and reports outcomes relative to the total number of attempted subtasks, derived from in-world evidence.
>   As an initial snapshot, we instantiate the framework with GPT-4o and evaluate \textbf{216} subtasks across \textbf{8} experienced players. We observe recurring breakdown patterns in code execution, inventory/tool handling, referencing, and navigation, alongside recoveries supported by mixed-initiative clarifications and lightweight memory. Participants rated interaction quality and interface usability positively, while highlighting the need for stronger memory persistence across tasks. We release the complete task suite, validators, logs, and harness to support transparent, reproducible evaluation of future memory-aware embodied agents.

