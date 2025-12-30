---
layout: default
title: Divergent-Convergent Thinking in Large Language Models for Creative Problem Generation
---

# Divergent-Convergent Thinking in Large Language Models for Creative Problem Generation
**arXiv**：[2512.23601v1](https://arxiv.org/abs/2512.23601) · [PDF](https://arxiv.org/pdf/2512.23601.pdf)  
**作者**：Manh Hung Nguyen, Adish Singla  

**一句话要点**：提出CreativeDC两阶段提示方法，以增强大语言模型在教育问题生成中的多样性与新颖性。

**关键词**：大语言模型, 问题生成, 发散-收敛思维, 创意提示, 教育技术, 多样性评估

## 3 点简述
- 核心问题：大语言模型存在‘人工蜂群’效应，生成问题过于相似，损害思维多样性。
- 方法要点：基于发散-收敛思维理论，将推理分为创意探索和约束满足两阶段，解耦创意过程。
- 实验或效果：评估显示CreativeDC在多样性、新颖性上显著优于基线，同时保持高实用性。

## 摘要（原文）

> Large language models (LLMs) have significant potential for generating educational questions and problems, enabling educators to create large-scale learning materials. However, LLMs are fundamentally limited by the ``Artificial Hivemind'' effect, where they generate similar responses within the same model and produce homogeneous outputs across different models. As a consequence, students may be exposed to overly similar and repetitive LLM-generated problems, which harms diversity of thought. Drawing inspiration from Wallas's theory of creativity and Guilford's framework of divergent-convergent thinking, we propose CreativeDC, a two-phase prompting method that explicitly scaffolds the LLM's reasoning into distinct phases. By decoupling creative exploration from constraint satisfaction, our method enables LLMs to explore a broader space of ideas before committing to a final problem. We evaluate CreativeDC for creative problem generation using a comprehensive set of metrics that capture diversity, novelty, and utility. The results show that CreativeDC achieves significantly higher diversity and novelty compared to baselines while maintaining high utility. Moreover, scaling analysis shows that CreativeDC generates a larger effective number of distinct problems as more are sampled, increasing at a faster rate than baseline methods.

