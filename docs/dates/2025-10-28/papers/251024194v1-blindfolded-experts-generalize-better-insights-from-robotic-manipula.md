---
layout: default
title: Blindfolded Experts Generalize Better: Insights from Robotic Manipulation and Videogames
---

# Blindfolded Experts Generalize Better: Insights from Robotic Manipulation and Videogames
**arXiv**：[2510.24194v1](https://arxiv.org/abs/2510.24194) · [PDF](https://arxiv.org/pdf/2510.24194.pdf)  
**作者**：Ev Zisselman, Mirco Mutti, Shelly Francis-Meretzki, Elisei Shafer, Aviv Tamar  

**一句话要点**：提出盲视专家行为克隆方法，以提升机器人操作和视频游戏中的泛化能力。

**关键词**：行为克隆, 机器人操作, 泛化学习, 探索策略, 任务信息隐藏

## 3 点简述
- 行为克隆泛化需大量演示，但全信息专家演示可能限制泛化。
- 方法隐藏任务信息，迫使专家探索，克隆其行为以提升泛化。
- 实验在机器人插入任务和Procgen游戏验证，理论分析支持泛化误差与信息量相关。

## 摘要（原文）

> Behavioral cloning is a simple yet effective technique for learning
> sequential decision-making from demonstrations. Recently, it has gained
> prominence as the core of foundation models for the physical world, where
> achieving generalization requires countless demonstrations of a multitude of
> tasks. Typically, a human expert with full information on the task demonstrates
> a (nearly) optimal behavior. In this paper, we propose to hide some of the
> task's information from the demonstrator. This ``blindfolded'' expert is
> compelled to employ non-trivial exploration to solve the task. We show that
> cloning the blindfolded expert generalizes better to unseen tasks than its
> fully-informed counterpart. We conduct experiments of real-world robot peg
> insertion tasks with (limited) human demonstrations, alongside videogames from
> the Procgen benchmark. Additionally, we support our findings with theoretical
> analysis, which confirms that the generalization error scales with
> $\sqrt{I/m}$, where $I$ measures the amount of task information available to
> the demonstrator, and $m$ is the number of demonstrated tasks. Both theory and
> practice indicate that cloning blindfolded experts generalizes better with
> fewer demonstrated tasks. Project page with videos and code:
> https://sites.google.com/view/blindfoldedexperts/home

