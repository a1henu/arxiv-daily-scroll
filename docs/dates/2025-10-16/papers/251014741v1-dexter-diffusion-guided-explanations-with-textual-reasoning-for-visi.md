---
layout: default
title: DEXTER: Diffusion-Guided EXplanations with TExtual Reasoning for Vision Models
---

# DEXTER: Diffusion-Guided EXplanations with TExtual Reasoning for Vision Models
**arXiv**：[2510.14741v1](https://arxiv.org/abs/2510.14741) · [PDF](https://arxiv.org/pdf/2510.14741.pdf)  
**作者**：Simone Carnemolla, Matteo Pennisi, Sarinda Samarasinghe, Giovanni Bellitto, Simone Palazzo, Daniela Giordano, Mubarak Shah, Concetto Spampinato  

**一句话要点**：提出DEXTER框架，利用扩散模型和语言模型生成视觉分类器的全局文本解释。

**关键词**：视觉模型解释, 扩散模型, 语言模型, 全局解释, 数据自由框架, 分类器偏见分析

## 3 点简述
- 核心问题：无需训练数据或真实标签，解释视觉分类器的决策过程。
- 方法要点：优化文本提示合成类条件图像，激活分类器并生成语言报告。
- 实验或效果：在ImageNet等数据集上优于现有方法，提供准确可解释输出。

## 摘要（原文）

> Understanding and explaining the behavior of machine learning models is
> essential for building transparent and trustworthy AI systems. We introduce
> DEXTER, a data-free framework that employs diffusion models and large language
> models to generate global, textual explanations of visual classifiers. DEXTER
> operates by optimizing text prompts to synthesize class-conditional images that
> strongly activate a target classifier. These synthetic samples are then used to
> elicit detailed natural language reports that describe class-specific decision
> patterns and biases. Unlike prior work, DEXTER enables natural language
> explanation about a classifier's decision process without access to training
> data or ground-truth labels. We demonstrate DEXTER's flexibility across three
> tasks-activation maximization, slice discovery and debiasing, and bias
> explanation-each illustrating its ability to uncover the internal mechanisms of
> visual classifiers. Quantitative and qualitative evaluations, including a user
> study, show that DEXTER produces accurate, interpretable outputs. Experiments
> on ImageNet, Waterbirds, CelebA, and FairFaces confirm that DEXTER outperforms
> existing approaches in global model explanation and class-level bias reporting.
> Code is available at https://github.com/perceivelab/dexter.

