---
layout: default
title: Agentic Design of Compositional Machines
---

# Agentic Design of Compositional Machines
**arXiv**：[2510.14980v1](https://arxiv.org/abs/2510.14980) · [PDF](https://arxiv.org/pdf/2510.14980.pdf)  
**作者**：Wenqian Zhang, Weiyang Liu, Zhen Liu  

**一句话要点**：提出基于LLM的智能体工作流以解决组合机器设计问题

**关键词**：组合机器设计, 大型语言模型, 智能体工作流, 强化学习微调, 物理模拟, 空间推理

## 3 点简述
- 核心问题：LLM能否学习在模拟物理环境中设计组合机器以满足功能需求
- 方法要点：引入BesiegeField测试平台，结合空间推理和强化学习微调
- 实验或效果：基准测试显示开源模型不足，RL微调探索改进路径

## 摘要（原文）

> The design of complex machines stands as both a marker of human intelligence
> and a foundation of engineering practice. Given recent advances in large
> language models (LLMs), we ask whether they, too, can learn to create. We
> approach this question through the lens of compositional machine design: a task
> in which machines are assembled from standardized components to meet functional
> demands like locomotion or manipulation in a simulated physical environment. To
> support this investigation, we introduce BesiegeField, a testbed built on the
> machine-building game Besiege, which enables part-based construction, physical
> simulation and reward-driven evaluation. Using BesiegeField, we benchmark
> state-of-the-art LLMs with agentic workflows and identify key capabilities
> required for success, including spatial reasoning, strategic assembly, and
> instruction-following. As current open-source models fall short, we explore
> reinforcement learning (RL) as a path to improvement: we curate a cold-start
> dataset, conduct RL finetuning experiments, and highlight open challenges at
> the intersection of language, machine design, and physical reasoning.

