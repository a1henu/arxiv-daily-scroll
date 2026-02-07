---
layout: default
title: RISE-Video: Can Video Generators Decode Implicit World Rules?
---

# RISE-Video: Can Video Generators Decode Implicit World Rules?
**arXiv**：[2602.05986v1](https://arxiv.org/abs/2602.05986) · [PDF](https://arxiv.org/pdf/2602.05986.pdf)  
**作者**：Mingxin Liu, Shuran Ma, Shibei Meng, Xiangyu Zhao, Zicheng Zhang, Shaofeng Zhang, Zhihang Zhong, Peixian Chen, Haoyu Cao, Xing Sun, Haodong Duan, Xue Yang  

**一句话要点**：提出RISE-Video基准以评估文本图像到视频生成模型的隐式世界规则推理能力

**关键词**：视频生成评估, 隐式规则推理, 多模态基准, 自动化评估, 世界模拟

## 3 点简述
- 核心问题：生成视频模型在隐式世界规则推理方面存在不足，缺乏评估标准
- 方法要点：构建包含467个样本的基准，涵盖八个类别，引入四维评估指标
- 实验或效果：在11个先进模型上测试，揭示其在复杂场景下的普遍缺陷

## 摘要（原文）

> While generative video models have achieved remarkable visual fidelity, their capacity to internalize and reason over implicit world rules remains a critical yet under-explored frontier. To bridge this gap, we present RISE-Video, a pioneering reasoning-oriented benchmark for Text-Image-to-Video (TI2V) synthesis that shifts the evaluative focus from surface-level aesthetics to deep cognitive reasoning. RISE-Video comprises 467 meticulously human-annotated samples spanning eight rigorous categories, providing a structured testbed for probing model intelligence across diverse dimensions, ranging from commonsense and spatial dynamics to specialized subject domains. Our framework introduces a multi-dimensional evaluation protocol consisting of four metrics: \textit{Reasoning Alignment}, \textit{Temporal Consistency}, \textit{Physical Rationality}, and \textit{Visual Quality}. To further support scalable evaluation, we propose an automated pipeline leveraging Large Multimodal Models (LMMs) to emulate human-centric assessment. Extensive experiments on 11 state-of-the-art TI2V models reveal pervasive deficiencies in simulating complex scenarios under implicit constraints, offering critical insights for the advancement of future world-simulating generative models.

