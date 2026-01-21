---
layout: default
title: OmniTransfer: All-in-one Framework for Spatio-temporal Video Transfer
---

# OmniTransfer: All-in-one Framework for Spatio-temporal Video Transfer
**arXiv**：[2601.14250v1](https://arxiv.org/abs/2601.14250) · [PDF](https://arxiv.org/pdf/2601.14250.pdf)  
**作者**：Pengze Zhang, Yanze Wu, Mengtian Li, Xu Bai, Songtao Zhao, Fulong Ye, Chong Mou, Xinghui Li, Zhuowei Chen, Qian He, Mingyuan Gao  

**一句话要点**：提出OmniTransfer统一框架，通过多视图信息和时序线索解决视频时空转移中的灵活性与泛化问题。

**关键词**：视频生成, 时空转移, 多模态对齐, 因果学习, 任务自适应, 高保真视频

## 3 点简述
- 现有视频定制方法依赖参考图像或任务特定时序先验，未能充分利用视频的丰富时空信息，限制生成灵活性和泛化能力。
- OmniTransfer引入任务感知位置偏置、参考解耦因果学习和任务自适应多模态对齐，统一处理外观和时序转移任务。
- 实验表明，OmniTransfer在外观和时序转移上优于现有方法，并在无姿态输入下匹配姿态引导方法的运动转移效果。

## 摘要（原文）

> Videos convey richer information than images or text, capturing both spatial and temporal dynamics. However, most existing video customization methods rely on reference images or task-specific temporal priors, failing to fully exploit the rich spatio-temporal information inherent in videos, thereby limiting flexibility and generalization in video generation. To address these limitations, we propose OmniTransfer, a unified framework for spatio-temporal video transfer. It leverages multi-view information across frames to enhance appearance consistency and exploits temporal cues to enable fine-grained temporal control. To unify various video transfer tasks, OmniTransfer incorporates three key designs: Task-aware Positional Bias that adaptively leverages reference video information to improve temporal alignment or appearance consistency; Reference-decoupled Causal Learning separating reference and target branches to enable precise reference transfer while improving efficiency; and Task-adaptive Multimodal Alignment using multimodal semantic guidance to dynamically distinguish and tackle different tasks. Extensive experiments show that OmniTransfer outperforms existing methods in appearance (ID and style) and temporal transfer (camera movement and video effects), while matching pose-guided methods in motion transfer without using pose, establishing a new paradigm for flexible, high-fidelity video generation.

