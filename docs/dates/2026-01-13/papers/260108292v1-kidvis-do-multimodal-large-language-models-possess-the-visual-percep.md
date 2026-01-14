---
layout: default
title: KidVis: Do Multimodal Large Language Models Possess the Visual Perceptual Capabilities of a 6-Year-Old?
---

# KidVis: Do Multimodal Large Language Models Possess the Visual Perceptual Capabilities of a 6-Year-Old?
**arXiv**：[2601.08292v1](https://arxiv.org/abs/2601.08292) · [PDF](https://arxiv.org/pdf/2601.08292.pdf)  
**作者**：Xianfeng Wang, Kaiwei Zhang, Qi Jia, Zijian Chen, Guangtao Zhai, Xiongkuo Min  

**一句话要点**：提出KidVis基准，基于人类视觉发展理论评估MLLMs的基础视觉感知能力。

**关键词**：多模态大语言模型, 视觉感知基准, 人类视觉发展, 基础视觉能力, 缩放定律悖论

## 3 点简述
- 核心问题：MLLMs是否具备类似6-7岁儿童的基础视觉感知能力。
- 方法要点：将视觉智能分解为六个原子能力，设计低语义依赖的视觉任务。
- 实验或效果：评估20个MLLMs，发现性能远低于人类儿童，存在缩放定律悖论。

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have demonstrated impressive proficiency in high-level reasoning tasks, such as complex diagrammatic interpretation, it remains an open question whether they possess the fundamental visual primitives comparable to human intuition. To investigate this, we introduce KidVis, a novel benchmark grounded in the theory of human visual development. KidVis deconstructs visual intelligence into six atomic capabilities - Concentration, Tracking, Discrimination, Memory, Spatial, and Closure - already possessed by 6-7 year old children, comprising 10 categories of low-semantic-dependent visual tasks. Evaluating 20 state-of-the-art MLLMs against a human physiological baseline reveals a stark performance disparity. Results indicate that while human children achieve a near-perfect average score of 95.32, the state-of-the-art GPT-5 attains only 67.33. Crucially, we observe a "Scaling Law Paradox": simply increasing model parameters fails to yield linear improvements in these foundational visual capabilities. This study confirms that current MLLMs, despite their reasoning prowess, lack the essential physiological perceptual primitives required for generalized visual intelligence.

