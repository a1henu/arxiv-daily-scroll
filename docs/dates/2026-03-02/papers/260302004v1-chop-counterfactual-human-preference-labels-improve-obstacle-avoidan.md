---
layout: default
title: CHOP: Counterfactual Human Preference Labels Improve Obstacle Avoidance in Visuomotor Navigation Policies
---

# CHOP: Counterfactual Human Preference Labels Improve Obstacle Avoidance in Visuomotor Navigation Policies
**arXiv**：[2603.02004v1](https://arxiv.org/abs/2603.02004) · [PDF](https://arxiv.org/pdf/2603.02004.pdf)  
**作者**：Gershom Seneviratne, Jianyu An, Vaibhav Shende, Sahire Ellahy, Yaxita Amin, Kondapi Manasanjani, Samarth Chopra, Jonathan Deepak Kannan, Dinesh Manocha  

**一句话要点**：提出CHOP方法，利用反事实人类偏好标签提升视觉运动导航策略的避障能力

**关键词**：视觉运动导航, 反事实学习, 人类偏好对齐, 避障策略, 机器人导航, 安全感知

## 3 点简述
- 视觉运动导航策略在复杂环境中常面临避障和安全挑战
- CHOP通过人类标注反事实轨迹偏好，微调策略以对齐人类安全直觉
- 实验显示CHOP显著减少碰撞事件，提升避障性能，并在真实机器人部署中验证效果

## 摘要（原文）

> Visuomotor navigation policies have shown strong perception-action coupling for embodied agents, yet they often struggle with safe navigation and dynamic obstacle avoidance in complex real-world environments. We introduce CHOP, a novel approach that leverages Counterfactual Human Preference Labels to align visuomotor navigation policies towards human intuition of safety and obstacle avoidance in navigation. In CHOP, for each visual observation, the robot's executed trajectory is included among a set of counterfactual navigation trajectories: alternative trajectories the robot could have followed under identical conditions. Human annotators provide pairwise preference labels over these trajectories based on anticipated outcomes such as collision risk and path efficiency. These aggregated preferences are then used to fine-tune visuomotor navigation policies, aligning their behavior with human preferences in navigation. Experiments on the SCAND dataset show that visuomotor navigation policies fine-tuned with CHOP reduce near-collision events by 49.7%, decrease deviation from human-preferred trajectories by 45.0%, and increase average obstacle clearance by 19.8% on average across multiple state-of-the-art models, compared to their pretrained baselines. These improvements transfer to real-world deployments on a Ghost Robotics Vision60 quadruped, where CHOP-aligned policies improve average goal success rates by 24.4%, increase minimum obstacle clearance by 6.8%, reduce collision and intervention events by 45.7%, and improve normalized path completion by 38.6% on average across navigation scenarios, compared to their pretrained baselines. Our results highlight the value of counterfactual preference supervision in bridging the gap between large-scale visuomotor policies and human-aligned, safety-aware embodied navigation.

