---
layout: default
title: LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion
---

# LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion
**arXiv**：[2602.12215v1](https://arxiv.org/abs/2602.12215) · [PDF](https://arxiv.org/pdf/2602.12215.pdf)  
**作者**：Jiangran Lyu, Kai Liu, Xuheng Zhang, Haoran Liao, Yusen Feng, Wenxuan Zhu, Tingrui Shen, Jiayi Chen, Jiazhao Zhang, Yifei Dong, Wenbo Cui, Senmao Qi, Shuo Wang, Yixin Zheng, Mi Yan, Xuesong Shi, Haoran Li, Dongbin Zhao, Ming-Yu Liu, Zhizheng Zhang, Li Yi, Yizhou Wang, He Wang  

**一句话要点**：提出LDA-1B机器人基础模型，通过通用具身数据摄入联合学习动力学、策略和视觉预测，以解决异构数据利用不足的问题。

**关键词**：机器人基础模型, 具身数据摄入, 动力学学习, 多模态扩散变换器, 结构化潜在空间, 数据高效微调

## 3 点简述
- 核心问题：现有机器人基础模型依赖大规模行为克隆，丢弃异构具身数据中的可迁移动力学知识，且统一世界模型实例化因数据使用粗放和数据集碎片化难以扩展。
- 方法要点：LDA-1B基于结构化DINO潜在空间预测和多模态扩散变换器，处理异步视觉与动作流，实现1B参数规模的稳定训练，并利用EI-30k数据集标准化数据。
- 实验或效果：在仿真和真实世界任务中，LDA-1B在接触丰富、灵巧和长时程任务上分别提升高达21%、48%和23%，并能通过低质量轨迹进行数据高效微调，增益10%。

## 摘要（原文）

> Recent robot foundation models largely rely on large-scale behavior cloning, which imitates expert actions but discards transferable dynamics knowledge embedded in heterogeneous embodied data. While the Unified World Model (UWM) formulation has the potential to leverage such diverse data, existing instantiations struggle to scale to foundation-level due to coarse data usage and fragmented datasets. We introduce LDA-1B, a robot foundation model that scales through universal embodied data ingestion by jointly learning dynamics, policy, and visual forecasting, assigning distinct roles to data of varying quality. To support this regime at scale, we assemble and standardize EI-30k, an embodied interaction dataset comprising over 30k hours of human and robot trajectories in a unified format. Scalable dynamics learning over such heterogeneous data is enabled by prediction in a structured DINO latent space, which avoids redundant pixel-space appearance modeling. Complementing this representation, LDA-1B employs a multi-modal diffusion transformer to handle asynchronous vision and action streams, enabling stable training at the 1B-parameter scale. Experiments in simulation and the real world show LDA-1B outperforms prior methods (e.g., $π_{0.5}$) by up to 21\%, 48\%, and 23\% on contact-rich, dexterous, and long-horizon tasks, respectively. Notably, LDA-1B enables data-efficient fine-tuning, gaining 10\% by leveraging 30\% low-quality trajectories typically harmful and discarded.

