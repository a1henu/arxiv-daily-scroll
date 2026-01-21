---
layout: default
title: Federated Balanced Learning
---

# Federated Balanced Learning
**arXiv**：[2601.14042v1](https://arxiv.org/abs/2601.14042) · [PDF](https://arxiv.org/pdf/2601.14042.pdf)  
**作者**：Jiaze Li, Haoran Xu, Wanyi Wu, Changwei Wang, Shuaiguang Li, Jianzhong Ju, Zhenbo Luo, Jian Luan, Youyang Qu, Longxiang Gao, Xudong Yang, Lumin Xing  

**一句话要点**：提出联邦平衡学习以解决非独立同分布下的客户端漂移问题

**关键词**：联邦学习, 非独立同分布, 样本平衡, 知识填充, 客户端漂移, 生成模型

## 3 点简述
- 核心问题：非独立同分布数据导致全局模型客户端漂移，影响性能
- 方法要点：客户端通过知识填充和采样实现样本平衡，结合知识对齐和丢弃策略
- 实验或效果：在真实复杂场景中超越现有基线，代码将发布

## 摘要（原文）

> Federated learning is a paradigm of joint learning in which clients collaborate by sharing model parameters instead of data. However, in the non-iid setting, the global model experiences client drift, which can seriously affect the final performance of the model. Previous methods tend to correct the global model that has already deviated based on the loss function or gradient, overlooking the impact of the client samples. In this paper, we rethink the role of the client side and propose Federated Balanced Learning, i.e., FBL, to prevent this issue from the beginning through sample balance on the client side. Technically, FBL allows unbalanced data on the client side to achieve sample balance through knowledge filling and knowledge sampling using edge-side generation models, under the limitation of a fixed number of data samples on clients. Furthermore, we design a Knowledge Alignment Strategy to bridge the gap between synthetic and real data, and a Knowledge Drop Strategy to regularize our method. Meanwhile, we scale our method to real and complex scenarios, allowing different clients to adopt various methods, and extend our framework to further improve performance. Numerous experiments show that our method outperforms state-of-the-art baselines. The code is released upon acceptance.

