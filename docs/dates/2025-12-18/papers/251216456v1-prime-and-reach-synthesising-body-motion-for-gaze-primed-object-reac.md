---
layout: default
title: Prime and Reach: Synthesising Body Motion for Gaze-Primed Object Reach
---

# Prime and Reach: Synthesising Body Motion for Gaze-Primed Object Reach
**arXiv**：[2512.16456v1](https://arxiv.org/abs/2512.16456) · [PDF](https://arxiv.org/pdf/2512.16456.pdf)  
**作者**：Masashi Hatano, Saptarshi Sinha, Jacob Chalk, Wei-Hong Li, Hideo Saito, Dima Damen  

**一句话要点**：提出扩散模型以生成注视引导的物体抓取/放置人体运动序列

**关键词**：人体运动生成, 扩散模型, 注视引导, 物体抓取, 数据集构建

## 3 点简述
- 核心问题：生成注视引导的物体抓取/放置人体运动序列，模仿自然人类行为。
- 方法要点：基于文本条件扩散模型预训练，再以目标姿态或位置为条件微调。
- 实验或效果：在HD-EPIC数据集上，模型达到60%注视成功率和89%抓取成功率。

## 摘要（原文）

> Human motion generation is a challenging task that aims to create realistic motion imitating natural human behaviour. We focus on the well-studied behaviour of priming an object/location for pick up or put down -- that is, the spotting of an object/location from a distance, known as gaze priming, followed by the motion of approaching and reaching the target location. To that end, we curate, for the first time, 23.7K gaze-primed human motion sequences for reaching target object locations from five publicly available datasets, i.e., HD-EPIC, MoGaze, HOT3D, ADT, and GIMO. We pre-train a text-conditioned diffusion-based motion generation model, then fine-tune it conditioned on goal pose or location, on our curated sequences. Importantly, we evaluate the ability of the generated motion to imitate natural human movement through several metrics, including the 'Reach Success' and a newly introduced 'Prime Success' metric. On the largest dataset, HD-EPIC, our model achieves 60% prime success and 89% reach success when conditioned on the goal object location.

