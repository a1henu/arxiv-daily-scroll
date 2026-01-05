---
layout: default
title: Federated Customization of Large Models: Approaches, Experiments, and Insights
---

# Federated Customization of Large Models: Approaches, Experiments, and Insights
**arXiv**：[2601.00526v1](https://arxiv.org/abs/2601.00526) · [PDF](https://arxiv.org/pdf/2601.00526.pdf)  
**作者**：Yuchuan Ye, Ming Ding, Youjia Chen, Peng Cheng, Dusit Niyato  

**一句话要点**：探索联邦学习下大模型定制方法，首次实验验证联邦前缀调优的可行性。

**关键词**：联邦学习, 大模型定制, 前缀调优, 高效微调, 知识蒸馏, 检索增强生成

## 3 点简述
- 核心问题：联邦学习框架下大模型定制面临数据隐私与模型性能平衡的挑战。
- 方法要点：综述多种定制技术，并讨论其在联邦学习中的实现方式。
- 实验或效果：首次在联邦学习中应用前缀调优，实验显示性能接近集中式方法，且具有竞争力。

## 摘要（原文）

> In this article, we explore federated customization of large models and highlight the key challenges it poses within the federated learning framework. We review several popular large model customization techniques, including full fine-tuning, efficient fine-tuning, prompt engineering, prefix-tuning, knowledge distillation, and retrieval-augmented generation. Then, we discuss how these techniques can be implemented within the federated learning framework. Moreover, we conduct experiments on federated prefix-tuning, which, to the best of our knowledge, is the first trial to apply prefix-tuning in the federated learning setting. The conducted experiments validate its feasibility with performance close to centralized approaches. Further comparison with three other federated customization methods demonstrated its competitive performance, satisfactory efficiency, and consistent robustness.

