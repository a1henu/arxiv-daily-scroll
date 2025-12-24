---
layout: default
title: DS-HGCN: A Dual-Stream Hypergraph Convolutional Network for Predicting Student Engagement via Social Contagion
---

# DS-HGCN: A Dual-Stream Hypergraph Convolutional Network for Predicting Student Engagement via Social Contagion
**arXiv**：[2512.20059v1](https://arxiv.org/abs/2512.20059) · [PDF](https://arxiv.org/pdf/2512.20059.pdf)  
**作者**：Ziyang Fan, Li Tao, Yi Wang, Jingwei Qu, Ying Wang, Fei Jiang  

**一句话要点**：提出双流超图卷积网络DS-HGCN，通过社交传染预测学生参与度

**关键词**：学生参与度预测, 超图卷积网络, 社交传染, 多特征融合, 注意力机制

## 3 点简述
- 核心问题：学生参与度预测需考虑社交传染和多维特征融合
- 方法要点：构建超图编码参与度传染，引入注意力机制动态加权影响
- 实验或效果：在公开数据集上性能优于现有方法，验证模型有效性

## 摘要（原文）

> Student engagement is a critical factor influencing academic success and learning outcomes. Accurately predicting student engagement is essential for optimizing teaching strategies and providing personalized interventions. However, most approaches focus on single-dimensional feature analysis and assessing engagement based on individual student factors. In this work, we propose a dual-stream multi-feature fusion model based on hypergraph convolutional networks (DS-HGCN), incorporating social contagion of student engagement. DS-HGCN enables accurate prediction of student engagement states by modeling multi-dimensional features and their propagation mechanisms between students. The framework constructs a hypergraph structure to encode engagement contagion among students and captures the emotional and behavioral differences and commonalities by multi-frequency signals. Furthermore, we introduce a hypergraph attention mechanism to dynamically weigh the influence of each student, accounting for individual differences in the propagation process. Extensive experiments on public benchmark datasets demonstrate that our proposed method achieves superior performance and significantly outperforms existing state-of-the-art approaches.

