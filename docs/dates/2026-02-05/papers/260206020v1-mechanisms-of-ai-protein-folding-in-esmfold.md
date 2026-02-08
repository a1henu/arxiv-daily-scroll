---
layout: default
title: Mechanisms of AI Protein Folding in ESMFold
---

# Mechanisms of AI Protein Folding in ESMFold
**arXiv**：[2602.06020v1](https://arxiv.org/abs/2602.06020) · [PDF](https://arxiv.org/pdf/2602.06020.pdf)  
**作者**：Kevin Lu, Jannik Brinkmann, Stefan Huber, Aaron Mueller, Yonatan Belinkov, David Bau, Chris Wendler  

**一句话要点**：通过干预模型潜在变量揭示ESMFold折叠蛋白质的计算机制

**关键词**：蛋白质折叠, ESMFold, 反事实干预, 计算机制, 可解释性

## 3 点简述
- 核心问题：探究蛋白质结构预测模型如何折叠蛋白质，以beta hairpin为例
- 方法要点：对模型潜在变量进行反事实干预，识别折叠过程中的两个计算阶段
- 实验或效果：定位结构决策机制，通过可解释表示追踪并操纵因果效应

## 摘要（原文）

> How do protein structure prediction models fold proteins? We investigate this question by tracing how ESMFold folds a beta hairpin, a prevalent structural motif. Through counterfactual interventions on model latents, we identify two computational stages in the folding trunk. In the first stage, early blocks initialize pairwise biochemical signals: residue identities and associated biochemical features such as charge flow from sequence representations into pairwise representations. In the second stage, late blocks develop pairwise spatial features: distance and contact information accumulate in the pairwise representation. We demonstrate that the mechanisms underlying structural decisions of ESMFold can be localized, traced through interpretable representations, and manipulated with strong causal effects.

