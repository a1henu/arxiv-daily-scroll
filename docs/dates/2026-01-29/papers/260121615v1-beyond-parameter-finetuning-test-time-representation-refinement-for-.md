---
layout: default
title: Beyond Parameter Finetuning: Test-Time Representation Refinement for Node Classification
---

# Beyond Parameter Finetuning: Test-Time Representation Refinement for Node Classification
**arXiv**：[2601.21615v1](https://arxiv.org/abs/2601.21615) · [PDF](https://arxiv.org/pdf/2601.21615.pdf)  
**作者**：Jiaxin Zhang, Yiqi Wang, Siwei Wang, Xihong Yang, Yu Shi, Xinwang Liu, En Zhu  

**一句话要点**：提出TTReFT框架，通过表示微调解决图神经网络在分布外测试中的性能下降问题。

**关键词**：图神经网络, 测试时训练, 表示微调, 分布外泛化, 节点分类

## 3 点简述
- 核心问题：图神经网络在分布外测试场景下性能显著下降，现有参数微调方法存在灾难性遗忘。
- 方法要点：TTReFT通过不确定性引导节点选择、低秩表示干预和干预感知掩码自编码器，将适应目标从参数转向表示。
- 实验或效果：在五个基准数据集上验证，TTReFT实现一致且优越的性能，提供理论保证和实际应用价值。

## 摘要（原文）

> Graph Neural Networks frequently exhibit significant performance degradation in the out-of-distribution test scenario. While test-time training (TTT) offers a promising solution, existing Parameter Finetuning (PaFT) paradigm suffer from catastrophic forgetting, hindering their real-world applicability. We propose TTReFT, a novel Test-Time Representation FineTuning framework that transitions the adaptation target from model parameters to latent representations. Specifically, TTReFT achieves this through three key innovations: (1) uncertainty-guided node selection for specific interventions, (2) low-rank representation interventions that preserve pre-trained knowledge, and (3) an intervention-aware masked autoencoder that dynamically adjust masking strategy to accommodate the node selection scheme. Theoretically, we establish guarantees for TTReFT in OOD settings. Empirically, extensive experiments across five benchmark datasets demonstrate that TTReFT achieves consistent and superior performance. Our work establishes representation finetuning as a new paradigm for graph TTT, offering both theoretical grounding and immediate practical utility for real-world deployment.

