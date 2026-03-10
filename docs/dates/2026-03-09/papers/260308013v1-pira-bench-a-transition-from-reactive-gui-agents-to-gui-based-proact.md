---
layout: default
title: PIRA-Bench: A Transition from Reactive GUI Agents to GUI-based Proactive Intent Recommendation Agents
---

# PIRA-Bench: A Transition from Reactive GUI Agents to GUI-based Proactive Intent Recommendation Agents
**arXiv**：[2603.08013v1](https://arxiv.org/abs/2603.08013) · [PDF](https://arxiv.org/pdf/2603.08013.pdf)  
**作者**：Yuxiang Chai, Shunye Tang, Han Xiao, Rui Liu, Hongsheng Li  

**一句话要点**：提出PIRA-Bench基准和PIRF框架，以评估MLLMs在连续视觉输入下的主动意图推荐能力。

**关键词**：主动意图推荐, 多模态大语言模型, GUI代理基准, 连续视觉输入, 状态跟踪框架

## 3 点简述
- 核心问题：当前GUI代理为被动响应，需转向基于连续视觉输入的主动意图推荐。
- 方法要点：引入PIRA-Bench基准，包含复杂轨迹和噪声段，并设计PIRF框架进行状态跟踪。
- 实验或效果：PIRA-Bench作为初步步骤，挑战代理在真实屏幕活动中的事件检测和偏好适应。

## 摘要（原文）

> Current Graphical User Interface (GUI) agents operate primarily under a reactive paradigm: a user must provide an explicit instruction for the agent to execute a task. However, an intelligent AI assistant should be proactive, which is capable of anticipating user intentions directly from continuous visual inputs, such as mobile or desktop screenshots, and offering timely recommendations without explicit user prompting. Transitioning to this proactive paradigm presents significant challenges. Real-world screen activity is rarely linear; it consists of long-horizon trajectories fraught with noisy browsing, meaningless actions, and multithreaded task-switching. To address this gap, we introduce PIRA-Bench (Proactive Intent Recommendation Agent Benchmark), a novel benchmark for evaluating multimodal large language models (MLLMs) on continuous, weakly-supervised visual inputs. Unlike reactive datasets, PIRA-Bench features complex trajectories with multiple interleaved intents and noisy segments with various user profile contexts, challenging agents to detect actionable events while fitting to user preferences. Furthermore, we propose the PIRF baseline, a memory-aware, state-tracking framework that empowers general MLLMs to manage multiple task threads and handle misleading visual inputs. PIRA-Bench serves as an initial step toward robust and proactive GUI-based personal assistants.

