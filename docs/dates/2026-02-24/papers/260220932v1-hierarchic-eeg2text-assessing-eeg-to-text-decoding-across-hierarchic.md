---
layout: default
title: Hierarchic-EEG2Text: Assessing EEG-To-Text Decoding across Hierarchical Abstraction Levels
---

# Hierarchic-EEG2Text: Assessing EEG-To-Text Decoding across Hierarchical Abstraction Levels
**arXiv**：[2602.20932v1](https://arxiv.org/abs/2602.20932) · [PDF](https://arxiv.org/pdf/2602.20932.pdf)  
**作者**：Anupam Sharma, Harish Katti, Prajwal Singh, Shanmuganathan Raman, Krishna Miyapuram  

**一句话要点**：提出层次感知的片段分析框架，评估EEG信号在WordNet层次结构下的文本解码性能。

**关键词**：脑电图解码, 层次语义分析, 片段学习, WordNet, 文本分类, 神经动力学

## 3 点简述
- 核心问题：EEG信号能否捕获跨多个语义抽象层次的对象表示，以提升细粒度分类。
- 方法要点：采用WordNet生成可变类别数的层次感知片段，进行多任务机器学习评估。
- 实验或效果：在PEERS数据集上验证，模型在更高抽象层次分类表现更佳，揭示抽象深度对解码的影响。

## 摘要（原文）

> An electroencephalogram (EEG) records the spatially averaged electrical activity of neurons in the brain, measured from the human scalp. Prior studies have explored EEG-based classification of objects or concepts, often for passive viewing of briefly presented image or video stimuli, with limited classes. Because EEG exhibits a low signal-to-noise ratio, recognizing fine-grained representations across a large number of classes remains challenging; however, abstract-level object representations may exist. In this work, we investigate whether EEG captures object representations across multiple hierarchical levels, and propose episodic analysis, in which a Machine Learning (ML) model is evaluated across various, yet related, classification tasks (episodes). Unlike prior episodic EEG studies that rely on fixed or randomly sampled classes of equal cardinality, we adopt hierarchy-aware episode sampling using WordNet to generate episodes with variable classes of diverse hierarchy. We also present the largest episodic framework in the EEG domain for detecting observed text from EEG signals in the PEERS dataset, comprising $931538$ EEG samples under $1610$ object labels, acquired from $264$ human participants (subjects) performing controlled cognitive tasks, enabling the study of neural dynamics underlying perception, decision-making, and performance monitoring.
>   We examine how the semantic abstraction level affects classification performance across multiple learning techniques and architectures, providing a comprehensive analysis. The models tend to improve performance when the classification categories are drawn from higher levels of the hierarchy, suggesting sensitivity to abstraction. Our work highlights abstraction depth as an underexplored dimension of EEG decoding and motivates future research in this direction.

