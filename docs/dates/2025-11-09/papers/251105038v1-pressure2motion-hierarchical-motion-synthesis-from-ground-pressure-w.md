---
layout: default
title: Pressure2Motion: Hierarchical Motion Synthesis from Ground Pressure with Text Guidance
---

# Pressure2Motion: Hierarchical Motion Synthesis from Ground Pressure with Text Guidance
**arXiv**：[2511.05038v1](https://arxiv.org/abs/2511.05038) · [PDF](https://arxiv.org/pdf/2511.05038.pdf)  
**作者**：Zhengxuan Li, Qinhui Yang, Yiyu Zhuang, Chuan Guo, Xinxin Zuo, Xiaoxiao Long, Yao Yao, Xun Cao, Qiu Shen, Hao Zhu  

**一句话要点**：提出Pressure2Motion，从地面压力和文本生成人体运动，适用于隐私保护和低成本场景。

**关键词**：运动合成, 压力数据, 文本引导, 扩散模型, 隐私保护, 基准测试

## 3 点简述
- 核心问题：地面压力信号与全身运动映射不确定，导致任务严重不适定。
- 方法要点：使用双级特征提取器和分层扩散模型，结合压力特征与文本引导。
- 实验或效果：生成高保真、物理合理的运动，在MPL基准上达到新最优性能。

## 摘要（原文）

> We present Pressure2Motion, a novel motion capture algorithm that synthesizes
> human motion from a ground pressure sequence and text prompt. It eliminates the
> need for specialized lighting setups, cameras, or wearable devices, making it
> suitable for privacy-preserving, low-light, and low-cost motion capture
> scenarios. Such a task is severely ill-posed due to the indeterminate nature of
> the pressure signals to full-body motion. To address this issue, we introduce
> Pressure2Motion, a generative model that leverages pressure features as input
> and utilizes a text prompt as a high-level guiding constraint. Specifically,
> our model utilizes a dual-level feature extractor that accurately interprets
> pressure data, followed by a hierarchical diffusion model that discerns
> broad-scale movement trajectories and subtle posture adjustments. Both the
> physical cues gained from the pressure sequence and the semantic guidance
> derived from descriptive texts are leveraged to guide the motion generation
> with precision. To the best of our knowledge, Pressure2Motion is a pioneering
> work in leveraging both pressure data and linguistic priors for motion
> generation, and the established MPL benchmark is the first benchmark for this
> task. Experiments show our method generates high-fidelity, physically plausible
> motions, establishing a new state-of-the-art for this task. The codes and
> benchmarks will be publicly released upon publication.

