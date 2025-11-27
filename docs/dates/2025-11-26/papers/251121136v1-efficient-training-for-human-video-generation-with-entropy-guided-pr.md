---
layout: default
title: Efficient Training for Human Video Generation with Entropy-Guided Prioritized Progressive Learning
---

# Efficient Training for Human Video Generation with Entropy-Guided Prioritized Progressive Learning
**arXiv**：[2511.21136v1](https://arxiv.org/abs/2511.21136) · [PDF](https://arxiv.org/pdf/2511.21136.pdf)  
**作者**：Changlin Li, Jiawei Zhang, Shuhao Liu, Sihao Lin, Zeyi Shi, Zhihui Li, Xiaojun Chang  

**一句话要点**：提出熵引导优先渐进学习框架以高效训练人类视频生成扩散模型

**关键词**：人类视频生成, 扩散模型, 高效训练, 条件熵膨胀, 渐进学习, GPU内存优化

## 3 点简述
- 高分辨率多帧人类视频生成训练计算成本高、内存消耗大
- 引入条件熵膨胀评估组件重要性，优先训练关键部分；自适应渐进计划提升计算复杂度
- 实验显示训练速度提升2.2倍，GPU内存减少2.4倍，生成性能未下降

## 摘要（原文）

> Human video generation has advanced rapidly with the development of diffusion models, but the high computational cost and substantial memory consumption associated with training these models on high-resolution, multi-frame data pose significant challenges. In this paper, we propose Entropy-Guided Prioritized Progressive Learning (Ent-Prog), an efficient training framework tailored for diffusion models on human video generation. First, we introduce Conditional Entropy Inflation (CEI) to assess the importance of different model components on the target conditional generation task, enabling prioritized training of the most critical components. Second, we introduce an adaptive progressive schedule that adaptively increases computational complexity during training by measuring the convergence efficiency. Ent-Prog reduces both training time and GPU memory consumption while maintaining model performance. Extensive experiments across three datasets, demonstrate the effectiveness of Ent-Prog, achieving up to 2.2$\times$ training speedup and 2.4$\times$ GPU memory reduction without compromising generative performance.

