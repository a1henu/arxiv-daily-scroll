---
layout: default
title: Calibrating Generative AI to Produce Realistic Essays for Data Augmentation
---

# Calibrating Generative AI to Produce Realistic Essays for Data Augmentation
**arXiv**：[2602.06772v1](https://arxiv.org/abs/2602.06772) · [PDF](https://arxiv.org/pdf/2602.06772.pdf)  
**作者**：Edward W. Wolfe, Justin O. Barber  

**一句话要点**：评估大语言模型提示策略以生成真实作文用于自动评分数据增强

**关键词**：数据增强, 大语言模型, 自动评分, 作文生成, 提示策略

## 3 点简述
- 核心问题：数据增强在自动评分训练中如何生成高质量、真实的作文文本。
- 方法要点：比较三种大语言模型提示策略（预测下一个、句子、25个示例）生成模拟作文。
- 实验或效果：预测下一个策略在评分一致性和文本真实性方面表现最佳。

## 摘要（原文）

> Data augmentation can mitigate limited training data in machine-learning automated scoring engines for constructed response items. This study seeks to determine how well three approaches to large language model prompting produce essays that preserve the writing quality of the original essays and produce realistic text for augmenting ASE training datasets. We created simulated versions of student essays, and human raters assigned scores to them and rated the realism of the generated text. The results of the study indicate that the predict next prompting strategy produces the highest level of agreement between human raters regarding simulated essay scores, predict next and sentence strategies best preserve the rated quality of the original essay in the simulated essays, and predict next and 25 examples strategies produce the most realistic text as judged by human raters.

