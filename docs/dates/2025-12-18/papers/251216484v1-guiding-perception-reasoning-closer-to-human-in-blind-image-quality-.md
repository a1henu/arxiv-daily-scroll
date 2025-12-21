---
layout: default
title: Guiding Perception-Reasoning Closer to Human in Blind Image Quality Assessment
---

# Guiding Perception-Reasoning Closer to Human in Blind Image Quality Assessment
**arXiv**：[2512.16484v1](https://arxiv.org/abs/2512.16484) · [PDF](https://arxiv.org/pdf/2512.16484.pdf)  
**作者**：Yuan Li, Yahan Yu, Youyuan Lin, Yong-Hao Yang, Chenhui Chu, Shin'ya Nishida  

**一句话要点**：提出基于强化学习的感知-推理引导方法，以提升盲图像质量评估中的人机对齐与自洽性。

**关键词**：盲图像质量评估, 感知-推理, 强化学习, 人机对齐, 自洽性推理, 解释性评估

## 3 点简述
- 核心问题：盲图像质量评估中模型缺乏人类感知-推理的自洽性和解释性。
- 方法要点：利用人类标注作为奖励信号，通过强化学习引导模型模仿人类感知-推理过程。
- 实验或效果：在通用指标上达到先进水平，ROUGE-1分数提升至0.512，显示人机对齐改进。

## 摘要（原文）

> Humans assess image quality through a perception-reasoning cascade, integrating sensory cues with implicit reasoning to form self-consistent judgments. In this work, we investigate how a model can acquire both human-like and self-consistent reasoning capability for blind image quality assessment (BIQA). We first collect human evaluation data that capture several aspects of human perception-reasoning pipeline. Then, we adopt reinforcement learning, using human annotations as reward signals to guide the model toward human-like perception and reasoning. To enable the model to internalize self-consistent reasoning capability, we design a reward that drives the model to infer the image quality purely from self-generated descriptions. Empirically, our approach achieves score prediction performance comparable to state-of-the-art BIQA systems under general metrics, including Pearson and Spearman correlation coefficients. In addition to the rating score, we assess human-model alignment using ROUGE-1 to measure the similarity between model-generated and human perception-reasoning chains. On over 1,000 human-annotated samples, our model reaches a ROUGE-1 score of 0.512 (cf. 0.443 for baseline), indicating substantial coverage of human explanations and marking a step toward human-like interpretable reasoning in BIQA.

