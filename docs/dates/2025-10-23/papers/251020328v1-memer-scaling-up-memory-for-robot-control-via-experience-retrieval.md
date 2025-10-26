---
layout: default
title: MemER: Scaling Up Memory for Robot Control via Experience Retrieval
---

# MemER: Scaling Up Memory for Robot Control via Experience Retrieval
**arXiv**：[2510.20328v1](https://arxiv.org/abs/2510.20328) · [PDF](https://arxiv.org/pdf/2510.20328.pdf)  
**作者**：Ajay Sridhar, Jennifer Pan, Satvik Sharma, Chelsea Finn  

**一句话要点**：提出MemER框架，通过经验检索扩展机器人控制中的记忆能力，以解决长时依赖任务。

**关键词**：机器人控制, 经验检索, 分层策略, 长时程依赖, 视觉语言动作模型, 关键帧选择

## 3 点简述
- 核心问题：机器人策略缺乏记忆能力，长观测历史处理计算昂贵且易受协变量偏移影响。
- 方法要点：采用分层策略框架，高层策略选择并跟踪相关关键帧，指导低层策略执行。
- 实验或效果：在三个真实世界长时程机器人操作任务中优于先前方法，依赖分钟级记忆。

## 摘要（原文）

> Humans routinely rely on memory to perform tasks, yet most robot policies
> lack this capability; our goal is to endow robot policies with the same
> ability. Naively conditioning on long observation histories is computationally
> expensive and brittle under covariate shift, while indiscriminate subsampling
> of history leads to irrelevant or redundant information. We propose a
> hierarchical policy framework, where the high-level policy is trained to select
> and track previous relevant keyframes from its experience. The high-level
> policy uses selected keyframes and the most recent frames when generating text
> instructions for a low-level policy to execute. This design is compatible with
> existing vision-language-action (VLA) models and enables the system to
> efficiently reason over long-horizon dependencies. In our experiments, we
> finetune Qwen2.5-VL-7B-Instruct and $\pi_{0.5}$ as the high-level and low-level
> policies respectively, using demonstrations supplemented with minimal language
> annotations. Our approach, MemER, outperforms prior methods on three real-world
> long-horizon robotic manipulation tasks that require minutes of memory. Videos
> and code can be found at https://jen-pan.github.io/memer/.

