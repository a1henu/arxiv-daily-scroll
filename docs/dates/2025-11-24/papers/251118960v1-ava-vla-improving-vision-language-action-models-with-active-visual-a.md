---
layout: default
title: AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention
---

# AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention
**arXiv**：[2511.18960v1](https://arxiv.org/abs/2511.18960) · [PDF](https://arxiv.org/pdf/2511.18960.pdf)  
**作者**：Lei Xiao, Jifeng Li, Juntao Gao, Feiyang Ye, Yan Jin, Jingjing Qian, Jing Zhang, Yong Wu, Xiaoyuan Yu  

**一句话要点**：提出AVA-VLA框架，通过主动视觉注意力改进视觉-语言-动作模型在动态决策中的性能。

**关键词**：视觉-语言-动作模型, 主动视觉注意力, 部分可观测马尔可夫决策过程, 机器人基准测试, 模拟到真实迁移

## 3 点简述
- 现有VLA模型在动态序列决策中忽略历史上下文，导致视觉处理效率低下。
- 引入主动视觉注意力模块，利用循环状态动态调制视觉令牌处理。
- 在LIBERO和CALVIN基准测试中达到最优，并在真实机器人平台验证实用性。

## 摘要（原文）

> Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in embodied AI tasks. However, existing VLA models, often built upon Vision-Language Models (VLMs), typically process dense visual inputs independently at each timestep. This approach implicitly models the task as a Markov Decision Process (MDP). However, this history-agnostic design is suboptimal for effective visual token processing in dynamic sequential decision-making, as it fails to leverage the context of history. To address this limitation, we reformulate the problem from a Partially Observable Markov Decision Process (POMDP) perspective and propose a novel framework named AVA-VLA. Inspired by the POMDP that the action generation should be conditioned on the belief state. AVA-VLA introduces Active Visual Attention (AVA) to dynamically modulate visual processing. It achieves this by leveraging the recurrent state, which is a neural approximation of the agent's belief state derived from the previous decision step. Specifically, the AVA module uses the recurrent state to compute the soft weights to actively process task-relevant visual tokens based on its historical context. Comprehensive evaluations demonstrate that AVA-VLA achieves state-of-the-art performance across popular robotic benchmarks, including LIBERO and CALVIN. Furthermore, real-world deployments on a dual-arm robot platform validate the framework's practical applicability and robust sim-to-real transferability.

