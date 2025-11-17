---
layout: default
title: AdaptPNP: Integrating Prehensile and Non-Prehensile Skills for Adaptive Robotic Manipulation
---

# AdaptPNP: Integrating Prehensile and Non-Prehensile Skills for Adaptive Robotic Manipulation
**arXiv**：[2511.11052v1](https://arxiv.org/abs/2511.11052) · [PDF](https://arxiv.org/pdf/2511.11052.pdf)  
**作者**：Jinxuan Zhu, Chenrui Tie, Xinyi Cao, Yuran Wang, Jingxiang Guo, Zixuan Chen, Haonan Chen, Junting Chen, Yangyu Xiao, Ruihai Wu, Lin Shao  

**一句话要点**：提出AdaptPNP框架，集成抓取与非抓取技能以实现自适应机器人操作

**关键词**：机器人操作, 视觉语言模型, 任务与运动规划, 数字孪生, 自适应控制

## 3 点简述
- 核心问题：统一框架难以泛化任务、对象和环境，并融合抓取与非抓取动作
- 方法要点：利用视觉语言模型生成高层计划，结合数字孪生预测对象姿态
- 实验或效果：在仿真和真实环境中评估混合操作任务，展示泛化潜力

## 摘要（原文）

> Non-prehensile (NP) manipulation, in which robots alter object states without forming stable grasps (for example, pushing, poking, or sliding), significantly broadens robotic manipulation capabilities when grasping is infeasible or insufficient. However, enabling a unified framework that generalizes across different tasks, objects, and environments while seamlessly integrating non-prehensile and prehensile (P) actions remains challenging: robots must determine when to invoke NP skills, select the appropriate primitive for each context, and compose P and NP strategies into robust, multi-step plans. We introduce ApaptPNP, a vision-language model (VLM)-empowered task and motion planning framework that systematically selects and combines P and NP skills to accomplish diverse manipulation objectives. Our approach leverages a VLM to interpret visual scene observations and textual task descriptions, generating a high-level plan skeleton that prescribes the sequence and coordination of P and NP actions. A digital-twin based object-centric intermediate layer predicts desired object poses, enabling proactive mental rehearsal of manipulation sequences. Finally, a control module synthesizes low-level robot commands, with continuous execution feedback enabling online task plan refinement and adaptive replanning through the VLM. We evaluate ApaptPNP across representative P&NP hybrid manipulation tasks in both simulation and real-world environments. These results underscore the potential of hybrid P&NP manipulation as a crucial step toward general-purpose, human-level robotic manipulation capabilities. Project Website: https://sites.google.com/view/adaptpnp/home

