---
layout: default
title: World Models That Know When They Don't Know: Controllable Video Generation with Calibrated Uncertainty
---

# World Models That Know When They Don't Know: Controllable Video Generation with Calibrated Uncertainty
**arXiv**：[2512.05927v1](https://arxiv.org/abs/2512.05927) · [PDF](https://arxiv.org/pdf/2512.05927.pdf)  
**作者**：Zhiting Mei, Tenny Yin, Micah Baker, Ola Shorinwa, Anirudha Majumdar  

**一句话要点**：提出C3方法以解决可控视频生成中的幻觉问题，通过校准不确定性实现高分辨率置信度估计。

**关键词**：可控视频生成, 不确定性量化, 校准训练, 潜在空间估计, 机器人学习, 幻觉缓解

## 3 点简述
- 核心问题：可控视频模型易产生幻觉，缺乏置信度评估能力，影响机器人任务可靠性。
- 方法要点：基于严格适当评分规则训练模型，在潜在空间估计不确定性，映射到像素级热图可视化。
- 实验或效果：在大规模机器人数据集上验证，提供校准不确定性估计和有效分布外检测。

## 摘要（原文）

> Recent advances in generative video models have led to significant breakthroughs in high-fidelity video synthesis, specifically in controllable video generation where the generated video is conditioned on text and action inputs, e.g., in instruction-guided video editing and world modeling in robotics. Despite these exceptional capabilities, controllable video models often hallucinate - generating future video frames that are misaligned with physical reality - which raises serious concerns in many tasks such as robot policy evaluation and planning. However, state-of-the-art video models lack the ability to assess and express their confidence, impeding hallucination mitigation. To rigorously address this challenge, we propose C3, an uncertainty quantification (UQ) method for training continuous-scale calibrated controllable video models for dense confidence estimation at the subpatch level, precisely localizing the uncertainty in each generated video frame. Our UQ method introduces three core innovations to empower video models to estimate their uncertainty. First, our method develops a novel framework that trains video models for correctness and calibration via strictly proper scoring rules. Second, we estimate the video model's uncertainty in latent space, avoiding training instability and prohibitive training costs associated with pixel-space approaches. Third, we map the dense latent-space uncertainty to interpretable pixel-level uncertainty in the RGB space for intuitive visualization, providing high-resolution uncertainty heatmaps that identify untrustworthy regions. Through extensive experiments on large-scale robot learning datasets (Bridge and DROID) and real-world evaluations, we demonstrate that our method not only provides calibrated uncertainty estimates within the training distribution, but also enables effective out-of-distribution detection.

