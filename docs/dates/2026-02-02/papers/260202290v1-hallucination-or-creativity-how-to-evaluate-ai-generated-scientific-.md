---
layout: default
title: Hallucination or Creativity: How to Evaluate AI-Generated Scientific Stories?
---

# Hallucination or Creativity: How to Evaluate AI-Generated Scientific Stories?
**arXiv**：[2602.02290v1](https://arxiv.org/abs/2602.02290) · [PDF](https://arxiv.org/pdf/2602.02290.pdf)  
**作者**：Alex Argese, Pasquale Lisena, Raphaël Troncy  

**一句话要点**：提出StoryScore以评估AI生成科学故事，解决幻觉检测与创造力衡量的挑战。

**关键词**：AI生成故事评估, 幻觉检测, 叙事创造力, 科学传播, 复合指标

## 3 点简述
- 核心问题：标准指标难以评估科学故事中的叙事创造力和幻觉，现有检测器易误判。
- 方法要点：StoryScore整合语义对齐、词汇基础、叙事控制等多维度指标于统一框架。
- 实验或效果：分析揭示自动指标在评估叙事方式上的局限性，强调创造力与事实错误的区分困难。

## 摘要（原文）

> Generative AI can turn scientific articles into narratives for diverse audiences, but evaluating these stories remains challenging. Storytelling demands abstraction, simplification, and pedagogical creativity-qualities that are not often well-captured by standard summarization metrics. Meanwhile, factual hallucinations are critical in scientific contexts, yet, detectors often misclassify legitimate narrative reformulations or prove unstable when creativity is involved. In this work, we propose StoryScore, a composite metric for evaluating AI-generated scientific stories. StoryScore integrates semantic alignment, lexical grounding, narrative control, structural fidelity, redundancy avoidance, and entity-level hallucination detection into a unified framework. Our analysis also reveals why many hallucination detection methods fail to distinguish pedagogical creativity from factual errors, highlighting a key limitation: while automatic metrics can effectively assess semantic similarity with original content, they struggle to evaluate how it is narrated and controlled.

