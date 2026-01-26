---
layout: default
title: I Guess That's Why They Call it the Blues: Causal Analysis for Audio Classifiers
---

# I Guess That's Why They Call it the Blues: Causal Analysis for Audio Classifiers
**arXiv**：[2601.16675v1](https://arxiv.org/abs/2601.16675) · [PDF](https://arxiv.org/pdf/2601.16675.pdf)  
**作者**：David A. Kelly, Hana Chockler  

**一句话要点**：提出基于因果推理的FreqReX工具，以分析音频分类器依赖的频率特征。

**关键词**：音频分类, 因果推理, 频率分析, 模型可解释性, 对抗攻击

## 3 点简述
- 音频分类器常依赖非音乐相关特征和虚假相关性，导致易被操纵或误分类。
- 使用因果推理方法发现频率空间中充分必要的分类特征，实现于FreqReX工具。
- 实验显示，微小频率变化（如1/240,000）可改变分类结果58%的时间，且变化几乎不可闻。

## 摘要（原文）

> It is well-known that audio classifiers often rely on non-musically relevant features and spurious correlations to classify audio. Hence audio classifiers are easy to manipulate or confuse, resulting in wrong classifications. While inducing a misclassification is not hard, until now the set of features that the classifiers rely on was not well understood.
>   In this paper we introduce a new method that uses causal reasoning to discover features of the frequency space that are sufficient and necessary for a given classification. We describe an implementation of this algorithm in the tool FreqReX and provide experimental results on a number of standard benchmark datasets. Our experiments show that causally sufficient and necessary subsets allow us to manipulate the outputs of the models in a variety of ways by changing the input very slightly. Namely, a change to one out of 240,000 frequencies results in a change in classification 58% of the time, and the change can be so small that it is practically inaudible. These results show that causal analysis is useful for understanding the reasoning process of audio classifiers and can be used to successfully manipulate their outputs.

