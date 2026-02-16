---
layout: default
title: Scaling Single Human Demonstrations for Imitation Learning using Generative Foundational Models
---

# Scaling Single Human Demonstrations for Imitation Learning using Generative Foundational Models
**arXiv**：[2602.12734v1](https://arxiv.org/abs/2602.12734) · [PDF](https://arxiv.org/pdf/2602.12734.pdf)  
**作者**：Nick Heppert, Minh Quang Nguyen, Abhinav Valada  

**一句话要点**：提出Real2Gen方法，利用生成基础模型从单个人类演示扩展数据以训练机器人模仿学习策略。

**关键词**：模仿学习, 生成基础模型, 机器人操作, 数据扩展, 流匹配策略, 零样本迁移

## 3 点简述
- 核心问题：机器人模仿学习依赖耗时的人工演示，而人类演示数据丰富但难以直接迁移。
- 方法要点：从人类演示提取信息，在模拟环境中通过可编程专家生成无限数据，训练流匹配策略。
- 实验或效果：在三个真实任务中，成功率平均提升26.6%，并实现零样本部署，提升泛化能力。

## 摘要（原文）

> Imitation learning is a popular paradigm to teach robots new tasks, but collecting robot demonstrations through teleoperation or kinesthetic teaching is tedious and time-consuming. In contrast, directly demonstrating a task using our human embodiment is much easier and data is available in abundance, yet transfer to the robot can be non-trivial. In this work, we propose Real2Gen to train a manipulation policy from a single human demonstration. Real2Gen extracts required information from the demonstration and transfers it to a simulation environment, where a programmable expert agent can demonstrate the task arbitrarily many times, generating an unlimited amount of data to train a flow matching policy. We evaluate Real2Gen on human demonstrations from three different real-world tasks and compare it to a recent baseline. Real2Gen shows an average increase in the success rate of 26.6% and better generalization of the trained policy due to the abundance and diversity of training data. We further deploy our purely simulation-trained policy zero-shot in the real world. We make the data, code, and trained models publicly available at real2gen.cs.uni-freiburg.de.

