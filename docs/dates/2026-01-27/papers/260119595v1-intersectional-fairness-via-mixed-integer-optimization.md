---
layout: default
title: Intersectional Fairness via Mixed-Integer Optimization
---

# Intersectional Fairness via Mixed-Integer Optimization
**arXiv**：[2601.19595v1](https://arxiv.org/abs/2601.19595) · [PDF](https://arxiv.org/pdf/2601.19595.pdf)  
**作者**：Jiří Němeček, Mark Kozdoba, Illia Kryvoviaz, Tomáš Pevný, Jakub Mareček  

**一句话要点**：提出基于混合整数优化的统一框架，以训练交叉公平且可解释的分类器，适用于金融和医疗等高风险领域。

**关键词**：交叉公平性, 混合整数优化, 可解释分类器, 偏见缓解, AI法规合规, 高风险领域AI

## 3 点简述
- 核心问题：AI部署需公平透明，但现有法规对偏见定义模糊，需处理保护群体交叉点的偏见。
- 方法要点：利用混合整数优化训练分类器，证明两种交叉公平度量在检测最不公平子群上的等价性。
- 实验或效果：算法提升偏见检测性能，训练出高性能、可解释的分类器，将交叉偏见限制在可接受阈值内。

## 摘要（原文）

> The deployment of Artificial Intelligence in high-risk domains, such as finance and healthcare, necessitates models that are both fair and transparent. While regulatory frameworks, including the EU's AI Act, mandate bias mitigation, they are deliberately vague about the definition of bias. In line with existing research, we argue that true fairness requires addressing bias at the intersections of protected groups. We propose a unified framework that leverages Mixed-Integer Optimization (MIO) to train intersectionally fair and intrinsically interpretable classifiers. We prove the equivalence of two measures of intersectional fairness (MSD and SPSF) in detecting the most unfair subgroup and empirically demonstrate that our MIO-based algorithm improves performance in finding bias. We train high-performing, interpretable classifiers that bound intersectional bias below an acceptable threshold, offering a robust solution for regulated industries and beyond.

