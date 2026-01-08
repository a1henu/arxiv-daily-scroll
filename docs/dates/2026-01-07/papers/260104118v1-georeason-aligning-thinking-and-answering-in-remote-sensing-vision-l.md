---
layout: default
title: GeoReason: Aligning Thinking And Answering In Remote Sensing Vision-Language Models Via Logical Consistency Reinforcement Learning
---

# GeoReason: Aligning Thinking And Answering In Remote Sensing Vision-Language Models Via Logical Consistency Reinforcement Learning
**arXiv**：[2601.04118v1](https://arxiv.org/abs/2601.04118) · [PDF](https://arxiv.org/pdf/2601.04118.pdf)  
**作者**：Wenshuai Li, Xiantai Xiang, Zixiao Wen, Guangyao Zhou, Ben Niu, Feng Wang, Lijia Huang, Qiantong Wang, Yuxin Hu  

**一句话要点**：提出GeoReason框架，通过逻辑一致性强化学习解决遥感视觉语言模型中的推理幻觉问题

**关键词**：遥感视觉语言模型, 逻辑一致性强化学习, 推理幻觉, 空间决策, GeoReason-Bench数据集

## 3 点简述
- 核心问题：遥感视觉语言模型存在逻辑幻觉，推理链与答案脱节，影响空间决策可靠性。
- 方法要点：构建GeoReason-Bench数据集，采用监督知识初始化和一致性感知强化学习两阶段训练策略。
- 实验或效果：框架显著提升认知可靠性和可解释性，在实验中达到先进性能。

## 摘要（原文）

> The evolution of Remote Sensing Vision-Language Models(RS-VLMs) emphasizes the importance of transitioning from perception-centric recognition toward high-level deductive reasoning to enhance cognitive reliability in complex spatial tasks. However, current models often suffer from logical hallucinations, where correct answers are derived from flawed reasoning chains or rely on positional shortcuts rather than spatial logic. This decoupling undermines reliability in strategic spatial decision-making. To address this, we present GeoReason, a framework designed to synchronize internal thinking with final decisions. We first construct GeoReason-Bench, a logic-driven dataset containing 4,000 reasoning trajectories synthesized from geometric primitives and expert knowledge. We then formulate a two-stage training strategy: (1) Supervised Knowledge Initialization to equip the model with reasoning syntax and domain expertise, and (2) Consistency-Aware Reinforcement Learning to refine deductive reliability. This second stage integrates a novel Logical Consistency Reward, which penalizes logical drift via an option permutation strategy to anchor decisions in verifiable reasoning traces. Experimental results demonstrate that our framework significantly enhances the cognitive reliability and interpretability of RS-VLMs, achieving state-of-the-art performance compared to other advanced methods.

