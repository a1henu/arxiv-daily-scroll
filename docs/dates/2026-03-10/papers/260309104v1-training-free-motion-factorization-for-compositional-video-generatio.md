---
layout: default
title: Training-free Motion Factorization for Compositional Video Generation
---

# Training-free Motion Factorization for Compositional Video Generation
**arXiv**：[2603.09104v1](https://arxiv.org/abs/2603.09104) · [PDF](https://arxiv.org/pdf/2603.09104.pdf)  
**作者**：Zixuan Wang, Ziqin Zhou, Feng Chen, Duo Peng, Yixin Hu, Changsheng Li, Yinjie Lei  

**一句话要点**：提出免训练运动分解框架以解决组合视频生成中的运动类别理解问题

**关键词**：组合视频生成, 运动分解, 扩散模型, 运动规划, 非刚体运动, 语义理解

## 3 点简述
- 核心问题：现有方法忽视提示中多样运动类别，导致语义模糊
- 方法要点：将复杂运动分解为静止、刚体和非刚体三类，采用规划后生成范式
- 实验或效果：在真实世界基准测试中实现优异运动合成性能，框架模型无关

## 摘要（原文）

> Compositional video generation aims to synthesize multiple instances with diverse appearance and motion, which is widely applicable in real-world scenarios. However, current approaches mainly focus on binding semantics, neglecting to understand diverse motion categories specified in prompts. In this paper, we propose a motion factorization framework that decomposes complex motion into three primary categories: motionlessness, rigid motion, and non-rigid motion. Specifically, our framework follows a planning before generation paradigm. (1) During planning, we reason about motion laws on the motion graph to obtain frame-wise changes in the shape and position of each instance. This alleviates semantic ambiguities in the user prompt by organizing it into a structured representation of instances and their interactions. (2) During generation, we modulate the synthesis of distinct motion categories in a disentangled manner. Conditioned on the motion cues, guidance branches stabilize appearance in motionless regions, preserve rigid-body geometry, and regularize local non-rigid deformations. Crucially, our two modules are model-agnostic, which can be seamlessly incorporated into various diffusion model architectures. Extensive experiments demonstrate that our framework achieves impressive performance in motion synthesis on real-world benchmarks. Our code will be released soon.

