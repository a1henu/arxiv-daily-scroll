---
layout: default
title: RadioFlow: Efficient Radio Map Construction Framework with Flow Matching
---

# RadioFlow: Efficient Radio Map Construction Framework with Flow Matching
**arXiv**：[2510.09314v1](https://arxiv.org/abs/2510.09314) · [PDF](https://arxiv.org/pdf/2510.09314.pdf)  
**作者**：Haozhe Jia, Wenshuo Chen, Xiucheng Wang, Nan Cheng, Hongbo Zhang, Kuimou Yu, Songning Lai, Nanjian Jia, Bowen Tian, Hongru Xiao, Yutao Yue  

**一句话要点**：提出RadioFlow框架，通过流匹配实现高效无线地图构建，解决扩散模型参数大、推理慢问题。

**关键词**：无线地图构建, 流匹配生成, 高效采样, 6G网络, 数字孪生, 推理加速

## 3 点简述
- 扩散模型在无线地图生成中参数大、迭代去噪慢，推理延迟高，阻碍实际部署。
- 采用流匹配方法学习噪声到数据的连续传输轨迹，实现单步高效采样。
- 实验显示参数减少8倍、推理加速4倍，保持高精度，适用于6G网络数字孪生。

## 摘要（原文）

> Accurate and real-time radio map (RM) generation is crucial for
> next-generation wireless systems, yet diffusion-based approaches often suffer
> from large model sizes, slow iterative denoising, and high inference latency,
> which hinder practical deployment. To overcome these limitations, we propose
> \textbf{RadioFlow}, a novel flow-matching-based generative framework that
> achieves high-fidelity RM generation through single-step efficient sampling.
> Unlike conventional diffusion models, RadioFlow learns continuous transport
> trajectories between noise and data, enabling both training and inference to be
> significantly accelerated while preserving reconstruction accuracy.
> Comprehensive experiments demonstrate that RadioFlow achieves state-of-the-art
> performance with \textbf{up to 8$\times$ fewer parameters} and \textbf{over
> 4$\times$ faster inference} compared to the leading diffusion-based baseline
> (RadioDiff). This advancement provides a promising pathway toward scalable,
> energy-efficient, and real-time electromagnetic digital twins for future 6G
> networks. We release the code at
> \href{https://github.com/Hxxxz0/RadioFlow}{GitHub}.

