---
layout: default
title: CoMo: Compositional Motion Customization for Text-to-Video Generation
---

# CoMo: Compositional Motion Customization for Text-to-Video Generation
**arXiv**：[2510.23007v1](https://arxiv.org/abs/2510.23007) · [PDF](https://arxiv.org/pdf/2510.23007.pdf)  
**作者**：Youcan Xu, Zhen Wang, Jiaxin Shi, Kexin Li, Feifei Shao, Jun Xiao, Yi Yang, Jun Yu, Long Chen  

**一句话要点**：提出CoMo框架以解决文本到视频生成中的多运动定制问题

**关键词**：文本到视频生成, 运动定制, 多运动合成, 解耦学习, 可控生成

## 3 点简述
- 核心问题：现有方法难以控制复杂多主体运动，存在运动-外观纠缠和多运动混合无效问题。
- 方法要点：采用两阶段方法，包括静态-动态解耦调谐和即插即用分合策略，实现多运动合成。
- 实验或效果：在引入的新基准上，CoMo实现最先进性能，提升可控视频生成能力。

## 摘要（原文）

> While recent text-to-video models excel at generating diverse scenes, they
> struggle with precise motion control, particularly for complex, multi-subject
> motions. Although methods for single-motion customization have been developed
> to address this gap, they fail in compositional scenarios due to two primary
> challenges: motion-appearance entanglement and ineffective multi-motion
> blending. This paper introduces CoMo, a novel framework for
> $\textbf{compositional motion customization}$ in text-to-video generation,
> enabling the synthesis of multiple, distinct motions within a single video.
> CoMo addresses these issues through a two-phase approach. First, in the
> single-motion learning phase, a static-dynamic decoupled tuning paradigm
> disentangles motion from appearance to learn a motion-specific module. Second,
> in the multi-motion composition phase, a plug-and-play divide-and-merge
> strategy composes these learned motions without additional training by
> spatially isolating their influence during the denoising process. To facilitate
> research in this new domain, we also introduce a new benchmark and a novel
> evaluation metric designed to assess multi-motion fidelity and blending.
> Extensive experiments demonstrate that CoMo achieves state-of-the-art
> performance, significantly advancing the capabilities of controllable video
> generation. Our project page is at https://como6.github.io/.

