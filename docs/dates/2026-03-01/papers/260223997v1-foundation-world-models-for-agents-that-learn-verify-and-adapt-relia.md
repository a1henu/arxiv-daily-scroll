---
layout: default
title: Foundation World Models for Agents that Learn, Verify, and Adapt Reliably Beyond Static Environments
---

# Foundation World Models for Agents that Learn, Verify, and Adapt Reliably Beyond Static Environments
**arXiv**：[2602.23997v1](https://arxiv.org/abs/2602.23997) · [PDF](https://arxiv.org/pdf/2602.23997.pdf)  
**作者**：Florent Delgrange  

**一句话要点**：提出基础世界模型以支持智能体在开放世界中可靠学习、验证和适应

**关键词**：基础世界模型, 强化学习, 形式验证, 程序合成, 自适应智能体

## 3 点简述
- 核心问题：现有方法假设固定任务和环境，限制智能体在变化条件下的策略演化能力。
- 方法要点：结合可学习奖励模型、自适应形式验证、在线抽象校准和测试时合成，构建持久组合表示。
- 实验或效果：未知，论文为愿景性框架，未报告具体实验数据。

## 摘要（原文）

> The next generation of autonomous agents must not only learn efficiently but also act reliably and adapt their behavior in open worlds. Standard approaches typically assume fixed tasks and environments with little or no novelty, which limits world models' ability to support agents that must evolve their policies as conditions change. This paper outlines a vision for foundation world models: persistent, compositional representations that unify reinforcement learning, reactive/program synthesis, and abstraction mechanisms. We propose an agenda built around four components: (i) learnable reward models from specifications to support optimization with clear objectives; (ii) adaptive formal verification integrated throughout learning; (iii) online abstraction calibration to quantify the reliability of the model's predictions; and (iv) test-time synthesis and world-model generation guided by verifiers. Together, these components enable agents to synthesize verifiable programs, derive new policies from a small number of interactions, and maintain correctness while adapting to novelty. The resulting framework positions foundation world models as a substrate for learning, reasoning, and adaptation, laying the groundwork for agents that not only act well but can explain and justify the behavior they adopt.

