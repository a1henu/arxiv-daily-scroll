---
layout: default
title: Selective Perception for Robot: Task-Aware Attention in Multimodal VLA
---

# Selective Perception for Robot: Task-Aware Attention in Multimodal VLA
**arXiv**：[2602.15543v1](https://arxiv.org/abs/2602.15543) · [PDF](https://arxiv.org/pdf/2602.15543.pdf)  
**作者**：Young-Chae Son, Jung-Woo Lee, Yoon-Ji Choi, Dae-Kwan Ko, Soo-Chul Lim  

**一句话要点**：提出动态信息融合框架以提升机器人VLA模型在实时控制中的效率与鲁棒性

**关键词**：机器人视觉语言动作模型, 动态信息融合, 自适应路由, 任务感知注意力, 多视图输入, 实时控制

## 3 点简述
- 核心问题：现有VLA模型采用静态融合处理多视图输入，导致计算冗余和任务无关噪声干扰
- 方法要点：引入轻量级自适应路由架构，基于文本提示和腕部摄像头观测实时预测视图任务相关性，选择性提供视觉特征
- 实验或效果：在真实机器人操作场景中，相比现有VLA模型，显著提升推理效率和操控性能

## 摘要（原文）

> In robotics, Vision-Language-Action (VLA) models that integrate diverse multimodal signals from multi-view inputs have emerged as an effective approach. However, most prior work adopts static fusion that processes all visual inputs uniformly, which incurs unnecessary computational overhead and allows task-irrelevant background information to act as noise. Inspired by the principles of human active perception, we propose a dynamic information fusion framework designed to maximize the efficiency and robustness of VLA models. Our approach introduces a lightweight adaptive routing architecture that analyzes the current text prompt and observations from a wrist-mounted camera in real-time to predict the task-relevance of multiple camera views. By conditionally attenuating computations for views with low informational utility and selectively providing only essential visual features to the policy network, Our framework achieves computation efficiency proportional to task relevance. Furthermore, to efficiently secure large-scale annotation data for router training, we established an automated labeling pipeline utilizing Vision-Language Models (VLMs) to minimize data collection and annotation costs. Experimental results in real-world robotic manipulation scenarios demonstrate that the proposed approach achieves significant improvements in both inference efficiency and control performance compared to existing VLA models, validating the effectiveness and practicality of dynamic information fusion in resource-constrained, real-time robot control environments.

