---
layout: default
title: Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
---

# Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
**arXiv**：[2601.04575v1](https://arxiv.org/abs/2601.04575) · [PDF](https://arxiv.org/pdf/2601.04575.pdf)  
**作者**：Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J Hunt  

**一句话要点**：提出开放的行为克隆模型，用于实时视频游戏，并研究其因果推理的缩放规律。

**关键词**：行为克隆, 视频游戏AI, 因果推理, 缩放规律, 实时推理, 开放模型

## 3 点简述
- 核心问题：行为克隆在视频游戏任务中如何通过缩放模型和数据规模提升性能与因果推理能力。
- 方法要点：发布开放训练方案，包括数据、代码和预训练模型，支持实时推理。
- 实验或效果：在玩具问题和1.2B参数模型中验证缩放能增强因果推理，模型表现与人类竞争。

## 摘要（原文）

> Behavior cloning is enjoying a resurgence in popularity as scaling both model and data sizes proves to provide a strong starting point for many tasks of interest. In this work, we introduce an open recipe for training a video game playing foundation model designed for inference in realtime on a consumer GPU. We release all data (8300+ hours of high quality human gameplay), training and inference code, and pretrained checkpoints under an open license. We show that our best model is capable of playing a variety of 3D video games at a level competitive with human play. We use this recipe to systematically examine the scaling laws of behavior cloning to understand how the model's performance and causal reasoning varies with model and data scale. We first show in a simple toy problem that, for some types of causal reasoning, increasing both the amount of training data and the depth of the network results in the model learning a more causal policy. We then systematically study how causality varies with the number of parameters (and depth) and training steps in scaled models of up to 1.2 billion parameters, and we find similar scaling results to what we observe in the toy problem.

