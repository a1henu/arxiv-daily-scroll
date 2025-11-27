---
layout: default
title: From Bits to Rounds: Parallel Decoding with Exploration for Diffusion Language Models
---

# From Bits to Rounds: Parallel Decoding with Exploration for Diffusion Language Models
**arXiv**：[2511.21103v1](https://arxiv.org/abs/2511.21103) · [PDF](https://arxiv.org/pdf/2511.21103.pdf)  
**作者**：Hengyu Fu, Baihe Huang, Virginia Adams, Charles Wang, Venkat Srinivasan, Jiantao Jiao  

**一句话要点**：提出探索-利用策略以解决扩散语言模型并行解码效率瓶颈

**关键词**：扩散语言模型, 并行解码, 信息瓶颈, 探索-利用策略, 解码效率

## 3 点简述
- 标准解码依赖高置信度词元，存在信息瓶颈限制解码进度
- 引入探索-利用策略，结合跨块解码和高不确定性词元探索
- 实验显示减少解码轮次，保持生成质量，验证理论界限

## 摘要（原文）

> Diffusion Language Models (DLMs) have recently emerged as a strong alternative to autoregressive language models (LMs). DLMs offer comparable accuracy with faster inference speed via parallel decoding. However, standard DLM decoding strategies relying on high-confidence tokens encounter an inherent information-theoretic bottleneck that restricts decoding progress and ultimately slows generation. We demonstrate both theoretically and empirically that prioritizing high-confidence tokens is inherently inefficient. High-probability tokens carry negligible information and strictly relying on them limits the effective progress made in each decoding round. We prove that the number of decoding rounds must grow linearly with the sample's total information (negative log-likelihood) and inversely with the per-round information budget, establishing a bits-to-rounds principle. We also propose Explore-Then-Exploit (ETE), a training-free decoding strategy that maximizes information throughput and decoding efficiency. ETE combines cross-block decoding with targeted exploration of high-uncertainty tokens to reshape the conditional distribution and trigger cascades of confident predictions. Experiments verify our theoretical bounds and demonstrate that ETE consistently reduces the required number of decoding rounds compared to confidence-only baselines without compromising generation quality.

