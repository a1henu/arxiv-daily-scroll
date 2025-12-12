---
layout: default
title: MultiHateLoc: Towards Temporal Localisation of Multimodal Hate Content in Online Videos
---

# MultiHateLoc: Towards Temporal Localisation of Multimodal Hate Content in Online Videos
**arXiv**：[2512.10408v1](https://arxiv.org/abs/2512.10408) · [PDF](https://arxiv.org/pdf/2512.10408.pdf)  
**作者**：Qiyue Sun, Tailin Chen, Yinghui Zhang, Yuchen Zhang, Jiangbei Yue, Jianbo Jiao, Zeyu Fu  

**一句话要点**：提出MultiHateLoc框架以解决弱监督下在线视频多模态仇恨内容的时间定位问题

**关键词**：多模态仇恨内容检测, 弱监督时间定位, 跨模态融合, 在线视频分析, 时序建模

## 3 点简述
- 核心问题：在线视频中多模态仇恨内容传播加剧，现有方法缺乏时间定位能力，尤其在弱监督下难以捕捉跨模态时序动态。
- 方法要点：采用模态感知时序编码器、动态跨模态融合与对比对齐策略，以及模态感知MIL目标，实现帧级预测。
- 实验或效果：在HateMM和MultiHateClip数据集上验证，达到时间定位任务的先进性能。

## 摘要（原文）

> The rapid growth of video content on platforms such as TikTok and YouTube has intensified the spread of multimodal hate speech, where harmful cues emerge subtly and asynchronously across visual, acoustic, and textual streams. Existing research primarily focuses on video-level classification, leaving the practically crucial task of temporal localisation, identifying when hateful segments occur, largely unaddressed. This challenge is even more noticeable under weak supervision, where only video-level labels are available, and static fusion or classification-based architectures struggle to capture cross-modal and temporal dynamics. To address these challenges, we propose MultiHateLoc, the first framework designed for weakly-supervised multimodal hate localisation. MultiHateLoc incorporates (1) modality-aware temporal encoders to model heterogeneous sequential patterns, including a tailored text-based preprocessing module for feature enhancement; (2) dynamic cross-modal fusion to adaptively emphasise the most informative modality at each moment and a cross-modal contrastive alignment strategy to enhance multimodal feature consistency; (3) a modality-aware MIL objective to identify discriminative segments under video-level supervision. Despite relying solely on coarse labels, MultiHateLoc produces fine-grained, interpretable frame-level predictions. Experiments on HateMM and MultiHateClip show that our method achieves state-of-the-art performance in the localisation task.

