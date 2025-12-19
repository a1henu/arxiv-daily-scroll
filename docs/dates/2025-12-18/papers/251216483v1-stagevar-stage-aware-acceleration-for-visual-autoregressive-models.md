---
layout: default
title: StageVAR: Stage-Aware Acceleration for Visual Autoregressive Models
---

# StageVAR: Stage-Aware Acceleration for Visual Autoregressive Models
**arXiv**：[2512.16483v1](https://arxiv.org/abs/2512.16483) · [PDF](https://arxiv.org/pdf/2512.16483.pdf)  
**作者**：Senmao Li, Kai Wang, Salman Khan, Fahad Shahbaz Khan, Jian Yang, Yaxing Wang  

**一句话要点**：提出StageVAR框架，通过阶段感知加速解决视觉自回归模型计算复杂度高的问题。

**关键词**：视觉自回归模型, 阶段感知加速, 计算复杂度优化, 图像生成, 低秩近似, 即插即用框架

## 3 点简述
- 核心问题：VAR模型在大规模步骤下计算复杂度和运行时间急剧增加，现有加速方法依赖手动步骤选择且忽视生成过程不同阶段的重要性差异。
- 方法要点：基于分析，早期步骤对语义和结构一致性关键需保留，后期步骤可修剪或近似；StageVAR利用后期计算的语义无关性和低秩特性，实现即插即用加速，无需额外训练。
- 实验或效果：在GenEval上仅下降0.01，DPG下降0.26，实现最高3.4倍加速，优于现有基线。

## 摘要（原文）

> Visual Autoregressive (VAR) modeling departs from the next-token prediction paradigm of traditional Autoregressive (AR) models through next-scale prediction, enabling high-quality image generation. However, the VAR paradigm suffers from sharply increased computational complexity and running time at large-scale steps. Although existing acceleration methods reduce runtime for large-scale steps, but rely on manual step selection and overlook the varying importance of different stages in the generation process. To address this challenge, we present StageVAR, a systematic study and stage-aware acceleration framework for VAR models. Our analysis shows that early steps are critical for preserving semantic and structural consistency and should remain intact, while later steps mainly refine details and can be pruned or approximated for acceleration. Building on these insights, StageVAR introduces a plug-and-play acceleration strategy that exploits semantic irrelevance and low-rank properties in late-stage computations, without requiring additional training. Our proposed StageVAR achieves up to 3.4x speedup with only a 0.01 drop on GenEval and a 0.26 decrease on DPG, consistently outperforming existing acceleration baselines. These results highlight stage-aware design as a powerful principle for efficient visual autoregressive image generation.

