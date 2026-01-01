---
layout: default
title: Evolving, Not Training: Zero-Shot Reasoning Segmentation via Evolutionary Prompting
---

# Evolving, Not Training: Zero-Shot Reasoning Segmentation via Evolutionary Prompting
**arXiv**：[2512.24702v1](https://arxiv.org/abs/2512.24702) · [PDF](https://arxiv.org/pdf/2512.24702.pdf)  
**作者**：Kai Ye, Xiaotong You, Jianghang Lin, Jiayi Ji, Pingyang Dai, Liujuan Cao  

**一句话要点**：提出EVOL-SAM3框架，通过进化提示实现零样本推理分割，避免训练依赖。

**关键词**：推理分割, 零样本学习, 进化算法, 提示工程, 语义理解, 像素级定位

## 3 点简述
- 核心问题：现有推理分割方法依赖训练或静态推理，导致遗忘、不稳定或深度不足。
- 方法要点：采用进化搜索，通过生成-评估-进化循环动态优化提示，引入视觉竞技场和语义突变。
- 实验或效果：在ReasonSeg基准上零样本超越静态方法和全监督SOTA，代码开源。

## 摘要（原文）

> Reasoning Segmentation requires models to interpret complex, context-dependent linguistic queries to achieve pixel-level localization. Current dominant approaches rely heavily on Supervised Fine-Tuning (SFT) or Reinforcement Learning (RL). However, SFT suffers from catastrophic forgetting and domain dependency, while RL is often hindered by training instability and rigid reliance on predefined reward functions. Although recent training-free methods circumvent these training burdens, they are fundamentally limited by a static inference paradigm. These methods typically rely on a single-pass "generate-then-segment" chain, which suffers from insufficient reasoning depth and lacks the capability to self-correct linguistic hallucinations or spatial misinterpretations. In this paper, we challenge these limitations and propose EVOL-SAM3, a novel zero-shot framework that reformulates reasoning segmentation as an inference-time evolutionary search process. Instead of relying on a fixed prompt, EVOL-SAM3 maintains a population of prompt hypotheses and iteratively refines them through a "Generate-Evaluate-Evolve" loop. We introduce a Visual Arena to assess prompt fitness via reference-free pairwise tournaments, and a Semantic Mutation operator to inject diversity and correct semantic errors. Furthermore, a Heterogeneous Arena module integrates geometric priors with semantic reasoning to ensure robust final selection. Extensive experiments demonstrate that EVOL-SAM3 not only substantially outperforms static baselines but also significantly surpasses fully supervised state-of-the-art methods on the challenging ReasonSeg benchmark in a zero-shot setting. The code is available at https://github.com/AHideoKuzeA/Evol-SAM3.

