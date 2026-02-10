---
layout: default
title: VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning
---

# VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning
**arXiv**：[2602.08828v1](https://arxiv.org/abs/2602.08828) · [PDF](https://arxiv.org/pdf/2602.08828.pdf)  
**作者**：Hao Tan, Jun Lan, Senyuan Shi, Zichang Tan, Zijian Yu, Huijia Zhu, Weiqiang Wang, Jun Wan, Zhen Lei  

**一句话要点**：提出VideoVeritas框架，通过感知预任务强化学习检测AI生成视频，以应对安全风险。

**关键词**：AI生成视频检测, 感知预任务强化学习, 多模态大语言模型, 时空定位, 自监督学习, 视频数据集

## 3 点简述
- 核心问题：AI视频生成能力提升带来安全风险，现有检测方法在细粒度感知和事实推理间存在偏差。
- 方法要点：采用联合偏好对齐和感知预任务强化学习，通过时空定位和自监督对象计数增强检测性能。
- 实验或效果：引入MintVid数据集评估，VideoVeritas在多样化基准上实现更平衡的性能，优于现有方法。

## 摘要（原文）

> The growing capability of video generation poses escalating security risks, making reliable detection increasingly essential. In this paper, we introduce VideoVeritas, a framework that integrates fine-grained perception and fact-based reasoning. We observe that while current multi-modal large language models (MLLMs) exhibit strong reasoning capacity, their granular perception ability remains limited. To mitigate this, we introduce Joint Preference Alignment and Perception Pretext Reinforcement Learning (PPRL). Specifically, rather than directly optimizing for detection task, we adopt general spatiotemporal grounding and self-supervised object counting in the RL stage, enhancing detection performance with simple perception pretext tasks. To facilitate robust evaluation, we further introduce MintVid, a light yet high-quality dataset containing 3K videos from 9 state-of-the-art generators, along with a real-world collected subset that has factual errors in content. Experimental results demonstrate that existing methods tend to bias towards either superficial reasoning or mechanical analysis, while VideoVeritas achieves more balanced performance across diverse benchmarks.

