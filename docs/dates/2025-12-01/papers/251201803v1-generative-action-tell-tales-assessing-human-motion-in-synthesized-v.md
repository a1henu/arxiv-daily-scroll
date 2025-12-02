---
layout: default
title: Generative Action Tell-Tales: Assessing Human Motion in Synthesized Videos
---

# Generative Action Tell-Tales: Assessing Human Motion in Synthesized Videos
**arXiv**：[2512.01803v1](https://arxiv.org/abs/2512.01803) · [PDF](https://arxiv.org/pdf/2512.01803.pdf)  
**作者**：Xavier Thomas, Youngsun Lim, Ananya Srinivasan, Audrey Zheng, Deepti Ghadiyaram  

**一句话要点**：提出基于真实动作潜在空间的评估指标，以解决视频生成中复杂人类动作的视觉与时间正确性评估难题。

**关键词**：视频生成评估, 人类动作分析, 潜在空间学习, 时间动态理解, 骨骼几何特征

## 3 点简述
- 核心问题：现有视频生成评估指标存在外观偏见，缺乏时间理解，难以检测动作动态和解剖学不合理性。
- 方法要点：融合外观无关的骨骼几何特征与外观特征，学习真实动作的潜在空间，量化生成视频与真实分布的距离。
- 实验或效果：在新基准上比现有方法提升超过68%，在外部基准上表现竞争性，与人类感知相关性更强。

## 摘要（原文）

> Despite rapid advances in video generative models, robust metrics for evaluating visual and temporal correctness of complex human actions remain elusive. Critically, existing pure-vision encoders and Multimodal Large Language Models (MLLMs) are strongly appearance-biased, lack temporal understanding, and thus struggle to discern intricate motion dynamics and anatomical implausibilities in generated videos. We tackle this gap by introducing a novel evaluation metric derived from a learned latent space of real-world human actions. Our method first captures the nuances, constraints, and temporal smoothness of real-world motion by fusing appearance-agnostic human skeletal geometry features with appearance-based features. We posit that this combined feature space provides a robust representation of action plausibility. Given a generated video, our metric quantifies its action quality by measuring the distance between its underlying representations and this learned real-world action distribution. For rigorous validation, we develop a new multi-faceted benchmark specifically designed to probe temporally challenging aspects of human action fidelity. Through extensive experiments, we show that our metric achieves substantial improvement of more than 68% compared to existing state-of-the-art methods on our benchmark, performs competitively on established external benchmarks, and has a stronger correlation with human perception. Our in-depth analysis reveals critical limitations in current video generative models and establishes a new standard for advanced research in video generation.

