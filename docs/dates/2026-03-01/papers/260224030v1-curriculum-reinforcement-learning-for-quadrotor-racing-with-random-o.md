---
layout: default
title: Curriculum Reinforcement Learning for Quadrotor Racing with Random Obstacles
---

# Curriculum Reinforcement Learning for Quadrotor Racing with Random Obstacles
**arXiv**：[2602.24030v1](https://arxiv.org/abs/2602.24030) · [PDF](https://arxiv.org/pdf/2602.24030.pdf)  
**作者**：Fangyu Sun, Fanxing Li, Yu Hu, Linzuo Zhang, Yueqian Liu, Wenxian Yu, Danping Zou  

**一句话要点**：提出基于视觉的课程强化学习框架，以解决无人机竞速中随机障碍物的鲁棒控制问题。

**关键词**：无人机竞速, 课程强化学习, 障碍物避障, 端到端控制, 领域随机化

## 3 点简述
- 核心问题：现有无人机竞速研究多忽略障碍物，导致真实环境中成功率低、鲁棒性差。
- 方法要点：结合多阶段课程学习、领域随机化和多场景更新策略，训练端到端控制网络。
- 实验或效果：硬件在环和真实实验显示，该方法在障碍物丰富环境中实现更快圈速和更高成功率。

## 摘要（原文）

> Autonomous drone racing has attracted increasing interest as a research topic for exploring the limits of agile flight. However, existing studies primarily focus on obstacle-free racetracks, while the perception and dynamic challenges introduced by obstacles remain underexplored, often resulting in low success rates and limited robustness in real-world flight. To this end, we propose a novel vision-based curriculum reinforcement learning framework for training a robust controller capable of addressing unseen obstacles in drone racing. We combine multi-stage cu rriculum learning, domain randomization, and a multi-scene updating strategy to address the conflicting challenges of obstacle avoidance and gate traversal. Our end-to-end control policy is implemented as a single network, allowing high-speed flight of quadrotors in environments with variable obstacles. Both hardware-in-the-loop and real-world experiments demonstrate that our method achieves faster lap times and higher success rates than existing approaches, effectively advancing drone racing in obstacle-rich environments. The video and code are available at: https://github.com/SJTU-ViSYS-team/CRL-Drone-Racing.

