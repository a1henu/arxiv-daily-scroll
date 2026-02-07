---
layout: default
title: Erase at the Core: Representation Unlearning for Machine Unlearning
---

# Erase at the Core: Representation Unlearning for Machine Unlearning
**arXiv**：[2602.05375v1](https://arxiv.org/abs/2602.05375) · [PDF](https://arxiv.org/pdf/2602.05375.pdf)  
**作者**：Jaewon Lee, Yongwoo Kim, Donghyun Kim  

**一句话要点**：提出Erase at the Core框架，通过多层次对比学习解决机器学习遗忘中的表征残留问题。

**关键词**：机器学习遗忘, 表征遗忘, 对比学习, 多层次监督, 模型无关性, 插件模块

## 3 点简述
- 核心问题：现有遗忘方法仅改变分类器，导致中间表征残留，形成表面遗忘。
- 方法要点：在中间层附加辅助模块，结合对比遗忘和交叉熵损失，实现全网络层次遗忘。
- 实验效果：有效降低与原始模型的表征相似性，同时保持保留集性能，模型无关且可插件集成。

## 摘要（原文）

> Many approximate machine unlearning methods demonstrate strong logit-level forgetting -- such as near-zero accuracy on the forget set -- yet continue to preserve substantial information within their internal feature representations. We refer to this discrepancy as superficial forgetting. Recent studies indicate that most existing unlearning approaches primarily alter the final classifier, leaving intermediate representations largely unchanged and highly similar to those of the original model. To address this limitation, we introduce the Erase at the Core (EC), a framework designed to enforce forgetting throughout the entire network hierarchy. EC integrates multi-layer contrastive unlearning on the forget set with retain set preservation through deeply supervised learning. Concretely, EC attaches auxiliary modules to intermediate layers and applies both contrastive unlearning and cross-entropy losses at each supervision point, with layer-wise weighted losses. Experimental results show that EC not only achieves effective logit-level forgetting, but also substantially reduces representational similarity to the original model across intermediate layers. Furthermore, EC is model-agnostic and can be incorporated as a plug-in module into existing unlearning methods, improving representation-level forgetting while maintaining performance on the retain set.

