---
layout: default
title: RadDiff: Describing Differences in Radiology Image Sets with Natural Language
---

# RadDiff: Describing Differences in Radiology Image Sets with Natural Language
**arXiv**：[2601.03733v1](https://arxiv.org/abs/2601.03733) · [PDF](https://arxiv.org/pdf/2601.03733.pdf)  
**作者**：Xiaoxian Shen, Yuhui Zhang, Sahithi Ankireddy, Xiaohan Wang, Maya Varma, Henry Guo, Curtis Langlotz, Serena Yeung-Levy  

**一句话要点**：提出RadDiff系统，通过多模态代理推理描述放射学图像集间的临床差异

**关键词**：放射学图像分析, 多模态推理, 医学AI解释, 视觉语言模型, 临床差异描述

## 3 点简述
- 核心问题：理解放射学图像集间的差异对临床洞察和医学AI解释至关重要
- 方法要点：基于VisDiff框架，结合医学知识注入、多模态推理、迭代假设精炼和针对性视觉搜索
- 实验或效果：在RadDiffBench基准上达到47%准确率，显著优于VisDiff基线

## 摘要（原文）

> Understanding how two radiology image sets differ is critical for generating clinical insights and for interpreting medical AI systems. We introduce RadDiff, a multimodal agentic system that performs radiologist-style comparative reasoning to describe clinically meaningful differences between paired radiology studies. RadDiff builds on a proposer-ranker framework from VisDiff, and incorporates four innovations inspired by real diagnostic workflows: (1) medical knowledge injection through domain-adapted vision-language models; (2) multimodal reasoning that integrates images with their clinical reports; (3) iterative hypothesis refinement across multiple reasoning rounds; and (4) targeted visual search that localizes and zooms in on salient regions to capture subtle findings. To evaluate RadDiff, we construct RadDiffBench, a challenging benchmark comprising 57 expert-validated radiology study pairs with ground-truth difference descriptions. On RadDiffBench, RadDiff achieves 47% accuracy, and 50% accuracy when guided by ground-truth reports, significantly outperforming the general-domain VisDiff baseline. We further demonstrate RadDiff's versatility across diverse clinical tasks, including COVID-19 phenotype comparison, racial subgroup analysis, and discovery of survival-related imaging features. Together, RadDiff and RadDiffBench provide the first method-and-benchmark foundation for systematically uncovering meaningful differences in radiological data.

