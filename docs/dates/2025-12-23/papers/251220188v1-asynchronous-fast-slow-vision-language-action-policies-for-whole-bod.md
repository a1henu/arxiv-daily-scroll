---
layout: default
title: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation
---

# Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation
**arXiv**：[2512.20188v1](https://arxiv.org/abs/2512.20188) · [PDF](https://arxiv.org/pdf/2512.20188.pdf)  
**作者**：Teqiang Zou, Hongliang Zeng, Yuxuan Nong, Yifan Li, Kehui Liu, Haotian Yang, Xinyang Ling, Xin Li, Lianyang Ma  

**一句话要点**：提出异步快慢视觉-语言-动作框架以解决全身机器人操控中同步执行限制性能的问题

**关键词**：异步执行, 视觉-语言-动作策略, 全身机器人操控, 潜在表示缓冲, 动作分词器, 端到端训练

## 3 点简述
- 核心问题：现有VLA系统因视觉语言模型推理慢，强制同步执行限制控制稳定性和实时性
- 方法要点：设计异步快慢双通路，通过潜在表示缓冲和全身动作分词器实现高频动作生成与丰富语义推理解耦
- 实验或效果：在真实世界全身操控实验中，相比同步基线，任务成功率提升，响应性显著增强

## 摘要（原文）

> Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

