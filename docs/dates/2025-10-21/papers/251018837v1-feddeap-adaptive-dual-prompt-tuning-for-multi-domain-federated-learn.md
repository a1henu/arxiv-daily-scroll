---
layout: default
title: FedDEAP: Adaptive Dual-Prompt Tuning for Multi-Domain Federated Learning
---

# FedDEAP: Adaptive Dual-Prompt Tuning for Multi-Domain Federated Learning
**arXiv**：[2510.18837v1](https://arxiv.org/abs/2510.18837) · [PDF](https://arxiv.org/pdf/2510.18837.pdf)  
**作者**：Yubin Zheng, Pak-Hei Yeung, Jing Xia, Tianjie Ju, Peng Tang, Weidong Qiu, Jagath C. Rajapakse  

**一句话要点**：提出FedDEAP自适应双提示调优框架以增强多领域联邦学习中CLIP的泛化能力

**关键词**：联邦学习, 多领域学习, 提示调优, CLIP模型, 图像识别

## 3 点简述
- 核心问题：联邦学习中领域偏移和标签异构性阻碍全局模型泛化。
- 方法要点：使用语义和领域变换网络解耦特征，并设计全局语义提示与局部领域提示。
- 实验或效果：在四个数据集上验证了方法对多领域图像识别的有效性。

## 摘要（原文）

> Federated learning (FL) enables multiple clients to collaboratively train
> machine learning models without exposing local data, balancing performance and
> privacy. However, domain shift and label heterogeneity across clients often
> hinder the generalization of the aggregated global model. Recently, large-scale
> vision-language models like CLIP have shown strong zero-shot classification
> capabilities, raising the question of how to effectively fine-tune CLIP across
> domains in a federated setting. In this work, we propose an adaptive federated
> prompt tuning framework, FedDEAP, to enhance CLIP's generalization in
> multi-domain scenarios. Our method includes the following three key components:
> (1) To mitigate the loss of domain-specific information caused by
> label-supervised tuning, we disentangle semantic and domain-specific features
> in images by using semantic and domain transformation networks with unbiased
> mappings; (2) To preserve domain-specific knowledge during global prompt
> aggregation, we introduce a dual-prompt design with a global semantic prompt
> and a local domain prompt to balance shared and personalized information; (3)
> To maximize the inclusion of semantic and domain information from images in the
> generated text features, we align textual and visual representations under the
> two learned transformations to preserve semantic and domain consistency.
> Theoretical analysis and extensive experiments on four datasets demonstrate the
> effectiveness of our method in enhancing the generalization of CLIP for
> federated image recognition across multiple domains.

