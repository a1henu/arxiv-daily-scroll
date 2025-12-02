---
layout: default
title: Directed evolution algorithm drives neural prediction
---

# Directed evolution algorithm drives neural prediction
**arXiv**：[2512.01362v1](https://arxiv.org/abs/2512.01362) · [PDF](https://arxiv.org/pdf/2512.01362.pdf)  
**作者**：Yanlin Wang, Nancy M Young, Patrick C M Wong  

**一句话要点**：提出定向进化模型以解决神经预测中的领域偏移和标签稀缺问题

**关键词**：神经预测, 定向进化算法, 领域自适应, 强化学习, 医学人工智能, 跨域预测

## 3 点简述
- 核心问题：神经预测模型在医学AI应用中面临领域偏移和标签稀缺的挑战，导致跨域预测性能下降。
- 方法要点：定向进化模型模仿生物定向进化的试错过程，结合重放缓冲和持续反向传播，优化探索与利用的平衡。
- 实验或效果：在儿童人工耳蜗植入数据集上，模型有效提升了跨域术前神经预测的准确性，并缓解了目标域标签稀缺问题。

## 摘要（原文）

> Neural prediction offers a promising approach to forecasting the individual variability of neurocognitive functions and disorders and providing prognostic indicators for personalized invention. However, it is challenging to translate neural predictive models into medical artificial intelligent applications due to the limitations of domain shift and label scarcity. Here, we propose the directed evolution model (DEM), a novel computational model that mimics the trial-and-error processes of biological directed evolution to approximate optimal solutions for predictive modeling tasks. We demonstrated that the directed evolution algorithm is an effective strategy for uncertainty exploration, enhancing generalization in reinforcement learning. Furthermore, by incorporating replay buffer and continual backpropagate methods into DEM, we provide evidence of achieving better trade-off between exploitation and exploration in continuous learning settings. We conducted experiments on four different datasets for children with cochlear implants whose spoken language developmental outcomes vary considerably on the individual-child level. Preoperative neural MRI data has shown to accurately predict the post-operative outcome of these children within but not across datasets. Our results show that DEM can efficiently improve the performance of cross-domain pre-implantation neural predictions while addressing the challenge of label scarcity in target domain.

