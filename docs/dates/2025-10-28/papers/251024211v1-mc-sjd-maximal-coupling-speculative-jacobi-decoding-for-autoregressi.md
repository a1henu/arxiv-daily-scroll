---
layout: default
title: MC-SJD : Maximal Coupling Speculative Jacobi Decoding for Autoregressive Visual Generation Acceleration
---

# MC-SJD : Maximal Coupling Speculative Jacobi Decoding for Autoregressive Visual Generation Acceleration
**arXiv**：[2510.24211v1](https://arxiv.org/abs/2510.24211) · [PDF](https://arxiv.org/pdf/2510.24211.pdf)  
**作者**：Junhyuk So, Hyunho Kook, Chaeyeon Jang, Eunhyeok Park  

**一句话要点**：提出MC-SJD以加速自回归视觉生成，通过最大化耦合提高接受率

**关键词**：自回归视觉生成, 并行解码加速, 耦合理论, 无损生成, 图像生成, 视频生成

## 3 点简述
- 自回归视觉生成推理慢，每令牌生成需数千步，限制实际应用
- 基于耦合理论，最大化迭代间草稿令牌相同概率，保持无损并行解码
- 实验显示图像生成加速约4.2倍，视频生成加速约13.3倍，无质量损失

## 摘要（原文）

> While autoregressive (AR) modeling has recently emerged as a new paradigm in
> visual generation, its practical adoption is severely constrained by the slow
> inference speed of per-token generation, which often requires thousands of
> steps to produce a single sample. To address this challenge, we propose MC-SJD,
> a training-free, lossless parallel decoding framework designed to accelerate AR
> visual generation by extending the recently introduced Speculative Jacobi
> Decoding (SJD). Although SJD shows strong potential for accelerating AR
> generation, we demonstrate that token instability across iterations
> significantly reduces the acceptance rate, a limitation that primarily arises
> from the independent sampling process used during draft token generation. To
> overcome this, we introduce MC-SJD, an information-theoretic approach based on
> coupling, which substantially accelerates standard SJD by maximizing the
> probability of sampling identical draft tokens across consecutive iterations,
> all while preserving its lossless property. Remarkably, this method requires
> only a single-line modification to the existing algorithm, yet achieves
> substantial performance gains, delivering up to a ~4.2x acceleration in image
> generation and ~13.3x acceleration in video generation compared to standard AR
> decoding, without any degradation in output quality.

