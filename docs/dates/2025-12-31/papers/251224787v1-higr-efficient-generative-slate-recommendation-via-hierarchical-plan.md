---
layout: default
title: HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment
---

# HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment
**arXiv**：[2512.24787v1](https://arxiv.org/abs/2512.24787) · [PDF](https://arxiv.org/pdf/2512.24787.pdf)  
**作者**：Yunsheng Pang, Zijian Liu, Yudong Li, Shaojie Zhu, Zijian Luo, Chenyun Yu, Sikai Wu, Shichen Shen, Cong Xu, Bin Wang, Kai Jiang, Hongyong Yu, Chengxiang Zhuo, Zang Li  

**一句话要点**：提出HiGR框架，通过分层规划与多目标偏好对齐，高效解决板岩推荐中的语义纠缠与解码效率问题。

**关键词**：板岩推荐, 生成模型, 分层规划, 偏好对齐, 残差量化, 在线部署

## 3 点简述
- 核心问题：现有自回归方法在板岩推荐中存在语义纠缠的项标记化和缺乏整体规划的低效顺序解码。
- 方法要点：采用残差量化和对比约束的自动编码器进行项标记化，结合列表级规划和项级解码的分层生成策略。
- 实验或效果：在商业媒体平台实验中，离线推荐质量提升超10%，推理速度加快5倍，在线A/B测试中平均观看时间和视频观看次数分别增加1.22%和1.73%。

## 摘要（原文）

> Slate recommendation, where users are presented with a ranked list of items simultaneously, is widely adopted in online platforms. Recent advances in generative models have shown promise in slate recommendation by modeling sequences of discrete semantic IDs autoregressively. However, existing autoregressive approaches suffer from semantically entangled item tokenization and inefficient sequential decoding that lacks holistic slate planning. To address these limitations, we propose HiGR, an efficient generative slate recommendation framework that integrates hierarchical planning with listwise preference alignment. First, we propose an auto-encoder utilizing residual quantization and contrastive constraints to tokenize items into semantically structured IDs for controllable generation. Second, HiGR decouples generation into a list-level planning stage for global slate intent, followed by an item-level decoding stage for specific item selection. Third, we introduce a listwise preference alignment objective to directly optimize slate quality using implicit user feedback. Experiments on our large-scale commercial media platform demonstrate that HiGR delivers consistent improvements in both offline evaluations and online deployment. Specifically, it outperforms state-of-the-art methods by over 10% in offline recommendation quality with a 5x inference speedup, while further achieving a 1.22% and 1.73% increase in Average Watch Time and Average Video Views in online A/B tests.

