---
layout: default
title: ViterbiPlanNet: Injecting Procedural Knowledge via Differentiable Viterbi for Planning in Instructional Videos
---

# ViterbiPlanNet: Injecting Procedural Knowledge via Differentiable Viterbi for Planning in Instructional Videos
**arXiv**：[2603.04265v1](https://arxiv.org/abs/2603.04265) · [PDF](https://arxiv.org/pdf/2603.04265.pdf)  
**作者**：Luigi Seminara, Davide Moltisanti, Antonino Furnari  

**一句话要点**：提出ViterbiPlanNet，通过可微分维特比层注入程序知识，用于教学视频中的规划任务。

**关键词**：程序规划, 可微分维特比, 教学视频, 知识图嵌入, 样本效率

## 3 点简述
- 核心问题：现有方法依赖大规模模型隐式学习程序结构，导致样本效率低和计算成本高。
- 方法要点：引入可微分维特比层，将程序知识图嵌入维特比解码算法，实现端到端优化。
- 实验或效果：在CrossTask等数据集上实现SOTA性能，参数少一个数量级，提升样本效率和鲁棒性。

## 摘要（原文）

> Procedural planning aims to predict a sequence of actions that transforms an initial visual state into a desired goal, a fundamental ability for intelligent agents operating in complex environments. Existing approaches typically rely on large-scale models that learn procedural structures implicitly, resulting in limited sample-efficiency and high computational cost. In this work we introduce ViterbiPlanNet, a principled framework that explicitly integrates procedural knowledge into the learning process through a Differentiable Viterbi Layer (DVL). The DVL embeds a Procedural Knowledge Graph (PKG) directly with the Viterbi decoding algorithm, replacing non-differentiable operations with smooth relaxations that enable end-to-end optimization. This design allows the model to learn through graph-based decoding. Experiments on CrossTask, COIN, and NIV demonstrate that ViterbiPlanNet achieves state-of-the-art performance with an order of magnitude fewer parameters than diffusion- and LLM-based planners. Extensive ablations show that performance gains arise from our differentiable structure-aware training rather than post-hoc refinement, resulting in improved sample efficiency and robustness to shorter unseen horizons. We also address testing inconsistencies establishing a unified testing protocol with consistent splits and evaluation metrics. With this new protocol, we run experiments multiple times and report results using bootstrapping to assess statistical significance.

