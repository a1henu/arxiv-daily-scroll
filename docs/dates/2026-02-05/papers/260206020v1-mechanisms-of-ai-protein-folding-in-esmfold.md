---
layout: default
title: Mechanisms of AI Protein Folding in ESMFold
---

# Mechanisms of AI Protein Folding in ESMFold
**arXiv**：[2602.06020v1](https://arxiv.org/abs/2602.06020) · [PDF](https://arxiv.org/pdf/2602.06020.pdf)  
**作者**：Kevin Lu, Jannik Brinkmann, Stefan Huber, Aaron Mueller, Yonatan Belinkov, David Bau, Chris Wendler  

**一句话要点**：揭示ESMFold折叠蛋白质的计算机制，通过干预模型潜在变量分析beta hairpin折叠过程。

**关键词**：蛋白质折叠, ESMFold, 反事实干预, 计算机制, beta hairpin, 模型解释性

## 3 点简述
- 核心问题：探究蛋白质结构预测模型如何折叠蛋白质，聚焦beta hairpin结构基序。
- 方法要点：通过反事实干预模型潜在变量，识别折叠主干中的两个计算阶段。
- 实验或效果：定位ESMFold结构决策机制，可追踪可解释表示并产生强因果效应。

## 摘要（原文）

> How do protein structure prediction models fold proteins? We investigate this question by tracing how ESMFold folds a beta hairpin, a prevalent structural motif. Through counterfactual interventions on model latents, we identify two computational stages in the folding trunk. In the first stage, early blocks initialize pairwise biochemical signals: residue identities and associated biochemical features such as charge flow from sequence representations into pairwise representations. In the second stage, late blocks develop pairwise spatial features: distance and contact information accumulate in the pairwise representation. We demonstrate that the mechanisms underlying structural decisions of ESMFold can be localized, traced through interpretable representations, and manipulated with strong causal effects.

