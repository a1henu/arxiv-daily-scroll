---
layout: default
title: SemiNFT: Learning to Transfer Presets from Imitation to Appreciation via Hybrid-Sample Reinforcement Learning
---

# SemiNFT: Learning to Transfer Presets from Imitation to Appreciation via Hybrid-Sample Reinforcement Learning
**arXiv**：[2602.08582v1](https://arxiv.org/abs/2602.08582) · [PDF](https://arxiv.org/pdf/2602.08582.pdf)  
**作者**：Melany Yang, Yuhang Yu, Diwang Weng, Jinwei Chen, Wei Dong  

**一句话要点**：提出SemiNFT框架，通过混合样本强化学习实现从模仿到审美的预设色彩迁移。

**关键词**：预设色彩迁移, 扩散Transformer, 强化学习, 美学感知, 零样本任务, 混合奖励机制

## 3 点简述
- 核心问题：现有参考方法依赖像素统计，缺乏语义理解和美学感知。
- 方法要点：基于扩散Transformer，先配对学习基础技能，后强化学习提升美学。
- 实验效果：在标准基准和零样本任务中超越现有方法，展现高级审美理解。

## 摘要（原文）

> Photorealistic color retouching plays a vital role in visual content creation, yet manual retouching remains inaccessible to non-experts due to its reliance on specialized expertise. Reference-based methods offer a promising alternative by transferring the preset color of a reference image to a source image. However, these approaches often operate as novice learners, performing global color mappings derived from pixel-level statistics, without a true understanding of semantic context or human aesthetics. To address this issue, we propose SemiNFT, a Diffusion Transformer (DiT)-based retouching framework that mirrors the trajectory of human artistic training: beginning with rigid imitation and evolving into intuitive creation. Specifically, SemiNFT is first taught with paired triplets to acquire basic structural preservation and color mapping skills, and then advanced to reinforcement learning (RL) on unpaired data to cultivate nuanced aesthetic perception. Crucially, during the RL stage, to prevent catastrophic forgetting of old skills, we design a hybrid online-offline reward mechanism that anchors aesthetic exploration with structural review. % experiments Extensive experiments show that SemiNFT not only outperforms state-of-the-art methods on standard preset transfer benchmarks but also demonstrates remarkable intelligence in zero-shot tasks, such as black-and-white photo colorization and cross-domain (anime-to-photo) preset transfer. These results confirm that SemiNFT transcends simple statistical matching and achieves a sophisticated level of aesthetic comprehension. Our project can be found at https://melanyyang.github.io/SemiNFT/.

