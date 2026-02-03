---
layout: default
title: Rethinking Generative Recommender Tokenizer: Recsys-Native Encoding and Semantic Quantization Beyond LLMs
---

# Rethinking Generative Recommender Tokenizer: Recsys-Native Encoding and Semantic Quantization Beyond LLMs
**arXiv**：[2602.02338v1](https://arxiv.org/abs/2602.02338) · [PDF](https://arxiv.org/pdf/2602.02338.pdf)  
**作者**：Yu Liang, Zhongjin Zhang, Yuxuan Zhu, Kerui Zhang, Zhiluohan Guo, Wenhang Zhou, Zonqi Yang, Kangle Wu, Yabo Ni, Anxiang Zeng, Cong Fu, Jianxin Wang, Jiazhi Xia  

**一句话要点**：提出ReSID框架，通过推荐原生编码与量化解决语义ID推荐中的表示与序列预测问题

**关键词**：语义ID推荐, 表示学习, 量化方法, 序列推荐, 生成式推荐, 信息保留

## 3 点简述
- 核心问题：现有语义ID推荐方法依赖基础模型和通用量化，导致表示与协同预测弱耦合，量化效率低
- 方法要点：设计FAMAE从结构化特征学习预测充分表示，GAOQ联合减少语义歧义和前缀条件不确定性
- 实验或效果：在十个数据集上平均性能提升超10%，tokenization成本降低达122倍

## 摘要（原文）

> Semantic ID (SID)-based recommendation is a promising paradigm for scaling sequential recommender systems, but existing methods largely follow a semantic-centric pipeline: item embeddings are learned from foundation models and discretized using generic quantization schemes. This design is misaligned with generative recommendation objectives: semantic embeddings are weakly coupled with collaborative prediction, and generic quantization is inefficient at reducing sequential uncertainty for autoregressive modeling. To address these, we propose ReSID, a recommendation-native, principled SID framework that rethinks representation learning and quantization from the perspective of information preservation and sequential predictability, without relying on LLMs. ReSID consists of two components: (i) Field-Aware Masked Auto-Encoding (FAMAE), which learns predictive-sufficient item representations from structured features, and (ii) Globally Aligned Orthogonal Quantization (GAOQ), which produces compact and predictable SID sequences by jointly reducing semantic ambiguity and prefix-conditional uncertainty. Theoretical analysis and extensive experiments across ten datasets show the effectiveness of ReSID. ReSID consistently outperforms strong sequential and SID-based generative baselines by an average of over 10%, while reducing tokenization cost by up to 122x. Code is available at https://github.com/FuCongResearchSquad/ReSID.

