---
layout: default
title: Arcee Trinity Large Technical Report
---

# Arcee Trinity Large Technical Report
**arXiv**：[2602.17004v1](https://arxiv.org/abs/2602.17004) · [PDF](https://arxiv.org/pdf/2602.17004.pdf)  
**作者**：Varun Singh, Lucas Krauss, Sami Jaghouar, Matej Sirovatka, Charles Goddard, Fares Obied, Jack Min Ong, Jannik Straube, Fern, Aria Harley, Conner Stewart, Colin Kealty, Maziyar Panahi, Simon Kirsten, Anushka Deshpande, Anneketh Vij, Arthur Bresnu, Pranav Veldurthi, Raghav Ravishankar, Hardik Bishnoi, DatologyAI Team, Arcee AI Team, Prime Intellect Team, Mark McQuade, Johannes Hagemann, Lucas Atkins  

**一句话要点**：提出Arcee Trinity系列稀疏专家混合模型，包括400B总参数的大模型，以高效处理大规模语言预训练任务。

**关键词**：稀疏专家混合模型, 大规模预训练, 注意力机制, 参数效率, 优化器, 公开检查点

## 3 点简述
- 核心问题：设计高效的大规模稀疏专家混合模型，减少每token激活参数以提升计算效率。
- 方法要点：采用现代架构如交错局部与全局注意力、门控注意力、深度缩放三明治归一化和Sigmoid路由，并引入软钳位动量专家偏置更新策略。
- 实验或效果：模型在10万亿或17万亿token上预训练，无损失尖峰，检查点已公开。

## 摘要（原文）

> We present the technical report for Arcee Trinity Large, a sparse Mixture-of-Experts model with 400B total parameters and 13B activated per token. Additionally, we report on Trinity Nano and Trinity Mini, with Trinity Nano having 6B total parameters with 1B activated per token, Trinity Mini having 26B total parameters with 3B activated per token. The models' modern architecture includes interleaved local and global attention, gated attention, depth-scaled sandwich norm, and sigmoid routing for Mixture-of-Experts. For Trinity Large, we also introduce a new MoE load balancing strategy titled Soft-clamped Momentum Expert Bias Updates (SMEBU). We train the models using the Muon optimizer. All three models completed training with zero loss spikes. Trinity Nano and Trinity Mini were pre-trained on 10 trillion tokens, and Trinity Large was pre-trained on 17 trillion tokens. The model checkpoints are available at https://huggingface.co/arcee-ai.

