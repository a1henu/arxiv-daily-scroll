---
layout: default
title: LLM-Enhanced Reinforcement Learning for Long-Term User Satisfaction in Interactive Recommendation
---

# LLM-Enhanced Reinforcement Learning for Long-Term User Satisfaction in Interactive Recommendation
**arXiv**：[2601.19585v1](https://arxiv.org/abs/2601.19585) · [PDF](https://arxiv.org/pdf/2601.19585.pdf)  
**作者**：Chongjun Xia, Yanchun Peng, Xianzhi Wang  

**一句话要点**：提出LLM增强强化学习框架，以提升交互推荐中的长期用户满意度

**关键词**：交互推荐系统, 强化学习, 大语言模型, 长期用户满意度, 分层框架

## 3 点简述
- 核心问题：交互推荐系统因短期偏好过拟合导致内容同质化和过滤气泡，忽视用户兴趣长期演化。
- 方法要点：结合LLM语义规划与RL细粒度适应，构建分层框架，高层LLM选择多样类别，低层RL推荐个性化物品。
- 实验或效果：在真实数据集上验证，相比先进基线显著提升长期用户满意度，代码已开源。

## 摘要（原文）

> Interactive recommender systems can dynamically adapt to user feedback, but often suffer from content homogeneity and filter bubble effects due to overfitting short-term user preferences. While recent efforts aim to improve content diversity, they predominantly operate in static or one-shot settings, neglecting the long-term evolution of user interests. Reinforcement learning provides a principled framework for optimizing long-term user satisfaction by modeling sequential decision-making processes. However, its application in recommendation is hindered by sparse, long-tailed user-item interactions and limited semantic planning capabilities. In this work, we propose LLM-Enhanced Reinforcement Learning (LERL), a novel hierarchical recommendation framework that integrates the semantic planning power of LLM with the fine-grained adaptability of RL. LERL consists of a high-level LLM-based planner that selects semantically diverse content categories, and a low-level RL policy that recommends personalized items within the selected semantic space. This hierarchical design narrows the action space, enhances planning efficiency, and mitigates overexposure to redundant content. Extensive experiments on real-world datasets demonstrate that LERL significantly improves long-term user satisfaction when compared with state-of-the-art baselines. The implementation of LERL is available at https://anonymous.4open.science/r/code3-18D3/.

