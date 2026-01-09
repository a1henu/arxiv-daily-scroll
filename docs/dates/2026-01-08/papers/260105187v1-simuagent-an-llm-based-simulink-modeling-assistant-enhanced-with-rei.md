---
layout: default
title: SimuAgent: An LLM-Based Simulink Modeling Assistant Enhanced with Reinforcement Learning
---

# SimuAgent: An LLM-Based Simulink Modeling Assistant Enhanced with Reinforcement Learning
**arXiv**：[2601.05187v1](https://arxiv.org/abs/2601.05187) · [PDF](https://arxiv.org/pdf/2601.05187.pdf)  
**作者**：Yanchang Liang, Xiaowei Zhao  

**一句话要点**：提出SimuAgent，一种基于LLM的Simulink建模助手，通过强化学习增强以解决图形化工程工作流自动化问题。

**关键词**：Simulink建模, 大语言模型应用, 强化学习优化, 工程自动化, 隐私保护部署, 数据增强

## 3 点简述
- 核心问题：LLM在图形化工程工作流（如Simulink建模）中的应用潜力未充分探索，传统XML表示冗长且效率低。
- 方法要点：采用轻量级计划-执行架构，结合两阶段训练和ReGRPO强化学习算法，以字典式Python表示替代XML，提升效率和可解释性。
- 实验或效果：在SimuBench基准测试中，SimuAgent收敛更快、建模精度更高，优于标准RL基线，并在少样本提示下超越GPT-4o，支持本地部署。

## 摘要（原文）

> Large language models (LLMs) have revolutionized text-based code automation, but their potential in graph-oriented engineering workflows remains under-explored. We introduce SimuAgent, an LLM-powered modeling and simulation agent tailored for Simulink. SimuAgent replaces verbose XML with a concise, dictionary-style Python representation, dramatically cutting token counts, improving interpretability, and enabling fast, in-process simulation. A lightweight plan-execute architecture, trained in two stages, equips the agent with both low-level tool skills and high-level design reasoning. To tackle sparse rewards in long-horizon tasks, we propose Reflection-GRPO (ReGRPO), which augments Group Relative Policy Optimization (GRPO) with self-reflection traces that supply rich intermediate feedback, accelerating convergence and boosting robustness. Experiments on SimuBench, our newly released benchmark comprising 5300 multi-domain modeling tasks, show that a Qwen2.5-7B model fine-tuned with SimuAgent converges faster and achieves higher modeling accuracy than standard RL baselines, and even surpasses GPT-4o when evaluated with few-shot prompting on the same benchmark. Ablations confirm that the two-stage curriculum and abstract-reconstruct data augmentation further enhance generalization. SimuAgent trains and runs entirely on-premise with modest hardware, delivering a privacy-preserving, cost-effective solution for industrial model-driven engineering. SimuAgent bridges the gap between LLMs and graphical modeling environments, offering a practical solution for AI-assisted engineering design in industrial settings.

