---
layout: default
title: Benchmarking Diversity in Image Generation via Attribute-Conditional Human Evaluation
---

# Benchmarking Diversity in Image Generation via Attribute-Conditional Human Evaluation
**arXiv**：[2511.10547v1](https://arxiv.org/abs/2511.10547) · [PDF](https://arxiv.org/pdf/2511.10547.pdf)  
**作者**：Isabela Albuquerque, Ira Ktena, Olivia Wiles, Ivana Kajić, Amal Rannen-Triki, Cristina Vasconcelos, Aida Nematzadeh  

**一句话要点**：提出基于属性条件人类评估的框架以解决文本到图像模型多样性不足问题

**关键词**：文本到图像生成, 多样性评估, 人类评估, 属性条件, 模型比较, 图像嵌入

## 3 点简述
- 核心问题：当前文本到图像模型生成输出同质化，缺乏多样性。
- 方法要点：引入人类评估模板和提示集，系统评估概念及其变化因素。
- 实验或效果：通过二项检验比较模型，并评估图像嵌入以衡量多样性。

## 摘要（原文）

> Despite advances in generation quality, current text-to-image (T2I) models often lack diversity, generating homogeneous outputs. This work introduces a framework to address the need for robust diversity evaluation in T2I models. Our framework systematically assesses diversity by evaluating individual concepts and their relevant factors of variation. Key contributions include: (1) a novel human evaluation template for nuanced diversity assessment; (2) a curated prompt set covering diverse concepts with their identified factors of variation (e.g. prompt: An image of an apple, factor of variation: color); and (3) a methodology for comparing models in terms of human annotations via binomial tests.
>   Furthermore, we rigorously compare various image embeddings for diversity measurement. Notably, our principled approach enables ranking of T2I models by diversity, identifying categories where they particularly struggle. This research offers a robust methodology and insights, paving the way for improvements in T2I model diversity and metric development.

