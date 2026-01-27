---
layout: default
title: Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability
---

# Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability
**arXiv**：[2601.18778v1](https://arxiv.org/abs/2601.18778) · [PDF](https://arxiv.org/pdf/2601.18778.pdf)  
**作者**：Shobhita Sundaram, John Quan, Ariel Kwiatkowski, Kartik Ahuja, Yann Ollivier, Julia Kempe  

**一句话要点**：提出SOAR框架，通过元强化学习生成自动课程以解决推理模型在低成功率数据集上的学习停滞问题。

**关键词**：元强化学习, 自动课程生成, 推理模型, 学习停滞, 自我改进框架

## 3 点简述
- 核心问题：预训练大模型在初始成功率低的推理任务上因训练信号稀疏而陷入学习停滞。
- 方法要点：设计SOAR框架，教师模型生成合成问题供学生模型学习，基于学生进步进行奖励，实现元强化学习。
- 实验或效果：在数学基准最难题集上验证，SOAR能解锁学习，生成的结构质量比答案正确性更关键。

## 摘要（原文）

> Can a model learn to escape its own learning plateau? Reinforcement learning methods for finetuning large reasoning models stall on datasets with low initial success rates, and thus little training signal. We investigate a fundamental question: Can a pretrained LLM leverage latent knowledge to generate an automated curriculum for problems it cannot solve? To explore this, we design SOAR: A self-improvement framework designed to surface these pedagogical signals through meta-RL. A teacher copy of the model proposes synthetic problems for a student copy, and is rewarded with its improvement on a small subset of hard problems. Critically, SOAR grounds the curriculum in measured student progress rather than intrinsic proxy rewards. Our study on the hardest subsets of mathematical benchmarks (0/128 success) reveals three core findings. First, we show that it is possible to realize bi-level meta-RL that unlocks learning under sparse, binary rewards by sharpening a latent capacity of pretrained models to generate useful stepping stones. Second, grounded rewards outperform intrinsic reward schemes used in prior LLM self-play, reliably avoiding the instability and diversity collapse modes they typically exhibit. Third, analyzing the generated questions reveals that structural quality and well-posedness are more critical for learning progress than solution correctness. Our results suggest that the ability to generate useful stepping stones does not require the preexisting ability to actually solve the hard problems, paving a principled path to escape reasoning plateaus without additional curated data.

