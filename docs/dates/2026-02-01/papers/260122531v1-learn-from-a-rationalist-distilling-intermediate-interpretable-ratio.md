---
layout: default
title: Learn from A Rationalist: Distilling Intermediate Interpretable Rationales
---

# Learn from A Rationalist: Distilling Intermediate Interpretable Rationales
**arXiv**：[2601.22531v1](https://arxiv.org/abs/2601.22531) · [PDF](https://arxiv.org/pdf/2601.22531.pdf)  
**作者**：Jiayi Dai, Randy Goebel  

**一句话要点**：提出REKD方法，通过知识蒸馏提升基于较小神经网络的理性提取模型的预测性能。

**关键词**：理性提取, 知识蒸馏, 特征选择, 神经网络解释性, 预测性能提升

## 3 点简述
- 核心问题：基于较小神经网络的理性提取模型在特征选择空间搜索中面临计算挑战，导致预测性能受限。
- 方法要点：引入教师模型（理性主义者）的理性和预测作为额外监督，学生模型通过知识蒸馏学习，增强特征选择能力。
- 实验或效果：在语言和视觉分类数据集上，REKD显著提升学生模型的预测性能，验证了方法的有效性。

## 摘要（原文）

> Because of the pervasive use of deep neural networks (DNNs), especially in high-stakes domains, the interpretability of DNNs has received increased attention. The general idea of rationale extraction (RE) is to provide an interpretable-by-design framework for DNNs via a select-predict architecture where two neural networks learn jointly to perform feature selection and prediction, respectively. Given only the remote supervision from the final task prediction, the process of learning to select subsets of features (or \emph{rationales}) requires searching in the space of all possible feature combinations, which is computationally challenging and even harder when the base neural networks are not sufficiently capable. To improve the predictive performance of RE models that are based on less capable or smaller neural networks (i.e., the students), we propose \textbf{REKD} (\textbf{R}ationale \textbf{E}xtraction with \textbf{K}nowledge \textbf{D}istillation) where a student RE model learns from the rationales and predictions of a teacher (i.e., a \emph{rationalist}) in addition to the student's own RE optimization. This structural adjustment to RE aligns well with how humans could learn effectively from interpretable and verifiable knowledge. Because of the neural-model agnostic nature of the method, any black-box neural network could be integrated as a backbone model. To demonstrate the viability of REKD, we conduct experiments with multiple variants of BERT and vision transformer (ViT) models. Our experiments across language and vision classification datasets (i.e., IMDB movie reviews, CIFAR 10 and CIFAR 100) show that REKD significantly improves the predictive performance of the student RE models.

