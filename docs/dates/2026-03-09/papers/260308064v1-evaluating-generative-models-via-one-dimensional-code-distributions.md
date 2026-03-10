---
layout: default
title: Evaluating Generative Models via One-Dimensional Code Distributions
---

# Evaluating Generative Models via One-Dimensional Code Distributions
**arXiv**：[2603.08064v1](https://arxiv.org/abs/2603.08064) · [PDF](https://arxiv.org/pdf/2603.08064.pdf)  
**作者**：Zexi Jia, Pengcheng Luo, Yijia Zhong, Jinchao Zhang, Jie Zhou  

**一句话要点**：提出基于离散视觉令牌的生成模型评估方法，以提升与人类感知的相关性。

**关键词**：生成模型评估, 离散视觉令牌, Codebook Histogram Distance, Code Mixture Model Score, VisForm基准

## 3 点简述
- 核心问题：传统特征分布指标如FID忽略感知质量线索，导致评估不全面。
- 方法要点：引入Codebook Histogram Distance和Code Mixture Model Score，在令牌空间进行训练免费和无需参考的评估。
- 实验或效果：在多个基准测试中，新指标与人类判断的相关性达到最先进水平。

## 摘要（原文）

> Most evaluations of generative models rely on feature-distribution metrics such as FID, which operate on continuous recognition features that are explicitly trained to be invariant to appearance variations, and thus discard cues critical for perceptual quality. We instead evaluate models in the space of \emph{discrete} visual tokens, where modern 1D image tokenizers compactly encode both semantic and perceptual information and quality manifests as predictable token statistics. We introduce \emph{Codebook Histogram Distance} (CHD), a training-free distribution metric in token space, and \emph{Code Mixture Model Score} (CMMS), a no-reference quality metric learned from synthetic degradations of token sequences. To stress-test metrics under broad distribution shifts, we further propose \emph{VisForm}, a benchmark of 210K images spanning 62 visual forms and 12 generative models with expert annotations. Across AGIQA, HPDv2/3, and VisForm, our token-based metrics achieve state-of-the-art correlation with human judgments, and we will release all code and datasets to facilitate future research.

