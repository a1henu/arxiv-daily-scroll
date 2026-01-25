---
layout: default
title: Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning
---

# Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning
**arXiv**：[2601.16163v1](https://arxiv.org/abs/2601.16163) · [PDF](https://arxiv.org/pdf/2601.16163.pdf)  
**作者**：Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, Yen-Chen Lin, Yunhao Ge, Grace Lam, Percy Liang, Shuran Song, Ming-Yu Liu, Chelsea Finn, Jinwei Gu  

**一句话要点**：提出Cosmos Policy，通过单阶段后训练将预训练视频模型适配为机器人策略，实现视觉运动控制和规划。

**关键词**：视频模型适配, 机器人策略学习, 潜在扩散过程, 视觉运动控制, 模型规划

## 3 点简述
- 核心问题：现有视频模型用于机器人策略学习需多阶段后训练和架构修改，复杂度高。
- 方法要点：直接生成编码为潜在帧的机器人动作，利用预训练先验捕获复杂动作分布，无需架构改动。
- 实验或效果：在LIBERO和RoboCasa仿真基准及真实世界双手机器人任务中达到最先进性能。

## 摘要（原文）

> Recent video generation models demonstrate remarkable ability to capture complex physical interactions and scene evolution over time. To leverage their spatiotemporal priors, robotics works have adapted video models for policy learning but introduce complexity by requiring multiple stages of post-training and new architectural components for action generation. In this work, we introduce Cosmos Policy, a simple approach for adapting a large pretrained video model (Cosmos-Predict2) into an effective robot policy through a single stage of post-training on the robot demonstration data collected on the target platform, with no architectural modifications. Cosmos Policy learns to directly generate robot actions encoded as latent frames within the video model's latent diffusion process, harnessing the model's pretrained priors and core learning algorithm to capture complex action distributions. Additionally, Cosmos Policy generates future state images and values (expected cumulative rewards), which are similarly encoded as latent frames, enabling test-time planning of action trajectories with higher likelihood of success. In our evaluations, Cosmos Policy achieves state-of-the-art performance on the LIBERO and RoboCasa simulation benchmarks (98.5% and 67.1% average success rates, respectively) and the highest average score in challenging real-world bimanual manipulation tasks, outperforming strong diffusion policies trained from scratch, video model-based policies, and state-of-the-art vision-language-action models fine-tuned on the same robot demonstrations. Furthermore, given policy rollout data, Cosmos Policy can learn from experience to refine its world model and value function and leverage model-based planning to achieve even higher success rates in challenging tasks. We release code, models, and training data at https://research.nvidia.com/labs/dir/cosmos-policy/

