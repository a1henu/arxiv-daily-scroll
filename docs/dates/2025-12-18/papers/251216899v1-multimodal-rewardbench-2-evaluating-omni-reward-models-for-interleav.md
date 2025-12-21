---
layout: default
title: Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image
---

# Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image
**arXiv**：[2512.16899v1](https://arxiv.org/abs/2512.16899) · [PDF](https://arxiv.org/pdf/2512.16899.pdf)  
**作者**：Yushi Hu, Reyhane Askari-Hemmat, Melissa Hall, Emily Dinan, Luke Zettlemoyer, Marjan Ghazvininejad  

**一句话要点**：提出Multimodal RewardBench 2以评估处理交错图文序列的全能奖励模型

**关键词**：多模态奖励模型, 交错图文序列, 基准评估, 专家标注, 全能模型, 下游任务相关性

## 3 点简述
- 核心问题：全能模型处理交错图文序列的奖励模型评估缺乏基准。
- 方法要点：构建首个全面基准MMRB2，涵盖四个任务，提供专家标注偏好对。
- 实验或效果：评估现有模型，Gemini 3 Pro准确率达75-80%，性能与下游任务强相关。

## 摘要（原文）

> Reward models (RMs) are essential for training large language models (LLMs), but remain underexplored for omni models that handle interleaved image and text sequences. We introduce Multimodal RewardBench 2 (MMRB2), the first comprehensive benchmark for reward models on multimodal understanding and (interleaved) generation. MMRB2 spans four tasks: text-to-image, image editing, interleaved generation, and multimodal reasoning ("thinking-with-images"), providing 1,000 expert-annotated preference pairs per task from 23 models and agents across 21 source tasks. MMRB2 is designed with: (1) practical but challenging prompts; (2) responses from state-of-the-art models and agents; and (3) preference pairs with strong human-expert consensus, curated via an ensemble filtering strategy. Using MMRB2, we study existing judges for each subtask, including multimodal LLM-as-a-judge and models trained with human preferences. The latest Gemini 3 Pro attains 75-80% accuracy. GPT-5 and Gemini 2.5 Pro reach 66-75% accuracy, compared to >90% for humans, yet surpass the widely used GPT-4o (59%). The best performing open-source model Qwen3-VL-32B achieves similar accuracies as Gemini 2.5 Flash (64%). We also show that MMRB2 performance strongly correlates with downstream task success using Best-of-N sampling and conduct an in-depth analysis that shows key areas to improve the reward models going forward.

