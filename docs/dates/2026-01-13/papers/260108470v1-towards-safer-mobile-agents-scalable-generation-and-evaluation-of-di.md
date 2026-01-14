---
layout: default
title: Towards Safer Mobile Agents: Scalable Generation and Evaluation of Diverse Scenarios for VLMs
---

# Towards Safer Mobile Agents: Scalable Generation and Evaluation of Diverse Scenarios for VLMs
**arXiv**：[2601.08470v1](https://arxiv.org/abs/2601.08470) · [PDF](https://arxiv.org/pdf/2601.08470.pdf)  
**作者**：Takara Taniguchi, Kuniaki Saito, Atsushi Hashimoto  

**一句话要点**：提出HazardForge以生成移动代理安全评估的多样化场景，并构建MovSafeBench基准。

**关键词**：视觉语言模型, 安全评估, 场景生成, 移动代理, 基准构建

## 3 点简述
- 核心问题：现有基准难以覆盖动态异常场景，影响视觉语言模型在移动系统中的安全决策评估。
- 方法要点：利用图像编辑模型和布局决策算法，可扩展地生成包含移动、侵入和远距离对象的危险场景。
- 实验或效果：基于MovSafeBench的实验显示，视觉语言模型在异常对象条件下性能显著下降，尤其在运动理解场景中。

## 摘要（原文）

> Vision Language Models (VLMs) are increasingly deployed in autonomous vehicles and mobile systems, making it crucial to evaluate their ability to support safer decision-making in complex environments. However, existing benchmarks inadequately cover diverse hazardous situations, especially anomalous scenarios with spatio-temporal dynamics. While image editing models are a promising means to synthesize such hazards, it remains challenging to generate well-formulated scenarios that include moving, intrusive, and distant objects frequently observed in the real world. To address this gap, we introduce \textbf{HazardForge}, a scalable pipeline that leverages image editing models to generate these scenarios with layout decision algorithms, and validation modules. Using HazardForge, we construct \textbf{MovSafeBench}, a multiple-choice question (MCQ) benchmark comprising 7,254 images and corresponding QA pairs across 13 object categories, covering both normal and anomalous objects. Experiments using MovSafeBench show that VLM performance degrades notably under conditions including anomalous objects, with the largest drop in scenarios requiring nuanced motion understanding.

