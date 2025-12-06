---
layout: default
title: Open-Ended Goal Inference through Actions and Language for Human-Robot Collaboration
---

# Open-Ended Goal Inference through Actions and Language for Human-Robot Collaboration
**arXiv**：[2512.04453v1](https://arxiv.org/abs/2512.04453) · [PDF](https://arxiv.org/pdf/2512.04453.pdf)  
**作者**：Debasmita Ghose, Oz Gitelson, Marynel Vazquez, Brian Scassellati  

**一句话要点**：提出BALI方法，通过双向动作-语言推理解决人机协作中的开放目标推断问题。

**关键词**：人机协作, 目标推断, 动作-语言融合, 滚动时域规划, 开放目标集

## 3 点简述
- 核心问题：机器人需推断人类模糊、难以表达或非预设的协作目标，现有方法依赖固定目标集、仅观察动作或仅依赖指令，导致脆弱性。
- 方法要点：BALI整合自然语言偏好与观察动作，在滚动时域规划树中双向推理，仅在信息增益大于中断成本时提问，并选择支持性动作。
- 实验或效果：在协作烹饪任务中评估，BALI相比基线实现更稳定的目标预测和显著更少的错误。

## 摘要（原文）

> To collaborate with humans, robots must infer goals that are often ambiguous, difficult to articulate, or not drawn from a fixed set. Prior approaches restrict inference to a predefined goal set, rely only on observed actions, or depend exclusively on explicit instructions, making them brittle in real-world interactions. We present BALI (Bidirectional Action-Language Inference) for goal prediction, a method that integrates natural language preferences with observed human actions in a receding-horizon planning tree. BALI combines language and action cues from the human, asks clarifying questions only when the expected information gain from the answer outweighs the cost of interruption, and selects supportive actions that align with inferred goals. We evaluate the approach in collaborative cooking tasks, where goals may be novel to the robot and unbounded. Compared to baselines, BALI yields more stable goal predictions and significantly fewer mistakes.

