---
layout: default
title: InnoAds-Composer: Efficient Condition Composition for E-Commerce Poster Generation
---

# InnoAds-Composer: Efficient Condition Composition for E-Commerce Poster Generation
**arXiv**：[2603.05898v1](https://arxiv.org/abs/2603.05898) · [PDF](https://arxiv.org/pdf/2603.05898.pdf)  
**作者**：Yuxin Qin, Ke Cao, Haowei Liu, Ao Ma, Fengheng Li, Honghe Zhu, Zheng Zhang, Run Ling, Wei Feng, Xuanhua He, Zhanjie Zhang, Zhen Guo, Haoyi Bian, Jingjing Lv, Junjie Shen, Ching Law  

**一句话要点**：提出InnoAds-Composer以解决电商海报生成中多条件控制效率与准确性问题

**关键词**：电商海报生成, 扩散模型, 多条件控制, 文本渲染, 单阶段框架, 数据集构建

## 3 点简述
- 核心问题：现有多阶段扩散模型在电商海报生成中面临主体保真度低、文本不准确和风格不一致的挑战
- 方法要点：设计单阶段框架，通过重要性分析路由条件令牌，并引入文本特征增强模块提升中文文本渲染精度
- 实验或效果：在自建数据集上显著优于现有方法，且未明显增加推理延迟

## 摘要（原文）

> E-commerce product poster generation aims to automatically synthesize a single image that effectively conveys product information by presenting a subject, text, and a designed style. Recent diffusion models with fine-grained and efficient controllability have advanced product poster synthesis, yet they typically rely on multi-stage pipelines, and simultaneous control over subject, text, and style remains underexplored. Such naive multi-stage pipelines also show three issues: poor subject fidelity, inaccurate text, and inconsistent style. To address these issues, we propose InnoAds-Composer, a single-stage framework that enables efficient tri-conditional control tokens over subject, glyph, and style. To alleviate the quadratic overhead introduced by naive tri-conditional token concatenation, we perform importance analysis over layers and timesteps and route each condition only to the most responsive positions, thereby shortening the active token sequence. Besides, to improve the accuracy of Chinese text rendering, we design a Text Feature Enhancement Module (TFEM) that integrates features from both glyph images and glyph crops. To support training and evaluation, we also construct a high-quality e-commerce product poster dataset and benchmark, which is the first dataset that jointly contains subject, text, and style conditions. Extensive experiments demonstrate that InnoAds-Composer significantly outperforms existing product poster methods without obviously increasing inference latency.

