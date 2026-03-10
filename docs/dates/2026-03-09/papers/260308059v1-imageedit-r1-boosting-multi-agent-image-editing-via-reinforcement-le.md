---
layout: default
title: ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning
---

# ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning
**arXiv**：[2603.08059v1](https://arxiv.org/abs/2603.08059) · [PDF](https://arxiv.org/pdf/2603.08059.pdf)  
**作者**：Yiran Zhao, Yaoqi Ye, Xiang Liu, Michael Qizhe Shieh, Trung Bui  

**一句话要点**：提出ImageEdit-R1多智能体框架，利用强化学习协调图像编辑以处理复杂用户指令。

**关键词**：多智能体图像编辑, 强化学习协调, 视觉语言模型, 生成模型, 序列决策

## 3 点简述
- 现有图像编辑系统难以处理复杂、间接或多步骤用户指令，影响编辑精度。
- 采用多智能体框架，结合强化学习协调预训练视觉语言和生成智能体进行动态决策。
- 实验显示在多个数据集上优于闭源扩散模型和其他多智能体基线方法。

## 摘要（原文）

> With the rapid advancement of commercial multi-modal models, image editing has garnered significant attention due to its widespread applicability in daily life. Despite impressive progress, existing image editing systems, particularly closed-source or proprietary models, often struggle with complex, indirect, or multi-step user instructions. These limitations hinder their ability to perform nuanced, context-aware edits that align with human intent. In this work, we propose ImageEdit-R1, a multi-agent framework for intelligent image editing that leverages reinforcement learning to coordinate high-level decision-making across a set of specialized, pretrained vision-language and generative agents. Each agent is responsible for distinct capabilities--such as understanding user intent, identifying regions of interest, selecting appropriate editing actions, and synthesizing visual content--while reinforcement learning governs their collaboration to ensure coherent and goal-directed behavior. Unlike existing approaches that rely on monolithic models or hand-crafted pipelines, our method treats image editing as a sequential decision-making problem, enabling dynamic and context-aware editing strategies. Experimental results demonstrate that ImageEdit-R1 consistently outperforms both individual closed-source diffusion models and alternative multi-agent framework baselines across multiple image editing datasets.

