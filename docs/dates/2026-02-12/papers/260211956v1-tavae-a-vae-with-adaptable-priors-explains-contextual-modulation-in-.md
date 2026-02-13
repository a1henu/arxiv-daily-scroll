---
layout: default
title: TAVAE: A VAE with Adaptable Priors Explains Contextual Modulation in the Visual Cortex
---

# TAVAE: A VAE with Adaptable Priors Explains Contextual Modulation in the Visual Cortex
**arXiv**：[2602.11956v1](https://arxiv.org/abs/2602.11956) · [PDF](https://arxiv.org/pdf/2602.11956.pdf)  
**作者**：Balázs Meszéna, Keith T. Murray, Julien Corbo, O. Batuhan Erkat, Márton A. Hajnal, Pierre-Olivier Polack, Gergő Orbán  

**一句话要点**：提出任务摊销变分自编码器以解释视觉皮层中的上下文调制机制

**关键词**：变分自编码器, 视觉皮层, 上下文调制, 任务特定先验, 概率推断, 神经编码

## 3 点简述
- 研究视觉系统能否灵活学习任务特定先验以支持概率推断
- 扩展变分自编码器框架，通过重用学习表示高效获取任务
- 模型与小鼠实验数据匹配，解释V1群体活动中的不确定性特征

## 摘要（原文）

> The brain interprets visual information through learned regularities, a computation formalized as probabilistic inference under a prior. The visual cortex establishes priors for this inference, some delivered through established top-down connections that inform low-level cortices about statistics represented at higher levels in the cortical hierarchy. While evidence shows that adaptation leads to priors reflecting the structure of natural images, it remains unclear whether similar priors can be flexibly acquired when learning a specific task. To investigate this, we built a generative model of V1 optimized for a simple discrimination task and analyzed it together with large-scale recordings from mice performing an analogous task. In line with recent approaches, we assumed that neuronal activity in V1 corresponds to latent posteriors in the generative model, enabling investigation of task-related priors in neuronal responses. To obtain a flexible test bed, we extended the VAE formalism so that a task can be acquired efficiently by reusing previously learned representations. Task-specific priors learned by this Task-Amortized VAE were used to investigate biases in mice and model when presenting stimuli that violated trained task statistics. Mismatch between learned task statistics and incoming sensory evidence produced signatures of uncertainty in stimulus category in the TAVAE posterior, reflecting properties of bimodal response profiles in V1 recordings. The task-optimized generative model accounted for key characteristics of V1 population activity, including within-day updates to population responses. Our results confirm that flexible task-specific contextual priors can be learned on demand by the visual system and deployed as early as the entry level of visual cortex.

