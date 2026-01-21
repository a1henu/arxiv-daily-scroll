---
layout: default
title: TrackletGPT: A Language-like GPT Framework for White Matter Tract Segmentation
---

# TrackletGPT: A Language-like GPT Framework for White Matter Tract Segmentation
**arXiv**：[2601.13935v1](https://arxiv.org/abs/2601.13935) · [PDF](https://arxiv.org/pdf/2601.13935.pdf)  
**作者**：Anoushkrit Goel, Simroop Singh, Ankita Joshi, Ranjeet Ranjan Jha, Chirag Ahuja, Aditya Nigam, Arnav Bhavsar  

**一句话要点**：提出TrackletGPT框架，利用轨迹段在脑白质束分割中引入序列信息，提升跨数据集性能。

**关键词**：脑白质束分割, GPT框架, 轨迹段编码, 跨数据集泛化, 自动分割

## 3 点简述
- 脑白质束分割任务复杂，束间、跨受试者和条件差异大，但跨半球和受试者结构相似。
- TrackletGPT采用类似GPT的语言框架，通过轨迹段编码细粒度子流线信息，自动处理分割。
- 实验表明，在TractoInferno和HCP数据集上，TrackletGPT在DICE、重叠和过伸分数上优于现有方法。

## 摘要（原文）

> White Matter Tract Segmentation is imperative for studying brain structural connectivity, neurological disorders and neurosurgery. This task remains complex, as tracts differ among themselves, across subjects and conditions, yet have similar 3D structure across hemispheres and subjects. To address these challenges, we propose TrackletGPT, a language-like GPT framework which reintroduces sequential information in tokens using tracklets. TrackletGPT generalises seamlessly across datasets, is fully automatic, and encodes granular sub-streamline segments, Tracklets, scaling and refining GPT models in Tractography Segmentation. Based on our experiments, TrackletGPT outperforms state-of-the-art methods on average DICE, Overlap and Overreach scores on TractoInferno and HCP datasets, even on inter-dataset experiments.

