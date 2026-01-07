---
layout: default
title: Limited Linguistic Diversity in Embodied AI Datasets
---

# Limited Linguistic Diversity in Embodied AI Datasets
**arXiv**：[2601.03136v1](https://arxiv.org/abs/2601.03136) · [PDF](https://arxiv.org/pdf/2601.03136.pdf)  
**作者**：Selma Wanna, Agnes Luhtaru, Jonathan Salfity, Ryan Barron, Juston Moore, Cynthia Matuszek, Mitch Pryor  

**一句话要点**：系统审计VLA数据集，揭示其语言多样性有限，支持更优数据选择与增强策略。

**关键词**：视觉语言动作模型, 数据集审计, 语言多样性, 指令分析, 数据增强

## 3 点简述
- 核心问题：VLA模型依赖语言，但训练与评估数据集的语言特性缺乏文档化，可能导致指令重复与结构单一。
- 方法要点：通过量化分析多个广泛使用的VLA数据集，从词汇、语义、句法等维度评估指令语言的多样性与重复性。
- 实验或效果：发现数据集常包含高度重复的模板化指令，语言形式分布狭窄，为数据报告、选择和增强提供描述性文档。

## 摘要（原文）

> Language plays a critical role in Vision-Language-Action (VLA) models, yet the linguistic characteristics of the datasets used to train and evaluate these systems remain poorly documented. In this work, we present a systematic dataset audit of several widely used VLA corpora, aiming to characterize what kinds of instructions these datasets actually contain and how much linguistic variety they provide. We quantify instruction language along complementary dimensions-including lexical variety, duplication and overlap, semantic similarity, and syntactic complexity. Our analysis shows that many datasets rely on highly repetitive, template-like commands with limited structural variation, yielding a narrow distribution of instruction forms. We position these findings as descriptive documentation of the language signal available in current VLA training and evaluation data, intended to support more detailed dataset reporting, more principled dataset selection, and targeted curation or augmentation strategies that broaden language coverage.

