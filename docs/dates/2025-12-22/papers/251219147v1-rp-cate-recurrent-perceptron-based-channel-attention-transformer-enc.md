---
layout: default
title: RP-CATE: Recurrent Perceptron-based Channel Attention Transformer Encoder for Industrial Hybrid Modeling
---

# RP-CATE: Recurrent Perceptron-based Channel Attention Transformer Encoder for Industrial Hybrid Modeling
**arXiv**：[2512.19147v1](https://arxiv.org/abs/2512.19147) · [PDF](https://arxiv.org/pdf/2512.19147.pdf)  
**作者**：Haoran Yang, Yinan Zhang, Wenjie Zhang, Dongxia Wang, Peiyu Liu, Yuqi Ye, Kexin Chen, Wenhai Wang  

**一句话要点**：提出RP-CATE以解决工业混合建模中架构不全面和关联利用不足的问题

**关键词**：工业混合建模, 通道注意力, 循环感知机, Transformer编码器, 伪图像数据, 伪序列数据

## 3 点简述
- 现有工业混合建模方法架构单一，难以全面表示复杂工业场景
- RP-CATE用通道注意力和循环感知机模块替换自注意力，提升建模效果
- 实验在化工混合建模中验证，RP-CATE性能优于基线模型

## 摘要（原文）

> Nowadays, industrial hybrid modeling which integrates both mechanistic modeling and machine learning-based modeling techniques has attracted increasing interest from scholars due to its high accuracy, low computational cost, and satisfactory interpretability. Nevertheless, the existing industrial hybrid modeling methods still face two main limitations. First, current research has mainly focused on applying a single machine learning method to one specific task, failing to develop a comprehensive machine learning architecture suitable for modeling tasks, which limits their ability to effectively represent complex industrial scenarios. Second, industrial datasets often contain underlying associations (e.g., monotonicity or periodicity) that are not adequately exploited by current research, which can degrade model's predictive performance. To address these limitations, this paper proposes the Recurrent Perceptron-based Channel Attention Transformer Encoder (RP-CATE), with three distinctive characteristics: 1: We developed a novel architecture by replacing the self-attention mechanism with channel attention and incorporating our proposed Recurrent Perceptron (RP) Module into Transformer, achieving enhanced effectiveness for industrial modeling tasks compared to the original Transformer. 2: We proposed a new data type called Pseudo-Image Data (PID) tailored for channel attention requirements and developed a cyclic sliding window method for generating PID. 3: We introduced the concept of Pseudo-Sequential Data (PSD) and a method for converting industrial datasets into PSD, which enables the RP Module to capture the underlying associations within industrial dataset more effectively. An experiment aimed at hybrid modeling in chemical engineering was conducted by using RP-CATE and the experimental results demonstrate that RP-CATE achieves the best performance compared to other baseline models.

