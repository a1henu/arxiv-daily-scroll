---
layout: default
title: Dyna-Mind: Learning to Simulate from Experience for Better AI Agents
---

# Dyna-Mind: Learning to Simulate from Experience for Better AI Agents
**arXiv**：[2510.09577v1](https://arxiv.org/abs/2510.09577) · [PDF](https://arxiv.org/pdf/2510.09577.pdf)  
**作者**：Xiao Yu, Baolin Peng, Michel Galley, Hao Cheng, Qianhui Wu, Janardhan Kulkarni, Suman Nath, Zhou Yu, Jianfeng Gao  
**一句话要点**：提出Dyna-Mind框架以提升AI代理在复杂交互任务中的推理与决策能力

**关键词**：AI代理, 模拟推理, 强化学习, 长时程任务, 交互环境, 决策优化

## 3 点简述
- 核心问题：AI代理在数学和编码领域表现优异，但在长时程交互任务中性能不足。
- 方法要点：采用两阶段训练，先通过ReSim学习基于经验的模拟推理，再通过Dyna-GRPO强化决策。
- 实验效果：在Sokoban、ALFWorld和AndroidWorld基准测试中验证了模拟能力的有效性和策略改进。

## 摘要（原文）

> Reasoning models have recently shown remarkable progress in domains such as
> math and coding. However, their expert-level abilities in math and coding
> contrast sharply with their performance in long-horizon, interactive tasks such
> as web navigation and computer/phone-use. Inspired by literature on human
> cognition, we argue that current AI agents need ''vicarious trial and error'' -
> the capacity to mentally simulate alternative futures before acting - in order
> to enhance their understanding and performance in complex interactive
> environments. We introduce Dyna-Mind, a two-stage training framework that
> explicitly teaches (V)LM agents to integrate such simulation into their
> reasoning. In stage 1, we introduce Reasoning with Simulations (ReSim), which
> trains the agent to generate structured reasoning traces from expanded search
> trees built from real experience gathered through environment interactions.
> ReSim thus grounds the agent's reasoning in faithful world dynamics and equips
> it with the ability to anticipate future states in its reasoning. In stage 2,
> we propose Dyna-GRPO, an online reinforcement learning method to further
> strengthen the agent's simulation and decision-making ability by using both
> outcome rewards and intermediate states as feedback from real rollouts.
> Experiments on two synthetic benchmarks (Sokoban and ALFWorld) and one
> realistic benchmark (AndroidWorld) demonstrate that (1) ReSim effectively
> infuses simulation ability into AI agents, and (2) Dyna-GRPO leverages outcome
> and interaction-level signals to learn better policies for long-horizon,
> planning-intensive tasks. Together, these results highlight the central role of
> simulation in enabling AI agents to reason, plan, and act more effectively in
> the ever more challenging environments.

