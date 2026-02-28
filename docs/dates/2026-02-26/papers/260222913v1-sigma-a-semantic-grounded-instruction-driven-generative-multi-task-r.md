---
layout: default
title: SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress
---

# SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress
**arXiv**：[2602.22913v1](https://arxiv.org/abs/2602.22913) · [PDF](https://arxiv.org/pdf/2602.22913.pdf)  
**作者**：Yang Yu, Lei Kou, Huaikuan Yi, Bin Chen, Yayu Cao, Lei Shen, Chao Zhang, Bing Wang, Xiaoyi Zeng  

**一句话要点**：提出SIGMA，一种基于语义和指令驱动的生成式多任务推荐系统，以解决现实场景中推荐任务多样性和适应性不足的问题。

**关键词**：生成式推荐, 多任务学习, 指令驱动, 语义建模, 项目标记化, 自适应融合

## 3 点简述
- 核心问题：现有生成推荐方法局限于交互驱动的下一项预测，难以快速适应趋势变化或处理多样推荐任务。
- 方法要点：通过统一潜在空间捕获语义和协同关系，结合混合项目标记化和多任务SFT数据集，实现指令驱动的生成。
- 实验或效果：离线实验和在线A/B测试验证了SIGMA在推荐准确性和多样性方面的有效性。

## 摘要（原文）

> With the rapid evolution of Large Language Models, generative recommendation is gradually reshaping the paradigm of recommender systems. However, most existing methods are still confined to the interaction-driven next-item prediction paradigm, failing to rapidly adapt to evolving trends or address diverse recommendation tasks along with business-specific requirements in real-world scenarios. To this end, we present SIGMA, a Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress. Specifically, we first ground item entities in general semantics via a unified latent space capturing both semantic and collaborative relations. Building upon this, we develop a hybrid item tokenization method for precise modeling and efficient generation. Moreover, we construct a large-scale multi-task SFT dataset to empower SIGMA to fulfill various recommendation demands via instruction-following. Finally, we design a three-step item generation procedure integrated with an adaptive probabilistic fusion mechanism to calibrate the output distributions based on task-specific requirements for recommendation accuracy and diversity. Extensive offline experiments and online A/B tests demonstrate the effectiveness of SIGMA.

