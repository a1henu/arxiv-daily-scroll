---
layout: default
title: Generate, Transfer, Adapt: Learning Functional Dexterous Grasping from a Single Human Demonstration
---

# Generate, Transfer, Adapt: Learning Functional Dexterous Grasping from a Single Human Demonstration
**arXiv**：[2601.05243v1](https://arxiv.org/abs/2601.05243) · [PDF](https://arxiv.org/pdf/2601.05243.pdf)  
**作者**：Xingyi He, Adhitya Polavaram, Yunhao Cao, Om Deshmukh, Tianrui Wang, Xiaowei Zhou, Kuan Fang  

**一句话要点**：提出CorDex框架，从单次人类演示学习灵巧功能抓取，解决数据稀缺与语义几何推理缺失问题。

**关键词**：灵巧抓取, 功能抓取, 数据生成, 多模态学习, 机器人操作

## 3 点简述
- 核心问题：灵巧功能抓取面临大规模数据集稀缺和模型缺乏语义几何集成推理的瓶颈。
- 方法要点：基于对应关系的数据引擎生成合成数据，通过多模态网络融合视觉与几何信息预测抓取。
- 实验或效果：在多种物体类别上验证，CorDex泛化至未见实例，显著优于现有基线方法。

## 摘要（原文）

> Functional grasping with dexterous robotic hands is a key capability for enabling tool use and complex manipulation, yet progress has been constrained by two persistent bottlenecks: the scarcity of large-scale datasets and the absence of integrated semantic and geometric reasoning in learned models. In this work, we present CorDex, a framework that robustly learns dexterous functional grasps of novel objects from synthetic data generated from just a single human demonstration. At the core of our approach is a correspondence-based data engine that generates diverse, high-quality training data in simulation. Based on the human demonstration, our data engine generates diverse object instances of the same category, transfers the expert grasp to the generated objects through correspondence estimation, and adapts the grasp through optimization. Building on the generated data, we introduce a multimodal prediction network that integrates visual and geometric information. By devising a local-global fusion module and an importance-aware sampling mechanism, we enable robust and computationally efficient prediction of functional dexterous grasps. Through extensive experiments across various object categories, we demonstrate that CorDex generalizes well to unseen object instances and significantly outperforms state-of-the-art baselines.

