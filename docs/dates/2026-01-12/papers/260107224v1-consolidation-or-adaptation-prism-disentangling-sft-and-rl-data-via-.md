---
layout: default
title: Consolidation or Adaptation? PRISM: Disentangling SFT and RL Data via Gradient Concentration
---

# Consolidation or Adaptation? PRISM: Disentangling SFT and RL Data via Gradient Concentration
**arXiv**：[2601.07224v1](https://arxiv.org/abs/2601.07224) · [PDF](https://arxiv.org/pdf/2601.07224.pdf)  
**作者**：Yang Zhao, Yangou Ouyang, Xiao Ding, Hepeng Wang, Bibo Cai, Kai Xiong, Jinglong Gao, Zhouhao Sun, Li Du, Bing Qin, Ting Liu  

**一句话要点**：提出PRISM框架，基于梯度空间几何结构，为LLM代理的SFT和RL阶段分配数据以解决优化干扰问题。

**关键词**：LLM代理训练, 数据分配策略, 梯度分析, Schema Theory, 优化干扰, 计算效率

## 3 点简述
- 核心问题：当前LLM代理训练中，SFT和RL阶段的数据分配缺乏有效机制，导致优化干扰。
- 方法要点：PRISM利用Schema Theory，通过分析梯度空间浓度，将高冲突数据分配至RL，低冲突数据分配至SFT。
- 实验或效果：在WebShop和ALFWorld上，PRISM实现Pareto改进，性能优于现有方法，计算成本降低达3.22倍。

## 摘要（原文）

> While Hybrid Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL) has become the standard paradigm for training LLM agents, effective mechanisms for data allocation between these stages remain largely underexplored. Current data arbitration strategies often rely on surface-level heuristics that fail to diagnose intrinsic learning needs. Since SFT targets pattern consolidation through imitation while RL drives structural adaptation via exploration, misaligning data with these functional roles causes severe optimization interference. We propose PRISM, a dynamics-aware framework grounded in Schema Theory that arbitrates data based on its degree of cognitive conflict with the model's existing knowledge. By analyzing the spatial geometric structure of gradients, PRISM identifies data triggering high spatial concentration as high-conflict signals that require RL for structural restructuring. In contrast, data yielding diffuse updates is routed to SFT for efficient consolidation. Extensive experiments on WebShop and ALFWorld demonstrate that PRISM achieves a Pareto improvement, outperforming state-of-the-art hybrid methods while reducing computational costs by up to 3.22$\times$. Our findings suggest that disentangling data based on internal optimization regimes is crucial for scalable and robust agent alignment.

