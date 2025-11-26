---
layout: default
title: VKnowU: Evaluating Visual Knowledge Understanding in Multimodal LLMs
---

# VKnowU: Evaluating Visual Knowledge Understanding in Multimodal LLMs
**arXiv**：[2511.20272v1](https://arxiv.org/abs/2511.20272) · [PDF](https://arxiv.org/pdf/2511.20272.pdf)  
**作者**：Tianxiang Jiang, Sheng Xia, Yicheng Xu, Linquan Wu, Xiangyu Zeng, Limin Wang, Yu Qiao, Yi Wang  

**一句话要点**：提出VKnowU基准和VideoKnow+模型以评估和提升多模态大模型的视觉知识理解能力

**关键词**：多模态大模型, 视觉知识理解, 基准评估, 视频问答, 强化学习, 世界知识

## 3 点简述
- 核心问题：多模态大模型缺乏对物理和社会世界底层原理的直观视觉知识理解
- 方法要点：构建VKnowU基准和VideoKnow+模型，采用See-Think-Answer范式和强化学习奖励机制
- 实验或效果：VideoKnow+在VKnowU上提升3.7%，并在多个基准上表现一致改进

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have become adept at recognizing objects, they often lack the intuitive, human-like understanding of the world's underlying physical and social principles. This high-level vision-grounded semantics, which we term visual knowledge, forms a bridge between perception and reasoning, yet remains an underexplored area in current MLLMs. To systematically evaluate this capability, we present VKnowU, a comprehensive benchmark featuring 1,680 questions in 1,249 videos, covering 8 core types of visual knowledge spanning both world-centric (e.g., intuitive physics) and human-centric (e.g., subjective intentions). Evaluation of 23 SOTA MLLMs reveals that leading models still fall short of human performance, with particularly notable gaps in the world-centric. To bridge this gap, we introduce a new dataset, VKnowQA, and VideoKnow+, a baseline model that explicitly incorporates visual knowledge into MLLMs. VideoKnow+ follows a structured See-Think-Answer paradigm and adopts reinforcement learning with visual knowledge reward, achieving a +3.7% improvement on VKnowU and consistent gains on MVBench, Video-MME, and MMVU. Our work highlights visual knowledge as a missing cornerstone for developing more generalizable MLLMs that can not only see but also truly understand our physical and social worlds.

