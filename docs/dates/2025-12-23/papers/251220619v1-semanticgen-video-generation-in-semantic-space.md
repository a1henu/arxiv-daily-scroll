---
layout: default
title: SemanticGen: Video Generation in Semantic Space
---

# SemanticGen: Video Generation in Semantic Space
**arXiv**：[2512.20619v1](https://arxiv.org/abs/2512.20619) · [PDF](https://arxiv.org/pdf/2512.20619.pdf)  
**作者**：Jianhong Bai, Xiaoshi Wu, Xintao Wang, Fu Xiao, Yuanxing Zhang, Qinghe Wang, Xiaoyu Shi, Menghan Xia, Zuozhu Liu, Haoji Hu, Pengfei Wan, Kun Gai  

**一句话要点**：提出SemanticGen，通过在语义空间生成视频以解决收敛慢和计算成本高的问题。

**关键词**：视频生成, 语义空间, 扩散模型, 两阶段生成, 长视频生成

## 3 点简述
- 现有视频生成模型在VAE空间学习分布，导致收敛慢且计算成本高。
- 采用两阶段生成：先扩散生成语义特征规划全局，再扩散生成VAE潜在细节。
- 实验表明，该方法能高效生成高质量视频，优于现有方法。

## 摘要（原文）

> State-of-the-art video generative models typically learn the distribution of video latents in the VAE space and map them to pixels using a VAE decoder. While this approach can generate high-quality videos, it suffers from slow convergence and is computationally expensive when generating long videos. In this paper, we introduce SemanticGen, a novel solution to address these limitations by generating videos in the semantic space. Our main insight is that, due to the inherent redundancy in videos, the generation process should begin in a compact, high-level semantic space for global planning, followed by the addition of high-frequency details, rather than directly modeling a vast set of low-level video tokens using bi-directional attention. SemanticGen adopts a two-stage generation process. In the first stage, a diffusion model generates compact semantic video features, which define the global layout of the video. In the second stage, another diffusion model generates VAE latents conditioned on these semantic features to produce the final output. We observe that generation in the semantic space leads to faster convergence compared to the VAE latent space. Our method is also effective and computationally efficient when extended to long video generation. Extensive experiments demonstrate that SemanticGen produces high-quality videos and outperforms state-of-the-art approaches and strong baselines.

