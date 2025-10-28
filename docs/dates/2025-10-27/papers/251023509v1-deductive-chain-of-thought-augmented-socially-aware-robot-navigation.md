---
layout: default
title: Deductive Chain-of-Thought Augmented Socially-aware Robot Navigation World Model
---

# Deductive Chain-of-Thought Augmented Socially-aware Robot Navigation World Model
**arXiv**：[2510.23509v1](https://arxiv.org/abs/2510.23509) · [PDF](https://arxiv.org/pdf/2510.23509.pdf)  
**作者**：Weizheng Wang, Obi Ike, Soyun Choi, Sungeun Hong, Byung-Cheol Min  

**一句话要点**：提出NaviWM世界模型以增强社交机器人导航的安全性和合规性

**关键词**：社交机器人导航, 世界模型, 演绎推理, LLM增强, 安全导航, 逻辑编码

## 3 点简述
- 核心问题：LLM在社交导航中因缺乏物理基础和逻辑一致性导致行为不可预测
- 方法要点：结合空间-时间世界模型和演绎推理模块，使用一阶逻辑编码社会规范
- 实验或效果：在拥挤环境中提高成功率并减少社交违规，验证了方法的有效性

## 摘要（原文）

> Social robot navigation increasingly relies on large language models for
> reasoning, path planning, and enabling movement in dynamic human spaces.
> However, relying solely on LLMs for planning often leads to unpredictable and
> unsafe behaviors, especially in dynamic human spaces, due to limited physical
> grounding and weak logical consistency. In this work, we introduce NaviWM, a
> socially-aware robot Navigation World Model that augments LLM reasoning with a
> structured world model and a logic-driven chain-of-thought process. NaviWM
> consists of two main components: (1) a spatial-temporal world model that
> captures the positions, velocities, and activities of agents in the
> environment, and (2) a deductive reasoning module that guides LLMs through a
> multi-step, logic-based inference process. This integration enables the robot
> to generate navigation decisions that are both socially compliant and
> physically safe, under well-defined constraints such as personal space,
> collision avoidance, and timing. Unlike previous methods based on prompting or
> fine-tuning, NaviWM encodes social norms as first-order logic, enabling
> interpretable and verifiable reasoning. Experiments show that NaviWM improves
> success rates and reduces social violations, particularly in crowded
> environments. These results demonstrate the benefit of combining formal
> reasoning with LLMs for robust social navigation. Additional experimental
> details and demo videos for this work can be found at:
> https://sites.google.com/view/NaviWM.

