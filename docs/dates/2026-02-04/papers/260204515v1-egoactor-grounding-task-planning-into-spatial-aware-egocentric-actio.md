---
layout: default
title: EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models
---

# EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models
**arXiv**：[2602.04515v1](https://arxiv.org/abs/2602.04515) · [PDF](https://arxiv.org/pdf/2602.04515.pdf)  
**作者**：Yu Bai, MingMing Yu, Chaojie Li, Ziyi Bai, Xinlong Wang, Börje F. Karlsson  

**一句话要点**：提出EgoActor视觉语言模型，以解决人形机器人在部分观测动态环境中将高层指令接地为空间感知动作的挑战。

**关键词**：人形机器人, 视觉语言模型, 任务规划, 空间感知动作, 实时执行, 泛化能力

## 3 点简述
- 核心问题：人形机器人在真实世界部署需整合感知、移动和操作，面临部分信息观测和动态环境变化。
- 方法要点：引入EgoActor统一视觉语言模型，预测移动、头部运动、操作命令和交互，利用真实世界RGB数据、空间推理问答和模拟演示进行监督。
- 实验或效果：在模拟和真实环境中评估，模型能稳健决策、流畅推理（<1秒），并泛化到未见任务和环境。

## 摘要（原文）

> Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments. As well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

