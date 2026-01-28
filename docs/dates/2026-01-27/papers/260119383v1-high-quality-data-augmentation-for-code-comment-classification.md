---
layout: default
title: High-quality data augmentation for code comment classification
---

# High-quality data augmentation for code comment classification
**arXiv**：[2601.19383v1](https://arxiv.org/abs/2601.19383) · [PDF](https://arxiv.org/pdf/2601.19383.pdf)  
**作者**：Thomas Borsani, Andrea Rosani, Giuseppe Di Fatta  

**一句话要点**：提出高质量数据增强技术Q-SYNTH以解决代码注释分类中的数据集限制问题

**关键词**：代码注释分类, 数据增强, 合成过采样, 自然语言处理, 深度学习, 软件工程

## 3 点简述
- 核心问题：代码注释分类数据集存在规模小和类别不平衡问题，影响模型性能
- 方法要点：基于高质量数据生成，引入合成过采样和增强技术Q-SYNTH
- 实验或效果：在NLBSE'26挑战数据集上，Q-SYNTH将基础分类器性能提升2.56%

## 摘要（原文）

> Code comments serve a crucial role in software development for documenting functionality, clarifying design choices, and assisting with issue tracking. They capture developers' insights about the surrounding source code, serving as an essential resource for both human comprehension and automated analysis. Nevertheless, since comments are in natural language, they present challenges for machine-based code understanding. To address this, recent studies have applied natural language processing (NLP) and deep learning techniques to classify comments according to developers' intentions. However, existing datasets for this task suffer from size limitations and class imbalance, as they rely on manual annotations and may not accurately represent the distribution of comments in real-world codebases. To overcome this issue, we introduce new synthetic oversampling and augmentation techniques based on high-quality data generation to enhance the NLBSE'26 challenge datasets. Our Synthetic Quality Oversampling Technique and Augmentation Technique (Q-SYNTH) yield promising results, improving the base classifier by $2.56\%$.

