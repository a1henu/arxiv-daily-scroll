---
layout: default
title: VisGym: Diverse, Customizable, Scalable Environments for Multimodal Agents
---

# VisGym: Diverse, Customizable, Scalable Environments for Multimodal Agents
**arXiv**：[2601.16973v1](https://arxiv.org/abs/2601.16973) · [PDF](https://arxiv.org/pdf/2601.16973.pdf)  
**作者**：Zirui Wang, Junyi Zhang, Jiaxin Ge, Long Lian, Letian Fu, Lisa Dunlap, Ken Goldberg, XuDong Wang, Ion Stoica, David M. Chan, Sewon Min, Joseph E. Gonzalez  

**一句话要点**：提出VisGym环境套件以评估和训练多模态代理在长时程视觉交互中的能力

**关键词**：视觉语言模型, 多步交互评估, 环境套件, 监督微调, 长时程决策, 视觉导航

## 3 点简述
- 核心问题：现代视觉语言模型在多步视觉交互中整合感知、记忆和行动的能力不足，缺乏评估基准。
- 方法要点：构建包含17个多样化环境的套件，支持难度、输入表示和反馈的灵活控制，并提供结构化演示用于监督微调。
- 实验或效果：前沿模型在交互设置中成功率低，揭示长上下文利用困难、视觉渲染增加任务难度等问题，但特定干预措施可带来改进。

## 摘要（原文）

> Modern Vision-Language Models (VLMs) remain poorly characterized in multi-step visual interactions, particularly in how they integrate perception, memory, and action over long horizons. We introduce VisGym, a gymnasium of 17 environments for evaluating and training VLMs. The suite spans symbolic puzzles, real-image understanding, navigation, and manipulation, and provides flexible controls over difficulty, input representation, planning horizon, and feedback. We also provide multi-step solvers that generate structured demonstrations, enabling supervised finetuning. Our evaluations show that all frontier models struggle in interactive settings, achieving low success rates in both the easy (46.6%) and hard (26.0%) configurations. Our experiments reveal notable limitations: models struggle to effectively leverage long context, performing worse with an unbounded history than with truncated windows. Furthermore, we find that several text-based symbolic tasks become substantially harder once rendered visually. However, explicit goal observations, textual feedback, and exploratory demonstrations in partially observable or unknown-dynamics settings for supervised finetuning yield consistent gains, highlighting concrete failure modes and pathways for improving multi-step visual decision-making. Code, data, and models can be found at: https://visgym.github.io/.

