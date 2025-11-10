---
layout: default
title: Let Me Show You: Learning by Retrieving from Egocentric Video for Robotic Manipulation
---

# Let Me Show You: Learning by Retrieving from Egocentric Video for Robotic Manipulation
**arXiv**：[2511.05199v1](https://arxiv.org/abs/2511.05199) · [PDF](https://arxiv.org/pdf/2511.05199.pdf)  
**作者**：Yichen Zhu, Feifei Feng  

**一句话要点**：提出从视频检索方法以解决机器人操作任务学习问题

**关键词**：机器人操作, 视频检索, 物体可操作掩码, 手部轨迹, 策略生成, 泛化学习

## 3 点简述
- 核心问题：机器人在复杂环境中学习操作任务时依赖大量数据，缺乏人类式视频学习能力。
- 方法要点：构建视频库，提取物体可操作掩码和手部轨迹，结合检索器和策略生成器。
- 实验或效果：在模拟和真实环境中测试，性能优于传统系统，提升泛化能力。

## 摘要（原文）

> Robots operating in complex and uncertain environments face considerable
> challenges. Advanced robotic systems often rely on extensive datasets to learn
> manipulation tasks. In contrast, when humans are faced with unfamiliar tasks,
> such as assembling a chair, a common approach is to learn by watching video
> demonstrations. In this paper, we propose a novel method for learning robot
> policies by Retrieving-from-Video (RfV), using analogies from human
> demonstrations to address manipulation tasks. Our system constructs a video
> bank comprising recordings of humans performing diverse daily tasks. To enrich
> the knowledge from these videos, we extract mid-level information, such as
> object affordance masks and hand motion trajectories, which serve as additional
> inputs to enhance the robot model's learning and generalization capabilities.
> We further feature a dual-component system: a video retriever that taps into an
> external video bank to fetch task-relevant video based on task specification,
> and a policy generator that integrates this retrieved knowledge into the
> learning cycle. This approach enables robots to craft adaptive responses to
> various scenarios and generalize to tasks beyond those in the training data.
> Through rigorous testing in multiple simulated and real-world settings, our
> system demonstrates a marked improvement in performance over conventional
> robotic systems, showcasing a significant breakthrough in the field of
> robotics.

