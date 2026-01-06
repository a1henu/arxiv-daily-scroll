---
layout: default
title: DDNet: A Dual-Stream Graph Learning and Disentanglement Framework for Temporal Forgery Localization
---

# DDNet: A Dual-Stream Graph Learning and Disentanglement Framework for Temporal Forgery Localization
**arXiv**：[2601.01784v1](https://arxiv.org/abs/2601.01784) · [PDF](https://arxiv.org/pdf/2601.01784.pdf)  
**作者**：Boyang Zhao, Xin Liao, Jiaxin Chen, Xiaoshuai Wu, Yufeng Wu  

**一句话要点**：提出DDNet双流图学习与解缠框架，以解决视频时序伪造定位中全局异常捕获不足的问题。

**关键词**：时序伪造定位, 双流图学习, 特征解缠, 跨域鲁棒性, 视频伪造检测

## 3 点简述
- 核心问题：现有方法受限于局部视角，难以捕捉视频时序伪造中的全局异常。
- 方法要点：通过协调局部伪影的时间距离流和长程连接的语义内容流，结合解缠与适应技术隔离通用伪造指纹。
- 实验或效果：在ForgeryNet和TVIL基准上，AP@0.95指标超越现有方法约9%，跨域鲁棒性显著提升。

## 摘要（原文）

> The rapid evolution of AIGC technology enables misleading viewers by tampering mere small segments within a video, rendering video-level detection inaccurate and unpersuasive. Consequently, temporal forgery localization (TFL), which aims to precisely pinpoint tampered segments, becomes critical. However, existing methods are often constrained by \emph{local view}, failing to capture global anomalies. To address this, we propose a \underline{d}ual-stream graph learning and \underline{d}isentanglement framework for temporal forgery localization (DDNet). By coordinating a \emph{Temporal Distance Stream} for local artifacts and a \emph{Semantic Content Stream} for long-range connections, DDNet prevents global cues from being drowned out by local smoothness. Furthermore, we introduce Trace Disentanglement and Adaptation (TDA) to isolate generic forgery fingerprints, alongside Cross-Level Feature Embedding (CLFE) to construct a robust feature foundation via deep fusion of hierarchical features. Experiments on ForgeryNet and TVIL benchmarks demonstrate that our method outperforms state-of-the-art approaches by approximately 9\% in AP@0.95, with significant improvements in cross-domain robustness.

