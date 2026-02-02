---
layout: default
title: MonoScale: Scaling Multi-Agent System with Monotonic Improvement
---

# MonoScale: Scaling Multi-Agent System with Monotonic Improvement
**arXiv**：[2601.23219v1](https://arxiv.org/abs/2601.23219) · [PDF](https://arxiv.org/pdf/2601.23219.pdf)  
**作者**：Shuai Shao, Yixiang Liu, Bingwei Lu, Weinan Zhang  

**一句话要点**：提出MonoScale框架，通过单调性能保证解决多智能体系统扩展中的性能崩溃问题。

**关键词**：多智能体系统, 智能体扩展, 单调性能保证, 自然语言记忆, 上下文赌博机, 路由优化

## 3 点简述
- 核心问题：多智能体系统扩展时，新智能体冷启动导致路由性能下降。
- 方法要点：生成熟悉化任务，收集交互证据，蒸馏为可审计自然语言记忆指导路由。
- 实验或效果：在GAIA和Humanity's Last Exam上实现稳定性能提升，优于基线方法。

## 摘要（原文）

> In recent years, LLM-based multi-agent systems (MAS) have advanced rapidly, using a router to decompose tasks and delegate subtasks to specialized agents. A natural way to expand capability is to scale up the agent pool by continually integrating new functional agents or tool interfaces, but naive expansion can trigger performance collapse when the router cold-starts on newly added, heterogeneous, and unreliable agents. We propose MonoScale, an expansion-aware update framework that proactively generates a small set of agent-conditioned familiarization tasks, harvests evidence from both successful and failed interactions, and distills it into auditable natural-language memory to guide future routing. We formalize sequential augmentation as a contextual bandit and perform trust-region memory updates, yielding a monotonic non-decreasing performance guarantee across onboarding rounds. Experiments on GAIA and Humanity's Last Exam show stable gains as the agent pool grows, outperforming naive scale-up and strong-router fixed-pool baselines.

