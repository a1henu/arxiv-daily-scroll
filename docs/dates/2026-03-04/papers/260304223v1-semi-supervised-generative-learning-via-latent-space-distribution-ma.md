---
layout: default
title: Semi-Supervised Generative Learning via Latent Space Distribution Matching
---

# Semi-Supervised Generative Learning via Latent Space Distribution Matching
**arXiv**：[2603.04223v1](https://arxiv.org/abs/2603.04223) · [PDF](https://arxiv.org/pdf/2603.04223.pdf)  
**作者**：Kwong Yu Chong, Long Feng  

**一句话要点**：提出LSDM框架，通过潜在空间分布匹配解决半监督生成建模中配对数据稀缺问题。

**关键词**：半监督生成建模, 潜在空间分布匹配, 1-Wasserstein距离, 条件分布生成, 图像超分辨率, 理论一致性分析

## 3 点简述
- 核心问题：半监督生成建模中配对数据不足，影响条件分布建模的准确性和效率。
- 方法要点：采用两阶段框架，先学习潜在空间，再用1-Wasserstein距离进行联合分布匹配，减少对配对数据的依赖。
- 实验或效果：在图像任务中验证有效性，提升生成质量，并为潜在扩散模型提供理论一致性见解。

## 摘要（原文）

> We introduce Latent Space Distribution Matching (LSDM), a novel framework for semi-supervised generative modeling of conditional distributions. LSDM operates in two stages: (i) learning a low-dimensional latent space from both paired and unpaired data, and (ii) performing joint distribution matching in this space via the 1-Wasserstein distance, using only paired data. This two-step approach minimizes an upper bound on the 1-Wasserstein distance between joint distributions, reducing reliance on scarce paired samples while enabling fast one-step generation. Theoretically, we establish non-asymptotic error bounds and demonstrate a key benefit of unpaired data: enhanced geometric fidelity in generated outputs. Furthermore, by extending the scope of its two core steps, LSDM provides a coherent statistical perspective that connects to a broad class of latent-space approaches. Notably, Latent Diffusion Models (LDMs) can be viewed as a variant of LSDM, in which joint distribution matching is achieved indirectly via score matching. Consequently, our results also provide theoretical insights into the consistency of LDMs. Empirical evaluations on real-world image tasks, including class-conditional generation and image super-resolution, demonstrate the effectiveness of LSDM in leveraging unpaired data to enhance generation quality.

