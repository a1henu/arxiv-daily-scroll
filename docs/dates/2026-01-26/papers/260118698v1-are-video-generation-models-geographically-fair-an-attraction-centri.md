---
layout: default
title: Are Video Generation Models Geographically Fair? An Attraction-Centric Evaluation of Global Visual Knowledge
---

# Are Video Generation Models Geographically Fair? An Attraction-Centric Evaluation of Global Visual Knowledge
**arXiv**：[2601.18698v1](https://arxiv.org/abs/2601.18698) · [PDF](https://arxiv.org/pdf/2601.18698.pdf)  
**作者**：Xiao Liu, Jiawei Zhang  

**一句话要点**：提出Geo-Attraction Landmark Probing框架，评估文本到视频模型的地理公平性。

**关键词**：文本到视频生成, 地理公平性, 视觉知识评估, 基准构建, 多指标分析

## 3 点简述
- 研究文本到视频模型的地理公平性，关注全球视觉知识编码。
- 开发GAP框架和GEOATTRACTION-500基准，结合多指标评估吸引力合成。
- 应用GAP于Sora 2模型，发现其地理知识相对均匀，偏差较弱。

## 摘要（原文）

> Recent advances in text-to-video generation have produced visually compelling results, yet it remains unclear whether these models encode geographically equitable visual knowledge. In this work, we investigate the geo-equity and geographically grounded visual knowledge of text-to-video models through an attraction-centric evaluation. We introduce Geo-Attraction Landmark Probing (GAP), a systematic framework for assessing how faithfully models synthesize tourist attractions from diverse regions, and construct GEOATTRACTION-500, a benchmark of 500 globally distributed attractions spanning varied regions and popularity levels. GAP integrates complementary metrics that disentangle overall video quality from attraction-specific knowledge, including global structural alignment, fine-grained keypoint-based alignment, and vision-language model judgments, all validated against human evaluation. Applying GAP to the state-of-the-art text-to-video model Sora 2, we find that, contrary to common assumptions of strong geographic bias, the model exhibits a relatively uniform level of geographically grounded visual knowledge across regions, development levels, and cultural groupings, with only weak dependence on attraction popularity. These results suggest that current text-to-video models express global visual knowledge more evenly than expected, highlighting both their promise for globally deployed applications and the need for continued evaluation as such systems evolve.

