---
layout: default
title: A Dataset is Worth 1 MB
---

# A Dataset is Worth 1 MB
**arXiv**：[2602.23358v1](https://arxiv.org/abs/2602.23358) · [PDF](https://arxiv.org/pdf/2602.23358.pdf)  
**作者**：Elad Kimchi Shoshani, Leeyam Gabay, Yedid Hoshen  

**一句话要点**：提出PLADA方法以解决数据集服务器传输成本高的问题，通过仅传输伪标签实现高效任务通信。

**关键词**：数据集蒸馏, 伪标签传输, 通信效率, 任务特定模型, 参考数据集剪枝, 分类准确率

## 3 点简述
- 核心问题：数据集服务器需向多客户端传输大量数据，通信成本高，且客户端硬件和框架多样，传输预训练模型不可行。
- 方法要点：假设客户端预加载通用未标记参考数据集，通过传输特定图像的类标签来通信新任务，引入剪枝机制过滤参考数据集以保留语义相关图像标签。
- 实验或效果：在10个数据集上测试，传输负载小于1 MB，同时保持高分类准确率，验证了方法的有效性。

## 摘要（原文）

> A dataset server must often distribute the same large payload to many clients, incurring massive communication costs. Since clients frequently operate on diverse hardware and software frameworks, transmitting a pre-trained model is often infeasible; instead, agents require raw data to train their own task-specific models locally. While dataset distillation attempts to compress training signals, current methods struggle to scale to high-resolution data and rarely achieve sufficiently small files. In this paper, we propose Pseudo-Labels as Data (PLADA), a method that completely eliminates pixel transmission. We assume agents are preloaded with a large, generic, unlabeled reference dataset (e.g., ImageNet-1K, ImageNet-21K) and communicate a new task by transmitting only the class labels for specific images. To address the distribution mismatch between the reference and target datasets, we introduce a pruning mechanism that filters the reference dataset to retain only the labels of the most semantically relevant images for the target task. This selection process simultaneously maximizes training efficiency and minimizes transmission payload. Experiments on 10 diverse datasets demonstrate that our approach can transfer task knowledge with a payload of less than 1 MB while retaining high classification accuracy, offering a promising solution for efficient dataset serving.

