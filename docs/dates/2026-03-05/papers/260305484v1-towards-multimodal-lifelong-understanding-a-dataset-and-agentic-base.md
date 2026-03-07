---
layout: default
title: Towards Multimodal Lifelong Understanding: A Dataset and Agentic Baseline
---

# Towards Multimodal Lifelong Understanding: A Dataset and Agentic Baseline
**arXiv**：[2603.05484v1](https://arxiv.org/abs/2603.05484) · [PDF](https://arxiv.org/pdf/2603.05484.pdf)  
**作者**：Guo Chen, Lidong Lu, Yicheng Liu, Liangrui Dong, Lidong Zou, Jixin Lv, Zhenquan Li, Xinyi Mao, Baoqi Pei, Shihao Wang, Zhiqi Li, Karan Sapra, Fuxiao Liu, Yin-Dong Zheng, Yifei Huang, Limin Wang, Zhiding Yu, Andrew Tao, Guilin Liu, Tong Lu  

**一句话要点**：提出MM-Lifelong数据集和递归多模态代理ReMA，以解决长视频理解中的记忆瓶颈和定位崩溃问题。

**关键词**：多模态理解, 长视频数据集, 代理模型, 记忆管理, 时间尺度分析, 泛化评估

## 3 点简述
- 核心问题：现有视频数据集与自然日常视频不匹配，导致端到端模型记忆饱和和代理模型长期定位失败。
- 方法要点：引入MM-Lifelong数据集，涵盖日、周、月尺度；提出ReMA代理，通过动态记忆管理迭代更新信念状态。
- 实验或效果：ReMA显著优于现有方法，数据集分割隔离了时间和领域偏差，支持监督学习和泛化研究。

## 摘要（原文）

> While datasets for video understanding have scaled to hour-long durations, they typically consist of densely concatenated clips that differ from natural, unscripted daily life. To bridge this gap, we introduce MM-Lifelong, a dataset designed for Multimodal Lifelong Understanding. Comprising 181.1 hours of footage, it is structured across Day, Week, and Month scales to capture varying temporal densities. Extensive evaluations reveal two critical failure modes in current paradigms: end-to-end MLLMs suffer from a Working Memory Bottleneck due to context saturation, while representative agentic baselines experience Global Localization Collapse when navigating sparse, month-long timelines. To address this, we propose the Recursive Multimodal Agent (ReMA), which employs dynamic memory management to iteratively update a recursive belief state, significantly outperforming existing methods. Finally, we establish dataset splits designed to isolate temporal and domain biases, providing a rigorous foundation for future research in supervised learning and out-of-distribution generalization.

