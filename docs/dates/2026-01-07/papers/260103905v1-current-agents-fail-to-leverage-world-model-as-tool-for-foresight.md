---
layout: default
title: Current Agents Fail to Leverage World Model as Tool for Foresight
---

# Current Agents Fail to Leverage World Model as Tool for Foresight
**arXiv**：[2601.03905v1](https://arxiv.org/abs/2601.03905) · [PDF](https://arxiv.org/pdf/2601.03905.pdf)  
**作者**：Cheng Qian, Emre Can Acikgoz, Bingxuan Li, Xiusi Chen, Yuji Zhang, Bingxiang He, Qinyu Luo, Dilek Hakkani-Tür, Gokhan Tur, Yunzhu Li, Heng Ji, Heng Ji  

**一句话要点**：实证揭示当前智能体难以利用世界模型作为前瞻工具，性能下降达5%

**关键词**：智能体认知, 世界模型, 前瞻推理, 视觉问答, 模拟调用, 性能瓶颈

## 3 点简述
- 核心问题：智能体在需预测未来状态的任务中，无法有效利用生成世界模型进行模拟和前瞻推理。
- 方法要点：通过多样化智能体和视觉问答任务，分析智能体调用模拟、误用预测结果及性能变化。
- 实验或效果：发现模拟调用率低于1%，误用率约15%，性能下降最高5%，瓶颈在于决策、解释和整合能力。

## 摘要（原文）

> Agents built on vision-language models increasingly face tasks that demand anticipating future states rather than relying on short-horizon reasoning. Generative world models offer a promising remedy: agents could use them as external simulators to foresee outcomes before acting. This paper empirically examines whether current agents can leverage such world models as tools to enhance their cognition. Across diverse agentic and visual question answering tasks, we observe that some agents rarely invoke simulation (fewer than 1%), frequently misuse predicted rollouts (approximately 15%), and often exhibit inconsistent or even degraded performance (up to 5%) when simulation is available or enforced. Attribution analysis further indicates that the primary bottleneck lies in the agents' capacity to decide when to simulate, how to interpret predicted outcomes, and how to integrate foresight into downstream reasoning. These findings underscore the need for mechanisms that foster calibrated, strategic interaction with world models, paving the way toward more reliable anticipatory cognition in future agent systems.

