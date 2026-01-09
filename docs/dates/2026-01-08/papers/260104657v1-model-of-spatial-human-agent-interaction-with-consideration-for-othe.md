---
layout: default
title: Model of Spatial Human-Agent Interaction with Consideration for Others
---

# Model of Spatial Human-Agent Interaction with Consideration for Others
**arXiv**：[2601.04657v1](https://arxiv.org/abs/2601.04657) · [PDF](https://arxiv.org/pdf/2601.04657.pdf)  
**作者**：Takafumi Sakamoto, Yugo Takeuchi  

**一句话要点**：提出考虑他人的空间交互模型，以优化公共空间中机器人对话启动

**关键词**：空间交互模型, 人机交互, 虚拟现实实验, 沟通意愿估计, 公共空间机器人

## 3 点简述
- 核心问题：公共空间机器人需启动对话且不干扰行人，需平衡沟通需求与干扰风险。
- 方法要点：构建计算模型，通过量化参数调整内部状态以估计他人沟通意愿。
- 实验或效果：VR实验验证模型，低考虑值机器人抑制参与者移动，高值则不抑制。

## 摘要（原文）

> Communication robots often need to initiate conversations with people in public spaces. At the same time, such robots must not disturb pedestrians. To handle these two requirements, an agent needs to estimate the communication desires of others based on their behavior and then adjust its own communication activities accordingly. In this study, we construct a computational spatial interaction model that considers others. Consideration is expressed as a quantitative parameter: the amount of adjustment of one's internal state to the estimated internal state of the other. To validate the model, we experimented with a human and a virtual robot interacting in a VR environment. The results show that when the participant moves to the target, a virtual robot with a low consideration value inhibits the participant's movement, while a robot with a higher consideration value did not inhibit the participant's movement. When the participant approached the robot, the robot also exhibited approaching behavior, regardless of the consideration value, thus decreasing the participant's movement. These results appear to verify the proposed model's ability to clarify interactions with consideration for others.

