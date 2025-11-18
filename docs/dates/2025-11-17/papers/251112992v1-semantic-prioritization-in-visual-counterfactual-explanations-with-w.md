---
layout: default
title: Semantic Prioritization in Visual Counterfactual Explanations with Weighted Segmentation and Auto-Adaptive Region Selection
---

# Semantic Prioritization in Visual Counterfactual Explanations with Weighted Segmentation and Auto-Adaptive Region Selection
**arXiv**：[2511.12992v1](https://arxiv.org/abs/2511.12992) · [PDF](https://arxiv.org/pdf/2511.12992.pdf)  
**作者**：Lintong Zhang, Kang Yin, Seong-Whan Lee  

**一句话要点**：提出WSAE-Net以优化非生成视觉反事实解释的语义相关性和计算效率

**关键词**：视觉反事实解释, 加权语义图, 自适应编辑序列, 计算效率优化, 语义相关性

## 3 点简述
- 传统方法忽略替换区域语义相关性，损害模型可解释性和编辑流程
- 引入加权语义图和自适应候选编辑序列，优化计算顺序和效率
- 实验显示方法性能优越，提升视觉反事实解释的清晰度和深度理解

## 摘要（原文）

> In the domain of non-generative visual counterfactual explanations (CE), traditional techniques frequently involve the substitution of sections within a query image with corresponding sections from distractor images. Such methods have historically overlooked the semantic relevance of the replacement regions to the target object, thereby impairing the model's interpretability and hindering the editing workflow. Addressing these challenges, the present study introduces an innovative methodology named as Weighted Semantic Map with Auto-adaptive Candidate Editing Network (WSAE-Net). Characterized by two significant advancements: the determination of an weighted semantic map and the auto-adaptive candidate editing sequence. First, the generation of the weighted semantic map is designed to maximize the reduction of non-semantic feature units that need to be computed, thereby optimizing computational efficiency. Second, the auto-adaptive candidate editing sequences are designed to determine the optimal computational order among the feature units to be processed, thereby ensuring the efficient generation of counterfactuals while maintaining the semantic relevance of the replacement feature units to the target object. Through comprehensive experimentation, our methodology demonstrates superior performance, contributing to a more lucid and in-depth understanding of visual counterfactual explanations.

