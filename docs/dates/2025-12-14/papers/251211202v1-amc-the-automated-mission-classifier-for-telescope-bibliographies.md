---
layout: default
title: amc: The Automated Mission Classifier for Telescope Bibliographies
---

# amc: The Automated Mission Classifier for Telescope Bibliographies
**arXiv**：[2512.11202v1](https://arxiv.org/abs/2512.11202) · [PDF](https://arxiv.org/pdf/2512.11202.pdf)  
**作者**：John F. Wu, Joshua E. G. Peek, Sophie J. Miller, Jenny Novacescu, Achu J. Usha, Christopher A. Wilkinson  

**一句话要点**：提出自动化任务分类器以解决望远镜文献手动标注瓶颈

**关键词**：望远镜文献分类, 大语言模型应用, 自动化标注, 天文图书馆学, TRACS挑战

## 3 点简述
- 核心问题：天文文献增长快，手动标注望远镜参考文献难以扩展。
- 方法要点：利用大语言模型处理大量论文文本，自动识别和分类望远镜引用。
- 实验或效果：在TRACS挑战中宏F1分数达0.84，可应用于NASA任务等望远镜。

## 摘要（原文）

> Telescope bibliographies record the pulse of astronomy research by capturing publication statistics and citation metrics for telescope facilities. Robust and scalable bibliographies ensure that we can measure the scientific impact of our facilities and archives. However, the growing rate of publications threatens to outpace our ability to manually label astronomical literature. We therefore present the Automated Mission Classifier (amc), a tool that uses large language models (LLMs) to identify and categorize telescope references by processing large quantities of paper text. A modified version of amc performs well on the TRACS Kaggle challenge, achieving a macro $F_1$ score of 0.84 on the held-out test set. amc is valuable for other telescopes beyond TRACS; we developed the initial software for identifying papers that featured scientific results by NASA missions. Additionally, we investigate how amc can also be used to interrogate historical datasets and surface potential label errors. Our work demonstrates that LLM-based applications offer powerful and scalable assistance for library sciences.

