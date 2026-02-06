---
layout: default
title: Aligning Large Language Model Behavior with Human Citation Preferences
---

# Aligning Large Language Model Behavior with Human Citation Preferences
**arXiv**：[2602.05205v1](https://arxiv.org/abs/2602.05205) · [PDF](https://arxiv.org/pdf/2602.05205.pdf)  
**作者**：Kenichiro Ando, Tatsuya Harada  

**一句话要点**：通过构建数据集和偏好优化，校准大语言模型引用行为以对齐人类偏好

**关键词**：大语言模型, 引用行为, 人类偏好对齐, 数据集构建, 直接偏好优化, 引用动机分类

## 3 点简述
- 研究大语言模型引用行为与人类偏好的对齐问题，关注引用动机类型
- 构建数据集评估人类引用偏好，分析模型在医疗文本等类型上的偏差
- 实验显示模型过度引用标记文本，欠引用数字和姓名句子，可通过优化校准

## 摘要（原文）

> Most services built on powerful large-scale language models (LLMs) add citations to their output to enhance credibility. Recent research has paid increasing attention to the question of what reference documents to link to outputs. However, how LLMs recognize cite-worthiness and how this process should be controlled remains underexplored. In this study, we focus on what kinds of content LLMs currently tend to cite and how well that behavior aligns with human preferences. We construct a dataset to characterize the relationship between human citation preferences and LLM behavior. Web-derived texts are categorized into eight citation-motivation types, and pairwise citation preferences are exhaustively evaluated across all type combinations to capture fine-grained contrasts. Our results show that humans most frequently seek citations for medical text, and stronger models display a similar tendency. We also find that current models are as much as $27\%$ more likely than humans to add citations to text that is explicitly marked as needing citations on sources such as Wikipedia, and this overemphasis reduces alignment accuracy. Conversely, models systematically underselect numeric sentences (by $-22.6\%$ relative to humans) and sentences containing personal names (by $-20.1\%$), categories for which humans typically demand citations. Furthermore, experiments with Direct Preference Optimization demonstrate that model behavior can be calibrated to better match human citation preferences. We expect this study to provide a foundation for more fine-grained investigations into LLM citation preferences.

