---
layout: default
title: From Instruction to Event: Sound-Triggered Mobile Manipulation
---

# From Instruction to Event: Sound-Triggered Mobile Manipulation
**arXiv**：[2601.21667v1](https://arxiv.org/abs/2601.21667) · [PDF](https://arxiv.org/pdf/2601.21667.pdf)  
**作者**：Hao Ju, Shaofei Huang, Hongyu Li, Zihan Ding, Si Liu, Meng Wang, Zhedong Zheng  

**一句话要点**：提出声音触发移动操作以解决指令驱动范式限制，增强自主性。

**关键词**：声音触发移动操作, 自主感知, 声学渲染, 物理交互, 任务规划, 基线模型

## 3 点简述
- 核心问题：指令驱动范式限制自主性，无法响应动态环境事件。
- 方法要点：开发Habitat-Echo平台，集成声学渲染与物理交互，提出高层任务规划与低层策略基线。
- 实验或效果：基线使代理主动检测声音事件，在双源场景中隔离主源并操作次对象，验证鲁棒性。

## 摘要（原文）

> Current mobile manipulation research predominantly follows an instruction-driven paradigm, where agents rely on predefined textual commands to execute tasks. However, this setting confines agents to a passive role, limiting their autonomy and ability to react to dynamic environmental events. To address these limitations, we introduce sound-triggered mobile manipulation, where agents must actively perceive and interact with sound-emitting objects without explicit action instructions. To support these tasks, we develop Habitat-Echo, a data platform that integrates acoustic rendering with physical interaction. We further propose a baseline comprising a high-level task planner and low-level policy models to complete these tasks. Extensive experiments show that the proposed baseline empowers agents to actively detect and respond to auditory events, eliminating the need for case-by-case instructions. Notably, in the challenging dual-source scenario, the agent successfully isolates the primary source from overlapping acoustic interference to execute the first interaction, and subsequently proceeds to manipulate the secondary object, verifying the robustness of the baseline.

