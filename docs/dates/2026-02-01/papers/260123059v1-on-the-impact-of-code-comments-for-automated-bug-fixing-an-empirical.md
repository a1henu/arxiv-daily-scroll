---
layout: default
title: On the Impact of Code Comments for Automated Bug-Fixing: An Empirical Study
---

# On the Impact of Code Comments for Automated Bug-Fixing: An Empirical Study
**arXiv**：[2601.23059v1](https://arxiv.org/abs/2601.23059) · [PDF](https://arxiv.org/pdf/2601.23059.pdf)  
**作者**：Antonio Vitale, Emanuela Guglielmi, Simone Scalabrino, Rocco Oliveto  

**一句话要点**：实证研究代码注释对自动修复错误的影响，揭示注释在训练和推理阶段提升准确率

**关键词**：自动错误修复, 代码注释, 大型语言模型, 实证研究, 软件工程

## 3 点简述
- 核心问题：代码注释在自动修复错误中的作用被低估，常见预处理移除注释可能影响模型性能
- 方法要点：比较不同训练和推理条件下LLMs的修复能力，使用LLM自动生成缺失注释以扩充数据集
- 实验或效果：注释在训练和推理阶段均存在时，准确率提升高达三倍，实现细节类注释效果显著

## 摘要（原文）

> Large Language Models (LLMs) are increasingly relevant in Software Engineering research and practice, with Automated Bug Fixing (ABF) being one of their key applications. ABF involves transforming a buggy method into its fixed equivalent. A common preprocessing step in ABF involves removing comments from code prior to training. However, we hypothesize that comments may play a critical role in fixing certain types of bugs by providing valuable design and implementation insights. In this study, we investigate how the presence or absence of comments, both during training and at inference time, impacts the bug-fixing capabilities of LLMs. We conduct an empirical evaluation comparing two model families, each evaluated under all combinations of training and inference conditions (with and without comments), and thereby revisiting the common practice of removing comments during training. To address the limited availability of comments in state-of-the-art datasets, we use an LLM to automatically generate comments for methods lacking them. Our findings show that comments improve ABF accuracy by up to threefold when present in both phases, while training with comments does not degrade performance when instances lack them. Additionally, an interpretability analysis identifies that comments detailing method implementation are particularly effective in aiding LLMs to fix bugs accurately.

