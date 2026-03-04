---
layout: default
title: Give me scissors: Collision-Free Dual-Arm Surgical Assistive Robot for Instrument Delivery
---

# Give me scissors: Collision-Free Dual-Arm Surgical Assistive Robot for Instrument Delivery
**arXiv**：[2603.02553v1](https://arxiv.org/abs/2603.02553) · [PDF](https://arxiv.org/pdf/2603.02553.pdf)  
**作者**：Xuejin Luo, Shiquan Sun, Runshi Zhang, Ruizhi Zhang, Junchen Wang  

**一句话要点**：提出碰撞感知双臂手术辅助机器人，基于视觉语言模型实现零样本器械递送

**关键词**：手术辅助机器人, 双臂机器人, 视觉语言模型, 碰撞避免, 二次规划, 器械递送

## 3 点简述
- 问题：现有机器人递送依赖预定义路径，在动态环境中泛化性差且存在安全风险
- 方法：利用视觉语言模型生成零样本抓取与递送轨迹，集成实时障碍物感知于二次规划框架
- 效果：实验验证递送成功率83.33%，所有试验中保持平滑无碰撞运动

## 摘要（原文）

> During surgery, scrub nurses are required to frequently deliver surgical instruments to surgeons, which can lead to physical fatigue and decreased focus. Robotic scrub nurses provide a promising solution that can replace repetitive tasks and enhance efficiency. Existing research on robotic scrub nurses relies on predefined paths for instrument delivery, which limits their generalizability and poses safety risks in dynamic environments. To address these challenges, we present a collision-free dual-arm surgical assistive robot capable of performing instrument delivery. A vision-language model is utilized to automatically generate the robot's grasping and delivery trajectories in a zero-shot manner based on surgeons' instructions. A real-time obstacle minimum distance perception method is proposed and integrated into a unified quadratic programming framework. This framework ensures reactive obstacle avoidance and self-collision prevention during the dual-arm robot's autonomous movement in dynamic environments. Extensive experimental validations demonstrate that the proposed robotic system achieves an 83.33% success rate in surgical instrument delivery while maintaining smooth, collision-free movement throughout all trials. The project page and source code are available at https://give-me-scissors.github.io/.

