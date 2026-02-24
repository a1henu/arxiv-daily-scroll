---
layout: default
title: NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning
---

# NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning
**arXiv**：[2602.20119v1](https://arxiv.org/abs/2602.20119) · [PDF](https://arxiv.org/pdf/2602.20119.pdf)  
**作者**：Jiahui Fu, Junyu Nan, Lingfeng Sun, Hongyu Li, Jianing Qian, Jennifer L. Barry, Kris Kitani, George Konidaris  

**一句话要点**：提出NovaPlan框架，通过闭环视频语言规划实现零样本长时程机器人操作。

**关键词**：零样本学习, 长时程操作, 视觉语言模型, 视频规划, 机器人执行, 错误恢复

## 3 点简述
- 核心问题：长时程任务需结合高层语义推理与低层物理交互，现有模型缺乏物理基础。
- 方法要点：分层框架统一闭环VLM与视频规划，利用关键点和手部姿态作为运动先验。
- 实验效果：在复杂装配任务中展示零样本执行和错误恢复能力，无需演示或训练。

## 摘要（原文）

> Solving long-horizon tasks requires robots to integrate high-level semantic reasoning with low-level physical interaction. While vision-language models (VLMs) and video generation models can decompose tasks and imagine outcomes, they often lack the physical grounding necessary for real-world execution. We introduce NovaPlan, a hierarchical framework that unifies closed-loop VLM and video planning with geometrically grounded robot execution for zero-shot long-horizon manipulation. At the high level, a VLM planner decomposes tasks into sub-goals and monitors robot execution in a closed loop, enabling the system to recover from single-step failures through autonomous re-planning. To compute low-level robot actions, we extract and utilize both task-relevant object keypoints and human hand poses as kinematic priors from the generated videos, and employ a switching mechanism to choose the better one as a reference for robot actions, maintaining stable execution even under heavy occlusion or depth inaccuracy. We demonstrate the effectiveness of NovaPlan on three long-horizon tasks and the Functional Manipulation Benchmark (FMB). Our results show that NovaPlan can perform complex assembly tasks and exhibit dexterous error recovery behaviors without any prior demonstrations or training. Project page: https://nova-plan.github.io/

