---
layout: default
title: Improving Few-Shot Change Detection Visual Question Answering via Decision-Ambiguity-guided Reinforcement Fine-Tuning
---

# Improving Few-Shot Change Detection Visual Question Answering via Decision-Ambiguity-guided Reinforcement Fine-Tuning
**arXiv**：[2512.24591v1](https://arxiv.org/abs/2512.24591) · [PDF](https://arxiv.org/pdf/2512.24591.pdf)  
**作者**：Fuyu Dong, Ke Li, Di Wang, Nan Luo, Yiming Zhang, Kaiyu Li, Jianfei Yang, Quan Wang  

**一句话要点**：提出决策模糊性引导的强化微调框架以提升少样本变化检测视觉问答性能

**关键词**：变化检测视觉问答, 决策模糊性, 强化微调, 少样本学习, 遥感图像分析

## 3 点简述
- 核心问题：变化检测视觉问答中模型常因决策模糊性（正确答案与强干扰项置信度相近）而失败
- 方法要点：通过监督微调策略挖掘决策模糊样本，并应用组内相对优势的强化优化来抑制干扰
- 实验或效果：在少样本设置下，相比基线方法实现一致性能提升，无需额外监督

## 摘要（原文）

> Change detection visual question answering (CDVQA) requires answering text queries by reasoning about semantic changes in bi-temporal remote sensing images. A straightforward approach is to boost CDVQA performance with generic vision-language models via supervised fine-tuning (SFT). Despite recent progress, we observe that a significant portion of failures do not stem from clearly incorrect predictions, but from decision ambiguity, where the model assigns similar confidence to the correct answer and strong distractors. To formalize this challenge, we define Decision-Ambiguous Samples (DAS) as instances with a small probability margin between the ground-truth answer and the most competitive alternative. We argue that explicitly optimizing DAS is crucial for improving the discriminability and robustness of CDVQA models. To this end, we propose DARFT, a Decision-Ambiguity-guided Reinforcement Fine-Tuning framework that first mines DAS using an SFT-trained reference policy and then applies group-relative policy optimization on the mined subset. By leveraging multi-sample decoding and intra-group relative advantages, DARFT suppresses strong distractors and sharpens decision boundaries without additional supervision. Extensive experiments demonstrate consistent gains over SFT baselines, particularly under few-shot settings.

