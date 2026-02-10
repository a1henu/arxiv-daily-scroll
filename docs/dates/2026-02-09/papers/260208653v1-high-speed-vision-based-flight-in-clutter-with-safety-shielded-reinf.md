---
layout: default
title: High-Speed Vision-Based Flight in Clutter with Safety-Shielded Reinforcement Learning
---

# High-Speed Vision-Based Flight in Clutter with Safety-Shielded Reinforcement Learning
**arXiv**：[2602.08653v1](https://arxiv.org/abs/2602.08653) · [PDF](https://arxiv.org/pdf/2602.08653.pdf)  
**作者**：Jiarui Zhang, Chengyong Lei, Chengjiang Dai, Lijie Wang, Zhichao Han, Fei Gao  

**一句话要点**：提出基于安全屏蔽强化学习的端到端框架，实现四旋翼无人机在密集障碍环境中的高速安全飞行。

**关键词**：四旋翼无人机, 强化学习, 安全屏蔽, 端到端导航, 避障算法, 高速飞行

## 3 点简述
- 核心问题：传统模块化方法延迟累积，纯强化学习缺乏形式化安全保证，难以兼顾高速飞行与可靠避障。
- 方法要点：结合物理先验，训练时设计物理信息奖励引导导航，部署时集成实时安全过滤器强制避障约束。
- 实验或效果：在密集障碍和户外森林环境中，实现高达7.5m/s的可靠高速导航，优于传统规划器和可微物理方法。

## 摘要（原文）

> Quadrotor unmanned aerial vehicles (UAVs) are increasingly deployed in complex missions that demand reliable autonomous navigation and robust obstacle avoidance. However, traditional modular pipelines often incur cumulative latency, whereas purely reinforcement learning (RL) approaches typically provide limited formal safety guarantees. To bridge this gap, we propose an end-to-end RL framework augmented with model-based safety mechanisms. We incorporate physical priors in both training and deployment. During training, we design a physics-informed reward structure that provides global navigational guidance. During deployment, we integrate a real-time safety filter that projects the policy outputs onto a provably safe set to enforce strict collision-avoidance constraints. This hybrid architecture reconciles high-speed flight with robust safety assurances. Benchmark evaluations demonstrate that our method outperforms both traditional planners and recent end-to-end obstacle avoidance approaches based on differentiable physics. Extensive experiments demonstrate strong generalization, enabling reliable high-speed navigation in dense clutter and challenging outdoor forest environments at velocities up to 7.5m/s.

