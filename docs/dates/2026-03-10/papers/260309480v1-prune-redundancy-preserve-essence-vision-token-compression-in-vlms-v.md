---
layout: default
title: Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity
---

# Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity
**arXiv**：[2603.09480v1](https://arxiv.org/abs/2603.09480) · [PDF](https://arxiv.org/pdf/2603.09480.pdf)  
**作者**：Zhengyao Fang, Pengyuan Lyu, Chengquan Zhang, Guangming Lu, Jun Yu, Wenjie Pei  

**一句话要点**：提出PruneSID方法，通过协同重要性-多样性压缩视觉令牌以提升视觉语言模型效率

**关键词**：视觉令牌压缩, 训练无关方法, 重要性-多样性平衡, 动态压缩比, 跨模态通用性

## 3 点简述
- 视觉语言模型因视觉令牌冗余导致计算效率低下，现有方法难以平衡重要性与多样性
- PruneSID采用两阶段流程：PSCA聚类语义组和组内NMS去冗余，并引入动态压缩比机制
- 实验显示在LLaVA-1.5上以11.1%令牌保留率达96.3%准确率，优于先前方法且速度快

## 摘要（原文）

> Vision-language models (VLMs) face significant computational inefficiencies caused by excessive generation of visual tokens. While prior work shows that a large fraction of visual tokens are redundant, existing compression methods struggle to balance importance preservation and information diversity. To address this, we propose PruneSID, a training-free Synergistic Importance-Diversity approach featuring a two-stage pipeline: (1) Principal Semantic Components Analysis (PSCA) for clustering tokens into semantically coherent groups, ensuring comprehensive concept coverage, and (2) Intra-group Non-Maximum Suppression (NMS) for pruning redundant tokens while preserving key representative tokens within each group. Additionally, PruneSID incorporates an information-aware dynamic compression ratio mechanism that optimizes token compression rates based on image complexity, enabling more effective average information preservation across diverse scenes. Extensive experiments demonstrate state-of-the-art performance, achieving 96.3% accuracy on LLaVA-1.5 with only 11.1% token retention, and 92.8% accuracy at extreme compression rates (5.6%) on LLaVA-NeXT, outperforming prior methods by 2.5% with 7.8 $\times$ faster prefilling speed compared to the original model. Our framework generalizes across diverse VLMs and both image and video modalities, showcasing strong cross-modal versatility. Code is available at https://github.com/ZhengyaoFang/PruneSID}{https://github.com/ZhengyaoFang/PruneSID.

