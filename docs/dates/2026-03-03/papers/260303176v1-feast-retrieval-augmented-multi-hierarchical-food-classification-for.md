---
layout: default
title: FEAST: Retrieval-Augmented Multi-Hierarchical Food Classification for the FoodEx2 System
---

# FEAST: Retrieval-Augmented Multi-Hierarchical Food Classification for the FoodEx2 System
**arXiv**：[2603.03176v1](https://arxiv.org/abs/2603.03176) · [PDF](https://arxiv.org/pdf/2603.03176.pdf)  
**作者**：Lorenzo Molfetta, Alessio Cocchieri, Stefano Fantazzini, Giacomo Frisoni, Luca Ragazzi, Gianluca Moro  

**一句话要点**：提出FEAST框架以解决FoodEx2系统中复杂层次分类的挑战

**关键词**：层次文本分类, 检索增强学习, FoodEx2系统, 深度度量学习, 多标签分类

## 3 点简述
- 核心问题：FoodEx2系统面临层次文本分类的复杂标签依赖、数据稀疏和极端输出维度问题。
- 方法要点：采用检索增强的三阶段方法，包括基词识别、多标签面预测和面描述符分配，结合深度度量学习。
- 实验或效果：在FoodEx2基准测试中，FEAST在稀有类别上的F1分数比基线提升12-38%。

## 摘要（原文）

> Hierarchical text classification (HTC) and extreme multi-label classification (XML) tasks face compounded challenges from complex label interdependencies, data sparsity, and extreme output dimensions. These challenges are exemplified in the European Food Safety Authority's FoodEx2 system-a standardized food classification framework essential for food consumption monitoring and contaminant exposure assessment across Europe. FoodEx2 coding transforms natural language food descriptions into a set of codes from multiple standardized hierarchies, but faces implementation barriers due to its complex structure. Given a food description (e.g., "organic yogurt''), the system identifies its base term ("yogurt''), all the applicable facet categories (e.g., "production method''), and then, every relevant facet descriptors to each category (e.g., "organic production''). While existing models perform adequately on well-balanced and semantically dense hierarchies, no work has been applied on the practical constraints imposed by the FoodEx2 system. The limited literature addressing such real-world scenarios further compounds these challenges. We propose FEAST (Food Embedding And Semantic Taxonomy), a novel retrieval-augmented framework that decomposes FoodEx2 classification into a three-stage approach: (1) base term identification, (2) multi-label facet prediction, and (3) facet descriptor assignment. By leveraging the system's hierarchical structure to guide training and performing deep metric learning, FEASTlearns discriminative embeddings that mitigate data sparsity and improve generalization on rare and fine-grained labels. Evaluated on the multilingual FoodEx2 benchmark, FEAST outperforms the prior European's CNN baseline F1 scores by 12-38 % on rare classes.

