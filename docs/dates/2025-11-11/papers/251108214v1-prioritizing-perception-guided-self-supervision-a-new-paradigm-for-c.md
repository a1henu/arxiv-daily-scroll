---
layout: default
title: Prioritizing Perception-Guided Self-Supervision: A New Paradigm for Causal Modeling in End-to-End Autonomous Driving
---

# Prioritizing Perception-Guided Self-Supervision: A New Paradigm for Causal Modeling in End-to-End Autonomous Driving
**arXiv**：[2511.08214v1](https://arxiv.org/abs/2511.08214) · [PDF](https://arxiv.org/pdf/2511.08214.pdf)  
**作者**：Yi Huang, Zhan Qu, Lihui Jiang, Bingbing Liu, Hongbo Zhang  

**一句话要点**：提出感知引导自监督范式以解决端到端自动驾驶中的因果混淆问题

**关键词**：端到端自动驾驶, 因果建模, 自监督学习, 感知引导, 闭环评估, 模仿学习

## 3 点简述
- 核心问题：模仿学习依赖专家轨迹导致因果混淆，影响闭环性能。
- 方法要点：利用感知输出作为监督信号，建模环境与驾驶动作的因果关系。
- 实验或效果：在Bench2Drive基准上，驾驶分数达78.08，显著优于现有方法。

## 摘要（原文）

> End-to-end autonomous driving systems, predominantly trained through imitation learning, have demonstrated considerable effectiveness in leveraging large-scale expert driving data. Despite their success in open-loop evaluations, these systems often exhibit significant performance degradation in closed-loop scenarios due to causal confusion. This confusion is fundamentally exacerbated by the overreliance of the imitation learning paradigm on expert trajectories, which often contain unattributable noise and interfere with the modeling of causal relationships between environmental contexts and appropriate driving actions.
>   To address this fundamental limitation, we propose Perception-Guided Self-Supervision (PGS) - a simple yet effective training paradigm that leverages perception outputs as the primary supervisory signals, explicitly modeling causal relationships in decision-making. The proposed framework aligns both the inputs and outputs of the decision-making module with perception results, such as lane centerlines and the predicted motions of surrounding agents, by introducing positive and negative self-supervision for the ego trajectory. This alignment is specifically designed to mitigate causal confusion arising from the inherent noise in expert trajectories.
>   Equipped with perception-driven supervision, our method, built on a standard end-to-end architecture, achieves a Driving Score of 78.08 and a mean success rate of 48.64% on the challenging closed-loop Bench2Drive benchmark, significantly outperforming existing state-of-the-art methods, including those employing more complex network architectures and inference pipelines. These results underscore the effectiveness and robustness of the proposed PGS framework and point to a promising direction for addressing causal confusion and enhancing real-world generalization in autonomous driving.

