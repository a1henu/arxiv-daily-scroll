---
layout: default
title: Replay Failures as Successes: Sample-Efficient Reinforcement Learning for Instruction Following
---

# Replay Failures as Successes: Sample-Efficient Reinforcement Learning for Instruction Following
**arXiv**：[2512.23457v1](https://arxiv.org/abs/2512.23457) · [PDF](https://arxiv.org/pdf/2512.23457.pdf)  
**作者**：Kongcheng Zhang, Qi Yao, Shunyu Liu, Wenjian Zhang, Min Cen, Yang Zhou, Wenkai Fang, Yiru Zhao, Baisheng Lai, Mingli Song  

**一句话要点**：提出Hindsight instruction Replay以解决指令跟随任务中强化学习样本效率低的问题

**关键词**：指令跟随, 强化学习, 样本效率, 奖励稀疏, 重放策略, 双偏好学习

## 3 点简述
- 核心问题：初始模型因能力有限难以生成满足约束的响应，导致奖励稀疏阻碍学习
- 方法要点：采用选择-重写策略，将失败尝试基于已满足约束重放为成功样本
- 实验或效果：在多种指令跟随任务中取得良好结果，且计算成本更低

## 摘要（原文）

> Reinforcement Learning (RL) has shown promise for aligning Large Language Models (LLMs) to follow instructions with various constraints. Despite the encouraging results, RL improvement inevitably relies on sampling successful, high-quality responses; however, the initial model often struggles to generate responses that satisfy all constraints due to its limited capabilities, yielding sparse or indistinguishable rewards that impede learning. In this work, we propose Hindsight instruction Replay (HiR), a novel sample-efficient RL framework for complex instruction following tasks, which employs a select-then-rewrite strategy to replay failed attempts as successes based on the constraints that have been satisfied in hindsight. We perform RL on these replayed samples as well as the original ones, theoretically framing the objective as dual-preference learning at both the instruction- and response-level to enable efficient optimization using only a binary reward signal. Extensive experiments demonstrate that the proposed HiR yields promising results across different instruction following tasks, while requiring less computational budget. Our code and dataset is available at https://github.com/sastpg/HIR.

