---
layout: default
title: RoboReward: General-Purpose Vision-Language Reward Models for Robotics
---

# RoboReward: General-Purpose Vision-Language Reward Models for Robotics
**arXiv**：[2601.00675v1](https://arxiv.org/abs/2601.00675) · [PDF](https://arxiv.org/pdf/2601.00675.pdf)  
**作者**：Tony Lee, Andrew Wagenmaker, Karl Pertsch, Percy Liang, Sergey Levine, Chelsea Finn  

**一句话要点**：提出RoboReward数据集与视觉语言奖励模型，以解决机器人强化学习中奖励设计难题。

**关键词**：视觉语言模型, 机器人奖励设计, 强化学习, 负例数据增强, 真实机器人数据集

## 3 点简述
- 核心问题：真实机器人任务中，奖励设计依赖人工标注或脆弱的手工目标，视觉语言模型作为自动奖励模型的效果未知。
- 方法要点：构建基于大规模真实机器人数据的RoboReward数据集，通过负例数据增强生成校准的失败和近失败示例。
- 实验或效果：训练4B/8B参数模型在短视界任务中优于更大视觉语言模型，并在真实机器人强化学习中显著提升策略学习效果。

## 摘要（原文）

> A well-designed reward is critical for effective reinforcement learning-based policy improvement. In real-world robotic domains, obtaining such rewards typically requires either labor-intensive human labeling or brittle, handcrafted objectives. Vision-language models (VLMs) have shown promise as automatic reward models, yet their effectiveness on real robot tasks is poorly understood. In this work, we aim to close this gap by introducing (1) \textbf{RoboReward}, a robotics reward dataset and benchmark built on large-scale real-robot corpora from Open X-Embodiment (OXE) and RoboArena, and (2) vision-language reward models trained on this dataset (RoboReward 4B/8B). Because OXE is success-heavy and lacks failure examples, we propose a \emph{negative examples data augmentation} pipeline that generates calibrated \emph{negatives} and \emph{near-misses} via counterfactual relabeling of successful episodes and temporal clipping to create partial-progress outcomes from the same videos. Using this framework, we produce an extensive training and evaluation dataset that spans diverse tasks and embodiments and enables systematic evaluation of whether state-of-the-art VLMs can reliably provide rewards for robotics. Our evaluation of leading open-weight and proprietary VLMs reveals that no model excels across all tasks, underscoring substantial room for improvement. We then train general-purpose 4B- and 8B-parameter models that outperform much larger VLMs in assigning rewards for short-horizon robotic tasks. Finally, we deploy the 8B-parameter reward VLM in real-robot reinforcement learning and find that it improves policy learning over Gemini Robotics-ER 1.5, a frontier physical reasoning VLM trained on robotics data, by a large margin, while substantially narrowing the gap to RL training with human-provided rewards.

