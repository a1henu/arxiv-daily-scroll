---
layout: default
title: Learning Affordances at Inference-Time for Vision-Language-Action Models
---

# Learning Affordances at Inference-Time for Vision-Language-Action Models
**arXiv**：[2510.19752v1](https://arxiv.org/abs/2510.19752) · [PDF](https://arxiv.org/pdf/2510.19752.pdf)  
**作者**：Ameesh Shah, William Chen, Adwait Godbole, Federico Mora, Sanjit A. Seshia, Sergey Levine  

**一句话要点**：提出LITEN方法，通过推理时学习提升视觉-语言-动作模型在机器人任务中的动态调整能力

**关键词**：视觉-语言-动作模型, 推理时学习, 机器人控制, 长时程任务, 自我反思

## 3 点简述
- 核心问题：视觉-语言-动作模型在机器人控制中缺乏失败后的上下文动态行为调整能力
- 方法要点：结合高低层模型，通过推理与评估阶段迭代学习低层模型的可用性与能力
- 实验或效果：LITEN能从经验中学习，生成高可用性指令以完成长时程任务

## 摘要（原文）

> Solving complex real-world control tasks often takes multiple tries: if we
> fail at first, we reflect on what went wrong, and change our strategy
> accordingly to avoid making the same mistake. In robotics,
> Vision-Language-Action models (VLAs) offer a promising path towards solving
> complex control tasks, but lack the ability to contextually and dynamically
> readjust behavior when they fail to accomplish a task. In this work, we
> introduce Learning from Inference-Time Execution (LITEN), which connects a VLA
> low-level policy to a high-level VLM that conditions on past experiences by
> including them in-context, allowing it to learn the affordances and
> capabilities of the low-level VLA. Our approach iterates between a reasoning
> phase that generates and executes plans for the low-level VLA, and an
> assessment phase that reflects on the resulting execution and draws useful
> conclusions to be included in future reasoning contexts. Unlike similar
> approaches to self-refinement in non-robotics domains, LITEN must reflect on
> unstructured real-world robot trajectories (e.g., raw videos), which requires
> structured guiderails during assessment. Our experimental results demonstrate
> LITEN is able to effectively learn from past experience to generate plans that
> use high-affordance instructions to accomplish long-horizon tasks.

