---
layout: default
title: Background Fades, Foreground Leads: Curriculum-Guided Background Pruning for Efficient Foreground-Centric Collaborative Perception
---

# Background Fades, Foreground Leads: Curriculum-Guided Background Pruning for Efficient Foreground-Centric Collaborative Perception
**arXiv**：[2510.19250v1](https://arxiv.org/abs/2510.19250) · [PDF](https://arxiv.org/pdf/2510.19250.pdf)  
**作者**：Yuheng Wu, Xiangbo Gao, Quang Tau, Zhengzhong Tu, Dongman Lee  

**一句话要点**：提出FadeLead框架以解决协作感知中带宽限制下背景上下文丢失问题

**关键词**：协作感知, 前景中心化, 课程学习, 背景修剪, 带宽优化, 上下文封装

## 3 点简述
- 核心问题：车辆网络带宽限制下，仅传输前景特征导致背景上下文丢失，影响感知可靠性。
- 方法要点：采用课程学习策略，逐步修剪背景，将背景上下文封装到紧凑前景特征中。
- 实验或效果：在模拟和真实基准测试中，优于现有方法，适应不同带宽设置。

## 摘要（原文）

> Collaborative perception enhances the reliability and spatial coverage of
> autonomous vehicles by sharing complementary information across vehicles,
> offering a promising solution to long-tail scenarios that challenge
> single-vehicle perception. However, the bandwidth constraints of vehicular
> networks make transmitting the entire feature map impractical. Recent methods,
> therefore, adopt a foreground-centric paradigm, transmitting only predicted
> foreground-region features while discarding the background, which encodes
> essential context. We propose FadeLead, a foreground-centric framework that
> overcomes this limitation by learning to encapsulate background context into
> compact foreground features during training. At the core of our design is a
> curricular learning strategy that leverages background cues early on but
> progressively prunes them away, forcing the model to internalize context into
> foreground representations without transmitting background itself. Extensive
> experiments on both simulated and real-world benchmarks show that FadeLead
> outperforms prior methods under different bandwidth settings, underscoring the
> effectiveness of context-enriched foreground sharing.

