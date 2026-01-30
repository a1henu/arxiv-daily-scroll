---
layout: default
title: Learn-to-Distance: Distance Learning for Detecting LLM-Generated Text
---

# Learn-to-Distance: Distance Learning for Detecting LLM-Generated Text
**arXiv**：[2601.21895v1](https://arxiv.org/abs/2601.21895) · [PDF](https://arxiv.org/pdf/2601.21895.pdf)  
**作者**：Hongyi Zhou, Jin Zhu, Erhan Xu, Kai Ye, Ying Yang, Chengchun Shi  

**一句话要点**：提出自适应距离学习算法以检测LLM生成文本，提升检测性能

**关键词**：LLM生成文本检测, 自适应距离学习, 改写检测算法, 几何分析, 检测性能提升

## 3 点简述
- 核心问题：LLM生成文本高度类人，引发误信息和学术诚信担忧，需可靠检测算法。
- 方法要点：基于几何分析改写检测算法，引入自适应学习距离函数，理论证明其优于固定距离。
- 实验或效果：在100多种设置中实验，相对最强基线提升57.8%至80.6%，覆盖GPT、Claude和Gemini。

## 摘要（原文）

> Modern large language models (LLMs) such as GPT, Claude, and Gemini have transformed the way we learn, work, and communicate. Yet, their ability to produce highly human-like text raises serious concerns about misinformation and academic integrity, making it an urgent need for reliable algorithms to detect LLM-generated content. In this paper, we start by presenting a geometric approach to demystify rewrite-based detection algorithms, revealing their underlying rationale and demonstrating their generalization ability. Building on this insight, we introduce a novel rewrite-based detection algorithm that adaptively learns the distance between the original and rewritten text. Theoretically, we demonstrate that employing an adaptively learned distance function is more effective for detection than using a fixed distance. Empirically, we conduct extensive experiments with over 100 settings, and find that our approach demonstrates superior performance over baseline algorithms in the majority of scenarios. In particular, it achieves relative improvements from 57.8\% to 80.6\% over the strongest baseline across different target LLMs (e.g., GPT, Claude, and Gemini).

