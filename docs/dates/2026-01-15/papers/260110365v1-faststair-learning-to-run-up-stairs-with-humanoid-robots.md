---
layout: default
title: FastStair: Learning to Run Up Stairs with Humanoid Robots
---

# FastStair: Learning to Run Up Stairs with Humanoid Robots
**arXiv**：[2601.10365v1](https://arxiv.org/abs/2601.10365) · [PDF](https://arxiv.org/pdf/2601.10365.pdf)  
**作者**：Yan Liu, Tao Yu, Haolin Song, Hongbo Zhu, Nianzong Hu, Yuzhi Hao, Xiuyong Yao, Xizhe Zang, Hua Chen, Jie Zhao  

**一句话要点**：提出FastStair框架，结合规划器与强化学习，实现人形机器人快速稳定上楼梯。

**关键词**：人形机器人控制, 强化学习, 运动规划, 楼梯攀爬, LoRA微调

## 3 点简述
- 核心问题：人形机器人上楼梯需高敏捷性与严格稳定性，传统方法易导致不安全或保守运动。
- 方法要点：集成基于模型的立足点规划器引导RL训练，通过LoRA整合速度专家策略，平衡安全与速度。
- 实验或效果：在Oli机器人上实现最高1.65 m/s上楼梯速度，12秒完成33级螺旋楼梯，竞赛中夺冠。

## 摘要（原文）

> Running up stairs is effortless for humans but remains extremely challenging for humanoid robots due to the simultaneous requirements of high agility and strict stability. Model-free reinforcement learning (RL) can generate dynamic locomotion, yet implicit stability rewards and heavy reliance on task-specific reward shaping tend to result in unsafe behaviors, especially on stairs; conversely, model-based foothold planners encode contact feasibility and stability structure, but enforcing their hard constraints often induces conservative motion that limits speed. We present FastStair, a planner-guided, multi-stage learning framework that reconciles these complementary strengths to achieve fast and stable stair ascent. FastStair integrates a parallel model-based foothold planner into the RL training loop to bias exploration toward dynamically feasible contacts and to pretrain a safety-focused base policy. To mitigate planner-induced conservatism and the discrepancy between low- and high-speed action distributions, the base policy was fine-tuned into speed-specialized experts and then integrated via Low-Rank Adaptation (LoRA) to enable smooth operation across the full commanded-speed range. We deploy the resulting controller on the Oli humanoid robot, achieving stable stair ascent at commanded speeds up to 1.65 m/s and traversing a 33-step spiral staircase (17 cm rise per step) in 12 s, demonstrating robust high-speed performance on long staircases. Notably, the proposed approach served as the champion solution in the Canton Tower Robot Run Up Competition.

