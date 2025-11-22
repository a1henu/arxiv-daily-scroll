---
layout: default
title: Lite Any Stereo: Efficient Zero-Shot Stereo Matching
---

# Lite Any Stereo: Efficient Zero-Shot Stereo Matching
**arXiv**：[2511.16555v1](https://arxiv.org/abs/2511.16555) · [PDF](https://arxiv.org/pdf/2511.16555.pdf)  
**作者**：Junpeng Jing, Weixun Luo, Ye Mao, Krystian Mikolajczyk  

**一句话要点**：提出Lite Any Stereo框架，实现高效零样本立体匹配

**关键词**：立体匹配, 零样本泛化, 高效模型, 成本聚合, 三阶段训练

## 3 点简述
- 核心问题：传统高效模型因容量有限难以实现零样本泛化
- 方法要点：设计紧凑主干和混合成本聚合模块，采用三阶段训练策略
- 实验或效果：在四个真实基准测试中排名第一，计算成本低于1%

## 摘要（原文）

> Recent advances in stereo matching have focused on accuracy, often at the cost of significantly increased model size. Traditionally, the community has regarded efficient models as incapable of zero-shot ability due to their limited capacity. In this paper, we introduce Lite Any Stereo, a stereo depth estimation framework that achieves strong zero-shot generalization while remaining highly efficient. To this end, we design a compact yet expressive backbone to ensure scalability, along with a carefully crafted hybrid cost aggregation module. We further propose a three-stage training strategy on million-scale data to effectively bridge the sim-to-real gap. Together, these components demonstrate that an ultra-light model can deliver strong generalization, ranking 1st across four widely used real-world benchmarks. Remarkably, our model attains accuracy comparable to or exceeding state-of-the-art non-prior-based accurate methods while requiring less than 1% computational cost, setting a new standard for efficient stereo matching.

