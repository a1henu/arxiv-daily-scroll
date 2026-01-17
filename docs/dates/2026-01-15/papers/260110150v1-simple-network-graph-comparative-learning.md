---
layout: default
title: Simple Network Graph Comparative Learning
---

# Simple Network Graph Comparative Learning
**arXiv**：[2601.10150v1](https://arxiv.org/abs/2601.10150) · [PDF](https://arxiv.org/pdf/2601.10150.pdf)  
**作者**：Qiang Yu, Xinran Cheng, Shiqiang Xu, Chuanyi Liu  

**一句话要点**：提出SNGCL方法以解决图对比学习中数据增强差异大和依赖负样本的问题，用于节点分类任务。

**关键词**：图对比学习, 节点分类, 拉普拉斯平滑, 孪生网络, 三元损失

## 3 点简述
- 核心问题：现有图对比学习方法在节点分类中面临数据增强导致视图差异大和过度依赖负样本的挑战。
- 方法要点：采用叠加多层拉普拉斯平滑滤波器处理数据，生成全局和局部特征平滑矩阵，并输入孪生网络，使用改进的三元重组损失函数优化类内和类间距离。
- 实验或效果：在节点分类任务中与先进模型比较，SNGCL在多数任务中表现出强竞争力。

## 摘要（原文）

> The effectiveness of contrastive learning methods has been widely recognized in the field of graph learning, especially in contexts where graph data often lack labels or are difficult to label. However, the application of these methods to node classification tasks still faces a number of challenges. First, existing data enhancement techniques may lead to significant differences from the original view when generating new views, which may weaken the relevance of the view and affect the efficiency of model training. Second, the vast majority of existing graph comparison learning algorithms rely on the use of a large number of negative samples. To address the above challenges, this study proposes a novel node classification contrast learning method called Simple Network Graph Comparative Learning (SNGCL). Specifically, SNGCL employs a superimposed multilayer Laplace smoothing filter as a step in processing the data to obtain global and local feature smoothing matrices, respectively, which are thus passed into the target and online networks of the siamese network, and finally employs an improved triple recombination loss function to bring the intra-class distance closer and the inter-class distance farther. We have compared SNGCL with state-of-the-art models in node classification tasks, and the experimental results show that SNGCL is strongly competitive in most tasks.

