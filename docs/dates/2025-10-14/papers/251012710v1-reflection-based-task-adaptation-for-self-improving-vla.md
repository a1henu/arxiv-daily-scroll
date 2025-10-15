---
layout: default
title: Reflection-Based Task Adaptation for Self-Improving VLA
---

# Reflection-Based Task Adaptation for Self-Improving VLA
**arXiv**：[2510.12710v1](https://arxiv.org/abs/2510.12710) · [PDF](https://arxiv.org/pdf/2510.12710.pdf)  
**作者**：Baicheng Li, Dong Wu, Zike Yan, Xinchen Liu, Zecui Zeng, Lusong Li, Hongbin Zha  

**一句话要点**：提出反射式自适应框架以解决VLA模型在机器人任务中适应效率低的问题

**关键词**：视觉语言动作模型, 任务自适应, 强化学习, 反思学习, 模仿学习, 机器人操作

## 3 点简述
- 核心问题：预训练VLA模型在适应新任务时效率低，强化学习收敛慢。
- 方法要点：采用双路径架构，结合失败驱动反思RL和成功驱动SFT，防止奖励黑客。
- 实验或效果：在操作任务中实现更快收敛和更高成功率，优于基线方法。

## 摘要（原文）

> Pre-trained Vision-Language-Action (VLA) models represent a major leap
> towards general-purpose robots, yet efficiently adapting them to novel,
> specific tasks in-situ remains a significant hurdle. While reinforcement
> learning (RL) is a promising avenue for such adaptation, the process often
> suffers from low efficiency, hindering rapid task mastery. We introduce
> Reflective Self-Adaptation, a framework for rapid, autonomous task adaptation
> without human intervention. Our framework establishes a self-improving loop
> where the agent learns from its own experience to enhance both strategy and
> execution.
>   The core of our framework is a dual-pathway architecture that addresses the
> full adaptation lifecycle. First, a Failure-Driven Reflective RL pathway
> enables rapid learning by using the VLM's causal reasoning to automatically
> synthesize a targeted, dense reward function from failure analysis. This
> provides a focused learning signal that significantly accelerates policy
> exploration. However, optimizing such proxy rewards introduces a potential risk
> of "reward hacking," where the agent masters the reward function but fails the
> actual task. To counteract this, our second pathway, Success-Driven
> Quality-Guided SFT, grounds the policy in holistic success. It identifies and
> selectively imitates high-quality successful trajectories, ensuring the agent
> remains aligned with the ultimate task goal. This pathway is strengthened by a
> conditional curriculum mechanism to aid initial exploration.
>   We conduct experiments in challenging manipulation tasks. The results
> demonstrate that our framework achieves faster convergence and higher final
> success rates compared to representative baselines. Our work presents a robust
> solution for creating self-improving agents that can efficiently and reliably
> adapt to new environments.

