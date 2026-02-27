---
layout: default
title: Generative Recommendation for Large-Scale Advertising
---

# Generative Recommendation for Large-Scale Advertising
**arXiv**：[2602.22732v1](https://arxiv.org/abs/2602.22732) · [PDF](https://arxiv.org/pdf/2602.22732.pdf)  
**作者**：Ben Xue, Dan Liu, Lixiang Wang, Mingjie Sun, Peng Wang, Pengfei Zhang, Shaoyun Shi, Tianyu Xu, Yunhao Sha, Zhiqiang Liu, Bo Kong, Bo Wang, Hang Yang, Jieting Xue, Junhao Wang, Shengyu Wang, Shuping Hui, Wencai Ye, Xiao Lin, Yongzhi Li, Yuhang Chen, Zhihui Yin, Quan Chen, Shiyang Wen, Wenjin Wu, Han Li, Guorui Zhou, Changcheng Li, Peng Jiang  

**一句话要点**：提出GR4AD生成式推荐系统，以解决大规模广告中实时部署的挑战。

**关键词**：生成式推荐, 广告系统, 实时推理, 语义ID, 自回归解码, 强化学习优化

## 3 点简述
- 核心问题：大规模广告中生成式推荐需超越LLM式训练与服务设计，实现实时高效部署。
- 方法要点：引入UA-SID统一语义ID、LazyAR懒自回归解码器、VSL与RSPO优化算法，降低推理成本并提升业务价值。
- 实验或效果：在线A/B测试显示广告收入提升达4.2%，已在快手广告系统部署，支持高吞吐实时服务。

## 摘要（原文）

> Generative recommendation has recently attracted widespread attention in industry due to its potential for scaling and stronger model capacity. However, deploying real-time generative recommendation in large-scale advertising requires designs beyond large-language-model (LLM)-style training and serving recipes. We present a production-oriented generative recommender co-designed across architecture, learning, and serving, named GR4AD (Generative Recommendation for ADdvertising). As for tokenization, GR4AD proposes UA-SID (Unified Advertisement Semantic ID) to capture complicated business information. Furthermore, GR4AD introduces LazyAR, a lazy autoregressive decoder that relaxes layer-wise dependencies for short, multi-candidate generation, preserving effectiveness while reducing inference cost, which facilitates scaling under fixed serving budgets. To align optimization with business value, GR4AD employs VSL (Value-Aware Supervised Learning) and proposes RSPO (Ranking-Guided Softmax Preference Optimization), a ranking-aware, list-wise reinforcement learning algorithm that optimizes value-based rewards under list-level metrics for continual online updates. For online inference, we further propose dynamic beam serving, which adapts beam width across generation levels and online load to control compute. Large-scale online A/B tests show up to 4.2% ad revenue improvement over an existing DLRM-based stack, with consistent gains from both model scaling and inference-time scaling. GR4AD has been fully deployed in Kuaishou advertising system with over 400 million users and achieves high-throughput real-time serving.

