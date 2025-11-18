---
layout: default
title: Uni-Hand: Universal Hand Motion Forecasting in Egocentric Views
---

# Uni-Hand: Universal Hand Motion Forecasting in Egocentric Views
**arXiv**：[2511.12878v1](https://arxiv.org/abs/2511.12878) · [PDF](https://arxiv.org/pdf/2511.12878.pdf)  
**作者**：Junyi Ma, Wentao Bao, Jingyi Xu, Guanzhong Sun, Yu Zheng, Erhang Zhang, Xieyuanli Chen, Hesheng Wang  

**一句话要点**：提出EgoLoc方法以零样本定位手-物接触/分离时刻，提升第一人称视频交互分析。

**关键词**：时序交互定位, 零样本学习, 第一人称视觉, 手-物交互, 视觉语言模型

## 3 点简述
- 核心问题：现有方法难以精确定位手与物体接触和分离的关键时刻，影响沉浸式交互和机器人规划。
- 方法要点：引入手动态引导采样和视觉语言模型，无需对象掩码或类别注释，实现零样本时序定位。
- 实验或效果：在公共数据集和新基准上验证，EgoLoc实现可信时序交互定位，并促进下游应用。

## 摘要（原文）

> Analyzing hand-object interaction in egocentric vision facilitates VR/AR applications and human-robot policy transfer. Existing research has mostly focused on modeling the behavior paradigm of interactive actions (i.e., "how to interact"). However, the more challenging and fine-grained problem of capturing the critical moments of contact and separation between the hand and the target object (i.e., "when to interact") is still underexplored, which is crucial for immersive interactive experiences in mixed reality and robotic motion planning. Therefore, we formulate this problem as temporal interaction localization (TIL). Some recent works extract semantic masks as TIL references, but suffer from inaccurate object grounding and cluttered scenarios. Although current temporal action localization (TAL) methods perform well in detecting verb-noun action segments, they rely on category annotations during training and exhibit limited precision in localizing hand-object contact/separation moments. To address these issues, we propose a novel zero-shot approach dubbed EgoLoc to localize hand-object contact and separation timestamps in egocentric videos. EgoLoc introduces hand-dynamics-guided sampling to generate high-quality visual prompts. It exploits the vision-language model to identify contact/separation attributes, localize specific timestamps, and provide closed-loop feedback for further refinement. EgoLoc eliminates the need for object masks and verb-noun taxonomies, leading to generalizable zero-shot implementation. Comprehensive experiments on the public dataset and our novel benchmarks demonstrate that EgoLoc achieves plausible TIL for egocentric videos. It is also validated to effectively facilitate multiple downstream applications in egocentric vision and robotic manipulation tasks. Code and relevant data will be released at https://github.com/IRMVLab/EgoLoc.

