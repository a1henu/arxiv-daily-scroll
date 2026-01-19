---
layout: default
title: Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse
---

# Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse
**arXiv**：[2601.11042v1](https://arxiv.org/abs/2601.11042) · [PDF](https://arxiv.org/pdf/2601.11042.pdf)  
**作者**：Chi Zhang, Mengqi Zhang, Xiaotian Ye, Runxi Cheng, Zisheng Zhou, Ying Zhou, Pengjie Ren, Zhumin Chen  

**一句话要点**：提出REVIVE框架以解决大语言模型顺序知识编辑中的能力崩溃问题

**关键词**：顺序知识编辑, 谱分析, 大语言模型, 能力崩溃, 奇异值分解

## 3 点简述
- 核心问题：顺序知识编辑导致模型通用能力灾难性崩溃，机制未明
- 方法要点：通过谱分析识别主导奇异方向，REVIVE保护该子空间以稳定编辑
- 实验或效果：在多个模型和基准上，REVIVE提升编辑效果并显著保留通用能力

## 摘要（原文）

> Sequential knowledge editing in large language models often causes catastrophic collapse of the model's general abilities, especially for parameter-modifying methods. Existing approaches mitigate this issue through heuristic constraints on parameter updates, yet the mechanisms underlying such degradation remain insufficiently understood. In this work, we present a spectral analysis of sequential knowledge editing and show that a model's general abilities are closely associated with dominant singular directions of pretrained weight matrices. These directions are highly sensitive to perturbations and are progressively disrupted by repeated edits, closely tracking the collapse in both editing efficacy and general performance. Building on this insight, we propose REVIVE, a plug-and-play framework that stabilizes sequential editing by explicitly preserving the dominant singular subspace. REVIVE represents parameter updates in the spectral basis of the original weights and filters components that would interfere with the protected region. Extensive experiments across multiple models and benchmarks show that REVIVE consistently improves editing efficacy while substantially preserving general abilities under long-horizon sequential editing, including extreme settings with up to 20,000 edits.

