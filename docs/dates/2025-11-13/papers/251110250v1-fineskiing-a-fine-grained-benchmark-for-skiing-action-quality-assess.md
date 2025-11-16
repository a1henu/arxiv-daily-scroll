---
layout: default
title: FineSkiing: A Fine-grained Benchmark for Skiing Action Quality Assessment
---

# FineSkiing: A Fine-grained Benchmark for Skiing Action Quality Assessment
**arXiv**：[2511.10250v1](https://arxiv.org/abs/2511.10250) · [PDF](https://arxiv.org/pdf/2511.10250.pdf)  
**作者**：Yongji Zhang, Siqi Li, Yue Gao, Yu Jiang  

**一句话要点**：提出JudgeMind方法以解决空中滑雪动作质量评估中的细粒度评分问题

**关键词**：动作质量评估, 细粒度数据集, 阶段感知特征, 知识融合, 空中滑雪, 视频分析

## 3 点简述
- 核心问题：现有动作质量评估方法缺乏细粒度注释，导致可解释性和可靠性不足。
- 方法要点：将动作视频分段评分，并融合阶段感知特征和基于知识的解码器。
- 实验或效果：在FineSkiing数据集上实现最先进性能，提升评分准确性和鲁棒性。

## 摘要（原文）

> Action Quality Assessment (AQA) aims to evaluate and score sports actions, which has attracted widespread interest in recent years. Existing AQA methods primarily predict scores based on features extracted from the entire video, resulting in limited interpretability and reliability. Meanwhile, existing AQA datasets also lack fine-grained annotations for action scores, especially for deduction items and sub-score annotations. In this paper, we construct the first AQA dataset containing fine-grained sub-score and deduction annotations for aerial skiing, which will be released as a new benchmark. For the technical challenges, we propose a novel AQA method, named JudgeMind, which significantly enhances performance and reliability by simulating the judgment and scoring mindset of professional referees. Our method segments the input action video into different stages and scores each stage to enhance accuracy. Then, we propose a stage-aware feature enhancement and fusion module to boost the perception of stage-specific key regions and enhance the robustness to visual changes caused by frequent camera viewpoints switching. In addition, we propose a knowledge-based grade-aware decoder to incorporate possible deduction items as prior knowledge to predict more accurate and reliable scores. Experimental results demonstrate that our method achieves state-of-the-art performance.

