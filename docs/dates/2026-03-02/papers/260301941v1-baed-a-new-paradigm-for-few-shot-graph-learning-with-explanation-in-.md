---
layout: default
title: BAED: a New Paradigm for Few-shot Graph Learning with Explanation in the Loop
---

# BAED: a New Paradigm for Few-shot Graph Learning with Explanation in the Loop
**arXiv**：[2603.01941v1](https://arxiv.org/abs/2603.01941) · [PDF](https://arxiv.org/pdf/2603.01941.pdf)  
**作者**：Chao Chen, Xujia Li, Dongsheng Hong, Shanshan Lin, Xiangwen Liao, Chuanyi Liu, Lei Chen  

**一句话要点**：提出BAED框架，通过解释循环解决少样本图学习中的鲁棒性和可解释性问题。

**关键词**：少样本图学习, 解释循环框架, 信念传播算法, 图神经网络, 标签增强, 解释性子图提取

## 3 点简述
- 核心问题：少样本图学习中标签不足导致模型鲁棒性和可解释性差，易过拟合噪声。
- 方法要点：结合信念传播算法进行标签增强，利用辅助图神经网络和梯度反向传播提取解释性子图。
- 实验或效果：在七个基准数据集上验证了BAED在预测精度、训练效率和解释质量上的优越性。

## 摘要（原文）

> The challenges of training and inference in few-shot environments persist in the area of graph representation learning. The quality and quantity of labels are often insufficient due to the extensive expert knowledge required to annotate graph data. In this context, Few-Shot Graph Learning (FSGL) approaches have been developed over the years. Through sophisticated neural architectures and customized training pipelines, these approaches enhance model adaptability to new label distributions. However, compromises in \textcolor{black}{the model's} robustness and interpretability can result in overfitting to noise in labeled data and degraded performance. This paper introduces the first explanation-in-the-loop framework for the FSGL problem, called BAED. We novelly employ the belief propagation algorithm to facilitate label augmentation on graphs. Then, leveraging an auxiliary graph neural network and the gradient backpropagation method, our framework effectively extracts explanatory subgraphs surrounding target nodes. The final predictions are based on these informative subgraphs while mitigating the influence of redundant information from neighboring nodes. Extensive experiments on seven benchmark datasets demonstrate superior prediction accuracy, training efficiency, and explanation quality of BAED. As a pioneer, this work highlights the potential of the explanation-based research paradigm in FSGL.

