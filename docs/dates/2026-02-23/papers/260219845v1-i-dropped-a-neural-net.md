---
layout: default
title: I Dropped a Neural Net
---

# I Dropped a Neural Net
**arXiv**：[2602.19845v1](https://arxiv.org/abs/2602.19845) · [PDF](https://arxiv.org/pdf/2602.19845.pdf)  
**作者**：Hyunwoo Park  

**一句话要点**：提出基于训练稳定性的方法，从乱序层中恢复残差网络的原始层序

**关键词**：残差网络, 层序恢复, 训练稳定性, 动态等距, 对角线优势比, 爬山搜索

## 3 点简述
- 核心问题：给定未标记的残差网络层和训练数据集，恢复层的精确排序，搜索空间巨大（约10^122）。
- 方法要点：利用动态等距等训练稳定性条件，通过负对角结构配对层，并使用对角线优势比作为信号。
- 实验或效果：通过代理指标（如delta-norm）初始化，爬山搜索实现零均方误差，成功恢复层序。

## 摘要（原文）

> A recent Dwarkesh Patel podcast with John Collison and Elon Musk featured an interesting puzzle from Jane Street: they trained a neural net, shuffled all 96 layers, and asked to put them back in order.
>   Given unlabelled layers of a Residual Network and its training dataset, we recover the exact ordering of the layers. The problem decomposes into pairing each block's input and output projections ($48!$ possibilities) and ordering the reassembled blocks ($48!$ possibilities), for a combined search space of $(48!)^2 \approx 10^{122}$, which is more than the atoms in the observable universe. We show that stability conditions during training like dynamic isometry leave the product $W_{\text{out}} W_{\text{in}}$ for correctly paired layers with a negative diagonal structure, allowing us to use diagonal dominance ratio as a signal for pairing. For ordering, we seed-initialize with a rough proxy such as delta-norm or $\\|W_{\text{out}}\\|_F$ then hill-climb to zero mean squared error.

