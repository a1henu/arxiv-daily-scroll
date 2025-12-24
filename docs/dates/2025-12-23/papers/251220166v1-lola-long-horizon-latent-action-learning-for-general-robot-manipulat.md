---
layout: default
title: LoLA: Long Horizon Latent Action Learning for General Robot Manipulation
---

# LoLA: Long Horizon Latent Action Learning for General Robot Manipulation
**arXiv**：[2512.20166v1](https://arxiv.org/abs/2512.20166) · [PDF](https://arxiv.org/pdf/2512.20166.pdf)  
**作者**：Xiaofan Wang, Xingyu Gao, Jianlong Fu, Zuolei Li, Dean Fortier, Galen Mullins, Andrey Kolobov, Baining Guo  

**一句话要点**：提出LoLA框架以解决长时程语言引导机器人操作任务中的历史信息利用与动作序列生成问题。

**关键词**：长时程机器人操作, 视觉-语言-动作模型, 潜在动作学习, 多视图观测, 状态感知表示, 仿真与真实评估

## 3 点简述
- 现有视觉-语言-动作模型常忽视长时程任务中的历史信息与连贯动作序列生成。
- LoLA通过状态感知潜在重表示模块，将视觉输入和语言指令映射到机器人动作空间。
- 在仿真和真实机器人任务中，LoLA显著优于现有方法，尤其在长时程操作任务上表现突出。

## 摘要（原文）

> The capability of performing long-horizon, language-guided robotic manipulation tasks critically relies on leveraging historical information and generating coherent action sequences. However, such capabilities are often overlooked by existing Vision-Language-Action (VLA) models. To solve this challenge, we propose LoLA (Long Horizon Latent Action Learning), a framework designed for robot manipulation that integrates long-term multi-view observations and robot proprioception to enable multi-step reasoning and action generation. We first employ Vision-Language Models to encode rich contextual features from historical sequences and multi-view observations. We further introduces a key module, State-Aware Latent Re-representation, which transforms visual inputs and language commands into actionable robot motion space. Unlike existing VLA approaches that merely concatenate robot proprioception (e.g., joint angles) with VL embeddings, this module leverages such robot states to explicitly ground VL representations in physical scale through a learnable "embodiment-anchored" latent space. We trained LoLA on diverse robotic pre-training datasets and conducted extensive evaluations on simulation benchmarks (SIMPLER and LIBERO), as well as two real-world tasks on Franka and Bi-Manual Aloha robots. Results show that LoLA significantly outperforms prior state-of-the-art methods (e.g., pi0), particularly in long-horizon manipulation tasks.

