---
layout: default
title: IF-VidCap: Can Video Caption Models Follow Instructions?
---

# IF-VidCap: Can Video Caption Models Follow Instructions?
**arXiv**：[2510.18726v1](https://arxiv.org/abs/2510.18726) · [PDF](https://arxiv.org/pdf/2510.18726.pdf)  
**作者**：Shihao Li, Yuanxing Zhang, Jiangtao Wu, Zhide Lei, Yiwen He, Runzhe Wen, Chenxi Liao, Chengkang Jiang, An Ping, Shuo Gao, Suhan Wang, Zhaozhou Bian, Zijun Zhou, Jingyi Xie, Jiayi Zhou, Jing Wang, Yifan Yao, Weihao Xie, Yingshui Tan, Yanghai Wang, Qianqian Xie, Zhaoxiang Zhang, Jiaheng Liu  

**一句话要点**：提出IF-VidCap基准以评估可控视频描述中的指令遵循能力

**关键词**：可控视频描述, 指令遵循基准, 多模态大语言模型, 格式正确性, 内容正确性

## 3 点简述
- 当前视频描述基准忽视指令遵循，专注于描述全面性
- 引入IF-VidCap基准，评估格式和内容正确性，含1400样本
- 评估20+模型显示专有模型领先，开源模型接近，密集描述模型表现不佳

## 摘要（原文）

> Although Multimodal Large Language Models (MLLMs) have demonstrated
> proficiency in video captioning, practical applications require captions that
> follow specific user instructions rather than generating exhaustive,
> unconstrained descriptions. Current benchmarks, however, primarily assess
> descriptive comprehensiveness while largely overlooking instruction-following
> capabilities. To address this gap, we introduce IF-VidCap, a new benchmark for
> evaluating controllable video captioning, which contains 1,400 high-quality
> samples. Distinct from existing video captioning or general
> instruction-following benchmarks, IF-VidCap incorporates a systematic framework
> that assesses captions on two dimensions: format correctness and content
> correctness. Our comprehensive evaluation of over 20 prominent models reveals a
> nuanced landscape: despite the continued dominance of proprietary models, the
> performance gap is closing, with top-tier open-source solutions now achieving
> near-parity. Furthermore, we find that models specialized for dense captioning
> underperform general-purpose MLLMs on complex instructions, indicating that
> future work should simultaneously advance both descriptive richness and
> instruction-following fidelity.

