---
layout: default
title: PersonaLive! Expressive Portrait Image Animation for Live Streaming
---

# PersonaLive! Expressive Portrait Image Animation for Live Streaming
**arXiv**：[2512.11253v1](https://arxiv.org/abs/2512.11253) · [PDF](https://arxiv.org/pdf/2512.11253.pdf)  
**作者**：Zhiyuan Li, Chi-Man Pun, Chen Fang, Jue Wang, Xiaodong Cun  

**一句话要点**：提出PersonaLive框架，通过混合隐式信号和蒸馏策略实现直播场景下的实时肖像动画。

**关键词**：肖像动画, 扩散模型, 实时生成, 隐式表示, 蒸馏训练, 直播应用

## 3 点简述
- 当前扩散模型在肖像动画中忽视生成延迟和实时性能，限制直播应用。
- 采用混合隐式信号和较少步数外观蒸馏，提升运动控制和推理效率。
- 实验显示PersonaLive在性能上达到先进水平，速度提升7-22倍。

## 摘要（原文）

> Current diffusion-based portrait animation models predominantly focus on enhancing visual quality and expression realism, while overlooking generation latency and real-time performance, which restricts their application range in the live streaming scenario. We propose PersonaLive, a novel diffusion-based framework towards streaming real-time portrait animation with multi-stage training recipes. Specifically, we first adopt hybrid implicit signals, namely implicit facial representations and 3D implicit keypoints, to achieve expressive image-level motion control. Then, a fewer-step appearance distillation strategy is proposed to eliminate appearance redundancy in the denoising process, greatly improving inference efficiency. Finally, we introduce an autoregressive micro-chunk streaming generation paradigm equipped with a sliding training strategy and a historical keyframe mechanism to enable low-latency and stable long-term video generation. Extensive experiments demonstrate that PersonaLive achieves state-of-the-art performance with up to 7-22x speedup over prior diffusion-based portrait animation models.

