---
layout: default
title: RESample: A Robust Data Augmentation Framework via Exploratory Sampling for Robotic Manipulation
---

# RESample: A Robust Data Augmentation Framework via Exploratory Sampling for Robotic Manipulation
**arXiv**：[2510.17640v1](https://arxiv.org/abs/2510.17640) · [PDF](https://arxiv.org/pdf/2510.17640.pdf)  
**作者**：Yuquan Xue, Guanxing Lu, Zhenyu Wu, Chuanrui Zhang, Bofang Jia, Zhengyi Gu, Yansong Tang, Ziwei Wang  

**一句话要点**：提出RESample框架，通过探索性采样增强机器人操作中视觉-语言-动作模型的鲁棒性。

**关键词**：机器人操作, 数据增强, 视觉-语言-动作模型, 离线强化学习, 分布外状态, 探索性采样

## 3 点简述
- 核心问题：模仿学习数据集缺乏失败和恢复数据，导致模型在分布外状态表现不佳。
- 方法要点：利用离线强化学习识别次优动作，并通过探索性采样自动扩充OOD数据。
- 实验或效果：在LIBERO基准和真实任务中验证，提升模型稳定性和泛化能力。

## 摘要（原文）

> Vision-Language-Action models (VLAs) have demonstrated remarkable performance
> on complex robotic manipulation tasks through imitation learning. However,
> existing imitation learning datasets contain only successful trajectories and
> lack failure or recovery data, especially for out-of-distribution (OOD) states
> where the robot deviates from the main policy due to minor perturbations or
> errors, leading VLA models to struggle with states deviating from the training
> distribution. To this end, we propose an automated OOD data augmentation
> framework named RESample through exploratory sampling. Specifically, we first
> leverage offline reinforcement learning to obtain an action-value network that
> accurately identifies sub-optimal actions under the current manipulation
> policy. We further sample potential OOD states from trajectories via rollout,
> and design an exploratory sampling mechanism that adaptively incorporates these
> action proxies into the training dataset to ensure efficiency. Subsequently,
> our framework explicitly encourages the VLAs to recover from OOD states and
> enhances their robustness against distributional shifts. We conduct extensive
> experiments on the LIBERO benchmark as well as real-world robotic manipulation
> tasks, demonstrating that RESample consistently improves the stability and
> generalization ability of VLA models.

