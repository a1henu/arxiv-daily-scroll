---
layout: default
title: VidLeaks: Membership Inference Attacks Against Text-to-Video Models
---

# VidLeaks: Membership Inference Attacks Against Text-to-Video Models
**arXiv**：[2601.11210v1](https://arxiv.org/abs/2601.11210) · [PDF](https://arxiv.org/pdf/2601.11210.pdf)  
**作者**：Li Wang, Wenyu Chen, Ning Yu, Zheng Li, Shanqing Guo  

**一句话要点**：提出VidLeaks框架，通过稀疏时空记忆信号攻击文本到视频模型的成员推断问题。

**关键词**：成员推断攻击, 文本到视频模型, 稀疏记忆, 时空分析, 隐私审计

## 3 点简述
- 核心问题：现有成员推断攻击方法无法处理视频生成的时空复杂性，忽略关键帧稀疏记忆和随机动态不稳定性。
- 方法要点：利用空间重建保真度放大稀疏关键帧记忆信号，结合时间生成稳定性测量语义一致性捕获时间泄漏。
- 实验或效果：在三种黑盒设置下评估，VidLeaks在AnimateDiff和InstructVideo上分别达到82.92%和97.01%的AUC，揭示严重隐私风险。

## 摘要（原文）

> The proliferation of powerful Text-to-Video (T2V) models, trained on massive web-scale datasets, raises urgent concerns about copyright and privacy violations. Membership inference attacks (MIAs) provide a principled tool for auditing such risks, yet existing techniques - designed for static data like images or text - fail to capture the spatio-temporal complexities of video generation. In particular, they overlook the sparsity of memorization signals in keyframes and the instability introduced by stochastic temporal dynamics. In this paper, we conduct the first systematic study of MIAs against T2V models and introduce a novel framework VidLeaks, which probes sparse-temporal memorization through two complementary signals: 1) Spatial Reconstruction Fidelity (SRF), using a Top-K similarity to amplify spatial memorization signals from sparsely memorized keyframes, and 2) Temporal Generative Stability (TGS), which measures semantic consistency across multiple queries to capture temporal leakage. We evaluate VidLeaks under three progressively restrictive black-box settings - supervised, reference-based, and query-only. Experiments on three representative T2V models reveal severe vulnerabilities: VidLeaks achieves AUC of 82.92% on AnimateDiff and 97.01% on InstructVideo even in the strict query-only setting, posing a realistic and exploitable privacy risk. Our work provides the first concrete evidence that T2V models leak substantial membership information through both sparse and temporal memorization, establishing a foundation for auditing video generation systems and motivating the development of new defenses. Code is available at: https://zenodo.org/records/17972831.

