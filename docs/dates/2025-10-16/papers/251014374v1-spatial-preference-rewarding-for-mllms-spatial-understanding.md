---
layout: default
title: Spatial Preference Rewarding for MLLMs Spatial Understanding
---

# Spatial Preference Rewarding for MLLMs Spatial Understanding
**arXiv**：[2510.14374v1](https://arxiv.org/abs/2510.14374) · [PDF](https://arxiv.org/pdf/2510.14374.pdf)  
**作者**：Han Qiu, Peng Gao, Lewei Lu, Xiaoqin Zhang, Ling Shao, Shijian Lu  

**一句话要点**：提出空间偏好奖励方法以增强多模态大语言模型的细粒度空间理解能力

**关键词**：多模态大语言模型, 空间理解, 偏好优化, 对象定位, 细粒度感知

## 3 点简述
- 核心问题：MLLMs在细粒度空间感知如区域描述和对象定位方面表现不足，且难以响应用户需求。
- 方法要点：SPR通过奖励详细响应和精确定位，使用语义和定位评分优化描述质量。
- 实验或效果：在标准基准测试中，SPR有效提升空间理解能力，训练开销最小。

## 摘要（原文）

> Multimodal large language models~(MLLMs) have demonstrated promising spatial
> understanding capabilities, such as referencing and grounding object
> descriptions. Despite their successes, MLLMs still fall short in fine-grained
> spatial perception abilities, such as generating detailed region descriptions
> or accurately localizing objects. Additionally, they often fail to respond to
> the user's requirements for desired fine-grained spatial understanding. This
> issue might arise because existing approaches primarily focus on tuning MLLMs
> to model pre-annotated instruction data to inject spatial knowledge, without
> direct supervision of MLLMs' actual responses. We address this issue by SPR, a
> Spatial Preference Rewarding~(SPR) approach that enhances MLLMs' spatial
> capabilities by rewarding MLLMs' detailed responses with precise object
> localization over vague or inaccurate responses. With randomly selected image
> regions and region descriptions from MLLMs, SPR introduces semantic and
> localization scores to comprehensively evaluate the text quality and
> localization quality in MLLM-generated descriptions. We also refine the MLLM
> descriptions with better localization accuracy and pair the best-scored
> refinement with the initial descriptions of the lowest score for direct
> preference optimization, thereby enhancing fine-grained alignment with visual
> input. Extensive experiments over standard referring and grounding benchmarks
> show that SPR improves MLLM spatial understanding capabilities effectively with
> minimal overhead in training. Data and code will be released at
> https://github.com/hanqiu-hq/SPR

