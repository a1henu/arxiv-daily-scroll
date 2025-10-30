---
layout: default
title: Using VLM Reasoning to Constrain Task and Motion Planning
---

# Using VLM Reasoning to Constrain Task and Motion Planning
**arXiv**：[2510.25548v1](https://arxiv.org/abs/2510.25548) · [PDF](https://arxiv.org/pdf/2510.25548.pdf)  
**作者**：Muyang Yan, Miras Mengdibayev, Ardon Floros, Weihang Guo, Lydia E. Kavraki, Zachary Kingston  

**一句话要点**：提出VIZ-COAST方法，利用视觉语言模型推理约束任务与运动规划，减少失败。

**关键词**：任务与运动规划, 视觉语言模型, 空间推理, 约束提取, 机器人规划

## 3 点简述
- 任务与运动规划中，抽象世界可能导致任务计划在细化时失败，需重新规划。
- 利用预训练视觉语言模型进行常识空间推理，提前识别细化问题，避免失败。
- 实验显示，方法提取约束减少规划时间，在某些情况下消除细化失败。

## 摘要（原文）

> In task and motion planning, high-level task planning is done over an
> abstraction of the world to enable efficient search in long-horizon robotics
> problems. However, the feasibility of these task-level plans relies on the
> downward refinability of the abstraction into continuous motion. When a
> domain's refinability is poor, task-level plans that appear valid may
> ultimately fail during motion planning, requiring replanning and resulting in
> slower overall performance. Prior works mitigate this by encoding refinement
> issues as constraints to prune infeasible task plans. However, these approaches
> only add constraints upon refinement failure, expending significant search
> effort on infeasible branches. We propose VIZ-COAST, a method of leveraging the
> common-sense spatial reasoning of large pretrained Vision-Language Models to
> identify issues with downward refinement a priori, bypassing the need to fix
> these failures during planning. Experiments on two challenging TAMP domains
> show that our approach is able to extract plausible constraints from images and
> domain descriptions, drastically reducing planning times and, in some cases,
> eliminating downward refinement failures altogether, generalizing to a diverse
> range of instances from the broader domain.

