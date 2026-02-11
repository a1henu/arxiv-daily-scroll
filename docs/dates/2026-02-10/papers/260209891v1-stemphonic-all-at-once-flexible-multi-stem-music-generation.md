---
layout: default
title: Stemphonic: All-at-once Flexible Multi-stem Music Generation
---

# Stemphonic: All-at-once Flexible Multi-stem Music Generation
**arXiv**：[2602.09891v1](https://arxiv.org/abs/2602.09891) · [PDF](https://arxiv.org/pdf/2602.09891.pdf)  
**作者**：Shih-Lun Wu, Ge Zhu, Juan-Pablo Caceres, Cheng-Zhi Anna Huang, Nicholas J. Bryan  

**一句话要点**：提出Stemphonic框架，通过单次推理生成可变多音轨，解决现有方法在灵活性与速度间的权衡问题。

**关键词**：多音轨音乐生成, 扩散模型, 音轨同步, 条件生成, 用户控制, 音乐制作

## 3 点简述
- 核心问题：现有音轨生成方法要么固定输出音轨集，要么单次生成一个音轨，导致灵活性与速度难以兼顾。
- 方法要点：基于扩散/流模型，训练时分组同步音轨并共享噪声潜在，推理时使用共享初始噪声和音轨特定文本输入。
- 实验或效果：在开源评估集上，Stemphonic输出质量更高，全混音生成速度提升25%至50%。

## 摘要（原文）

> Music stem generation, the task of producing musically-synchronized and isolated instrument audio clips, offers the potential of greater user control and better alignment with musician workflows compared to conventional text-to-music models. Existing stem generation approaches, however, either rely on fixed architectures that output a predefined set of stems in parallel, or generate only one stem at a time, resulting in slow inference despite flexibility in stem combination. We propose Stemphonic, a diffusion-/flow-based framework that overcomes this trade-off and generates a variable set of synchronized stems in one inference pass. During training, we treat each stem as a batch element, group synchronized stems in a batch, and apply a shared noise latent to each group. At inference-time, we use a shared initial noise latent and stem-specific text inputs to generate synchronized multi-stem outputs in one pass. We further expand our approach to enable one-pass conditional multi-stem generation and stem-wise activity controls to empower users to iteratively generate and orchestrate the temporal layering of a mix. We benchmark our results on multiple open-source stem evaluation sets and show that Stemphonic produces higher-quality outputs while accelerating the full mix generation process by 25 to 50%. Demos at: https://stemphonic-demo.vercel.app.

