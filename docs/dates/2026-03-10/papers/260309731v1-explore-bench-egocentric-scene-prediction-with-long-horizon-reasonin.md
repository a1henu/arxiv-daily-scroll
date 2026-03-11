---
layout: default
title: EXPLORE-Bench: Egocentric Scene Prediction with Long-Horizon Reasoning
---

# EXPLORE-Bench: Egocentric Scene Prediction with Long-Horizon Reasoning
**arXiv**：[2603.09731v1](https://arxiv.org/abs/2603.09731) · [PDF](https://arxiv.org/pdf/2603.09731.pdf)  
**作者**：Chengjun Yu, Xuhan Zhu, Chaoqun Du, Pengfei Yu, Wei Zhai, Yang Cao, Zheng-Jun Zha  

**一句话要点**：提出EXPLORE-Bench基准以评估多模态大模型在长时程自我中心场景预测中的推理能力

**关键词**：自我中心场景预测, 长时程推理, 多模态大语言模型, 基准评估, 动作序列理解

## 3 点简述
- 研究多模态大模型能否从自我中心视角可靠推理动作的长期物理后果
- 构建基于真实第一人称视频的基准，包含长动作序列和结构化场景标注
- 实验显示模型与人类存在显著性能差距，分步推理可部分提升效果但计算开销大

## 摘要（原文）

> Multimodal large language models (MLLMs) are increasingly considered as a foundation for embodied agents, yet it remains unclear whether they can reliably reason about the long-term physical consequences of actions from an egocentric viewpoint. We study this gap through a new task, Egocentric Scene Prediction with LOng-horizon REasoning: given an initial-scene image and a sequence of atomic action descriptions, a model is asked to predict the final scene after all actions are executed. To enable systematic evaluation, we introduce EXPLORE-Bench, a benchmark curated from real first-person videos spanning diverse scenarios. Each instance pairs long action sequences with structured final-scene annotations, including object categories, visual attributes, and inter-object relations, which supports fine-grained, quantitative assessment. Experiments on a range of proprietary and open-source MLLMs reveal a significant performance gap to humans, indicating that long-horizon egocentric reasoning remains a major challenge. We further analyze test-time scaling via stepwise reasoning and show that decomposing long action sequences can improve performance to some extent, while incurring non-trivial computational overhead. Overall, EXPLORE-Bench provides a principled testbed for measuring and advancing long-horizon reasoning for egocentric embodied perception.

