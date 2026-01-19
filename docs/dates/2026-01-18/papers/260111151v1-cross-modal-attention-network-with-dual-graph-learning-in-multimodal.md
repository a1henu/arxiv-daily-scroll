---
layout: default
title: Cross-Modal Attention Network with Dual Graph Learning in Multimodal Recommendation
---

# Cross-Modal Attention Network with Dual Graph Learning in Multimodal Recommendation
**arXiv**：[2601.11151v1](https://arxiv.org/abs/2601.11151) · [PDF](https://arxiv.org/pdf/2601.11151.pdf)  
**作者**：Ji Dai, Quan Fang, Jun Hu, Desheng Cai, Yang Yang, Can Zhao  

**一句话要点**：提出CRANE模型，通过递归跨模态注意力和双图学习解决多模态推荐中的浅层融合和特征不对称问题。

**关键词**：多模态推荐, 跨模态注意力, 图神经网络, 对比学习, 用户建模, 推荐系统

## 3 点简述
- 核心问题：现有方法存在浅层模态融合和用户-物品特征不对称，限制推荐准确性。
- 方法要点：设计递归跨模态注意力机制捕获高阶依赖，构建用户多模态档案，并集成双图框架进行对称学习。
- 实验或效果：在四个真实数据集上验证，关键指标平均提升5%，计算效率高，收敛快且性能优。

## 摘要（原文）

> Multimedia recommendation systems leverage user-item interactions and multimodal information to capture user preferences, enabling more accurate and personalized recommendations. Despite notable advancements, existing approaches still face two critical limitations: first, shallow modality fusion often relies on simple concatenation, failing to exploit rich synergic intra- and inter-modal relationships; second, asymmetric feature treatment-where users are only characterized by interaction IDs while items benefit from rich multimodal content-hinders the learning of a shared semantic space. To address these issues, we propose a Cross-modal Recursive Attention Network with dual graph Embedding (CRANE). To tackle shallow fusion, we design a core Recursive Cross-Modal Attention (RCA) mechanism that iteratively refines modality features based on cross-correlations in a joint latent space, effectively capturing high-order intra- and inter-modal dependencies. For symmetric multimodal learning, we explicitly construct users' multimodal profiles by aggregating features of their interacted items. Furthermore, CRANE integrates a symmetric dual-graph framework-comprising a heterogeneous user-item interaction graph and a homogeneous item-item semantic graph-unified by a self-supervised contrastive learning objective to fuse behavioral and semantic signals. Despite these complex modeling capabilities, CRANE maintains high computational efficiency. Theoretical and empirical analyses confirm its scalability and high practical efficiency, achieving faster convergence on small datasets and superior performance ceilings on large-scale ones. Comprehensive experiments on four public real-world datasets validate an average 5% improvement in key metrics over state-of-the-art baselines.

