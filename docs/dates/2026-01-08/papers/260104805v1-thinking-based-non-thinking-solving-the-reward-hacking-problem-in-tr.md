---
layout: default
title: Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning
---

# Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning
**arXiv**：[2601.04805v1](https://arxiv.org/abs/2601.04805) · [PDF](https://arxiv.org/pdf/2601.04805.pdf)  
**作者**：Siyuan Gan, Jiaheng Liu, Boyan Wang, Tianpei Yang, Runqing Miao, Yuyao Zhang, Fanyu Meng, Junlan Feng, Linjian Meng, Jing Huo, Yang Gao  

**一句话要点**：提出Thinking-Based Non-Thinking以解决混合推理模型训练中的奖励黑客问题

**关键词**：混合推理模型, 强化学习, 奖励黑客问题, 令牌效率优化, 数学推理基准

## 3 点简述
- 核心问题：混合推理模型使用强化学习训练时易受奖励黑客问题影响，导致奖励分配错误
- 方法要点：通过利用思考响应的解决方案信息，为不同查询设置非思考响应的最大令牌使用上限
- 实验或效果：在五个数学基准上，TNT减少约50%令牌使用，同时显著提升准确率，奖励黑客概率低于10%

## 摘要（原文）

> Large reasoning models (LRMs) have attracted much attention due to their exceptional performance. However, their performance mainly stems from thinking, a long Chain of Thought (CoT), which significantly increase computational overhead. To address this overthinking problem, existing work focuses on using reinforcement learning (RL) to train hybrid reasoning models that automatically decide whether to engage in thinking or not based on the complexity of the query. Unfortunately, using RL will suffer the the reward hacking problem, e.g., the model engages in thinking but is judged as not doing so, resulting in incorrect rewards. To mitigate this problem, existing works either employ supervised fine-tuning (SFT), which incurs high computational costs, or enforce uniform token limits on non-thinking responses, which yields limited mitigation of the problem. In this paper, we propose Thinking-Based Non-Thinking (TNT). It does not employ SFT, and sets different maximum token usage for responses not using thinking across various queries by leveraging information from the solution component of the responses using thinking. Experiments on five mathematical benchmarks demonstrate that TNT reduces token usage by around 50% compared to DeepSeek-R1-Distill-Qwen-1.5B/7B and DeepScaleR-1.5B, while significantly improving accuracy. In fact, TNT achieves the optimal trade-off between accuracy and efficiency among all tested methods. Additionally, the probability of reward hacking problem in TNT's responses, which are classified as not using thinking, remains below 10% across all tested datasets.

