---
layout: default
title: Clinical-Prior Guided Multi-Modal Learning with Latent Attention Pooling for Gait-Based Scoliosis Screening
---

# Clinical-Prior Guided Multi-Modal Learning with Latent Attention Pooling for Gait-Based Scoliosis Screening
**arXiv**：[2602.06743v1](https://arxiv.org/abs/2602.06743) · [PDF](https://arxiv.org/pdf/2602.06743.pdf)  
**作者**：Dong Chen, Zizhuang Wei, Jialei Xu, Xinyang Sun, Zonglin He, Meiru An, Huili Peng, Yong Hu, Kenneth MC Cheung  

**一句话要点**：提出临床先验引导的多模态学习框架，用于基于步态的脊柱侧弯筛查。

**关键词**：步态分析, 多模态学习, 临床先验, 注意力池化, 脊柱侧弯筛查

## 3 点简述
- 核心问题：传统脊柱侧弯筛查方法主观且难以扩展，现有步态分析存在数据泄露和模型简化问题。
- 方法要点：集成临床先验知识图和潜在注意力池化，融合视频、文本和知识图模态。
- 实验或效果：在新基准数据集上实现最优性能，提供可解释且临床基础的评估方案。

## 摘要（原文）

> Adolescent Idiopathic Scoliosis (AIS) is a prevalent spinal deformity whose progression can be mitigated through early detection. Conventional screening methods are often subjective, difficult to scale, and reliant on specialized clinical expertise. Video-based gait analysis offers a promising alternative, but current datasets and methods frequently suffer from data leakage, where performance is inflated by repeated clips from the same individual, or employ oversimplified models that lack clinical interpretability. To address these limitations, we introduce ScoliGait, a new benchmark dataset comprising 1,572 gait video clips for training and 300 fully independent clips for testing. Each clip is annotated with radiographic Cobb angles and descriptive text based on clinical kinematic priors. We propose a multi-modal framework that integrates a clinical-prior-guided kinematic knowledge map for interpretable feature representation, alongside a latent attention pooling mechanism to fuse video, text, and knowledge map modalities. Our method establishes a new state-of-the-art, demonstrating a significant performance gap on a realistic, non-repeating subject benchmark. Our approach establishes a new state of the art, showing a significant performance gain on a realistic, subject-independent benchmark. This work provides a robust, interpretable, and clinically grounded foundation for scalable, non-invasive AIS assessment.

