---
layout: default
title: Boosting Skeleton-based Zero-Shot Action Recognition with Training-Free Test-Time Adaptation
---

# Boosting Skeleton-based Zero-Shot Action Recognition with Training-Free Test-Time Adaptation
**arXiv**：[2512.11458v1](https://arxiv.org/abs/2512.11458) · [PDF](https://arxiv.org/pdf/2512.11458.pdf)  
**作者**：Jingmin Zhu, Anqi Zhu, Hossein Rahmani, Jun Liu, Mohammed Bennamoun, Qiuhong Ke  

**一句话要点**：提出Skeleton-Cache框架，通过无训练测试时适应提升骨架零样本动作识别的泛化能力。

**关键词**：骨架动作识别, 零样本学习, 测试时适应, 大语言模型, 非参数缓存

## 3 点简述
- 针对骨架零样本动作识别中未见动作泛化不足的问题，提出首个无训练测试时适应框架。
- 方法结合全局与局部骨架描述符，并利用大语言模型语义推理指导预测融合，实现动态适应。
- 在NTU RGB+D 60/120和PKU-MMD II数据集上验证，能提升多种骨干网络的零样本和广义零样本性能。

## 摘要（原文）

> We introduce Skeleton-Cache, the first training-free test-time adaptation framework for skeleton-based zero-shot action recognition (SZAR), aimed at improving model generalization to unseen actions during inference. Skeleton-Cache reformulates inference as a lightweight retrieval process over a non-parametric cache that stores structured skeleton representations, combining both global and fine-grained local descriptors. To guide the fusion of descriptor-wise predictions, we leverage the semantic reasoning capabilities of large language models (LLMs) to assign class-specific importance weights. By integrating these structured descriptors with LLM-guided semantic priors, Skeleton-Cache dynamically adapts to unseen actions without any additional training or access to training data. Extensive experiments on NTU RGB+D 60/120 and PKU-MMD II demonstrate that Skeleton-Cache consistently boosts the performance of various SZAR backbones under both zero-shot and generalized zero-shot settings. The code is publicly available at https://github.com/Alchemist0754/Skeleton-Cache.

